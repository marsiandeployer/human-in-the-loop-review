---
name: cms-docker-screenshots
description: >-
  Builds real CMS/application screenshots for SEO articles by running the target engine in Docker, navigating the actual admin/storefront screen with headless Puppeteer, validating the image visually, and saving only verified screenshots. Use when writing CMS/platform articles, landing pages, or banners that need real screenshots from WordPress, WooCommerce, Joomla, Drupal, PrestaShop, OpenCart, Magento, Shopware, Directus, Strapi, or similar engines.
---

# CMS Docker Screenshots

Use this skill whenever an article, landing page, or banner needs screenshots of a real CMS/application screen. Do not fake CMS UI with wireframes when the task calls for real screenshots.

## Core rule

Every screenshot must come from a running instance of the relevant engine, usually Docker. After capture, open the image and verify it shows the intended screen before using it in content, committing it, or sending it to Telegram.

If the screenshot does not show the exact screen discussed in the article, fix the environment/navigation/seed data and capture again.

## Workflow

1. **Define the target screen**
   - Identify CMS/app, version, article slug, and exact screen: storefront checkout, module settings, template editor, extension manager, admin error page, plugin config, etc.
   - Write down the intended visual proof in one sentence, for example: “WooCommerce checkout shows shipping notice and order total.”

2. **Create an isolated Docker workspace**
   - Use `/tmp/cms-screenshots/<article-slug>/` for compose files, DB volumes, and throwaway setup notes.
   - Prefer official images or official example compose files.
   - Pin versions when the article is version-specific.
   - Do not commit Docker volumes, DB dumps, generated passwords, or local compose secrets.

3. **Boot the engine**
   - Use `timeout` around setup and log commands.
   - Check readiness with HTTP and container logs, not blind sleeps.
   - If the app needs an installer, complete it once through CLI or browser automation.
   - Seed only the minimum realistic content needed for the screenshot.

4. **Capture with Puppeteer**
   - Always use the project browser defaults:

```javascript
const browser = await puppeteer.launch({
  headless: true,
  defaultViewport: { width: 1280, height: 800 },
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
});
```

   - Use `networkidle2` when opening pages.
   - Save screenshots under the article directory, usually:
     - `/root/vibers/<cms>/<article-slug>/screenshots/<short-name>.png`
     - or `/root/vibers/<cms>/<article-slug>/assets/<short-name>.png` if the article already uses `assets/`.
   - Prefer PNG for UI screenshots.

5. **Validate visually**
   - Open the screenshot with the image viewer tool before accepting it.
   - Check:
     - correct CMS/app and version context
     - correct screen/URL/admin section
     - target UI element is visible without scrolling ambiguity
     - no setup wizard, loading skeleton, login screen, cookie wall, or empty state unless the article is about that state
     - text is readable at article size
     - no accidental credentials, API keys, emails, or private URLs
   - If validation fails, recapture. Do not use “close enough” screenshots.

6. **Use in article and banner**
   - Add screenshots near the section that discusses that exact screen.
   - Add `alt` text describing the visible screen and the issue/fix.
   - Keep internal links between:
     - CMS hub: `/cms/`
     - article: `/cms/article-slug/`
     - related articles in the same CMS cluster
   - For animated banners, use `animated-banner` after screenshots are validated; real screenshots can be references, but the banner still needs its own visual QA.

7. **Record provenance**
   - Add a short HTML comment or article note only when useful:
     - CMS/app version
     - Docker image/tag
     - local route captured
   - Do not expose local credentials.

8. **Cleanup**
   - Stop containers when done unless the user asks to keep them running.
   - Leave only intentional article assets in the repo.

## Validation commands

Use these checks as a baseline:

```bash
timeout 30s docker compose ps
timeout 60s docker compose logs --tail=120
timeout 20s curl -fsS http://127.0.0.1:<port>/ >/dev/null
```

For browser capture, write a small one-off Puppeteer script or inline `node -e` command. It must fail non-zero on:
- navigation timeout
- console/page errors that indicate the target screen is broken
- screenshot file missing or too small
- target selector/text not found

## Acceptance checklist

- [ ] Docker instance is the target CMS/app, not a mock
- [ ] Screenshot shows the article’s exact screen
- [ ] Screenshot was opened and visually inspected
- [ ] No sensitive data visible
- [ ] Screenshot file is stored in the relevant article directory
- [ ] Article text references the screenshot naturally
- [ ] Internal links connect hub ↔ article ↔ related pages
- [ ] Animated banner, if present, was separately validated
- [ ] Containers stopped or explicitly left running for a reason

## Failure modes

Stop and report instead of fabricating screenshots when:
- the CMS cannot be installed or booted in Docker within the task budget
- the target screen requires a paid plugin/account/license not available locally
- sample data cannot reproduce the state discussed in the article
- visual validation shows a different screen than intended

