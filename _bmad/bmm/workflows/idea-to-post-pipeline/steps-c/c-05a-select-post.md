---
description: Select which post to edit
name: step-c-05a-select-post
nextStepFile: ./c-05b-improvements.md
type: selection
---

# CREATE C-05: Edit Post - Select Post

## STEP GOAL:

User selects which post they want to edit from their library.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Load Posts Library

Load posts_database.csv (all editable posts).
Filter to show: draft, published, archived (exclude deleted).

### 2. Display Posts List

```
═══════════════════════════════════════════════════════════════

  ✏️  EDIT POST: Select Post

═══════════════════════════════════════════════════════════════

Какой пост ты хочешь отредактировать?

─────────────────────────────────────────────────────────────

[1] "ИИ контент за 3 часа"
    📅 2026-01-25 | 📂 automation | 📊 published
    Статус: Хороший | Просмотры: 2.5K

[2] "Speech-to-Text для блогеров"
    📅 2026-01-20 | 📂 automation | 📊 draft
    Статус: Нужны улучшения | Просмотры: 0

[3] "Масштабирование личного бренда"
    📅 2026-01-15 | 📂 market | 📊 published
    Статус: Отличный | Просмотры: 5.8K

[4] "5 инструментов для экономии времени"
    📅 2026-01-10 | 📂 automation | 📊 published
    Статус: Хороший | Просмотры: 1.2K

[5] "Copywriting для социальных сетей"
    📅 2026-01-08 | 📂 writing | 📊 draft
    Статус: Требует доработки | Просмотры: 0

─────────────────────────────────────────────────────────────

FILTER BY:
[S] Status (draft, published, archived, all)
[C] Category (automation, tech, market, writing, business)
[D] Date Range (старые/новые)

SORT BY:
[N] Newest — Сначала новые
[O] Oldest — Сначала старые
[P] Popular — По популярности

─────────────────────────────────────────────────────────────

[+] CREATE NEW POST — Создать новый пост
[S] SEARCH — Поиск по названию
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

### 3. Handle Selection

**[1-N] Select post:**
```
Выбрал пост: "ИИ контент за 3 часа"

Загружаю предложения по улучшению...
```
Load, read entire file, then execute `./step-c-05b-improvements.md`

**[S] Filter by Status:**
```
Какой статус показать?

[1] draft — Черновики
[2] published — Опубликовано
[3] archived — Архив
[4] all — Все посты

_________________________________________
```
Apply filter, redisplay list

**[C] Filter by Category:**
```
Какую категорию показать?

[1] automation
[2] tech
[3] market
[4] writing
[5] business
[6] all — Все категории

_________________________________________
```
Apply filter, redisplay list

**[D] Filter by Date:**
```
[N] Newest First — Сначала новые
[O] Oldest First — Сначала старые

_________________________________________
```
Apply sort, redisplay list

**[+] CREATE NEW POST:**
```
Создаю новый пост...

Загружу, прочту весь файл, затем выполню C-03
```
Load, read entire file, then execute `./c-03a-select-idea.md`

**[S] SEARCH:**
```
Введи слово для поиска в названии:

_________________________________________
```
Search by title, redisplay filtered list

**[M] Back to MENU:**
Load `./c-00-menu.md`

### 4. No Posts Handling

If no posts available:
```
╔════════════════════════════════════════╗
║      NO POSTS FOUND                    ║
╚════════════════════════════════════════╝

У тебя нет постов для редактирования.

[+] CREATE NEW POST — Создать новый пост
[M] Back to MENU — Вернуться в меню

_________________________________________
```

---

## NEXT STEP

When post selected: Load, read entire file, then execute step-c-05b-improvements.md

### Menu Handling Logic

**IF [S]: Filter by Status:**
```
Какой статус показать?

[1] draft — Черновики
[2] published — Опубликовано
[3] archived — Архив
[4] all — Все посты

_________________________________________
```
Apply filter, redisplay list

**IF [C]: Filter by Category:**
```
Какую категорию показать?

[1] automation
[2] tech
[3] market
[4] writing
[5] business
[6] all — Все категории

_________________________________________
```
Apply filter, redisplay list

**IF [D]: Filter by Date:**
```
[N] Newest First — Сначала новые
[O] Oldest First — Сначала старые

_________________________________________
```
Apply sort, redisplay list

**IF [S]: SEARCH:**
```
Введи слово для поиска в названии:

_________________________________________
```
Search by title, redisplay filtered list

**IF [M]: Back to MENU:**
Load `./c-00-menu.md`

### 4. No Posts Handling

If no posts available:
```
╔════════════════════════════════════════╗
║      NO POSTS FOUND                    ║
╚════════════════════════════════════════╝

У тебя нет постов для редактирования.

[+] CREATE NEW POST — Создать новый пост
[M] Back to MENU — Вернуться в меню

_________________________________________
```

---

## NEXT STEP

When post selected: Load, read entire file, then execute step-c-05b-improvements.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
