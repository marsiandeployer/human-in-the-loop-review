# Marketplace Cover Banners

Reference for Kwork and similar marketplace cover banners for CMS/site-fix services.

## Current Source

The current approved banner style is stored in the Kwork workspace:

| Asset | Path | Notes |
|------|------|-------|
| Generator | `/root/kwork/generate-cms-covers.js` | Generates all CMS cover variants |
| HTML sources | `/root/kwork/cover-html/*.html` | Editable/generated HTML source for each banner |
| Final PNG covers | `/root/kwork/covers/*.png` | Uploaded marketplace covers |
| Cover rules | `/root/kwork/docs/marketplace-covers.md` | Canonical format and QA notes |
| Contact sheet | `/root/kwork/screenshots/covers_contact_sheet_660.png` | Quick visual review of all covers |

Keep the HTML sources. They are useful as reusable marketplace-cover variants even though they are generated artifacts.

## HTML Banner Variants

Current variants:

| Variant | HTML source | Final PNG |
|---------|-------------|-----------|
| WordPress | `/root/kwork/cover-html/wordpress.html` | `/root/kwork/covers/wordpress.png` |
| 1C-Bitrix | `/root/kwork/cover-html/bitrix.html` | `/root/kwork/covers/bitrix.png` |
| Magento 2 | `/root/kwork/cover-html/magento.html` | `/root/kwork/covers/magento.png` |
| Joomla | `/root/kwork/cover-html/joomla.html` | `/root/kwork/covers/joomla.png` |
| PrestaShop | `/root/kwork/cover-html/prestashop.html` | `/root/kwork/covers/prestashop.png` |
| CS-Cart | `/root/kwork/cover-html/cs-cart.html` | `/root/kwork/covers/cs-cart.png` |
| Webasyst / Shop-Script | `/root/kwork/cover-html/webasyst.html` | `/root/kwork/covers/webasyst.png` |
| OpenCart | `/root/kwork/cover-html/opencart.html` | `/root/kwork/covers/opencart.png` |
| Shopware 6 | `/root/kwork/cover-html/shopware.html` | `/root/kwork/covers/shopware.png` |
| Drupal | `/root/kwork/cover-html/drupal.html` | `/root/kwork/covers/drupal.png` |

## Approved Style

- Canvas: `660x440` PNG for Kwork.
- Safe zone: keep meaningful text at least `28-30px` from edges.
- Layout: left side contains the direct promise; right side shows proof/process.
- Core message: `Проблема -> Работа -> Фикс`.
- Headline pattern: `Проблема? Починю.`
- Include the CMS logo/name as an immediate first-screen signal.
- Use the SimpleReview-like browser/card composition: restrained white, orange, black, and only small CMS accent colors.
- Avoid unclear AI-art banners; the buyer should understand the offer in one glance.

## Reuse Notes

Use these HTML banners as the starting point for future marketplace covers:

1. Copy an existing HTML file from `/root/kwork/cover-html/`.
2. Change the CMS/product name, logo block, accent color, and process text.
3. Regenerate a `660x440` PNG with the existing generator pattern.
4. Inspect the individual PNG and contact sheet before upload.

For final Kwork uploads, avoid wider formats such as `800x464`, because Kwork listing previews can crop the sides.
