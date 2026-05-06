# Meta Ads CMS Creative Pack — 2026-05-05

Goal: test narrow CMS-specific audiences for SimpleReview. Message: click the visible problem on a site, describe the change, get a small fix that can be uploaded through Git, SFTP/SSH, or the normal deploy flow.

Do not use branch/review workflow language in ads. Keep the promise practical: small website fixes, not a replacement for a platform specialist.

## Global Controls

| Field | Value |
|-------|-------|
| Campaign | `onout.org | Direct site fixes | 2026-05` |
| Daily budget | `$5/day` |
| Default CTA | `Learn More` |
| Primary landing | `https://onout.org/simple-review/` |
| CMS landing UTM | `?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content={cms}_{angle}` |
| Tone | calm, concrete, owner-friendly |
| Avoid | hype, security-firm claims, guaranteed outcomes, "AI replaces developers" |

## Visual Templates

Use one of these visual systems per ad. Keep the image practical and readable on mobile.

| Template | Visual | Best for |
|----------|--------|----------|
| `click_to_fix` | Browser screenshot-style mockup. A cursor clicks a broken button, SimpleReview side panel shows "Fix it", bottom state shows "Ready to upload". | WordPress, WooCommerce, OpenCart, PrestaShop |
| `file_map` | Split screen: visible broken UI on left, highlighted platform file path on right. | Magento, Drupal, Joomla, Shopware, CS-Cart |
| `agency_queue` | Small task queue with three boring tickets: footer text, checkout label, mobile block. One is marked "fixed". | agencies and freelancers |
| `owner_waiting` | Site owner looking at a stale banner / wrong button in a browser admin, no decorative hero art. | non-technical owners |
| `self_hosted_console` | Admin/console style page with one obvious issue and a concise fix summary. | Discourse, Directus, Strapi, Payload |

## Priority Ads For Current Ad Sets

### WordPress

| Variant | Landing URL | Primary text | Headline | Description | Visual |
|---------|-------------|--------------|----------|-------------|--------|
| `wp_owner_small_fix` | `https://onout.org/wordpress/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=wordpress_owner_small_fix` | Small WordPress changes should not take a week. Click the broken text, banner, footer, or button. SimpleReview maps it to `wp-content`, prepares the fix, and you upload it through Git or SFTP. | Fix WordPress without waiting | Click any issue. Upload the fix. | `click_to_fix` |
| `wp_no_dev` | `https://onout.org/wordpress/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=wordpress_no_dev` | When the original WordPress developer is busy, the small fixes pile up: update nags, stale homepage text, broken mobile blocks. SimpleReview turns visible issues into focused site fixes. | WordPress site fixes, fast | For small UI and content edits. | `owner_waiting` |
| `wp_agency_queue` | `https://onout.org/wordpress/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=wordpress_agency_queue` | Agencies should not spend senior time on "hide this banner" and "rename this button" tickets. SimpleReview handles narrow WordPress edits so the team can stay on real engineering work. | Clear the boring WP queue | Site-ready fixes for small tasks. | `agency_queue` |

### WooCommerce

| Variant | Landing URL | Primary text | Headline | Description | Visual |
|---------|-------------|--------------|----------|-------------|--------|
| `woo_checkout` | `https://onout.org/woocommerce/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=woocommerce_checkout` | WooCommerce checkout issues are expensive when they sit in a queue. Click the broken cart, shipping notice, checkout label, or product block. Get a focused fix you can upload to the store. | Fix WooCommerce checkout UI | Click the issue. Get the fix. | `click_to_fix` |
| `woo_store_owner` | `https://onout.org/woocommerce/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=woocommerce_store_owner` | A product is in stock but the button says the wrong thing. A checkout note is stale. A theme override broke mobile. SimpleReview helps with the small WooCommerce fixes that do not need an agency call. | Small WooCommerce fixes | For store UI and template edits. | `owner_waiting` |
| `woo_agency` | `https://onout.org/woocommerce/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=woocommerce_agency` | Keep WooCommerce specialists on payment, tax, and subscription logic. Let SimpleReview turn simple template and copy tickets into upload-ready fixes. | Reduce WooCommerce ticket drag | For agencies and store teams. | `agency_queue` |

### Magento

| Variant | Landing URL | Primary text | Headline | Description | Visual |
|---------|-------------|--------------|----------|-------------|--------|
| `m2_owner` | `https://onout.org/magento/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=magento_owner` | Not every Magento change needs a $150/hr specialist. Click the broken newsletter block, footer text, breadcrumb, or layout issue. SimpleReview maps it to theme files and prepares a focused fix. | Fix Magento UI tweaks | Layout and template fixes. | `file_map` |
| `m2_file_map` | `https://onout.org/magento/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=magento_file_map` | Magento stores hide simple fixes in layout XML, `.phtml`, i18n CSV, and theme overrides. SimpleReview starts from the visible storefront problem and points the fix at the right file. | Magento fixes by visible issue | From storefront click to file edit. | `file_map` |
| `m2_agency` | `https://onout.org/magento/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=magento_agency` | Use senior Magento time for B2B logic, ERP, and checkout architecture. Use SimpleReview for the backlog of storefront text, theme, and layout cleanup. | Save Magento dev hours | Small storefront fixes first. | `agency_queue` |

## One-Creative Matrix For All Live Hubs

| CMS | Landing URL | Primary text | Headline | Description | Visual |
|-----|-------------|--------------|----------|-------------|--------|
| WordPress | `https://onout.org/wordpress/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=wordpress_matrix` | Click any visible WordPress issue: stale text, broken block, footer credit, mobile layout, admin nag. SimpleReview prepares a focused fix you can upload through Git or SFTP. | Fix WordPress site edits | No vague tickets. Just the fix. | `click_to_fix` |
| WooCommerce | `https://onout.org/woocommerce/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=woocommerce_matrix` | Click the broken WooCommerce cart, checkout, product template, or shipping notice. SimpleReview turns the visible issue into a site-ready fix. | Fix WooCommerce UI issues | Store fixes without agency delay. | `click_to_fix` |
| 1C-Bitrix | `https://onout.org/bitrix/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=bitrix_matrix` | Bitrix sites collect small template and content problems fast. Click the visible issue, describe the change, and get a focused fix for the site. | Fix Bitrix site tweaks | Small edits without long handoff. | `file_map` |
| Magento | `https://onout.org/magento/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=magento_matrix` | Click the visible Magento storefront problem. SimpleReview maps it to theme files, layout XML, templates, or translations and prepares a focused fix. | Fix Magento storefront issues | For small layout and copy edits. | `file_map` |
| Joomla | `https://onout.org/joomla/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=joomla_matrix` | Joomla template edits should not become a long support thread. Click the broken module, footer, menu, or layout block and get a fix you can upload. | Fix Joomla template issues | Click the problem. Get the fix. | `file_map` |
| PrestaShop | `https://onout.org/prestashop/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=prestashop_matrix` | Click the broken PrestaShop banner, hook block, checkout text, or theme issue. SimpleReview reads the store structure and prepares a focused site fix. | Fix PrestaShop store edits | Small store fixes, fewer delays. | `click_to_fix` |
| CS-Cart | `https://onout.org/cs-cart/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=cscart_matrix` | CS-Cart template and storefront tweaks often hide in `.tpl` files and addon overrides. Start from the visible problem and get a focused fix. | Fix CS-Cart storefront edits | Template fixes without a long queue. | `file_map` |
| Webasyst | `https://onout.org/webasyst/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=webasyst_matrix` | Shop-Script changes often sit between storefront templates, plugins, and old custom work. Click the visible issue and get a focused fix path. | Fix Webasyst store issues | For small Shop-Script edits. | `file_map` |
| OpenCart | `https://onout.org/opencart/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=opencart_matrix` | Click the broken OpenCart category, footer, checkout label, or theme block. SimpleReview maps it to Twig, language files, or modifications. | Fix OpenCart site tweaks | From storefront click to upload. | `click_to_fix` |
| Shopware | `https://onout.org/shopware/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=shopware_matrix` | Shopware theme and storefront issues should not block a release. Click the broken block, describe it, and get a focused fix for your store. | Fix Shopware storefront issues | Small fixes for store teams. | `file_map` |
| Drupal | `https://onout.org/drupal/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=drupal_matrix` | Click a broken Drupal block, Twig template issue, menu label, or theme problem. SimpleReview connects the visible issue to a focused file-level fix. | Fix Drupal site edits | For blocks, Twig, and theme UI. | `file_map` |
| MODX | `https://onout.org/modx/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=modx_matrix` | MODX sites often need small template, chunk, snippet, and content fixes. Click the visible issue and turn it into a focused site update. | Fix MODX site tweaks | Small CMS fixes, upload-ready. | `file_map` |
| Strapi | `https://onout.org/strapi/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=strapi_matrix` | When a Strapi admin or frontend content flow needs a small fix, start from the visible issue. SimpleReview prepares a focused change for the codebase. | Fix Strapi admin and UI issues | For code-accessible Strapi sites. | `self_hosted_console` |
| Directus | `https://onout.org/directus/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=directus_matrix` | Directus teams still get small admin, extension, and frontend issues. Click the visible problem and get a focused fix path instead of a vague ticket. | Fix Directus project issues | For admin and extension tweaks. | `self_hosted_console` |
| Craft CMS | `https://onout.org/craft-cms/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=craft_matrix` | Craft CMS sites live in Twig templates, fields, modules, and plugins. Click the visible issue and get a focused fix you can review and upload. | Fix Craft CMS site edits | Twig and plugin UI fixes. | `file_map` |
| Statamic | `https://onout.org/statamic/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=statamic_matrix` | Statamic changes often span Antlers templates, YAML, and content collections. Click the visible problem and get a focused fix for the site. | Fix Statamic site tweaks | Small edits without context loss. | `file_map` |
| Payload CMS | `https://onout.org/payload-cms/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=payload_matrix` | Payload projects move fast until a small admin, collection, or frontend issue blocks the team. Click the issue and turn it into a focused code fix. | Fix Payload CMS issues | Admin and collection fixes. | `self_hosted_console` |
| Umbraco | `https://onout.org/umbraco/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=umbraco_matrix` | Umbraco edits can hide in views, controllers, property editors, and theme files. Click the visible issue and get a focused fix path. | Fix Umbraco site edits | Small .NET CMS fixes. | `file_map` |
| nopCommerce | `https://onout.org/nopcommerce/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=nopcommerce_matrix` | Click a broken nopCommerce widget, checkout label, theme block, or plugin panel. SimpleReview maps the visible issue to a focused fix. | Fix nopCommerce store edits | For theme and plugin UI fixes. | `file_map` |
| DNN | `https://onout.org/dnn/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=dnn_matrix` | DNN portals collect small module, skin, and settings UI issues. Click the visible problem and get a focused fix your team can upload. | Fix DNN module and skin UI | Small portal fixes. | `file_map` |
| Concrete CMS | `https://onout.org/concrete-cms/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=concrete_matrix` | Concrete CMS sites need careful small fixes to blocks, packages, themes, and dashboard screens. Click the visible issue and keep the update focused. | Fix Concrete CMS blocks | Small fixes without losing editability. | `file_map` |
| TYPO3 | `https://onout.org/typo3/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=typo3_matrix` | TYPO3 sitepackage and extension edits can take too much context setup. Click the visible issue and get a focused fix for Fluid templates or configuration. | Fix TYPO3 sitepackage issues | For Fluid and extension UI. | `file_map` |
| Discourse | `https://onout.org/discourse/?utm_source=meta&utm_medium=cpc&utm_campaign=cms_fix&utm_content=discourse_matrix` | Discourse admins hit plugin, SSO, email, migration, and self-hosting issues that need focused fixes. Start from the error or admin screen and get the next change. | Fix Discourse admin issues | For self-hosted forum teams. | `self_hosted_console` |

## Channel Splits

Use separate ad names so spend can be read by CMS and angle.

| Channel | Ad naming pattern | Audience idea | Creative angle |
|---------|-------------------|---------------|----------------|
| `cms_owner` | `{cms} | owner | small fix` | CMS interest + site owner / ecommerce / small business | waiting on small site changes |
| `cms_agency` | `{cms} | agency | ticket queue` | CMS interest + web design / digital marketing / agency owner | reduce low-value ticket load |
| `cms_developer` | `{cms} | developer | file map` | CMS interest + web development / programming | visible UI mapped to correct files |
| `self_hosted` | `{platform} | admin | console` | self-hosted software, system admin, open source | admin issue to focused fix |

## Short Headlines Pool

Use these when Meta asks for extra headline variants.

| Angle | Headlines |
|-------|-----------|
| Owner | Fix site tweaks faster; Small website fixes; Get the site fix ready; Update the site without waiting |
| CMS-specific | Fix WordPress edits; Fix WooCommerce UI; Fix Magento storefront; Fix OpenCart templates; Fix Drupal blocks |
| Agency | Clear boring tickets; Reduce small-fix backlog; Keep seniors on hard work; Ship tiny fixes faster |
| Developer | From click to file edit; Map UI to code fast; Focused CMS file fixes; Less context setup |

## Descriptions Pool

| Description |
|-------------|
| Click a visible issue and get a focused fix. |
| Small CMS edits without the long handoff. |
| Works with Git, SFTP/SSH, or your deploy flow. |
| For theme, template, copy, and UI fixes. |
| Keep complex work for specialists. Automate the small stuff. |

## First Test Order

Start with the live ad sets we can explain cleanly:

1. WordPress owner small fix.
2. WooCommerce checkout.
3. Magento file map.
4. OpenCart matrix if Meta accepts the interest.
5. PrestaShop matrix if Meta accepts the interest.
6. Drupal file map if audience does not get rejected as too narrow.
7. Discourse only as retargeting or broader self-hosted/open-source audience.

Stop any ad after 300 impressions with zero outbound clicks. Duplicate winners by CMS, not by changing five variables at once.
