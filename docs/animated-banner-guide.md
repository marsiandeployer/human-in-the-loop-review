# Animated Banner Guide — SimpleReview Demo Banners

Инструкция по созданию анимированных баннеров в стиле SimpleReview для blog-статей и лендингов.

## ✅ Чеклист нового баннера

Перед публикацией обязательно проверить каждый пункт **в живом браузере**:

- [ ] Crosshair курсор появляется и проходит через поля (видны красные обводки)
- [ ] Курсор непрерывно движется без остановок на промежуточных элементах
- [ ] Cursor переключается с crosshair на arrow при достижении target
- [ ] Target подсвечивается оранжевой рамкой + badge "Selected"
- [ ] Popup появляется с набирающимся текстом
- [ ] Кнопка Fix it → спиннер → Done ✓
- [ ] Сайдбар открывается с PR-пузырями
- [ ] **Финальное состояние держится ≥3 секунд** (Done ✓ + сайдбар + PR)
- [ ] В captcha-слоте появляется виджет (Turnstile / нужный) в финальной фазе
- [ ] Прогрессбар заполняется и сбрасывается корректно
- [ ] Вайрфрейм покрывает весь сайт (nav + 2-колоночная панель справа)
- [ ] На мобильных (≤600px) вайрфрейм скрывается, форма на 100% ширины

> **Правило:** всегда открывать баннер в браузере (`file://` или live URL) и дождаться полного цикла (16s) перед сдачей. Скриншота недостаточно — нужно видеть анимацию в движении.

## Концепция

Баннер показывает рабочий процесс SimpleReview:
1. Crosshair курсор сканирует страницу — поля подсвечиваются красным
2. Курсор кликает на target — оранжевый border, badge "Selected"
3. Открывается попап с полем для комментария (текст «печатается»)
4. Пользователь нажимает Fix it → спиннер → Done ✓
5. Правый сайдбар открывается с результатом (PR)
6. В target-слоте появляется готовый виджет (e.g. Cloudflare Turnstile)
7. Финальное состояние держится ≥3 секунд

---

## Структура сайта внутри баннера

Сайт должен выглядеть как реальная страница — не просто форма на белом фоне:

```
┌─ .cap-nav (absolute, h:34px) ────────────────────────────────┐
│ [logo]  [link] [link] [link] [link]              [CTA btn]   │
├──────────────────────────────────────────────────────────────┤
│  .cap-form (left, ~220px)    │  .cap-wf (right, 2-col grid) │
│  ┌────────────────────────┐  │  ┌────────┐  ┌────────┐      │
│  │ h4 Contact us          │  │  │ card1  │  │ card2  │      │
│  │ label + input email    │  │  └────────┘  └────────┘      │
│  │ label + textarea       │  │  ┌──────────────────────┐    │
│  │ .cap-target [turnstile]│  │  │   map placeholder    │    │
│  │ button Send message    │  │  └──────────────────────┘    │
│  └────────────────────────┘  │  col1 text  │  col2 text     │
│                              │  [social]  [CTA]             │
└──────────────────────────────────────────────────────────────┘
```

### Обязательные элементы сайта

- **`.cap-nav`** — page nav bar (absolute, top:0, height:34px): logo + links + CTA
- **`.cap-form`** — форма с real-looking полями (не wireframe)
- **`.cap-wf`** — 2-column wireframe grid справа (`grid-template-columns: 1fr 1fr`)
- **`.cap-turnstile`** — виджет внутри `.cap-target`, появляется в Done-фазе

### Turnstile / виджет в финале

Добавить внутрь `.cap-target` (показывается при `opacity:1` в Done-фазе):

```html
<div class="cap-target">captcha goes here
  <div class="cap-turnstile">
    <div style="...cloudflare orange circle..."></div>
    <div style="font-size:7px;font-weight:600">✓ Verified<br>Cloudflare</div>
  </div>
</div>
```

```css
.cap-turnstile { position:absolute;inset:0;background:#fff;border-radius:3px;
  display:flex;align-items:center;justify-content:center;gap:5px;
  opacity:0;animation:tsVis 16s infinite }
@keyframes tsVis { 0%,59%{opacity:0} 63%,88%{opacity:1} 94%,100%{opacity:0} }
```

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

## Основные классы и тайминги (16-секундный цикл)

Цикл: **сканирование** (0-4.5s) → **действие** (4.5-10s) → **финальная пауза** (10-14s, ~4s держим результат) → **сброс** (14-16s).

| % времени | Секунды | Что происходит |
|-----------|---------|----------------|
| 0-3%      | 0-0.5s  | Crosshair курсор появляется вверху |
| 3-13%     | 0.5-2.1s| Курсор движется к email полю |
| 13-18%    | 2.1-2.9s| **Email подсвечивается красной рамкой** |
| 18-21%    | 2.9-3.4s| Курсор движется к textarea |
| 21-26%    | 3.4-4.2s| **Textarea подсвечивается красной рамкой** |
| 27-31%    | 4.3-5.0s| Курсор → target, переключается на arrow |
| 32-88%    | 5.1-14.1s| **Target: оранжевая рамка + "Selected"** |
| 38-88%    | 6.1-14.1s| Inline popup виден |
| 47-49%    | 7.5-7.8s | Fix it click |
| 48-61%    | 7.7-9.8s | Спиннер |
| 50-88%    | 8.0-14.1s| **Сайдбар открыт** |
| 59-88%    | 9.4-14.1s| **Done ✓ + PR-пузыри (~4.5s финальной паузы)** |
| 88-100%   | 14.1-16s | Сброс всего |

### Прогрессбар

Добавляется между `.cap-viewport` и `.cap-caption`:

```html
<div class="cap-progress"><div class="cap-progress-fill"></div></div>
```

```css
.cap-progress { height: 3px; background: rgba(255,255,255,0.08); }
.cap-progress-fill { height: 100%; background: #FF6B35; width: 0; animation: progFill 16s linear infinite; }
@keyframes progFill { 0%{width:0} 100%{width:100%} }
```

### Правило финальной паузы

Финальное состояние (Done ✓ + сайдбар + PR) должно держаться **не менее 3 секунд**. Все элементы финала должны иметь `opacity:1` в диапазоне `60-88%` (≥4.3 секунды в 16s цикле).

### Cursor: crosshair → arrow

Курсор содержит два SVG-элемента с независимыми анимациями:

```css
.cap-cross { animation: crossVis 13s infinite }  /* видим 0-35% */
.cap-arrow { animation: arrowVis 13s infinite }  /* видим 36-100% */

@keyframes crossVis { 0%,35%{opacity:1} 39%,100%{opacity:0} }
@keyframes arrowVis { 0%,35%{opacity:0} 39%,100%{opacity:1} }
```

HTML структура курсора:
```html
<div class="cap-cursor">
  <span class="cap-cross"><svg viewBox="0 0 24 24">
    <line x1="12" y1="3" x2="12" y2="21" stroke="#222" stroke-width="2" stroke-linecap="round"/>
    <line x1="3" y1="12" x2="21" y2="12" stroke="#222" stroke-width="2" stroke-linecap="round"/>
    <circle cx="12" cy="12" r="3.5" fill="none" stroke="#222" stroke-width="1.5"/>
  </svg></span>
  <span class="cap-arrow"><svg viewBox="0 0 24 24">
    <path d="M5 3l14 8-6 2-2 7-6-17z" fill="#1a1a1a" stroke="#fff" stroke-width="1.5"/>
  </svg></span>
</div>
```

### Красная обводка при сканировании

Добавить на input и textarea анимацию `outline`:

```css
.cap-form input[type=email] { animation: emailRed 13s infinite; outline-offset: 2px; }
@keyframes emailRed {
  0%,10%  { outline: none; box-shadow: none }
  14%,20% { outline: 2px solid #ef4444; box-shadow: 0 0 0 2px rgba(239,68,68,.12) }
  24%,100%{ outline: none; box-shadow: none }
}

.cap-form textarea { animation: taRed 13s infinite; outline-offset: 2px; }
@keyframes taRed {
  0%,22%  { outline: none; box-shadow: none }
  25%,31% { outline: 2px solid #ef4444; box-shadow: 0 0 0 2px rgba(239,68,68,.12) }
  35%,100%{ outline: none; box-shadow: none }
}
```

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

---

## Voiceover / Subtitle Timing (зашитые субтитры)

Каждый баннер должен содержать **скрытый JSON-блок с тайминговыми данными** для озвучки. Пользователь эти данные не видит — они зашиты в `<script type="application/json">` внутри `.cap-banner`.

### Формат

```html
<!-- Voiceover timing data for video/screen recording narration. Not shown to users.
     Extract: JSON.parse(document.getElementById('cap-voiceover').textContent) -->
<script type="application/json" id="cap-voiceover">
{
  "duration_s": 9,
  "loop": true,
  "notes": "Narration script aligned to CSS animation keyframes. t = seconds into loop.",
  "tracks": [
    {"t": 0.0, "voice": "Фраза в начале — описание контекста."},
    {"t": 0.7, "voice": "Что делает пользователь — курсор появляется."},
    {"t": 1.5, "voice": "Курсор движется к целевому элементу."},
    {"t": 2.0, "voice": "Элемент выделен."},
    {"t": 3.0, "voice": "Попап открылся — описываем поле ввода."},
    {"t": 4.5, "voice": "Текст комментария — то что пишет пользователь."},
    {"t": 5.0, "voice": "Нажатие Fix it."},
    {"t": 5.5, "voice": "Идёт создание PR..."},
    {"t": 7.0, "voice": "Готово — PR создан, сайдбар открылся."}
  ]
}
</script>
```

### Таблица тайминга (13-секундный цикл)

| Время (сек) | CSS keyframe % | Что происходит | Что говорит диктор |
|-------------|---------------|----------------|--------------------|
| 0.0 | 0% | Начало | Вводная фраза про инструмент |
| 0.5 | 4% | Crosshair появился | "Режим сканирования — цель не выбрана" |
| 1.8 | 14% | Курсор над email | "Email поле в зоне — красная рамка" |
| 3.3 | 25% | Курсор над textarea | "Textarea в зоне, но не то" |
| 4.6 | 37% | Cursor → arrow, клик по target | "Нашли — кликаем на captcha slot" |
| 5.9 | 46% | Элемент подсвечен оранжевым | "Выделен — оранжевая рамка" |
| 7.0 | 54% | Попап виден | Описание попапа |
| 8.5 | 65% | Текст напечатан | Озвучка текста комментария |
| 9.1 | 70% | Нажат Fix it | "Нажимаем Fix it" |
| 9.7 | 75% | Спиннер | "Создаётся PR..." |
| 11.2 | 86% | Done ✓ + сайдбар | Итог |

### Как извлечь субтитры

```js
// Прямо в DevTools или в скрипте генерации видео:
const data = JSON.parse(document.getElementById('cap-voiceover').textContent);
data.tracks.forEach(t => console.log(`[${t.t}s] ${t.voice}`));
```

Или из bash (для скрипта генерации):
```bash
node -e "
const html = require('fs').readFileSync('index.html','utf8');
const m = html.match(/<script type=\"application\/json\" id=\"cap-voiceover\">([\s\S]*?)<\/script>/);
const data = JSON.parse(m[1]);
data.tracks.forEach(t => console.log(t.t + 's: ' + t.voice));
"
```

### Правило для новых баннеров

- **Обязательно** добавлять `<script type="application/json" id="cap-voiceover">` внутрь `.cap-banner`
- `id` должен быть уникальным если несколько баннеров на странице: `cap-voiceover-2` и т.д.
- `t` = секунды от начала 9-секундного цикла (совпадает с % * 0.09 * duration_s)
- Озвучка пишется по-русски (для RU-видео) или по-английски (для EN-статей)

---

## Примеры адаптации под другие use-cases

| Статья | Элемент | Комментарий | Озвучка ключевой фразы (t≈4.5s) |
|--------|---------|-------------|----------------------------------|
| Add CAPTCHA | captcha slot | "Add Cloudflare Turnstile here" | "Add Cloudflare Turnstile CAPTCHA here." |
| Fix broken button | `.btn-submit` | "Button broken on mobile" | "Fix broken button on mobile." |
| Add alt text | `img.hero` | "Add alt text for accessibility" | "Add descriptive alt text to this image." |
| Fix layout | `.hero` | "Fix mobile layout" | "The hero section breaks on mobile. Fix it." |
| Add field | form area | "Add phone number field" | "Add a required phone number field to this form." |

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
