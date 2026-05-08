import { copyFile, mkdir, readdir } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();
const dist = path.join(root, 'dist');

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

const PUBLIC_EXTENSIONS = new Set([
  '.css',
  '.gif',
  '.ico',
  '.jpeg',
  '.jpg',
  '.js',
  '.json',
  '.md',
  '.mp3',
  '.mp4',
  '.pdf',
  '.png',
  '.svg',
  '.txt',
  '.wav',
  '.webp',
  '.xml',
  '.zip',
]);

const SKIP_NAMES = new Set([
  '.env',
  '.htpasswd',
  'package-lock.json',
  'package.json',
  'sitemap.xml',
  'skills-lock.json',
]);

function isPublicAsset(fileName) {
  if (SKIP_NAMES.has(fileName) || fileName.endsWith('.pem')) {
    return false;
  }
  return PUBLIC_EXTENSIONS.has(path.extname(fileName).toLowerCase());
}

async function copyAssets(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    const source = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(entry.name)) {
        await copyAssets(source);
      }
      continue;
    }
    if (!entry.isFile() || !isPublicAsset(entry.name)) {
      continue;
    }
    const rel = path.relative(root, source);
    const target = path.join(dist, rel);
    await mkdir(path.dirname(target), { recursive: true });
    await copyFile(source, target);

    // /vibers/ used to be an nginx alias to the repo root. Keep non-HTML
    // public files reachable under that prefix while Astro owns the HTML.
    const vibersTarget = path.join(dist, 'vibers', rel);
    await mkdir(path.dirname(vibersTarget), { recursive: true });
    await copyFile(source, vibersTarget);
  }
}

await copyAssets(root);
console.log('Copied static assets into dist/');
