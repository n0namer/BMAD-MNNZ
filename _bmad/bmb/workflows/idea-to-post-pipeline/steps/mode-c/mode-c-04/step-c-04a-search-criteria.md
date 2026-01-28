---
description: Define search criteria to find specific posts
name: step-c-04a-search-criteria
nextStepFile: ./step-c-04b-results.md
type: input
Введи дату конца (YYYY-MM-DD): 
Введи дату начала (YYYY-MM-DD): 
Введи ключевые слова (через запятую): 
Введи слово для поиска в названии: 
Выбери категорию: 
Выбери статус: 
Пример: ИИ, контент, продажи
Ты можешь комбинировать критерии: 
---

## NEXT STEP

When criteria defined: Load, read entire file, then execute step-c-04b-results.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-04: Search Posts - Define Criteria

## STEP GOAL:

User defines search parameters to find specific posts from the database.

## EXECUTION:

### 1. Load Posts Database

Load posts_database.csv (all published/drafted posts).

### 2. Display Search Interface

```
═══════════════════════════════════════════════════════════════

  🔍  SEARCH POSTS: Define Criteria

═══════════════════════════════════════════════════════════════

По каким критериям искать посты?

SEARCH OPTIONS:
─────────────────────────────────────────────────────────────

[T] Title / Заголовок (поиск по названию)
    Пример: "ИИ контент", "масштабирование"

[D] Date Range / Дата (найти посты за период)
    Пример: с 2026-01-01 по 2026-01-27

[C] Category / Категория (фильтр по рубрике)
    Доступно: automation, tech, market, writing, business

[K] Keyword / Ключевые слова (многоссловный поиск)
    Пример: "ИИ", "контент", "продажи"

[S] Status / Статус (черновик, готов, архив)
    Доступно: draft, published, archived

─────────────────────────────────────────────────────────────

[A] Advanced Search — Комбинировать критерии
[M] Back to MENU — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

### 3. Handle Selection

**[T] Search by Title:**
```
Введи слово для поиска в названии:
_________________________________________
```
Wait for input, save criteria, proceed to step-c-04b-results.md

**[D] Search by Date Range:**
```
Введи дату начала (YYYY-MM-DD):
_________________________________________

Введи дату конца (YYYY-MM-DD):
_________________________________________
```
Wait for input, save criteria, proceed to step-c-04b-results.md

**[C] Search by Category:**
```
Выбери категорию:

[1] automation
[2] tech
[3] market
[4] writing
[5] business
[6] ALL CATEGORIES (показать все)

_________________________________________
```
Wait for input, save criteria, proceed to step-c-04b-results.md

**[K] Search by Keywords:**
```
Введи ключевые слова (через запятую):
_________________________________________

Пример: ИИ, контент, продажи
```
Wait for input, save criteria, proceed to step-c-04b-results.md

**[S] Search by Status:**
```
Выбери статус:

[1] draft — Черновики
[2] published — Опубликовано
[3] archived — Архив
[4] ALL STATUSES (показать все)

_________________________________________
```
Wait for input, save criteria, proceed to step-c-04b-results.md

**[A] Advanced Search:**
```
Ты можешь комбинировать критерии:

[T] Title содержит: _____________________
[D] Дата от: _________ до: _____________
[C] Категория: ______________________
[K] Ключевые слова: ____________________
[S] Статус: _____________________________

[✓] Apply Filters — Применить фильтры
[✗] Clear All — Очистить все
[M] Back to MENU — Вернуться в меню

_________________________________________
```
Allow user to set multiple criteria, then proceed to step-c-04b-results.md

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

When criteria defined: Load, read entire file, then execute step-c-04b-results.md
