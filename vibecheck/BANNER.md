# Vibecheck Banner — Structure & Algorithm

Файл: `vibecheck/index.html`. Баннер — это главный hero-мокап на `/vibers/vibecheck/`, имитирующий работу Chrome-расширения VibeCheck.

## DOM-структура

```
div.demo-banner-outer
└── div.demo-banner
    ├── div.browser-chrome           ← fake browser chrome (dots, URL bar, "👁 VibeCheck" badge)
    ├── div.demo-viewport#tab-bug    ← 1 из 4 tab-viewport'ов показан (остальные display:none)
    │   ├── div.demo-site            ← левая часть: wireframe-макет сайта
    │   │                              (содержит ОДИН highlighted-элемент — оранжевая рамка)
    │   └── div.demo-panel           ← правая sidebar-панель VibeCheck
    │       ├── .panel-header        (logo + badge "bug"/"feature"/"improve"/"WordPress")
    │       ├── .panel-element       ("Selected element" карточка: tag, text, path, file)
    │       ├── .panel-comment-wrap  ("Comment" + .tw typed-output + мигающий cursor)
    │       ├── .panel-btn-wrap      ("Send it off →" кнопка)
    │       ├── .panel-success       (PR-сообщение, hidden изначально)
    │       └── .panel-deploy        (deploy-сообщение, hidden изначально)
    ├── div.demo-viewport#tab-feature   ← display:none
    ├── div.demo-viewport#tab-improve   ← display:none
    ├── div.demo-viewport#tab-wp        ← display:none
    └── p.demo-banner-caption#demo-caption  ← status-строка под баннером
```

Табы переключаются по hash (`#bug`, `#feature`, `#improve`, `#wp`) и кликом по `.demo-tab` кнопкам выше hero.

## Данные (JS, около line 1405)

`TAB_DATA[tab] = { url, desc, text, caption }`:
- `url` — текст в адресной строке fake-браузера
- `desc` — описание под табами (1-2-3 шаги)
- `text` — содержимое коммента, который печатается побуквенно
- `caption` — финальное сообщение в `.demo-banner-caption` после успеха

## Текущий алгоритм (`switchTab` → `applyFix`)

Вызывается на init, hashchange, клик по табу. Вся цепочка синхронизована через `animGen` — при переключении он инкрементится, все stale-таймеры проверяют `if (animGen !== gen) return` и прерываются.

```
switchTab(tab)
  1. animGen++; gen = animGen
  2. resetTab() для всех 4 табов (скрыть PR/deploy-блоки, вернуть кнопки, откатить DOM-мутации мокапа)
  3. Показать выбранный .demo-viewport, скрыть остальные
  4. Обновить URL-bar и descr
  5. caption = "⏳ Preparing patch…"
  6. typeText('tw-' + tab, data.text, delay=1200ms)
       per-char: 48-100ms + 22ms на пробел + 150ms после ,.?!—
  7. onDone → setTimeout 500ms → applyFix(tab, gen)

applyFix(tab)
  ├─ t=0:     button → "⏳ Sending…" + .sending class
  │           caption = "⚙ Generating code change…"
  ├─ t=900:   DOM-мутация мокапа (text swap / появление filter-bar / смена цвета кнопки)
  ├─ t=1600:  скрыть кнопку, показать .panel-success с PR-info
  │           caption = "📦 Opening pull request…"
  ├─ t=2300:  caption = TAB_DATA[tab].caption (финальный success)
  └─ t=3400:  показать .panel-deploy с deploy-info
```

## Поведение при смене языка

`setLang('ru')`:
- Меняет `TAB_DATA[tab].desc` на `TAB_DESC_RU[tab]` (при следующем switchTab)
- Комменты и captions — **не переводятся**, остаются на английском (выглядят как пример user input)

---

## Новый алгоритм (proposed)

**Цель:** баннер должен визуально отражать реальный flow расширения из `op.wpmix.net/embed.js`:
1. Пользователь кликает по элементу → у элемента появляется **мини-попап с textarea** (а не sidebar-панель с заполненной формой).
2. После "Fix it" → sidebar справа превращается в **чат**: сообщения element/comment/progress/PR/deploy появляются последовательно как bubble'ы.

### Новая DOM-модель viewport'а

```
div.demo-viewport
├── div.demo-site                   ← wireframe сайта, как сейчас
│   └── [highlighted element]
│       └── div.inline-popup        ← НОВОЕ: мини-попап у элемента (абсолютно позиционируется)
│           ├── .inline-popup-title ("Code review" + ×)
│           ├── textarea.inline-comment (sim: печатается text)
│           └── button.inline-fix   ("Fix it →")
└── div.demo-panel.chat-mode        ← теперь это чат
    ├── .chat-header                ("VibeCheck — chat" + status)
    └── .chat-messages              ← стек bubble'ов (появляются последовательно)
        ├── [bubble] system:  "Selected <span.kpi-btn> on src/components/KPICard.tsx:42"
        ├── [bubble] user:    "{typed comment}"
        ├── [bubble] agent:   "⚙ Analyzing codebase…"
        ├── [bubble] agent:   "📦 Opened PR #247 — fix: prevent kpi button overflow"
        └── [bubble] agent:   "🚀 Deployed to production — live on onout.org"
```

### Новый flow

```
switchTab(tab)
  1. Standard reset/show as before
  2. t=0:     показать inline-popup у highlighted-элемента + element-bubble в чате
              (system-bubble "Selected …" — уже висит, задаёт контекст)
  3. t=300:   caption = "Clicked element — leave a comment"
  4. t=800:   typeText в inline-popup.textarea
  5. onDone:  user-bubble с тем же текстом улетает в чат (animation: slide-to-panel)
              inline-popup исчезает
              caption = "Comment submitted"
  6. t=+600:  agent-bubble "⚙ Analyzing codebase…"
              caption = "⚙ Generating code change…"
  7. t=+900:  DOM-мутация мокапа (как сейчас)
  8. t=+700:  agent-bubble с PR-info
              caption = "📦 Opening pull request…"
  9. t=+700:  caption = final (TAB_DATA[tab].caption)
 10. t=+1100: agent-bubble с deploy-info

animGen-инвалидация таймеров сохраняется.
```

### Преимущества
- **Честный mental model:** пользователь видит тот же flow, что и в реальном расширении (комментарий у элемента, чат в сайдбаре).
- Панель становится живой — сообщения появляются последовательно, создают ощущение "AI-работы".
- Старый layout с "Selected element + Comment + Send" в одной панели был статичным dashboard'ом — он не передавал процесс.

### Миграция данных
`TAB_DATA` остаётся совместим: `url`, `desc`, `text`, `caption` используются как раньше. Добавляется:
- `element` — строка для system-bubble: `"<span class=\"kpi-btn\"> on src/components/KPICard.tsx"`
- `pr` — строка для PR-bubble (сейчас хардкод внутри `applyFix`, выносим в TAB_DATA)
- `deploy` — строка для deploy-bubble (аналогично)
