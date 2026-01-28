---
backStepFile: ./step-c-04b-results.md
description: Perform actions on selected post
name: step-c-04c-actions
nextStepFile: ../../mode-c/mode-c-00-menu.md
type: action
---

# CREATE C-04: Search Posts - Actions

## STEP GOAL:

User performs actions on selected post (view, edit, delete, export).

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Post Details

Show full post information:
```
═══════════════════════════════════════════════════════════════

  📄  POST DETAILS

═══════════════════════════════════════════════════════════════

TITLE: "ИИ контент за 3 часа"

─────────────────────────────────────────────────────────────

📋 META:
  • Created: 2026-01-25 10:30 AM
  • Modified: 2026-01-27 03:45 PM
  • Status: published
  • Category: automation
  • Views: 2,543
  • Likes: 187

─────────────────────────────────────────────────────────────

📝 CONTENT PREVIEW:

Как использовать ИИ для быстрого создания контента...

[Первые 300 символов текста]

─────────────────────────────────────────────────────────────

🏷️ TAGS: ИИ, контент, продажи, автоматизация

QUALITY SCORE: ⭐⭐⭐⭐⭐ (95/100)

═════════════════════════════════════════════════════════════════
```

### 2. Display Actions Menu

```
What do you want to do?
Что ты хочешь сделать?

─────────────────────────────────────────────────────────────

[V] VIEW FULL — Показать полный текст
    Прочитать весь пост целиком

[E] EDIT — Редактировать пост
    Открыть редактор для внесения изменений
    → Перейдёт на C-05 (Edit Post)

[D] DELETE — Удалить пост
    ⚠️  Действие необратимо!

[X] EXPORT — Экспортировать
    Скачать как: [PDF] [MD] [DOCX] [TXT]

[C] COMPARE — Сравнить с другим постом
    Показать различия между двумя постами

[A] ANALYZE — Анализ производительности
    Статистика просмотров, лайков, комментариев

─────────────────────────────────────────────────────────────

[<] BACK — Назад в результаты поиска
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

### 3. Handle Actions

**[V] VIEW FULL:**
```
═══════════════════════════════════════════════════════════════

  FULL POST TEXT

═══════════════════════════════════════════════════════════════

[Full post content here]

─────────────────────────────────────────────────────────────

[◄] Back to Details — Назад
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[E] EDIT:**
```
Открываю редактор...

Загружу, прочту весь файл, затем выполню C-05
```
Load, read entire file, then execute `../mode-c-05/step-c-05a-select-post.md`

**[D] DELETE:**
```
╔════════════════════════════════════════╗
║         CONFIRM DELETE                 ║
╚════════════════════════════════════════╝

Ты уверен что хочешь удалить?

"ИИ контент за 3 часа"

⚠️  Это действие НЕВОЗМОЖНО отменить!

[Y] YES, DELETE — Да, удалить
[N] CANCEL — Отмена

_________________________________________
```

If [Y]:
```
Пост удален успешно ✓

Возвращаюсь в поиск...
```
Load, read entire file, then execute `./step-c-04b-results.md`

If [N]: Redisplay actions menu

**[X] EXPORT:**
```
В каком формате экспортировать?

[P] PDF — Полный макет с форматированием
[M] Markdown — Простой текст с разметкой
[D] DOCX — Microsoft Word документ
[T] TXT — Чистый текст

_________________________________________
```

After selection:
```
Экспортирую... ✓

Файл скачан: post-ai-content-3h.pdf

Вернись к меню?
[Y] Yes / [M] Menu
```

**[C] COMPARE:**
```
Выбери второй пост для сравнения:

Загружаю список постов...
[Список других постов]

_________________________________________
```
Allow user to select second post, then show comparison view

**[A] ANALYZE:**
```
═══════════════════════════════════════════════════════════════

  PERFORMANCE ANALYTICS

═══════════════════════════════════════════════════════════════

POST: "ИИ контент за 3 часа"

VIEWS TREND:      📈 ████████░░ 2,543 views (↑12% this week)
ENGAGEMENT:       📊 ███████░░░ 187 likes, 42 comments
AVG READ TIME:    ⏱️  4 min 23 sec (good engagement)
BOUNCE RATE:      📉 12% (excellent, below avg 25%)
SHARING:          🔄 68 shares

TOP REFERRERS:
  • Twitter: 1,200 clicks
  • LinkedIn: 800 clicks
  • Email: 400 clicks
  • Organic: 143 clicks

═════════════════════════════════════════════════════════════════

[◄] Back to Details — Назад
[M] Back to MENU — Вернуться в меню
```

**[<] BACK:**
Load, read entire file, then execute `./step-c-04b-results.md`

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

Based on action selected, proceed accordingly or return to menu

### Menu Handling Logic

**IF [V]: VIEW FULL:**
```
═══════════════════════════════════════════════════════════════

  FULL POST TEXT

═══════════════════════════════════════════════════════════════

[Full post content here]

─────────────────────────────────────────────────────────────

[◄] Back to Details — Назад
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**IF [E]: EDIT:**
```
Открываю редактор...

Загружу, прочту весь файл, затем выполню C-05
```
Load, read entire file, then execute `../mode-c-05/step-c-05a-select-post.md`

**IF [D]: DELETE:**
```
╔════════════════════════════════════════╗
║         CONFIRM DELETE                 ║
╚════════════════════════════════════════╝

Ты уверен что хочешь удалить?

"ИИ контент за 3 часа"

⚠️  Это действие НЕВОЗМОЖНО отменить!

[Y] YES, DELETE — Да, удалить
[N] CANCEL — Отмена

_________________________________________
```

If [Y]:
```
Пост удален успешно ✓

Возвращаюсь в поиск...
```
Load, read entire file, then execute `./step-c-04b-results.md`

If [N]: Redisplay actions menu

**IF [X]: EXPORT:**
```
В каком формате экспортировать?

[P] PDF — Полный макет с форматированием
[M] Markdown — Простой текст с разметкой
[D] DOCX — Microsoft Word документ
[T] TXT — Чистый текст

_________________________________________
```

After selection:
```
Экспортирую... ✓

Файл скачан: post-ai-content-3h.pdf

Вернись к меню?
[Y] Yes / [M] Menu
```

**IF [C]: COMPARE:**
```
Выбери второй пост для сравнения:

Загружаю список постов...
[Список других постов]

_________________________________________
```
Allow user to select second post, then show comparison view

**IF [A]: ANALYZE:**
```
═══════════════════════════════════════════════════════════════

  PERFORMANCE ANALYTICS

═══════════════════════════════════════════════════════════════

POST: "ИИ контент за 3 часа"

VIEWS TREND:      📈 ████████░░ 2,543 views (↑12% this week)
ENGAGEMENT:       📊 ███████░░░ 187 likes, 42 comments
AVG READ TIME:    ⏱️  4 min 23 sec (good engagement)
BOUNCE RATE:      📉 12% (excellent, below avg 25%)
SHARING:          🔄 68 shares

TOP REFERRERS:
  • Twitter: 1,200 clicks
  • LinkedIn: 800 clicks
  • Email: 400 clicks
  • Organic: 143 clicks

═════════════════════════════════════════════════════════════════

[◄] Back to Details — Назад
[M] Back to MENU — Вернуться в меню
```

**IF [M]: Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

Based on action selected, proceed accordingly or return to menu

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
