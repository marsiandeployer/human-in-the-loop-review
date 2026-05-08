import { spawn } from 'node:child_process';
import { mkdir, readFile, rm, rmdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { getStaticHtmlRoutes } from '../src/lib/static-html-routes.mjs';
import './generate-astro-pages.mjs';

const root = process.cwd();
const pagesRoot = path.join(root, 'src', 'pages');
const manifestPath = path.join(pagesRoot, '.generated-routes.json');

function run(command, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      cwd: root,
      stdio: 'inherit',
      shell: false,
    });
    child.on('exit', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`${command} ${args.join(' ')} exited with ${code}`));
      }
    });
    child.on('error', reject);
  });
}

async function cleanupGeneratedPages() {
  let manifest;
  try {
    manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  } catch {
    return;
  }

  for (const file of manifest.files.toReversed()) {
    await rm(file, { force: true });
  }

  const dirs = [...new Set(manifest.files.map((file) => path.dirname(file)))].sort(
    (a, b) => b.length - a.length,
  );
  for (const dir of dirs) {
    let current = dir;
    while (current.startsWith(pagesRoot) && current !== pagesRoot) {
      try {
        await rmdir(current);
      } catch {
        break;
      }
      current = path.dirname(current);
    }
  }
  await rm(manifestPath, { force: true });
}

try {
  await run('npx', ['astro', 'build']);
  await run('node', ['scripts/normalize-astro-html-files.mjs']);
  await run('node', ['scripts/copy-astro-assets.mjs']);
  await run('node', ['scripts/write-astro-sitemap.mjs']);
} finally {
  await cleanupGeneratedPages();
}

const routeCount = (await getStaticHtmlRoutes()).length;
await mkdir(path.join(root, 'dist'), { recursive: true });
await writeFile(
  path.join(root, 'dist', 'astro-build-info.json'),
  JSON.stringify({ generatedAt: new Date().toISOString(), routeCount }, null, 2) + '\n',
  'utf8',
);
