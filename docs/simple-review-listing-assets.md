# SimpleReview — Listing Assets Pack

Готовый набор ассетов для заливки Chrome-расширения SimpleReview на каталоги (Chrome Web Store, AlternativeTo, Futurepedia, There's An AI For That, ProductHunt и т.д.).

> Это файл для **SimpleReview** — Chrome Extension: кликаешь элемент на сайте → AI-агент (Claude / Codex) открывает PR с фиксом.
> Для human-in-the-loop ревью Vibers (GitHub App) — см. `docs/listing-assets.md`.

---

## 1. Базовая информация

| Поле | Значение |
|------|----------|
| Product name | SimpleReview |
| Tagline (60 chars) | Click any issue on your site. Get a code fix as PR. |
| Tagline alt (80 chars) | Chrome extension that turns website feedback into real Pull Requests |
| Category (primary) | Developer Tools / Chrome Extension |
| Category (alt) | AI Tools, QA & Testing, Website Feedback |
| Pricing model | Free (BYO Claude Code / Codex) + optional hosted AI |
| Founded | 2025 |
| Languages | English, Russian |
| Platforms | Chrome Extension (Chromium / Edge) |

---

## 2. URLs

| Поле | URL |
|------|-----|
| Landing | https://onout.org/simple-review |
| Demo / interactive | https://onout.org/vibers/vibecheck |
| Chrome Web Store | (будет после публикации — placeholder) |
| GitHub | https://github.com/marsiandeployer/human-in-the-loop-review |
| Blog | https://onout.org/vibers/blog/ |
| Contact email | hello@onout.org |
| Product video (YouTube) | https://youtu.be/Qp_wiXltaQw |
| Demo: Remove Powered by Astra (YouTube) | https://youtu.be/FRdxDrELAko |

---

## 3. Pitch / Descriptions (по длине)

### Twitter (140 chars)
Click any bug on your live site. An AI agent (Claude or Codex) reads your repo, writes the fix, opens a real PR. Not just a screenshot.

### Short (160 chars — Chrome Web Store short, ProductHunt tagline)
Chrome extension for website feedback. Click any element, leave a comment — an AI agent opens a real Pull Request with the fix. Not just a screenshot tool.

### Medium (300 chars — AlternativeTo, Futurepedia)
SimpleReview is a Chrome extension that turns website feedback into real code fixes. Click any element on a live site, write what is wrong, pick Claude or Codex — the agent reads your repo, writes the patch, and opens a Pull Request on GitHub. Free with your own AI agent; hosted option available.

### Long (700 chars — Chrome Web Store long description)
SimpleReview is a Chrome extension for turning website feedback into real code fixes. Unlike Marker.io, Userback, or BugHerd — which just capture a screenshot and a comment, then dump it into your issue tracker — SimpleReview hands the feedback to an AI coding agent (Claude Code or Codex) that reads your repo, writes the patch, and opens a real Pull Request on GitHub.

Click any element on your live page, type what is broken or what you want changed, pick your agent, hit Fix it. Minutes later you have a PR to review and merge. Works on landing pages, WordPress / WooCommerce sites, SaaS dashboards, Chrome extensions — any web project with a Git repo. Free when you bring your own Claude Code or Codex; optional built-in AI mode with zero setup.

### Extra-long (1500 chars — G2 / Software Advice / Futurepedia)
SimpleReview is a Chrome extension that collapses the gap between "I see a bug on the live site" and "it is fixed in a PR". Traditional website feedback tools (Marker.io, Userback, BugHerd, Usersnap, Feedbucket) do one job: capture a screenshot with an annotation and send it to your issue tracker. Somebody still has to read the ticket, find the code, write the fix, and open a PR. SimpleReview does that last part for you.

How it works: install the Chrome extension, open your own site, click any element — a popup lets you write what is wrong or what you want, choose Claude Code or Codex as the agent, and hit Fix it. The extension sends the element selector, screenshot, and your comment to the agent. The agent reads your repo, locates the relevant file, writes the patch, runs a quick check, and opens a real Pull Request on GitHub. You get a notification with a PR link. Review, merge, ship.

Use cases:
- Landing page copy and layout tweaks — non-devs can file PR-ready fixes
- WordPress / WooCommerce bug fixes (e.g. "Add to cart shows Unavailable")
- SaaS dashboard bug reports with a one-click repro
- Chrome Extension and web-app feature requests with visual context
- Agencies collecting structured client feedback that becomes PRs

Free with your own Claude Code or Codex (BYO key / local agent). Optional hosted AI mode for one-click setup with no local install. Works on any site that has a connected Git repo.

---

## 4. Key features (bullet list)

- Click any element on a live page — extension captures selector + screenshot
- Write what is wrong / what you want changed
- Pick your AI agent: Claude Code or Codex (OpenAI)
- Agent reads your repo, writes the patch, opens a real Pull Request
- Works on any web project with a GitHub repo
- "Fix it" button for auto-PR; "Comment only" for screenshot-style feedback
- BYO agent (free) or hosted AI mode (one-click)
- Multi-language UI: EN + RU
- Lightweight Chromium extension — no backend to self-host

---

## 5. Target audience / Who is it for

- Product managers filing bugs with visual context that become real PRs
- Designers and marketers who want to tweak landing copy without pinging devs
- Solo devs and indie hackers maintaining vibe-coded sites
- WordPress / WooCommerce shops fixing small bugs via AI
- Agencies collecting client feedback on staged sites
- QA engineers who want structured, repo-aware bug reports

---

## 6. Differentiators (vs alternatives)

| Competitor | They do | We do |
|-----------|---------|-------|
| Marker.io | Screenshot + annotation → issue tracker | Screenshot + annotation → real Pull Request |
| BugHerd | Pins feedback to page, syncs to Jira | Pins feedback → AI agent writes fix → PR |
| Userback | Visual feedback widget | Visual feedback → AI-coded PR |
| Usersnap | Screenshot + video feedback | Same + AI writes the actual code fix |
| Feedbucket | Bug reports with console logs | Same + agent opens PR in your repo |
| Marker.io + ChatGPT | Copy bug text, ask AI to fix, paste back | One click: element → PR |

Используй для "SimpleReview vs X" страниц и сравнительных полей. Уже есть блог-статьи: `/vibers/blog/markerio-alternative`, `/vibers/blog/markerio-vs-vibers`, `/vibers/blog/usersnap-alternative`.

---

## 7. Tags / Keywords (для каталогов с тегами)

```
chrome-extension, website-feedback, bug-reporting, visual-feedback,
ai-tools, claude, codex, openai, pull-request, github, automation,
developer-tools, qa-testing, vibe-coding, no-code-fixes,
alternative-to-marker-io, alternative-to-usersnap, alternative-to-bugherd,
alternative-to-userback, wordpress, woocommerce, indie-hackers
```

---

## 8. Pricing блок

- Free — Bring your own Claude Code or Codex; unlimited use
- Hosted AI — optional one-click mode, no local agent required (paid)

Точные цифры — см. https://onout.org/simple-review#pricing (обновляется).

---

## 9. Visual assets (пути и публичные URL)

Marketplace/Kwork cover variants for CMS-fix services are documented separately:
[marketplace-cover-banners.md](marketplace-cover-banners.md). Source HTML files are kept in
`/root/kwork/cover-html/*.html`; final cover PNGs are in `/root/kwork/covers/*.png`.

| Asset | Public URL | Use |
|-------|------------|-----|
| Demo: comment → PR (1) | https://i.wpmix.net/image/photo/image_2026-04-19_18-15-44_1776611748531.png | screenshot: popup on landing |
| Demo: PR opened (2) | https://i.wpmix.net/image/photo/image_2026-04-19_18-16-17_1776611778828.png | screenshot: GitHub PR view |
| Demo: WordPress/WooCommerce use case | https://i.wpmix.net/image/photo/image_2026-04-20_10-07-11_1776668832499.png | screenshot: "Unavailable despite in stock" |
| Demo: Feature request flow | https://i.wpmix.net/image/photo/image_2026-04-20_10-10-53_1776669053918.png | screenshot: dashboard use case |
| Demo: Search transactions | https://i.wpmix.net/image/photo/image_2026-04-20_10-11-02_1776669063234.png | screenshot: feature tag |

Рекомендуемый порядок скриншотов в Chrome Web Store / галерее каталога:
1. Extension icon + popup on a live page (click any element)
2. Comment + agent picker (Claude / Codex) + Fix it button
3. PR opened on GitHub with the patch
4. Deploy result + metric (CTR +18%)
5. Use-case variant (WordPress / WooCommerce bug fix)

Chrome Web Store требует: 128×128 icon, 440×280 promo tile, минимум 1280×800 скриншоты (до 5).
Если каталог требует видео — 30-секундный screencast по тем же 5 шагам.

---

## 10. Founder / Maker bio (для ProductHunt, Indie Hackers)

Hi, I am Alex — I build developer tools at Noxon Digital Factory. SimpleReview came out of maintaining a bunch of small WordPress and landing sites: every feedback tool captured the bug nicely, then expected a human to read the ticket, find the code, and write the fix. With Claude Code and Codex around, that last mile can be an AI agent. So we built the extension: click any element on your live site, say what is wrong, pick your agent, and get a real PR back. Free with your own agent. Happy to answer anything in the comments.

---

## 11. FAQ блок

**Q: Does it actually write code or just capture feedback?**
It writes code. The agent (Claude or Codex) reads your repo, writes the patch, and opens a Pull Request on GitHub.

**Q: Do I need an API key?**
For the free tier — yes, BYO Claude Code or Codex (local or API). Hosted AI mode removes this.

**Q: Which sites does it work on?**
Any site with a connected Git repo. Works on landing pages, WordPress / WooCommerce, SaaS apps, Chrome extensions in dev mode.

**Q: Is it a Marker.io replacement?**
Only if your goal is PRs, not tickets. Marker.io is great for reporting bugs to a human dev team; SimpleReview is for teams willing to let an AI agent write the fix.

**Q: Is it safe to let AI write to my repo?**
It opens a Pull Request — you review and merge as usual. No direct commits to main.

**Q: Can I use only the "comment" feature without AI?**
Yes. Use Comment-only mode — it captures the selector + screenshot + comment and pushes to an issue tracker, no PR opened.

---

## 12. Submission checklist (один раз перед заливкой)

- [ ] 128×128 extension icon готов
- [ ] 440×280 promo tile (для Chrome Web Store) готов
- [ ] 5 скриншотов 1280×800 в правильном порядке
- [ ] Короткий и длинный pitch скопированы из этого файла
- [ ] Tags / keywords скопированы
- [ ] Pricing блок актуален (свериться с лендингом)
- [ ] Demo-ссылка работает: https://onout.org/vibers/vibecheck
- [ ] UTM-источник в URL: `?utm_source=<directory>&utm_medium=listing`

UTM пример для Futurepedia: `https://onout.org/simple-review?utm_source=futurepedia&utm_medium=listing`

---

## 13. Где использовать (приоритет)

1. **Chrome Web Store** — первичная дистрибуция, обязательна
2. **AlternativeTo** (issue #26) — категории: Marker.io alternative, Userback alternative, BugHerd alternative
3. **Futurepedia / There's An AI For That / Toolify.ai** — AI-каталоги, отдельный профиль
4. **ProductHunt / BetaList / Peerlist** — launch-площадки
5. **Indie Hackers / Hacker News** — dev-комьюнити

---

## Известные проблемы при регистрации

**Capterra — нет России и Армении в списке стран (2026-04-20)**
При заполнении профиля вендора Capterra не предлагает ни Россию, ни Армению в дропдауне стран.
Как следствие — нет возможности указать местный номер телефона.
Решение: выбрать другую страну (например, Georgia/Грузия или Cyprus) или пропустить поле телефона если оно не обязательное.

**G2 — проблемы с авторизацией (2026-04-20)**
При попытке войти или зарегистрироваться на G2 возникают проблемы с авторизацией.
Статус: не решено, требует дальнейшего исследования.

**AlternativeTO — период охлаждения 7 дней (2026-04-21)**
После создания аккаунта на AlternativeTO нельзя сразу добавить продукт — действует период охлаждения 7 дней.
Плановая дата сабмита: 2026-04-28 (вторник).
