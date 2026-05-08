#!/usr/bin/env python3
"""Generate onout.org sitemap from nginx-served static routes."""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


ONOUT = "https://onout.org"
HABAB = "https://habab.ru"

VIBERS_ROOT = Path("/root/vibers")
ONOUT_ROOT = Path("/var/www/onout.org")

CMS_SLUGS = (
    "wordpress",
    "bitrix",
    "magento",
    "joomla",
    "prestashop",
    "cs-cart",
    "webasyst",
    "opencart",
    "shopware",
    "drupal",
    "woocommerce",
    "modx",
    "strapi",
    "directus",
    "craft-cms",
    "statamic",
    "payload-cms",
    "umbraco",
    "nopcommerce",
    "dnn",
    "concrete-cms",
    "typo3",
    "dify",
    "open-webui",
    "cal-com",
    "posthog",
    "ghost",
    "hashnode",
    "storyblok",
    "contentstack",
    "decap-cms",
    "hygraph",
    "datocms",
    "tinacms",
    "keystonejs",
    "contentful",
    "sanity",
    "sitecore-xm",
    "builder-io",
    "buttercms",
    "prismic",
    "cloudcannon",
    "optimizely-cms",
    "kontent-ai",
    "headless-cms-landscape",
)
RU_CMS_SLUGS = {"bitrix", "webasyst"}

ROOT_HTML_ALLOWLIST = {"index.html"}
SKIP_NAMES = {
    "404.html",
    "ci-status.html",
    "googleb0ef9bfd96887057.html",
    "index_static.html",
}
SKIP_PARTS = {
    "chicken_files",
    ".claude",       # private skill files leaked into /var/www/onout.org/.claude/
    ".git",
    "node_modules",  # never expose dependency trees
}


@dataclass(frozen=True)
class SitemapUrl:
    loc: str
    lastmod: str
    alternates: tuple[tuple[str, str], ...] = ()


def lastmod(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(
        microsecond=0
    ).isoformat()


def add_url(
    urls: dict[str, SitemapUrl],
    loc: str,
    source: Path,
    alternates: tuple[tuple[str, str], ...] = (),
) -> None:
    urls[loc] = SitemapUrl(loc=loc, lastmod=lastmod(source), alternates=alternates)


def html_path_to_route(path: Path, root: Path, prefix: str = "") -> str | None:
    rel = path.relative_to(root)
    if any(part in SKIP_PARTS for part in rel.parts):
        return None
    if path.name in SKIP_NAMES or " " in path.name:
        return None
    if path.name.endswith(".ru.html"):
        return None
    if rel.parent == Path(".") and path.name not in ROOT_HTML_ALLOWLIST:
        return None
    if path.name == "index.html":
        route = "/" if rel.parent == Path(".") else f"/{rel.parent.as_posix()}/"
    else:
        route = f"/{rel.as_posix()}"
    return f"{prefix.rstrip('/')}{route}" if prefix else route


def collect_onout_root(urls: dict[str, SitemapUrl]) -> None:
    if not ONOUT_ROOT.exists():
        return
    for path in sorted(ONOUT_ROOT.rglob("*.html")):
        route = html_path_to_route(path, ONOUT_ROOT)
        if route and route.startswith("/promo/") and route.endswith(".html"):
            continue
        if route:
            add_url(urls, f"{ONOUT}{route}", path)


def is_public_astro_route(route: str) -> bool:
    if route.endswith(".html"):
        return False
    if route == "/":
        return True
    if route.startswith("/vibers/"):
        return True
    if route == "/simple-review-wordpress/":
        return True

    first_part = route.strip("/").split("/", 1)[0]
    return first_part in CMS_SLUGS


def load_astro_routes() -> list[dict[str, object]]:
    script = """
import { getStaticHtmlRoutes, sitemapAlternates } from './src/lib/static-html-routes.mjs';

const routes = await getStaticHtmlRoutes();
console.log(JSON.stringify(routes.map((item) => ({
  route: item.route,
  file: item.file,
  alternates: sitemapAlternates(item.route),
}))));
"""
    result = subprocess.run(
        ["node", "--input-type=module", "-e", script],
        cwd=VIBERS_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def normalize_alternates(raw: object) -> tuple[tuple[str, str], ...]:
    if not isinstance(raw, list):
        return ()
    alternates: list[tuple[str, str]] = []
    for item in raw:
        if (
            isinstance(item, list)
            and len(item) == 2
            and isinstance(item[0], str)
            and isinstance(item[1], str)
        ):
            alternates.append((item[0], item[1]))
    return tuple(alternates)


def collect_astro_routes(urls: dict[str, SitemapUrl]) -> None:
    if not VIBERS_ROOT.exists():
        return

    for item in load_astro_routes():
        route = item.get("route")
        file_path = item.get("file")
        if not isinstance(route, str) or not isinstance(file_path, str):
            continue
        if not is_public_astro_route(route):
            continue
        source = Path(file_path)
        if source.exists():
            add_url(
                urls,
                f"{ONOUT}{route}",
                source,
                normalize_alternates(item.get("alternates")),
            )

    # /simple-review/ intentionally stays out of the sitemap because nginx
    # redirects it to /. The clean review-service URL below is a legacy alias
    # configured explicitly in nginx and must remain canonical in search.
    code_review_path = VIBERS_ROOT / "blog" / "code-review-as-a-service" / "index.html"
    if code_review_path.exists():
        add_url(urls, f"{ONOUT}/code-review-as-a-service/", code_review_path)


def render_xml(urls: dict[str, SitemapUrl]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for item in sorted(urls.values(), key=lambda url: url.loc):
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(item.loc)}</loc>")
        lines.append(f"    <lastmod>{escape(item.lastmod)}</lastmod>")
        for language, href in item.alternates:
            lines.append(
                '    <xhtml:link rel="alternate" '
                f'hreflang="{escape(language)}" href="{escape(href)}"/>'
            )
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="/root/vibers/generated/onout-sitemap.xml",
        help="Path to write sitemap.xml",
    )
    args = parser.parse_args()

    urls: dict[str, SitemapUrl] = {}
    collect_onout_root(urls)
    collect_astro_routes(urls)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_xml(urls), encoding="utf-8")
    print(f"Wrote {len(urls)} URLs to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
