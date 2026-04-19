#!/usr/bin/env bash
# Lints the repo for any remaining "vibecheck" references that should be "SimpleReview".
# Exits 1 if any matches found. Run from repo root.
#
# Usage:
#   ./scripts/lint-vibecheck-rename.sh           # lint all tracked files
#   ./scripts/lint-vibecheck-rename.sh --staged  # lint only staged files (pre-commit use)

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

if [[ "${1:-}" == "--staged" ]]; then
  mapfile -t files < <(git diff --cached --name-only --diff-filter=ACM)
else
  mapfile -t files < <(git ls-files)
fi

# Skip the linter itself, the rename plan, and binary-ish assets.
filtered=()
for f in "${files[@]}"; do
  case "$f" in
    scripts/lint-vibecheck-rename.sh) continue ;;
    *.png|*.jpg|*.jpeg|*.gif|*.webp|*.ico|*.pdf|*.zip|*.woff*|*.ttf) continue ;;
  esac
  [[ -f "$f" ]] && filtered+=("$f")
done

[[ ${#filtered[@]} -eq 0 ]] && { echo "lint-vibecheck-rename: no files to scan"; exit 0; }

# Match "vibecheck" as a word/path segment (case-insensitive).
# Catches: vibecheck, VibeCheck, /vibecheck/, vibecheck.html, "vibecheck"
matches=$(grep -inE "vibecheck" "${filtered[@]}" 2>/dev/null || true)
path_matches=$(printf '%s\n' "${filtered[@]}" | grep -iE "(^|/)vibecheck($|/|[._-])" || true)

if [[ -z "$matches" && -z "$path_matches" ]]; then
  echo "lint-vibecheck-rename: OK (no vibecheck references found)"
  exit 0
fi

echo "lint-vibecheck-rename: FAIL — replace 'vibecheck' with 'SimpleReview' (or 'simple-review' for paths/URLs)"
echo

if [[ -n "$path_matches" ]]; then
  echo "Filenames/paths to rename:"
  echo "$path_matches" | sed 's/^/  /'
  echo
fi

if [[ -n "$matches" ]]; then
  echo "In-file references (file:line:content):"
  echo "$matches" | head -100 | sed 's/^/  /'
  total=$(echo "$matches" | wc -l)
  if (( total > 100 )); then
    echo "  ... and $((total - 100)) more"
  fi
fi

exit 1
