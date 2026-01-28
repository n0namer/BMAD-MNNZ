---
description: Display search results matching criteria
name: step-c-04b-results
nextStepFile: ./step-c-04c-actions.md
type: display
---

# CREATE C-04: Search Posts - Display Results

## STEP GOAL:

Display all posts matching the search criteria defined in previous step.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Apply Search Filters

Apply selected criteria from step-c-04a:
- Filter by title/keywords
- Filter by date range
- Filter by category
- Filter by status

Count total matches.

### 2. Display Results

```
═══════════════════════════════════════════════════════════════

  🔍  SEARCH RESULTS: Found 12 Posts

═══════════════════════════════════════════════════════════════

Search: Category = automation | Date = Jan 2026 | Status = all

─────────────────────────────────────────────────────────────

[1] "ИИ контент за 3 часа"
    📅 2026-01-25 | 📂 automation | 📊 published (2.5K views)
    Сводка: Как использовать ИИ для быстрого создания контента...

[2] "Speech-to-Text для блогеров"
    📅 2026-01-20 | 📂 automation | 📊 draft
    Сводка: Технология преобразования речи в текст для...

[3] "Автоматизация социальных сетей"
    📅 2026-01-15 | 📂 automation | 📊 published (890 views)
    Сводка: Инструменты для автоматизации постинга и...

[4] "5 инструментов для экономии времени"
    📅 2026-01-10 | 📂 automation | 📊 published (1.2K views)
    Сводка: Обзор лучших инструментов автоматизации...

...и ещё 8 постов

─────────────────────────────────────────────────────────════

SORT BY:
[1] Newest First — Сначала новые
[2] Oldest First — Сначала старые
[3] Most Popular — По популярности
[4] Title A-Z — По названию

─────────────────────────────────────────────────────────────

[+] NEW SEARCH — Новый поиск
[?] HELP — Справка
[M] Back to MENU — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

### 3. Handle Results

**[1-N] Select post number:**
```
Выбрал пост: "ИИ контент за 3 часа"

Загружаю опции...
```
Load, read entire file, then execute `./step-c-04c-actions.md`

**[1-4] Sort results:**
```
Переворачиваю результаты...

Сортировка: [Selected Option]
```
Redisplay results with new sort order, then allow [1-N] selection

**[+] NEW SEARCH:**
```
Вернись к поиску...
```
Load, read entire file, then execute `../mode-c-04/step-c-04a-search-criteria.md`

**[?] HELP:**
Show explanation of search features and sorting options

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

### 4. No Results Handling

If search returns 0 posts:
```
╔════════════════════════════════════════╗
║         NO POSTS FOUND                 ║
╚════════════════════════════════════════╝

Критерии поиска не совпали ни с одним постом.

[M] Try Different Search — Попробовать новый поиск
[M] Back to MENU — Вернуться в меню

_________________________________________
```

---

## NEXT STEP

When post selected: Load, read entire file, then execute step-c-04c-actions.md

### Menu Handling Logic

**IF [M]: Back to MENU:**
Load `../mode-c-00-menu.md`

### 4. No Results Handling

If search returns 0 posts:
```
╔════════════════════════════════════════╗
║         NO POSTS FOUND                 ║
╚════════════════════════════════════════╝

Критерии поиска не совпали ни с одним постом.

[M] Try Different Search — Попробовать новый поиск
[M] Back to MENU — Вернуться в меню

_________________________________________
```

---

## NEXT STEP

When post selected: Load, read entire file, then execute step-c-04c-actions.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
