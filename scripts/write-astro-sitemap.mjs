import { writeFile } from 'node:fs/promises';
import path from 'node:path';
import {
  getStaticHtmlRoutes,
  ONOUT_ORIGIN,
  sitemapAlternates,
} from '../src/lib/static-html-routes.mjs';

function escapeXml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

const routes = await getStaticHtmlRoutes();
const xml = [
  '<?xml version="1.0" encoding="UTF-8"?>',
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
  ...routes.map((item) => {
    const loc = `${ONOUT_ORIGIN}${item.route}`;
    const alternates = sitemapAlternates(item.route)
      .map(([language, href]) => `    <xhtml:link rel="alternate" hreflang="${escapeXml(language)}" href="${escapeXml(href)}"/>`)
      .join('\n');
    return [
      '  <url>',
      `    <loc>${escapeXml(loc)}</loc>`,
      `    <lastmod>${escapeXml(item.lastmod)}</lastmod>`,
      alternates,
      '  </url>',
    ].filter(Boolean).join('\n');
  }),
  '</urlset>',
  '',
].join('\n');

await writeFile(path.join(process.cwd(), 'dist', 'sitemap.xml'), xml, 'utf8');
console.log(`Wrote Astro sitemap with ${routes.length} URLs`);
