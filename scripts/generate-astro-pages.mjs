import { mkdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { getStaticHtmlRoutes, routeParts } from '../src/lib/static-html-routes.mjs';

const root = process.cwd();
const pagesRoot = path.join(root, 'src', 'pages');
const manifestPath = path.join(pagesRoot, '.generated-routes.json');

function routeToAstroPagePath(route) {
  if (route === '/') {
    return null;
  }
  const parts = routeParts(route);
  const last = parts.at(-1);
  if (!last) {
    return null;
  }
  if (last.endsWith('.html')) {
    const htmlPageName = `${last}.astro`;
    return path.join(pagesRoot, ...parts.slice(0, -1), htmlPageName);
  }
  return path.join(pagesRoot, ...parts, 'index.astro');
}

function renderAstroPage(sourceFile) {
  return `---
import { readFile } from 'node:fs/promises';

const html = await readFile(${JSON.stringify(sourceFile)}, 'utf8');
---
<Fragment set:html={html} />
`;
}

async function main() {
  await rm(manifestPath, { force: true });
  const generatedFiles = [];
  const routes = await getStaticHtmlRoutes();

  for (const item of routes) {
    const astroPath = routeToAstroPagePath(item.route);
    if (!astroPath) {
      continue;
    }
    await mkdir(path.dirname(astroPath), { recursive: true });
    await writeFile(astroPath, renderAstroPage(item.file), 'utf8');
    generatedFiles.push(astroPath);
  }

  await writeFile(
    manifestPath,
    JSON.stringify({ generatedAt: new Date().toISOString(), files: generatedFiles }, null, 2) + '\n',
    'utf8',
  );
  console.log(`Generated ${generatedFiles.length} Astro route files`);
}

await main();
