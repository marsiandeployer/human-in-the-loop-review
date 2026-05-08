#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-https://onout.org}"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

fetch() {
  local path="$1"
  local output="$2"
  local status
  status="$(timeout 20s curl -k -sSL -o "$output" -w "%{http_code}" "${BASE_URL}${path}")"
  [[ "$status" == "200" ]] || fail "${path} returned HTTP ${status}"
}

contains() {
  local file="$1"
  local pattern="$2"
  local label="$3"
  rg -q "$pattern" "$file" || fail "Missing ${label}"
}

not_contains() {
  local file="$1"
  local pattern="$2"
  local label="$3"
  if rg -q "$pattern" "$file"; then
    fail "Unexpected ${label}"
  fi
}

check_html() {
  local path="$1"
  local title_pattern="$2"
  local canonical="$3"
  local output="$TMP_DIR/$(echo "$path" | tr '/.' '__').html"

  fetch "$path" "$output"
  contains "$output" "$title_pattern" "${path} title/content marker"
  contains "$output" "rel=\"canonical\" href=\"${canonical}\"" "${path} canonical"
}

check_headers_have_last_modified() {
  local path="$1"
  local headers="$TMP_DIR/$(echo "$path" | tr '/.' '__').headers"
  timeout 20s curl -k -sSI "${BASE_URL}${path}" > "$headers"
  contains "$headers" '^last-modified:' "${path} Last-Modified header"
}

check_html "/" 'SimpleReview' "${BASE_URL}/"
check_headers_have_last_modified "/"

check_html "/vibers/" 'Human-in-the-Loop Code Review' "${BASE_URL}/vibers/"
check_headers_have_last_modified "/vibers/"

check_html "/vibers/blog/" 'Vibers Blog' "${BASE_URL}/vibers/blog/"
check_html "/bitrix/" 'Bitrix' "${BASE_URL}/bitrix/"
check_html "/webasyst/" 'Webasyst' "${BASE_URL}/webasyst/"
check_html "/simple-review-wordpress/" 'WordPress' "${BASE_URL}/simple-review-wordpress/"

blog_file="$TMP_DIR/blog.html"
fetch "/blog/" "$blog_file"
contains "$blog_file" 'Blog — Onout' "/blog/ legacy marker"
not_contains "$blog_file" 'Vibers Blog' "/blog/ serving Vibers blog"

dao_file="$TMP_DIR/dao.html"
fetch "/dao/" "$dao_file"
contains "$dao_file" 'DAO' "/dao/ legacy marker"

skill_file="$TMP_DIR/skill.md"
fetch "/vibers/SKILL.md" "$skill_file"
contains "$skill_file" 'name: vibers' "/vibers/SKILL.md content"

asset_file="$TMP_DIR/vibers-logo-source.jpg"
fetch "/vibers/assets/vibers-logo-source.jpg" "$asset_file"
asset_size="$(wc -c < "$asset_file")"
[[ "$asset_size" -gt 10000 ]] || fail "Logo asset is unexpectedly small: ${asset_size} bytes"

health_file="$TMP_DIR/health.json"
fetch "/vibers/health" "$health_file"
contains "$health_file" 'ok' "/vibers/health response"

sitemap_file="$TMP_DIR/sitemap.xml"
fetch "/sitemap.xml" "$sitemap_file"
sitemap_count="$(rg -c '<loc>' "$sitemap_file")"
[[ "$sitemap_count" -ge 200 ]] || fail "Sitemap has too few URLs: ${sitemap_count}"
contains "$sitemap_file" "<loc>${BASE_URL}/</loc>" "root URL in sitemap"
contains "$sitemap_file" "<loc>${BASE_URL}/vibers/</loc>" "Vibers URL in sitemap"
contains "$sitemap_file" "<loc>${BASE_URL}/vibers/blog/</loc>" "Vibers blog URL in sitemap"
contains "$sitemap_file" "<loc>${BASE_URL}/bitrix/</loc>" "Bitrix URL in sitemap"
contains "$sitemap_file" "<loc>${BASE_URL}/blog/</loc>" "legacy blog URL in sitemap"
contains "$sitemap_file" "<loc>${BASE_URL}/dao/</loc>" "legacy DAO URL in sitemap"
not_contains "$sitemap_file" "<loc>${BASE_URL}/simple-review/</loc>" "redirecting /simple-review/ URL in sitemap"
not_contains "$sitemap_file" "<loc>${BASE_URL}/blog/ai-code-review-bots-miss-bugs/" "Vibers blog under legacy /blog/"

echo "Production Astro smoke passed for ${BASE_URL} (${sitemap_count} sitemap URLs)."
