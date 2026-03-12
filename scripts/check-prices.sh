#!/bin/bash
# Pre-commit hook: verify prices match between SKILL.md, index.html, and README.md
# Also warns about description sync.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SKILL="$REPO_ROOT/SKILL.md"
INDEX="$REPO_ROOT/index.html"
README="$REPO_ROOT/README.md"

errors=0

# --- Price checks ---

# Extract promo price from SKILL.md
skill_promo=$(grep -oP '\$\d+/hour' "$SKILL" | head -1)
skill_standard=$(grep -oP '\$\d+/hour' "$SKILL" | tail -1)

# Extract promo price from index.html (from the price-amount div)
index_promo=$(grep -oP '\$\d+ <small>/ hour' "$INDEX" | head -1 | grep -oP '\$\d+')
index_standard=$(grep -oP '\$\d+ <small>/ hour' "$INDEX" | tail -1 | grep -oP '\$\d+')

# Extract prices from README.md
readme_promo=$(grep -oP '\$\d+/hour' "$README" | head -1)
readme_standard=$(grep -oP '\$\d+/hour' "$README" | tail -1)

# Normalize
skill_promo_num=$(echo "$skill_promo" | grep -oP '\d+')
skill_standard_num=$(echo "$skill_standard" | grep -oP '\d+')
readme_promo_num=$(echo "$readme_promo" | grep -oP '\d+')
readme_standard_num=$(echo "$readme_standard" | grep -oP '\d+')

if [ "$index_promo" != "\$$skill_promo_num" ]; then
    echo "ERROR: Promo price mismatch — index.html ($index_promo) != SKILL.md ($skill_promo)"
    errors=1
fi

if [ "$index_standard" != "\$$skill_standard_num" ]; then
    echo "ERROR: Standard price mismatch — index.html ($index_standard) != SKILL.md ($skill_standard)"
    errors=1
fi

if [ "$skill_promo_num" != "$readme_promo_num" ]; then
    echo "ERROR: Promo price mismatch — SKILL.md ($skill_promo) != README.md ($readme_promo)"
    errors=1
fi

if [ "$skill_standard_num" != "$readme_standard_num" ]; then
    echo "ERROR: Standard price mismatch — SKILL.md ($skill_standard) != README.md ($readme_standard)"
    errors=1
fi

if [ $errors -eq 0 ]; then
    echo "Price check passed: promo=$index_promo, standard=$index_standard"
fi

# --- Description sync warning ---
# Check if any of the 3 content files were modified
STAGED=$(git diff --cached --name-only)
modified_count=0
for f in index.html SKILL.md README.md; do
    if echo "$STAGED" | grep -q "^${f}$"; then
        modified_count=$((modified_count + 1))
    fi
done

if [ $modified_count -gt 0 ] && [ $modified_count -lt 3 ]; then
    echo ""
    echo "WARNING: You modified $modified_count of 3 content files."
    echo "  Keep descriptions in sync across: index.html, SKILL.md, README.md"
    echo "  (This is a warning, not blocking the commit.)"
    echo ""
fi

exit $errors
