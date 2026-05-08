import { stat, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const ONOUT_ORIGIN = 'https://onout.org';
export const HABAB_ORIGIN = 'https://habab.ru';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');

const SKIP_DIRS = new Set([
  '.astro',
  '.claude',
  '.entire',
  '.git',
  '.github',
  '.agents',
  'dist',
  'node_modules',
  'src',
]);

const SKIP_HTML_NAMES = new Set([
  '_template.html',
  '404.html',
]);

export const CMS_SLUGS = [
  'wordpress',
  'bitrix',
  'magento',
  'joomla',
  'prestashop',
  'cs-cart',
  'webasyst',
  'opencart',
  'shopware',
  'drupal',
  'woocommerce',
  'modx',
  'strapi',
  'directus',
  'craft-cms',
  'statamic',
  'payload-cms',
  'umbraco',
  'nopcommerce',
  'dnn',
  'concrete-cms',
  'typo3',
  'dify',
  'open-webui',
  'cal-com',
  'posthog',
  'ghost',
  'hashnode',
  'storyblok',
  'contentstack',
  'decap-cms',
  'hygraph',
  'datocms',
  'tinacms',
  'keystonejs',
  'contentful',
  'sanity',
  'sitecore-xm',
  'builder-io',
  'buttercms',
  'cloudcannon',
  'headless-cms-landscape',
  'kontent-ai',
  'optimizely-cms',
  'prismic',
];

export const RU_CMS_SLUGS = new Set(['bitrix', 'webasyst']);

function toPosix(value) {
  return value.split(path.sep).join('/');
}

async function walkHtml(dir, out = []) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(entry.name)) {
        await walkHtml(path.join(dir, entry.name), out);
      }
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) {
      continue;
    }
    if (SKIP_HTML_NAMES.has(entry.name) || entry.name.endsWith('.ru.html')) {
      continue;
    }
    out.push(path.join(dir, entry.name));
  }
  return out;
}

export function htmlFileToRoute(file) {
  const rel = toPosix(path.relative(repoRoot, file));
  if (rel === 'index.html') {
    return '/vibers/';
  }
  if (rel === 'simple-review/index.html') {
    return '/';
  }
  if (rel === 'blog/index.html') {
    return '/vibers/blog/';
  }
  if (rel.startsWith('blog/')) {
    const blogRel = rel.slice('blog/'.length);
    if (blogRel.endsWith('/index.html')) {
      return `/vibers/blog/${blogRel.slice(0, -'/index.html'.length)}/`;
    }
    return `/vibers/blog/${blogRel}`;
  }
  if (rel.endsWith('/index.html')) {
    return `/${rel.slice(0, -'/index.html'.length)}/`;
  }
  return `/${rel}`;
}

export function routeToAstroParam(route) {
  return route.replace(/^\/|\/$/g, '');
}

export function routeParts(route) {
  const clean = route.replace(/^\/|\/$/g, '');
  return clean ? clean.split('/') : [];
}

export function routeHtmlStem(part) {
  return part.endsWith('.html') ? part.slice(0, -'.html'.length) : part;
}

export async function getStaticHtmlRoutes() {
  const files = await walkHtml(repoRoot);
  const routes = [];
  for (const file of files) {
    const route = htmlFileToRoute(file);
    const fileStat = await stat(file);
    routes.push({
      route,
      astroParam: routeToAstroParam(route),
      file,
      lastmod: fileStat.mtime.toISOString().replace(/\.\d{3}Z$/, '+00:00'),
    });
  }
  return routes.sort((a, b) => a.route.localeCompare(b.route));
}

export async function getRoutesForShape({ depth, htmlFile }) {
  const routes = await getStaticHtmlRoutes();
  return routes.filter((item) => {
    if (item.route === '/') {
      return false;
    }
    const parts = routeParts(item.route);
    return parts.length === depth && item.route.endsWith('.html') === htmlFile;
  });
}

export function sitemapAlternates(route) {
  const slug = route.replace(/^\/|\/$/g, '');
  if (!RU_CMS_SLUGS.has(slug)) {
    return [];
  }
  return [
    ['en', `${ONOUT_ORIGIN}${route}`],
    ['ru', `${HABAB_ORIGIN}${route}`],
    ['x-default', `${ONOUT_ORIGIN}${route}`],
  ];
}
