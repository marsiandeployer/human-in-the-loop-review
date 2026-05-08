#!/usr/bin/env python3
"""Inspect onout.org URLs in Google Search Console and verify live status."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from google.oauth2 import service_account
from googleapiclient.discovery import build


DEFAULT_SITE = "sc-domain:onout.org"
DEFAULT_SITEMAP = "https://onout.org/sitemap.xml"
DEFAULT_KEY = "/root/mycity2_key.json"
URLSET_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


@dataclass(frozen=True)
class LiveResult:
    status: int
    final_url: str
    canonical: str


def fetch_sitemap_urls(sitemap_url: str) -> list[str]:
    request = urllib.request.Request(
        sitemap_url,
        headers={"User-Agent": "Mozilla/5.0 onout-gsc-audit/1.0"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = response.read()
    root = ET.fromstring(data)
    return [
        loc.text.strip()
        for loc in root.findall(".//sm:loc", URLSET_NS)
        if loc.text and loc.text.strip()
    ]


def build_service(key_path: str):
    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=scopes,
    )
    return build("searchconsole", "v1", credentials=credentials, cache_discovery=False)


def search_analytics_pages(service: Any, site_url: str, days: int) -> list[str]:
    end = date.today()
    start = end - timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["page"],
        "rowLimit": 25000,
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
    pages: list[str] = []
    for row in response.get("rows", []):
        keys = row.get("keys", [])
        if keys and isinstance(keys[0], str) and keys[0].startswith("https://onout.org"):
            pages.append(keys[0])
    return sorted(set(pages))


def search_analytics_rows(service: Any, site_url: str, days: int) -> list[dict[str, Any]]:
    end = date.today()
    start = end - timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["page"],
        "rowLimit": 25000,
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
    rows: list[dict[str, Any]] = []
    for row in response.get("rows", []):
        keys = row.get("keys", [])
        if not keys or not isinstance(keys[0], str):
            continue
        page = keys[0]
        if not page.startswith("https://onout.org"):
            continue
        rows.append(
            {
                "url": page,
                "clicks": row.get("clicks", 0),
                "impressions": row.get("impressions", 0),
                "ctr": row.get("ctr", 0),
                "position": row.get("position", 0),
            }
        )
    return sorted(rows, key=lambda item: (-item["impressions"], item["url"]))


def inspect_url(service: Any, site_url: str, url: str) -> dict[str, Any]:
    body = {"inspectionUrl": url, "siteUrl": site_url, "languageCode": "en-US"}
    response = service.urlInspection().index().inspect(body=body).execute()
    result = response.get("inspectionResult", {}).get("indexStatusResult", {})
    return {
        "url": url,
        "verdict": result.get("verdict", ""),
        "coverageState": result.get("coverageState", ""),
        "indexingState": result.get("indexingState", ""),
        "robotsTxtState": result.get("robotsTxtState", ""),
        "googleCanonical": result.get("googleCanonical", ""),
        "userCanonical": result.get("userCanonical", ""),
        "lastCrawlTime": result.get("lastCrawlTime", ""),
        "pageFetchState": result.get("pageFetchState", ""),
    }


def live_check(url: str) -> LiveResult:
    command = [
        "curl",
        "-k",
        "-sSL",
        "--max-time",
        "20",
        "-o",
        "/tmp/gsc-onout-live.html",
        "-w",
        "%{http_code} %{url_effective}",
        url,
    ]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    output = completed.stdout.strip()
    status_text, _, final_url = output.partition(" ")
    try:
        status = int(status_text)
    except ValueError:
        status = 0
    html = Path("/tmp/gsc-onout-live.html").read_text(encoding="utf-8", errors="ignore")
    match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html)
    canonical = match.group(1) if match else ""
    return LiveResult(status=status, final_url=final_url, canonical=canonical)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-url", default=DEFAULT_SITE)
    parser.add_argument("--sitemap", default=DEFAULT_SITEMAP)
    parser.add_argument("--key", default=DEFAULT_KEY)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--limit", type=int, default=0, help="Limit inspected URLs for debugging")
    parser.add_argument("--inspection-limit", type=int, default=0, help="Run slow URL Inspection API for the first N URLs")
    parser.add_argument("--sleep", type=float, default=0.12, help="Delay between URL Inspection calls")
    parser.add_argument("--output-dir", default="logs/gsc-onout")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    service = build_service(args.key)
    sitemap_urls = fetch_sitemap_urls(args.sitemap)
    analytics_rows = search_analytics_rows(service, args.site_url, args.days)
    analytics_urls = [item["url"] for item in analytics_rows]
    urls = sorted(set(sitemap_urls) | set(analytics_urls))
    if args.limit:
        urls = urls[: args.limit]

    inspected: list[dict[str, Any]] = []
    inspection_urls = urls[: args.inspection_limit] if args.inspection_limit else []
    for index, url in enumerate(inspection_urls, start=1):
        try:
            row = inspect_url(service, args.site_url, url)
        except Exception as exc:
            row = {
                "url": url,
                "verdict": "API_ERROR",
                "coverageState": str(exc)[:500],
                "indexingState": "",
                "robotsTxtState": "",
                "googleCanonical": "",
                "userCanonical": "",
                "lastCrawlTime": "",
                "pageFetchState": "",
            }
        inspected.append(row)
        if index % 25 == 0:
            print(f"Inspected {index}/{len(inspection_urls)}", file=sys.stderr)
        time.sleep(args.sleep)

    live_by_url: dict[str, LiveResult] = {}
    for index, url in enumerate(urls, start=1):
        live_by_url[url] = live_check(url)
        if index % 50 == 0:
            print(f"Live checked {index}/{len(urls)}", file=sys.stderr)

    json_path = output_dir / "gsc-onout-index-report.json"
    csv_path = output_dir / "gsc-onout-index-report.csv"
    analytics_path = output_dir / "gsc-onout-search-analytics-pages.csv"
    summary_path = output_dir / "gsc-onout-summary.json"

    json_path.write_text(json.dumps(inspected, ensure_ascii=False, indent=2), encoding="utf-8")
    with analytics_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["url", "clicks", "impressions", "ctr", "position", "inSitemap"])
        writer.writeheader()
        sitemap_set = set(sitemap_urls)
        for item in analytics_rows:
            writer.writerow({**item, "inSitemap": item["url"] in sitemap_set})

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "url",
                "verdict",
                "coverageState",
                "indexingState",
                "robotsTxtState",
                "pageFetchState",
                "googleCanonical",
                "userCanonical",
                "lastCrawlTime",
                "inSitemap",
                "searchImpressions",
                "searchClicks",
                "liveStatus",
                "liveFinalUrl",
                "liveCanonical",
            ],
        )
        writer.writeheader()
        inspected_by_url = {item["url"]: item for item in inspected}
        analytics_by_url = {item["url"]: item for item in analytics_rows}
        sitemap_set = set(sitemap_urls)
        for url in urls:
            item = inspected_by_url.get(
                url,
                {
                    "url": url,
                    "verdict": "",
                    "coverageState": "",
                    "indexingState": "",
                    "robotsTxtState": "",
                    "pageFetchState": "",
                    "googleCanonical": "",
                    "userCanonical": "",
                    "lastCrawlTime": "",
                },
            )
            live = live_by_url.get(url, LiveResult(0, "", ""))
            analytics = analytics_by_url.get(url, {})
            writer.writerow(
                {
                    **item,
                    "inSitemap": url in sitemap_set,
                    "searchImpressions": analytics.get("impressions", 0),
                    "searchClicks": analytics.get("clicks", 0),
                    "liveStatus": live.status,
                    "liveFinalUrl": live.final_url,
                    "liveCanonical": live.canonical,
                }
            )

    summary = {
        "siteUrl": args.site_url,
        "sitemapUrlCount": len(sitemap_urls),
        "analyticsUrlCount": len(analytics_urls),
        "checkedUrlCount": len(urls),
        "inspectedUrlCount": len(inspected),
        "byVerdict": {},
        "byCoverageState": {},
        "liveCheckedCount": len(live_by_url),
        "liveFailures": [
            {"url": url, "status": live.status, "finalUrl": live.final_url}
            for url, live in live_by_url.items()
            if live.status != 200
        ],
        "outputs": {
            "json": str(json_path),
            "csv": str(csv_path),
            "analyticsCsv": str(analytics_path),
        },
    }
    analytics_set = set(analytics_urls)
    sitemap_set = set(sitemap_urls)
    summary["analyticsUrlsNotInSitemap"] = sorted(analytics_set - sitemap_set)
    summary["sitemapUrlsWithoutAnalyticsRows"] = len(sitemap_set - analytics_set)
    for item in inspected:
        summary["byVerdict"][item["verdict"]] = summary["byVerdict"].get(item["verdict"], 0) + 1
        state = item["coverageState"]
        summary["byCoverageState"][state] = summary["byCoverageState"].get(state, 0) + 1
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
