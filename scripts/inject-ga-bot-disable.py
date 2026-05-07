#!/usr/bin/env python3
"""Inject GA4 bot/headless disable snippet before every gtag.js loader.

GA4 honours window['ga-disable-{MEASUREMENT_ID}']=true if set BEFORE gtag.js
loads. We use this to suppress events from headless Chrome / Puppeteer /
Playwright sessions our agents drive against onout.org.

Idempotent: looks for the marker comment and skips files already patched.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

MARKER = "<!-- ga-bot-disable v1 -->"

SNIPPET = (
    f'{MARKER}\n'
    '<script>(function(){var d=navigator.webdriver===true;'
    'if(!d&&navigator.userAgent){'
    'd=/HeadlessChrome|Puppeteer|Playwright|PhantomJS|Selenium|Bot|crawler|spider/i'
    '.test(navigator.userAgent);}'
    'if(!d&&location.search.indexOf("nogtag=1")>-1)d=true;'
    'if(d){window["ga-disable-G-LQLZ1SZS26"]=true;'
    'window["ga-disable-G-R05C1YP0CP"]=true;}})();</script>\n'
)

# Match: <script async src="https://www.googletagmanager.com/gtag/js?id=G-..."
GTAG_LOADER_RE = re.compile(
    r'(\s*)(<script\s+async\s+src="https://www\.googletagmanager\.com/gtag/js\?id=G-[A-Z0-9]+"></script>)',
    re.IGNORECASE,
)


def patch(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return "skip-already-patched"
    m = GTAG_LOADER_RE.search(text)
    if not m:
        return "skip-no-gtag-loader"
    indent = m.group(1).split("\n")[-1]
    new = GTAG_LOADER_RE.sub(
        lambda mm: f"{mm.group(1)}{SNIPPET.strip()}\n{indent}{mm.group(2)}", text, count=1
    )
    path.write_text(new, encoding="utf-8")
    return "patched"


def main() -> int:
    roots = [Path("/root/vibers"), Path("/var/www/onout.org")]
    skip_parts = {".git", ".claude", "node_modules", "chicken_files"}
    counts = {"patched": 0, "skip-already-patched": 0, "skip-no-gtag-loader": 0}
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*.html"):
            if any(part in skip_parts for part in p.parts):
                continue
            verdict = patch(p)
            counts[verdict] = counts.get(verdict, 0) + 1
            if verdict == "patched":
                print(f"  patched: {p}")
    print()
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
