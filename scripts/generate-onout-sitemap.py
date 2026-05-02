#!/usr/bin/env python3
"""Generate onout.org sitemap from nginx-served static routes."""

from __future__ import annotations

import argparse
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
)
RU_CMS_SLUGS = {"bitrix", "webasyst"}

ROOT_HTML_ALLOWLIST = {"index.html"}
SKIP_NAMES = {
    "404.html",
    "ci-status.html",
    "googleb0ef9bfd96887057.html",
    "index_static.html",
}
SKIP_PARTS = {"chicken_files"}


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
        if route:
            add_url(urls, f"{ONOUT}{route}", path)


def collect_vibers_alias(urls: dict[str, SitemapUrl]) -> None:
    if not VIBERS_ROOT.exists():
        return

    # /vibers/ remains a public nginx alias for the Vibers product and blog.
    for path in sorted((VIBERS_ROOT / "blog").rglob("index.html")):
        route = html_path_to_route(path, VIBERS_ROOT, prefix="/vibers")
        if route:
            add_url(urls, f"{ONOUT}{route}", path)
    index_path = VIBERS_ROOT / "index.html"
    if index_path.exists():
        add_url(urls, f"{ONOUT}/vibers/", index_path)

    # Clean product routes configured explicitly in nginx.
    for clean_slug in ("simple-review", "simple-review-wordpress"):
        path = VIBERS_ROOT / clean_slug / "index.html"
        if path.exists():
            add_url(urls, f"{ONOUT}/{clean_slug}/", path)

    code_review_path = VIBERS_ROOT / "blog" / "code-review-as-a-service" / "index.html"
    if code_review_path.exists():
        add_url(urls, f"{ONOUT}/code-review-as-a-service/", code_review_path)

    # Clean CMS routes from nginx regex. RU files are excluded from onout sitemap;
    # their canonical public URLs live on habab.ru.
    for slug in CMS_SLUGS:
        cms_root = VIBERS_ROOT / slug
        if not cms_root.exists():
            continue
        alternates: tuple[tuple[str, str], ...] = ()
        if slug in RU_CMS_SLUGS:
            alternates = (
                ("en", f"{ONOUT}/{slug}/"),
                ("ru", f"{HABAB}/{slug}/"),
                ("x-default", f"{ONOUT}/{slug}/"),
            )
        for path in sorted(cms_root.rglob("index.html")):
            route = html_path_to_route(path, VIBERS_ROOT)
            if route:
                add_url(urls, f"{ONOUT}{route}", path, alternates if path.parent == cms_root else ())


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
    collect_vibers_alias(urls)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_xml(urls), encoding="utf-8")
    print(f"Wrote {len(urls)} URLs to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
