import { getStaticHtmlRoutes, ONOUT_ORIGIN, sitemapAlternates } from '../lib/static-html-routes.mjs';

function escapeXml(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

export async function GET() {
  const routes = await getStaticHtmlRoutes();
  const body = [
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

  return new Response(body, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
}
