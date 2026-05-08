import { rename, rm, rmdir, readdir } from 'node:fs/promises';
import path from 'node:path';

const dist = path.join(process.cwd(), 'dist');

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (!entry.isDirectory()) {
      continue;
    }
    const current = path.join(dir, entry.name);
    await walk(current);
    if (!entry.name.endsWith('.html')) {
      continue;
    }
    const nestedIndex = path.join(current, 'index.html');
    const flatHtml = current;
    const tempHtml = `${current}.__astro_tmp`;
    try {
      await rename(nestedIndex, tempHtml);
      await rm(current, { recursive: true, force: true });
      await rename(tempHtml, flatHtml);
    } catch {
      await rm(tempHtml, { force: true }).catch(() => {});
      // Directory did not contain Astro's /foo.html/index.html shape.
    }
  }
}

await walk(dist);
console.log('Normalized .html routes in dist/');
