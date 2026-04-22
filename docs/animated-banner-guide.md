# Animated Banner Guide — SimpleReview Demo Banners

Инструкция по созданию анимированных баннеров в стиле SimpleReview для blog-статей и лендингов.

## Концепция

Баннер показывает рабочий процесс SimpleReview:
1. Курсор наводится на элемент страницы → элемент подсвечивается
2. Открывается попап с полем для комментария (текст «печатается»)
3. Пользователь нажимает Fix it → спиннер → Done ✓
4. Правый сайдбар мгновенно открывается с результатом (PR)

---

## Структура баннера

```
┌─ .cap-chrome ─────────────────────────────────────────────┐
│  • • •   your-site.com/...                     [favicon]  │
├─ .cap-viewport ──────────────────────────────────────────────┤
│  .cap-site                         │  .cap-sidebar (right)  │
│  ┌─ .cap-form ─┐  .cap-wf (декор)  │  SimpleReview AI      │
│  │  ... поля   │  ░░░░░░░          │  [selected element]   │
│  │  [target]◄──┼── курсор          │  user: "add X here"   │
│  └─────────────┘                   │  bot: ✓ PR #N         │
│  [inline-popup] Fix it→spinner→done│                       │
├─ .cap-caption ────────────────────────────────────────────────┤
│           Hover · comment · Fix it · get a real PR          │
└───────────────────────────────────────────────────────────────┘
```

---

## Основные классы и тайминги (9-секундный цикл)

| % времени | Что происходит |
|-----------|----------------|
| 0-8%      | Курсор появляется вверху |
| 8-20%     | Курсор движется к целевому элементу |
| 16-70%    | Элемент подсвечивается оранжевой рамкой + label "Selected" |
| 27-93%    | Inline popup виден |
| 33-93%    | Текст в попапе типирован |
| 55-56%    | Fix it click — кнопка переходит в спиннер |
| 56-93%    | Сайдбар справа мгновенно открывается |
| 77-93%    | Кнопка показывает "Done ✓" |
| 72-93%    | Чат-пузыри в сайдбаре |

---

## Адаптация под новый use-case

### 1. Выбрать целевой элемент

Замените `.cap-target` на нужный элемент формы:

```html
<!-- Поле email вместо captcha -->
<div class="cap-target">email field</div>

<!-- Кнопка -->
<div class="cap-target">submit button</div>

<!-- Блок с текстом -->
<div class="cap-target">hero headline</div>
```

### 2. Изменить комментарий в попапе

```html
<div class="cap-popup-ta">
  Add Cloudflare Turnstile here<span class="cap-blink">|</span>
</div>
```
Замените текст на описание нужного исправления.

### 3. Изменить результат в сайдбаре

```html
<div class="cap-bubble-user">Fix the broken layout</div>
<div class="cap-bubble-pr">✓ PR #42 — Layout fixed</div>
```

### 4. Изменить selected element info

```html
<div class="cap-el-tag">div.hero h1</div>
<div class="cap-el-text">Hero headline</div>
```

### 5. Рассчитать позицию курсора

Курсор позиционируется абсолютно внутри `.cap-site` (padding:16px).

Формула для `top` центра целевого элемента:
```
top = 16 (padding)
    + border(1) + padding-form(14)
    + высота каждого элемента формы до target
    + height/2 целевого элемента
```

Формула для `left` центра формы (220px wide):
```
left = 16 (padding) + 1 (border) + 14 (form-padding) + 95 (half of 190px content)
     ≈ 126px
```

Пример для captcha slot в текущей форме:
- `left:118px; top:182px` — центр слота
- `left:104px; top:278px` — центр Fix it кнопки

### 6. Изменить wireframe (декоративные блоки справа)

```html
<div class="cap-wf">
  <div class="cap-wf-line" style="width:75%"></div>
  <div class="cap-wf-line" style="width:100%"></div>
  <!-- для изображения: -->
  <div class="cap-wf-img"></div>
</div>
```

---

## Генерация OG-изображения

OG-image — это скриншот `og-banner.html` (статичная версия, без анимаций).

В `og-banner.html` показывать **финальное состояние**: сайдбар открыт, кнопка "Done ✓", курсор у целевого элемента.

### Команда для генерации:

```bash
node /tmp/gen-og.js
```

Скрипт `/tmp/gen-og.js`:
```js
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');

const fileUrl = 'file:///root/vibers/blog/YOUR-ARTICLE/og-banner.html';
const outPath = '/root/vibers/blog/YOUR-ARTICLE/og-image.png';

function cdpPut(path) {
  return new Promise((res, rej) => {
    const opts = { hostname: 'localhost', port: 9223, path, method: 'PUT' };
    const req = http.request(opts, r => {
      let d = ''; r.on('data', c => d += c);
      r.on('end', () => res(JSON.parse(d)));
    });
    req.on('error', rej); req.end();
  });
}

async function main() {
  const tab = await cdpPut('/json/new?' + encodeURIComponent(fileUrl));
  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  let id = 1;
  const send = (m, p) => new Promise((res) => {
    const _id = id++;
    ws.once('message', function onMsg(data) {
      const msg = JSON.parse(data);
      if (msg.id === _id) res(msg.result);
      else ws.once('message', onMsg);
    });
    ws.send(JSON.stringify({ id: _id, method: m, params: p || {} }));
  });
  ws.on('open', async () => {
    await new Promise(r => setTimeout(r, 2000));
    await send('Emulation.setDeviceMetricsOverride', {
      width: 1200, height: 630, deviceScaleFactor: 1, mobile: false
    });
    await new Promise(r => setTimeout(r, 500));
    const { data } = await send('Page.captureScreenshot', {
      format: 'png', clip: { x: 0, y: 0, width: 1200, height: 630, scale: 1 }
    });
    fs.writeFileSync(outPath, Buffer.from(data, 'base64'));
    console.log('OK: ' + outPath);
    ws.close();
    http.get({ hostname: 'localhost', port: 9223, path: '/json/close/' + tab.id }, () => {});
    process.exit(0);
  });
}
main();
```

---

## Примеры use-cases

| Статья | Целевой элемент | Комментарий в попапе |
|--------|-----------------|----------------------|
| Add CAPTCHA | `captcha goes here` | "Add Cloudflare Turnstile here" |
| Fix broken button | `.btn-submit` | "Button is broken on mobile" |
| Add alt text | `img.hero` | "Add alt text for accessibility" |
| Fix typo | `h1.headline` | "Typo: 'occured' → 'occurred'" |
| Add missing field | form area | "Add phone number field" |

---

## Файловая структура нового баннера

```
blog/
  your-article/
    index.html       ← статья + анимированный баннер (копировать секцию .cap-banner)
    og-banner.html   ← статичная версия для скриншота
    og-image.png     ← сгенерированный скриншот (1200×630)
```

Копировать секцию `/* ───────── Animated Captcha Banner ───────── */` из `blog/add-captcha-to-website/index.html` и адаптировать.
