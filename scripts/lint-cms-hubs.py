#!/usr/bin/env python3
"""Validate CMS marketplace hub i18n, SEO links, and animated banners."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


CMS_HUBS = {
    "wordpress": {"ru": False},
    "bitrix": {"ru": True},
    "magento": {"ru": False},
    "joomla": {"ru": False},
    "prestashop": {"ru": False},
    "cs-cart": {"ru": False},
    "webasyst": {"ru": True},
    "opencart": {"ru": False},
    "shopware": {"ru": False},
    "drupal": {"ru": False},
}

ONOUT = "https://onout.org"
HABAB = "https://habab.ru"


def fail(errors: list[str], path: Path | str, message: str) -> None:
    errors.append(f"{path}: {message}")


def read(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(errors, path, "missing file")
    return ""


def attr(html: str, pattern: str) -> str | None:
    match = re.search(pattern, html, flags=re.I | re.S)
    return match.group(1).strip() if match else None


def json_ld_blocks(html: str) -> list[dict]:
    blocks: list[dict] = []
    for match in re.finditer(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html,
        flags=re.I | re.S,
    ):
        raw = match.group(1).strip()
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            blocks.extend(item for item in parsed if isinstance(item, dict))
        elif isinstance(parsed, dict):
            blocks.append(parsed)
    return blocks


def validate_json_ld(
    html: str,
    expected_language: str,
    expected_url: str,
    path: Path,
    errors: list[str],
) -> None:
    blocks = json_ld_blocks(html)
    by_type = {block.get("@type"): block for block in blocks}

    for schema_type in ("BlogPosting", "FAQPage"):
        block = by_type.get(schema_type)
        if not block:
            fail(errors, path, f"missing {schema_type} JSON-LD block")
            continue
        if block.get("inLanguage") != expected_language:
            fail(errors, path, f"{schema_type} inLanguage must be {expected_language}")

    blog = by_type.get("BlogPosting", {})
    if blog.get("url") and blog.get("url") != expected_url:
        fail(errors, path, f"BlogPosting url must be {expected_url}")
    main_entity = blog.get("mainEntityOfPage")
    if isinstance(main_entity, dict) and main_entity.get("@id") != expected_url:
        fail(errors, path, f"BlogPosting mainEntityOfPage @id must be {expected_url}")


def validate_common(
    html: str,
    path: Path,
    slug: str,
    language: str,
    canonical: str,
    ru_enabled: bool,
    errors: list[str],
) -> None:
    html_lang = attr(html, r"<html[^>]+lang=[\"']([^\"']+)[\"']")
    if html_lang != language:
        fail(errors, path, f"html lang must be {language}, got {html_lang!r}")

    actual_canonical = attr(html, r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']')
    if actual_canonical != canonical:
        fail(errors, path, f"canonical must be {canonical}, got {actual_canonical!r}")

    og_url = attr(html, r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\']([^"\']+)["\']')
    if og_url != canonical:
        fail(errors, path, f"og:url must be {canonical}, got {og_url!r}")

    validate_json_ld(html, language, canonical, path, errors)

    if not re.search(r'id=["\']sc-[a-z0-9-]*banner-fallback["\']', html):
        fail(errors, path, "missing sc-* banner fallback element")
    if not re.search(r'sc-[a-z0-9-]*banner', html):
        fail(errors, path, "missing .sc-* banner markup/styles")
    if not re.search(r'sc-[a-z0-9-]*progress-fill', html):
        fail(errors, path, "missing animated banner progress bar")
    if "IntersectionObserver" not in html:
        fail(errors, path, "missing banner restart IntersectionObserver")
    if "28s" not in html:
        fail(errors, path, "banner must use the 28s animation cycle")

    alternates = dict(
        re.findall(
            r'<link[^>]+rel=["\']alternate["\'][^>]+hreflang=["\']([^"\']+)["\'][^>]+href=["\']([^"\']+)["\']',
            html,
            flags=re.I,
        )
    )
    expected_en = f"{ONOUT}/{slug}/"
    if ru_enabled:
        expected_ru = f"{HABAB}/{slug}/"
        for lang, url in (("en", expected_en), ("ru", expected_ru), ("x-default", expected_en)):
            if alternates.get(lang) != url:
                fail(errors, path, f"hreflang {lang} must be {url}, got {alternates.get(lang)!r}")
    elif "ru" in alternates:
        fail(errors, path, "EN-only hub must not expose ru hreflang until RU page is published")


def validate_hub(root: Path, slug: str, config: dict, errors: list[str]) -> None:
    en_path = root / slug / "index.html"
    en_html = read(en_path, errors)
    if not en_html:
        return

    ru_enabled = bool(config["ru"])
    en_url = f"{ONOUT}/{slug}/"
    validate_common(en_html, en_path, slug, "en", en_url, ru_enabled, errors)

    if ru_enabled:
        ru_path = root / slug / "index.ru.html"
        ru_html = read(ru_path, errors)
        if ru_html:
            ru_url = f"{HABAB}/{slug}/"
            validate_common(ru_html, ru_path, slug, "ru", ru_url, True, errors)
            if ru_url not in en_html:
                fail(errors, en_path, f"visible RU switch must link to {ru_url}")
            if en_url not in ru_html:
                fail(errors, ru_path, f"visible EN switch must link to {en_url}")
    elif (root / slug / "index.ru.html").exists():
        fail(errors, root / slug / "index.ru.html", "unexpected RU page for EN-only hub")


def fetch(url: str) -> tuple[int | None, str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "cms-hub-linter/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.getcode()
            body = response.read(200_000).decode("utf-8", errors="replace")
            final_url = response.geturl()
            return status, final_url, body
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), ""
    except Exception as exc:  # noqa: BLE001
        return None, url, str(exc)


def validate_live(errors: list[str]) -> None:
    onout_sitemap_status, _, onout_sitemap = fetch(f"{ONOUT}/sitemap.xml")
    if onout_sitemap_status != 200:
        fail(errors, f"{ONOUT}/sitemap.xml", f"sitemap must return 200, got {onout_sitemap_status}")

    habab_sitemap_status, _, habab_sitemap = fetch(f"{HABAB}/sitemap.xml")
    if habab_sitemap_status != 200:
        fail(errors, f"{HABAB}/sitemap.xml", f"sitemap must return 200, got {habab_sitemap_status}")

    for slug, config in CMS_HUBS.items():
        en_url = f"{ONOUT}/{slug}/"
        status, final_url, body = fetch(en_url)
        if status != 200:
            fail(errors, en_url, f"live EN must return 200, got {status} ({final_url})")
        elif f'<link rel="canonical" href="{en_url}">' not in body:
            fail(errors, en_url, "live EN canonical mismatch")
        if onout_sitemap_status == 200 and f"<loc>{en_url}</loc>" not in onout_sitemap:
            fail(errors, f"{ONOUT}/sitemap.xml", f"missing {en_url}")

        if config["ru"]:
            ru_url = f"{HABAB}/{slug}/"
            status, final_url, body = fetch(ru_url)
            if status != 200:
                fail(errors, ru_url, f"live RU must return 200, got {status} ({final_url})")
            elif f'<link rel="canonical" href="{ru_url}">' not in body:
                fail(errors, ru_url, "live RU canonical mismatch")
            if habab_sitemap_status == 200 and f"<loc>{ru_url}</loc>" not in habab_sitemap:
                fail(errors, f"{HABAB}/sitemap.xml", f"missing {ru_url}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--live", action="store_true", help="Also check production URLs")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors: list[str] = []
    for slug, config in CMS_HUBS.items():
        validate_hub(root, slug, config, errors)

    if args.live:
        validate_live(errors)

    if errors:
        print("CMS hub lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"CMS hub lint passed: {len(CMS_HUBS)} hubs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
