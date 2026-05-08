# Full article backlog (Phase 1 + missed-from-30K analysis)

Source data: 9 Semrush CSVs in `docs/keywords/` (8 from 2026-04-30 + WP from 2026-04-24).
Filter: vol ≥ 80, KD ≤ 30, deduplicated by topic-bucket.

## ✅ Tier 0 — shipped in c2c6c46 (10 articles)

| CMS | Slug |
|-----|------|
| bitrix | `bitrix/how-to-fix-and-customize-bitrix-sites/` |
| magento | `magento/how-to-fix-magento-2-issues/` |
| joomla | `joomla/how-to-fix-joomla-issues/` |
| prestashop | `prestashop/how-to-fix-prestashop-issues/` |
| shopware | `shopware/how-to-fix-shopware-6-issues/` |
| wordpress | `wordpress/how-to-fix-and-improve-wordpress-sites/` |
| opencart | `opencart/how-to-fix-opencart-issues/` |
| cs-cart | `cs-cart/how-to-fix-and-customize-cs-cart/` |
| webasyst | `webasyst/how-to-fix-and-customize-shop-script/` |
| drupal | `drupal/how-to-fix-drupal-issues/` |

## 🟢 Tier 1 — quick wins (31 articles, KD ≤ 15-25)

Cost: ~1-2 days. Target: ship-then-measure.

| ☐ | CMS | Slug | Title | Target KW | Vol | KD | Note |
|---|-----|------|-------|-----------|----:|---:|------|
| ☐ | wordpress | `wordpress-collapsible-info-block-tutorial` | Add a Collapsible Info Block to WordPress Forms | `collasable info wordpress forms` | 1900 | 5 | KD 5, opportunity gap |
| ☐ | wordpress | `how-to-make-clickable-phone-number-wordpress` | How to Make a Clickable Phone Number in WordPress | `how to make a clickable phone number wordpress` | 1300 | 14 | KD 14 |
| ☐ | magento | `magento-seo-services-without-agency` | Magento SEO Without an Agency Retainer | `magento seo expert` | 1600 | 8 | KD 4-11 |
| ☐ | magento | `magento-vs-shopify-stay-or-leave` | Magento vs Shopify: Stay-or-Leave Decision Guide | `magento vs shopify` | 1000 | 12 | KD 12-14 |
| ☐ | magento | `magento-1-to-2-migration-playbook` | Magento 1 → 2 Migration: The 2026 Playbook | `magento migration from 1 to 2` | 170 | 10 | KD 8-15 |
| ☐ | magento | `magento-to-shopify-migration-when-to-do-it` | Magento → Shopify Migration: When (Not) to Do It | `magento to shopify migration` | 590 | 9 | KD 9-26 |
| ☐ | drupal | `drupal-vs-wordpress-honest-tradeoffs` | Drupal vs WordPress: Honest Tradeoffs (2026) | `drupal vs wordpress` | 1600 | 22 | KD 20-22 |
| ☑ | drupal | `hire-drupal-developer-or-use-simplereview` | Hire a Drupal Developer or Use SimpleReview? | `hire drupal developer` | 320 | 4 | Published with Drupal-specific buyer guide, SimpleReview banner, and hub/internal links |
| ☐ | drupal | `wordpress-multisite-vs-drupal-multisite` | WordPress Multisite vs Drupal Multisite — Pros & Cons | `wordpress multisite vs drupal multisite comparison pros cons` | 590 | 0 | KD 0! |
| ☐ | drupal | `drupal-vs-sitecore` | Drupal vs Sitecore: Open-Source vs Enterprise DXP | `drupal vs sitecore` | 90 | 0 | KD 0! |
| ☐ | drupal | `drupal-7-eol-migration-path` | Drupal 7 EOL: Your Migration Path to Drupal 10/11 | `drupal 7 to 10 migration` | 140 | 21 | KD 16-21 |
| ☐ | opencart | `hire-opencart-developer-vs-no-code-fix` | Hire OpenCart Developer or Use SimpleReview? | `hire opencart developer` | 210 | 3 | KD 0-5 — almost empty SERP |
| ☐ | opencart | `opencart-meta-keywords-guide` | OpenCart Meta Keywords: SEO Guide for 3.x and 4.x | `opencart meta keywords` | 320 | 14 | KD 11-14 |
| ☐ | shopware | `shopware-vs-shopify-honest-comparison` | Shopware 6 vs Shopify: Honest Comparison | `shopware vs shopify` | 140 | 0 | KD 0-4 |
| ☐ | shopware | `cost-of-shopware-6-real-numbers` | Cost of Shopware 6 in 2026 — Real Numbers | `cost of shopware 6` | 590 | 16 | KD 16 |
| ☐ | shopware | `magento-to-shopware-migration-guide` | Magento → Shopware Migration Guide | `magento shopware migration` | 50 | 2 | KD 2-9 — very easy |
| ☐ | shopware | `shopware-agentur-oder-simplereview` | Shopware Agentur oder SimpleReview? (DE) | `shopware agentur` | 480 | 5 | KD 1-10 — DE market |
| ☑ | prestashop | `prestashop-stripe-double-charge-fix` | Fix the PrestaShop Stripe Double-Charge Bug | `prestashop stripe double charge` | 880 | 15 | Published 2026-05-02 with source research + SimpleReview animated banner |
| ☐ | prestashop | `prestashop-vs-bigcommerce` | PrestaShop vs BigCommerce | `prestashop vs bigcommerce` | 110 | 5 | KD 5 |
| ☐ | prestashop | `prestashop-vs-wordpress-when-each-wins` | PrestaShop vs WordPress: When Each Wins | `prestashop vs wordpress` | 110 | 3 | KD 3 |
| ☐ | prestashop | `prestashop-meta-keywords-guide` | PrestaShop Meta Keywords: Are They Still Worth It? | `prestashop meta keywords` | 390 | 11 | KD 11 |
| ☐ | prestashop | `hire-prestashop-developer-vs-simplereview` | Hire PrestaShop Developer vs SimpleReview | `hire prestashop developers` | 140 | 6 | KD 6-11 |
| ☑ | joomla | `joomla-extensions-search-errors-fix` | Joomla Extension "Searching for Errors" — Diagnose & Fix | `joomla: extension seaching for errors` | 2400 | 6 | Published 2026-05-08 with official Joomla research, real Joomla 5.4.5 Docker screenshots, SimpleReview animated banner video, and hub/internal links |
| ☑ | joomla | `joomla-form-errors-find-all` | How to Find All Form Errors on a Joomla Site | `joomla: how to find all form errors on a website` | 1900 | 7 | Published 2026-05-08 with official Joomla validation/debug research, real Joomla 5.4.5 contact-form error screenshots, SimpleReview animated banner video, and internal links |
| ☐ | joomla | `joomla-3-change-footer-template-js-unlimited` | Joomla 3: Change Footer Info in JS_Unlimited Template | `joomla 3: change footer info in template js_unlimited` | 720 | 9 | KD 9, vol 720 |
| ☑ | joomla | `joomla-4-to-5-upgrade-extension-issues` | Joomla 4 → 5 Upgrade: Extension Compatibility Fix | `joomla 4 to joomla 5 upgade extension` | 880 | 16 | Published 2026-05-08 with official Joomla migration/update-site research, real Joomla 5.4.5 extension screenshots, SimpleReview animated banner video, and internal links |
| ☐ | joomla | `joomla-imagick-php-module-not-loaded-fix` | Fix "Imagick PHP Module Not Loaded" on Joomla 3 | `automatic intro image: imagick php module not loaded joomla 3` | 720 | 16 | KD 16 |
| ☑ | joomla | `hire-joomla-developer-vs-simplereview` | Hire Joomla Developer or Use SimpleReview? | `hire joomla developer` | 210 | 5 | Published 2026-05-08 with Joomla service-provider/forum/update-site research, real Joomla 5.4.5 Docker screenshots, SimpleReview animated banner video, and hub/internal links |
| ☐ | bitrix | `тарифы-битрикс-24-сравнение` | Тарифы Битрикс 24: какой выбрать в 2026 | `тарифы битрикс 24` | 590 | 12 | KD 12-20 (RU) |
| ☐ | bitrix | `битрикс-резервное-копирование-полный-гид` | Резервное копирование Битрикс — полный гид 2026 | `битрикс резервное копирование` | 90 | 19 | KD 5-9 (RU) |
| ☐ | bitrix | `стоимость-разработки-битрикс-2026` | Сколько стоит разработка на Битрикс в 2026 | `стоимость разработки интернет магазина на битрикс` | 70 | 9 | KD 9-23 (RU) |

## 🟡 Tier 2 — pillar/comparison (38 articles, KD 15-30)

Cost: ~3-5 days. Target: pillar pages + service-intent CRO.

| ☐ | CMS | Slug | Title | Target KW | Vol | KD | Note |
|---|-----|------|-------|-----------|----:|---:|------|
| ☐ | wordpress | `wordpress-development-services-buyer-guide` | WordPress Development Services: Buyer's Guide 2026 | `wordpress development services` | 3600 | 23 | KD 23, vol 3600 |
| ☐ | wordpress | `wordpress-seo-services-vs-diy` | WordPress SEO Services vs DIY (When to Hire) | `wordpress seo services` | 3600 | 16 | KD 10-26, vol 1900-3600 |
| ☐ | wordpress | `is-wordpress-multisite-one-theme-or-many` | Is WordPress Multisite One Theme or Multiple? | `is wordpress multisite one theme or multiple` | 1900 | 11 | KD 11, vol 1900 |
| ☐ | wordpress | `clear-wordpress-cache-every-major-plugin` | Clear WordPress Cache (Every Major Plugin) | `clear wordpress cache` | 720 | 24 | KD 20-28 |
| ☐ | wordpress | `wordpress-speed-optimization-without-plugin` | WordPress Speed Optimization Without a Plugin | `wordpress speed optimization` | 1000 | 28 | KD 28 |
| ☐ | wordpress | `wordpress-maintenance-what-to-actually-do` | WordPress Maintenance: What to Actually Do | `wordpress maintenance` | 2900 | 24 | KD 24, vol 2900 |
| ☐ | wordpress | `squarespace-vs-wordpress-honest` | Squarespace vs WordPress: Honest 2026 Comparison | `squarespace vs wordpress` | 1900 | 24 | KD 21-24 |
| ☐ | wordpress | `wix-vs-wordpress-honest` | Wix vs WordPress: Real-World 2026 Comparison | `wix vs wordpress` | 1900 | 28 | KD 28 |
| ☐ | wordpress | `webflow-vs-wordpress-honest` | Webflow vs WordPress: Designer's Comparison | `webflow vs wordpress` | 1300 | 26 | KD 26 |
| ☐ | wordpress | `shopify-vs-wordpress-for-ecommerce` | Shopify vs WordPress for E-commerce | `shopify vs wordpress` | 720 | 24 | KD 24 |
| ☐ | magento | `magento-vs-woocommerce-when-each-wins` | Magento vs WooCommerce: When Each Wins | `magento vs woocommerce` | 480 | 25 | KD 25 |
| ☐ | magento | `shopify-plus-vs-magento` | Shopify Plus vs Magento (Adobe Commerce) | `shopify plus vs magento` | 320 | 16 | KD 16 |
| ☐ | magento | `bigcommerce-vs-magento` | BigCommerce vs Magento Open Source | `bigcommerce vs magento` | 260 | 15 | KD 15-24 |
| ☐ | magento | `magento-development-services-checklist` | Magento Development Services Buyer's Checklist | `magento development services` | 1900 | 29 | KD 16-29 |
| ☐ | magento | `magento-2-speed-optimization` | Magento 2 Speed Optimization (No Agency) | `magento performance optimization` | 210 | 14 | KD 14-20 |
| ☐ | magento | `magento-2-4-8-release-notes` | Magento 2.4.8 Release Notes & Breaking Changes | `magento 2.4.8` | 590 | 23 | KD 23 |
| ☐ | drupal | `drupal-development-services-buyer-guide` | Drupal Development Services: Buyer's Guide | `drupal development services` | 1300 | 20 | KD 20-30 |
| ☐ | drupal | `drupal-vs-joomla-2026` | Drupal vs Joomla in 2026 | `drupal vs joomla` | 170 | 18 | KD 18-23 |
| ☐ | drupal | `drupal-performance-optimization` | Drupal Performance Optimization Without Acquia | `drupal performance optimization` | 110 | 22 | KD 22-29 |
| ☐ | drupal | `drupal-tutorial-zero-to-deploy` | Drupal Tutorial: From Zero to Deployed Site | `drupal tutorial` | 260 | 24 | KD 21-24 |
| ☐ | joomla | `joomla-seo-complete-guide` | Joomla SEO: Complete 2026 Guide | `joomla seo` | 880 | 24 | KD 18-27 |
| ☐ | joomla | `joomla-sitemap-xml-setup` | Joomla Sitemap.xml Setup (Built-in + Plugins) | `joomla sitemap` | 320 | 22 | KD 18-22 |
| ☐ | joomla | `joomla-vs-wordpress-2026` | Joomla vs WordPress: 2026 Comparison | `joomla vs wordpress` | 590 | 26 | KD 22-30 |
| ☐ | joomla | `best-joomla-hosting-2026` | Best Joomla Hosting in 2026 | `best joomla hosting` | 170 | 18 | KD 18-20 |
| ☐ | joomla | `yoast-seo-on-joomla` | Yoast SEO on Joomla — Setup & Alternatives | `yoast seo joomla` | 260 | 23 | KD 23 |
| ☐ | prestashop | `prestashop-seo-complete-guide` | PrestaShop SEO: Complete 2026 Guide | `prestashop seo` | 720 | 20 | KD 17-20 |
| ☐ | prestashop | `prestashop-vs-woocommerce` | PrestaShop vs WooCommerce: Which to Pick | `prestashop vs woocommerce` | 320 | 26 | KD 16-26 |
| ☐ | prestashop | `prestashop-advanced-search-setup` | PrestaShop Advanced Search Setup | `advanced search prestashop` | 90 | 8 | KD 8-16 |
| ☐ | prestashop | `agence-seo-prestashop-vs-simplereview` | Agence SEO PrestaShop vs SimpleReview (FR) | `agence seo prestashop` | 170 | 9 | KD 0-23 |
| ☐ | opencart | `opencart-vs-shopify-honest` | OpenCart vs Shopify: Honest Comparison | `opencart vs shopify` | 70 | 5 | KD 5 |
| ☐ | opencart | `opencart-vs-woocommerce` | OpenCart vs WooCommerce | `opencart vs woocommerce` | 70 | 13 | KD 8-13 |
| ☐ | opencart | `opencart-development-services-buyer-guide` | OpenCart Development Services: Buyer's Guide | `opencart development services` | 260 | 17 | KD 8-17 |
| ☐ | opencart | `opencart-1-to-2-3-4-upgrade-paths` | OpenCart 2 → 3 → 4 Upgrade Paths | `upgrade opencart 2 to 3` | 40 | — | KD 4 |
| ☐ | shopware | `shopware-development-company-guide` | Shopware Development Company: How to Pick | `shopware development company` | 210 | 0 | KD 0-9 |
| ☐ | shopware | `shopware-6-demo-walkthrough` | Shopware 6 Demo Walkthrough — What to Look At | `shopware 6 demo` | 210 | 8 | KD 8 |
| ☐ | shopware | `magento-vs-shopware-pick-one` | Magento vs Shopware: Which Open-Source Stack? | `magento vs shopware` | 70 | 4 | KD 4-9 |
| ☐ | bitrix | `bitrix-разработчик-vs-simplereview` | Битрикс разработчик vs SimpleReview | `битрикс разработчик` | 110 | 24 | KD 12-24 (RU) |
| ☐ | bitrix | `настройка-битрикс-24-полный-гид` | Настройка Битрикс 24 — полный гид 2026 | `настройка битрикс 24` | 110 | 13 | KD 7-25 (RU) |

## 🔴 Tier 3 — programmatic / release-notes (6 articles)

⚠ Google March 2026 Core Update пенализит scaled-content abuse. Каждая статья должна нести Information Gain (original timing data, breaking-change summary, our own benchmarks). Без этого — не публиковать.

| ☐ | CMS | Slug | Title | Target KW | Vol | KD |
|---|-----|------|-------|-----------|----:|---:|
| ☐ | wordpress | `wordpress-6-8-2-release-notes` | WordPress 6.8.2 Release Notes — What Changed | `wordpress 6.8.2` | 1600 | 4 |
| ☐ | wordpress | `wordpress-6-8-1-release-notes` | WordPress 6.8.1 Release Notes & PHP Compat | `wordpress 6.8.1` | 1300 | 8 |
| ☐ | wordpress | `wordpress-6-7-release-news-recap` | WordPress 6.7: Release News Recap | `wordpress 6.7 release news` | 4400 | 30 |
| ☐ | wordpress | `wordpress-security-news-monthly-digest` | WordPress Security Digest — Monthly CVE Roundup | `wordpress security news` | 22200 | 18 |
| ☐ | drupal | `drupal-7-100-release-notes` | Drupal 7.100 Release Notes — What Changed | `drupal 7.100 release notes` | 90 | 26 |
| ☐ | drupal | `drupal-security-news-monthly` | Drupal Security Advisory — Monthly Digest | `drupal security news` | 320 | 38 |

## Summary

- Tier 0 (shipped): **10**
- Tier 1 (quick wins): **31**
- Tier 2 (pillars): **38**
- Tier 3 (programmatic, risky): **6**
- **Total backlog: 75 new articles**

## Что ещё НЕ покрыто (tail/long-tail)

Узкие сиды Semrush + Yandex Wordstat не запускались — даст ещё ~20-30 идей в категориях:
- Specific bug fixes (vol 30-80 диапазон): `magento setup:upgrade memory exhausted`, etc.
- Russian Wordstat data для Bitrix/Webasyst — semrush ru db даёт thin coverage
- Локализованные DE/FR/ES сайты для shopware/prestashop
- Plugin/extension-specific bugs (`elementor`, `divi`, `astra`, `yoast`)
