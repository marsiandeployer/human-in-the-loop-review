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

### WordPress-экосистема: добавлять WP Admin Bar

Если баннер показывает WordPress-сайт (WooCommerce, плагины, темы) — **обязательно** добавлять чёрную панель WordPress-администратора (`#wpadminbar`) в верх viewport-а баннера. Это делает сцену реалистичной (пользователь залогинен в WP) и соответствует тому, как разработчик видит свой сайт.

**HTML** (внутри `.sc-viewport`, перед `.sc-content-row`):
```html
<div class="sc-adminbar">
  <div class="sc-ab-left">
    <span class="sc-ab-wp">W</span>
    <span class="sc-ab-site">My WP Site</span>
    <span class="sc-ab-item">Edit site</span>
    <span class="sc-ab-cnt">3</span>
    <span class="sc-ab-item">🔍 AI Review</span>
  </div>
  <div class="sc-ab-right">
    <span class="sc-ab-item">Howdy, admin</span>
  </div>
</div>
```

**CSS**:
```css
.sc-viewport { display:flex; flex-direction:column; }
.sc-adminbar { background:#1d2327; height:26px; display:flex; align-items:center;
  justify-content:space-between; padding:0 8px; font-size:9px; color:#c3c4c7;
  flex-shrink:0; box-sizing:border-box; border-bottom:1px solid #2c3338; }
.sc-ab-left,.sc-ab-right { display:flex; align-items:center; gap:5px; }
.sc-ab-wp { color:#fff; font-size:12px; font-weight:900; opacity:.9; }
.sc-ab-site { color:#fff; font-weight:600; }
.sc-ab-cnt { background:#d63638; color:#fff; font-size:7px; padding:1px 3px;
  border-radius:8px; font-weight:700; min-width:12px; text-align:center; }
.sc-content-row { display:flex; flex:1; background:#fafafa; position:relative; }
```

**Пересчёт курсора**: adminbar добавляет +26px к top-координатам всех элементов внутри `.sc-content-row` (относительно `.sc-banner`). Всегда перемерять через CDP после добавления:
```js
document.querySelector('.sc-form').getBoundingClientRect()  // relative to viewport
// vs banner.getBoundingClientRect() → получить offset
```

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

### 2a. Структура попапа (comment + Fix it) — ОБЯЗАТЕЛЬНЫЙ блок

Попап появляется после того, как курсор кликнул на target и тот получил "Selected" badge. Внутри попапа: поле комментария с typewriter-анимацией + кнопка Fix it (текст → спиннер → Done).

**⚠️ Правило позиционирования: popup ВСЕГДА справа от выделенного элемента** — как в реальных code review инструментах (GitHub, Linear). НЕ ниже элемента.

**HTML:**

```html
<div class="cap-popup">
  <div class="cap-popup-hdr">
    <span>Comment</span>
    <span class="cap-popup-x">×</span>
  </div>
  <div class="cap-popup-ta">
    <span class="cap-ta-inner">{описание задачи}</span><span class="cap-blink">|</span>
  </div>
  <div class="cap-popup-fix">
    <span class="fxt">Fix it</span>
    <span class="fsp"><span class="fsp-icon">⟳</span></span>
    <span class="fdn">✓ Done</span>
  </div>
</div>
```

**CSS (ключевое):**

```css
/* Попап СПРАВА от selected-элемента. left = правый край формы + 10px зазор.
   Например, форма 360px + padding 18px → left:385px */
.cap-popup{position:absolute;left:385px;top:20px;width:210px;background:#fff;
  border:1px solid #ddd;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.18);
  padding:10px;z-index:6;opacity:0;animation:popupShow 14s infinite}
@keyframes popupShow{
  0%,19%   {opacity:0;transform:translateX(-6px)}  /* slide-in слева */
  20%,92%  {opacity:1;transform:translateX(0)}
  96%,100% {opacity:0}
}

/* Стрелочка СЛЕВА попапа — указывает влево на selected target */
.cap-popup::before{content:'';position:absolute;top:14px;left:-6px;width:10px;height:10px;
  background:#fff;border-top:1px solid #ddd;border-left:1px solid #ddd;transform:rotate(-45deg)}

/* Typewriter-эффект: текст набирается постепенно */
.cap-popup-ta{white-space:nowrap;overflow:hidden}
.cap-ta-inner{display:inline-block;overflow:hidden;white-space:nowrap;max-width:0;
  vertical-align:bottom;animation:typeText 14s infinite}
@keyframes typeText{0%,20%{max-width:0} 47%,92%{max-width:190px} 96%,100%{max-width:0}}

/* Fix it: 3 состояния в одной кнопке, каждое absolute inset:0 */
.fxt{animation:fxTxt 14s infinite}  /* "Fix it" текст */
.fsp{animation:fxSpin 14s infinite} /* спиннер */
.fdn{animation:fxDone 14s infinite} /* "✓ Done" */
@keyframes fxTxt {0%,52%{opacity:1} 55%,100%{opacity:0}}
@keyframes fxSpin{0%,54%{opacity:0} 57%,63%{opacity:1} 65%,100%{opacity:0}}
@keyframes fxDone{0%,63%{opacity:0} 66%,92%{opacity:1} 96%,100%{opacity:0}}
```

**Частые ошибки:**

- Попап снизу — неправильно. Попап всегда СПРАВА (см. правило выше).
- `left` считать от левого края `.cap-site` (или того positioned-предка, где лежит попап).
- Стрелочка `::before` с `rotate(-45deg)` + `border-top + border-left` = указывает влево. Для popups снизу (если нужно) — `rotate(45deg)` + `border-left + border-top` = указывает вверх.
- `cap-ta-inner` обязателен для typewriter — без него текст появляется мгновенно.
- Проверь что `.cap-popup-fix` имеет `position:relative` и `height:24px` фиксирован — иначе absolute-children (fxt/fsp/fdn) схлопнутся.

### 2b. Стартовый клик по extension иконке

Если хочешь показать: "пользователь кликает иконку SimpleReview в chrome bar → открывается sidebar":

1. **Добавь pulse вокруг иконки** в самом начале (0-6%):
   ```css
   .cap-ext-icon{animation:extPulse 14s infinite}
   @keyframes extPulse{
     0%,4%{box-shadow:0 0 0 0 rgba(255,107,53,.8)}
     2%  {box-shadow:0 0 0 6px rgba(255,107,53,0)}
     6%,100%{box-shadow:0 0 0 0 rgba(255,107,53,0)}
   }
   ```

2. **Вынеси cursor из `.cap-site` в root `.cap-banner`** (с `position:relative` на баннере).
   Тогда курсор может достать до chrome bar (extension icon).

3. **Первая точка курсора** — на иконке (top-right chrome bar):
   ```css
   @keyframes cCur{
     0%  {left:695px;top:12px;opacity:0}
     2%  {left:695px;top:12px;opacity:1}  /* click extension icon */
     7%  {left:695px;top:12px;opacity:1}  /* hold — sidebar opens */
     10% {left:80px;top:75px;opacity:1}   /* jump into page */
     ...
   }
   ```

4. **Sidebar reveal** (вместо translateX, проще через ::before overlay):
   ```css
   .cap-sidebar{position:relative}
   .cap-sidebar::before{content:'';position:absolute;inset:0;background:#fafafa;
     animation:sbReveal 14s infinite}
   @keyframes sbReveal{
     0%,4%{opacity:1}    /* сайдбар "закрыт" — серое покрытие */
     7%,95%{opacity:0}   /* overlay убран — контент виден */
     98%,100%{opacity:1}
   }
   ```
   Это проще чем transform:translateX — не ломает flex-лэйаут.

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

## Voiceover — OpenAI TTS

Голос генерируется через OpenAI TTS API (не espeak-ng — звучит слишком роботно).

### Выбор длины цикла

| Тип баннера | Цикл | Когда |
|-------------|------|-------|
| Простой (1-2 действия) | 14s | Быстрый demo-гиф стиль |
| **Сложный (3+ шага, нужно объяснение)** | **28s** | **По умолчанию для статей** |

Для 28s: меняй все `animation: X 14s infinite` → `28s infinite` (python replace `r'(\d+)s (infinite\|linear)'`).

### Скрипт генерации голоса

```python
import urllib.request, json, subprocess

OPENAI_API_KEY = "sk-..."  # из /root/aisell/botplatform/.env

# 4 сегмента для 28s баннера (delays в ms)
segments = [
    (600,  "Install the SimpleReview extension and click its icon"),
    (4800, "Select any element — like the slow checkout form"),
    (9500, "Leave a comment and click Fix it"),
    (18500,"An AI agent reviews your code and auto-deploys the fix"),
]

for i, (delay_ms, text) in enumerate(segments, 1):
    out = f"/tmp/vo{i}.mp3"
    payload = json.dumps({"model":"tts-1","input":text,"voice":"nova","speed":1.0}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=payload,
        headers={"Authorization":f"Bearer {OPENAI_API_KEY}","Content-Type":"application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        with open(out,"wb") as f: f.write(resp.read())
    dur = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration",
                          "-of","csv=p=0",out],capture_output=True,text=True).stdout.strip()
    print(f"VO{i} @{delay_ms}ms ends {delay_ms+int(float(dur)*1000)}ms: {text}")
```

### Таблица тайминга (28s цикл) — 3-click flow

| Delay (ms) | Анимация (%) | Что на экране | Текст голоса |
|------------|-------------|---------------|--------------|
| 600 | 2% | Курсор → extension icon | "Install the extension and click its icon" |
| 4800 | 17% | Cursor → форма | "Select any element — like the checkout form" |
| 9500 | 34% | Текст набран, Fix it виден | "Leave a comment and click Fix it" |
| 18500 | 66% | Done ✓ + сайдбар | "An AI agent reviews your code and auto-deploys the fix" |

### Правила тайминга (обязательно)

1. **Нет перекрытий** — каждый сегмент заканчивается до начала следующего. Проверяй: `delay + duration_ms < next_delay`
2. **VO опережает событие на ~0.5-1s** — голос начинается чуть раньше того, что показывается на экране
3. **Последний VO** заканчивается ≥ 5s до конца цикла (иначе слышно в начале следующего)
4. **Cursor → textarea перед набором текста**: добавь keyframe `23%{left:420px;top:120px}` — курсор должен переместиться в поле ДО начала typewriter-анимации

### Правило для новых баннеров

- Язык: **EN** для международных статей, RU только если сайт на русском
- Голос: `nova` (EN женский, чёткий) или `alloy` (нейтральный)
- Скорость: `speed: 1.0` (не ускорять — голос становится неразборчивым)
- **Точки в конце каждой фразы** — TTS делает естественную паузу на точке, без неё слова сливаются
- Файлы: `/tmp/vo1.mp3` ... `/tmp/vo4.mp3` — готовый скрипт записи подхватывает автоматически

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

---

## 🔍 Аудит видео-баннера (обязательно после каждой записи)

После создания `banner.mp4` всегда проверять покадровыми скриншотами.

### Шаг 1: Извлечь ключевые кадры

```bash
# Кадры для проверки курсора и VO-синхронизации
ffmpeg -y -i banner.mp4 -ss 2.0  -frames:v 1 /tmp/check_2s.jpg    # иконка кликнута
ffmpeg -y -i banner.mp4 -ss 4.5  -frames:v 1 /tmp/check_4s.jpg    # курсор кликает форму
ffmpeg -y -i banner.mp4 -ss 6.5  -frames:v 1 /tmp/check_6s.jpg    # Fix it нажат / Done
ffmpeg -y -i banner.mp4 -ss 10.0 -frames:v 1 /tmp/check_10s.jpg   # PR-сайдбар
```

### Шаг 2: Что проверять на каждом кадре

| Кадр (с) | CSS % | Ожидаемое состояние | Курсор |
|----------|-------|---------------------|--------|
| 2s  | 14%  | Sidebar открылся, форма начинает краснеть | Около extension icon |
| 4.5s | 32% | Форма оранжевая "SELECTED", popup появился | Над полем формы или popup |
| 6.5s | 46% | Popup "Done ✓", ROOT CAUSE в сайдбаре | Точно на кнопке Fix it |
| 10s | 71% | PR-пузырь в сайдбаре | Слева в сайдбаре |

**Красные флаги:**
- Курсор в нижней части баннера (y > высота баннера − 30px) — координата `top` в `@keyframes scCur` завышена
- Кадры 4.5s и 6.5s выглядят одинаково → анимации throttled (см. ниже)
- Кадр 11s+ показывает "waiting for selection..." → VO сегмент приходится на начало нового цикла, убрать или сдвинуть

### Шаг 3: Калибровка координат курсора

Алгоритм определения правильных `left`/`top` в `@keyframes scCur`:

```javascript
// В DevTools или CDP — найти позицию элемента относительно .sc-banner
const banner = document.querySelector('.sc-banner');
const target = document.querySelector('.sc-popup-fix');  // Fix it button
const bannerRect = banner.getBoundingClientRect();
const targetRect = target.getBoundingClientRect();
console.log({
  left: Math.round(targetRect.left - bannerRect.left + targetRect.width / 2),
  top:  Math.round(targetRect.top  - bannerRect.top  + targetRect.height / 2)
});
```

Используй полученные числа напрямую в `@keyframes scCur`.

### Шаг 4: Синхронизированная запись (правильный алгоритм)

**Симптомы throttling:**
- Все кадры выглядят одинаково (skip:98%+ в ffmpeg stats)
- `animation-play-state: paused` + resume — НЕ помогает (анимации продолжаются с середины цикла)
- Новый таб через CDP `PUT /json/new` — всегда в фоне → throttled

**Корень проблемы:** `animation-play-state: paused` только ставит паузу в текущей точке — после resume анимация продолжается с того же кадра (не с 0%). Кроме того, `querySelectorAll('*')` не захватывает `::before`/`::after`.

**Правильное решение — `animation: none` + reflow + инжект style-тега:**

```javascript
// В CDP Navigate в СУЩЕСТВУЮЩИЙ kiosk-таб (не создавать новый!)
// Существующий таб = foreground, новый CDP-таб = background (throttled)

// 1. Навигировать в kiosk-таб:
ws.send({method:'Page.navigate', params:{url: ARTICLE_URL}});

// 2. После loadEventFired — скроллить + сбросить ВСЕ анимации
// Используем <style> тег (охватывает ::before/::after, которые querySelectorAll не видит)
const s = document.createElement('style');
s.id = '__reset_all';
s.textContent = '.sc-banner,.sc-banner *,.sc-banner *::before,.sc-banner *::after { animation: none !important; }';
document.head.appendChild(s);
void document.body.offsetHeight;  // ОБЯЗАТЕЛЬНЫЙ reflow — сбрасывает animation state to 0

// 3. Старт ffmpeg (0.8s записывает статичную начальную позицию)

// 4. Через 800ms — убрать style-тег, все анимации стартуют с 0% одновременно
document.getElementById('__reset_all').remove();
void document.body.offsetHeight;
```

**Получить ID kiosk-таба:**
```bash
curl -s http://localhost:9223/json | python3 -c "
import sys,json
tabs = json.load(sys.stdin)
# Оригинальный kiosk-таб — тот, что был открыт первым (about:blank или самый старый)
print(tabs[-1]['id'])  # последний в списке — oldest
"
```

**Готовый скрипт:** `/tmp/record_v5.js` (WooCommerce banner, 29s, x11grab, audio mix через bash)

### Шаг 5: Проверка VO-синхронизации

Для каждого VO-сегмента проверь соответствие:

| VO сегмент | Delay | % в 28s цикле | Что должно быть на экране |
|------------|-------|---------------|---------------------------|
| Сег 1 | 600ms  | 2%  | Курсор над extension icon |
| Сег 2 | 4800ms | 17% | Cursor движется к форме |
| Сег 3 | 9500ms | 34% | Текст набран, Fix it виден |
| Сег 4 | 18500ms| 66% | Done ✓ + Auto-deployed в сайдбаре |

**Правило:** если на кадре `t=delay/1000` баннер уже перешёл в новый цикл ("waiting for selection...") — этот VO сегмент нужно убрать или перенести.

### Типичные ошибки и фиксы

| Ошибка | Диагностика | Фикс |
|--------|-------------|------|
| Курсор ниже кнопки | На кадре cursor.y > target.y | Уменьши `top` в keyframe на разницу |
| Курсор левее/правее | На кадре cursor.x ≠ target.x | Скорректируй `left` в keyframe |
| Видео короче 14s | ffprobe duration < 14 | Добавить `-t 14` в ffmpeg |
| VO слышен на пустом баннере | Кадр 11s+ = начало цикла | Убрать последний VO сегмент |
| Анимации заморожены | Все кадры одинаковы | Запустить prep_record.js перед ffmpeg |
