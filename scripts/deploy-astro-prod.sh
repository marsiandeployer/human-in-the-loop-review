#!/usr/bin/env bash
set -euo pipefail

cd /root/vibers

echo "Building Astro static site..."
npm run build:astro

echo "Regenerating combined production sitemap..."
timeout 30s python3 scripts/generate-onout-sitemap.py

echo "Validating nginx config..."
timeout 30s nginx -t

echo "Reloading nginx..."
timeout 30s systemctl reload nginx

echo "Running production smoke checks..."
timeout 90s bash scripts/smoke-prod-astro.sh

echo "Astro production deploy completed."
