const fs = require('fs');
const http = require('http');
const path = require('path');
const puppeteer = require('puppeteer');

const rootDir = path.resolve(__dirname, '..');
const logDir = path.join(rootDir, 'logs');
const requestedPort = Number(process.env.DEMO_CAPTURE_PORT || 0);

const mimeTypes = {
  '.css': 'text/css; charset=utf-8',
  '.gif': 'image/gif',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.txt': 'text/plain; charset=utf-8',
  '.webp': 'image/webp',
  '.xml': 'application/xml; charset=utf-8',
};

function send(res, status, body, type = 'text/plain; charset=utf-8') {
  res.writeHead(status, {
    'Content-Length': Buffer.byteLength(body),
    'Content-Type': type,
  });
  res.end(body);
}

function resolvePath(urlPath) {
  const cleanPath = decodeURIComponent(urlPath.split('?')[0]);
  const relativePath = cleanPath === '/' ? '/index.html' : cleanPath;
  const filePath = path.normalize(path.join(rootDir, relativePath));
  if (!filePath.startsWith(rootDir)) return null;
  return filePath;
}

const server = http.createServer((req, res) => {
  const filePath = resolvePath(req.url || '/');
  if (!filePath) return send(res, 403, 'Forbidden');

  fs.stat(filePath, (statError, stats) => {
    if (statError) return send(res, 404, 'Not found');

    const finalPath = stats.isDirectory() ? path.join(filePath, 'index.html') : filePath;
    fs.readFile(finalPath, (readError, content) => {
      if (readError) return send(res, 404, 'Not found');
      const ext = path.extname(finalPath).toLowerCase();
      send(res, 200, content, mimeTypes[ext] || 'application/octet-stream');
    });
  });
});

async function capturePage(browser, baseUrl, route, outputName) {
  const page = await browser.newPage();
  await page.goto(`${baseUrl}${route}`, { waitUntil: 'networkidle2' });
  await page.waitForSelector('.kpi-card');
  await sleep(1500);
  await page.screenshot({
    path: path.join(logDir, outputName),
    fullPage: false,
  });
  await page.close();
}

async function main() {
  fs.mkdirSync(logDir, { recursive: true });

  await new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(requestedPort, '127.0.0.1', resolve);
  });

  const address = server.address();
  if (!address || typeof address === 'string') {
    throw new Error('Failed to resolve local capture server address');
  }
  const baseUrl = `http://127.0.0.1:${address.port}`;

  const browser = await puppeteer.launch({
    headless: true,
    defaultViewport: { width: 1280, height: 800 },
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || '/snap/bin/chromium',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    await capturePage(browser, baseUrl, '/demo/visual-bug.html', 'visual-bug-full.png');
    await capturePage(browser, baseUrl, '/demo/visual-fix.html', 'visual-fix-full.png');
  } finally {
    await browser.close();
    await new Promise((resolve, reject) => {
      server.close((error) => (error ? reject(error) : resolve()));
    });
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
