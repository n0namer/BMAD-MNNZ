---
name: mode-c-00-menu
type: mode-menu
description: CREATE Mode submenu with 8 operational options
nextStepFile: ./c-01-add-idea.md

### Menu Handling Logic

**IF [A]: Advanced Elicitation:**
Execute Advanced Elicitation workflow, then return to this menu

**IF [P]: Party Mode:**
Execute Party Mode workflow, then return to this menu

**IF [M]: Back to MENU:**
Load step-00-menu.md (back to 4-mode selection)

---

## CRITICAL RULES

- 🛑 ALWAYS halt and wait for user input
- 📋 ONLY proceed when user selects [1-8]
- 💬 If user selects [A] or [P], return to menu after completion
- 🚫 NEVER force user into a sub-mode

---

## SUCCESS CRITERIA

- ✅ All 8 CREATE sub-modes clearly explained
- ✅ User understands which sub-mode fits their need
- ✅ Selection handled correctly and routed properly
- ✅ Can return to main menu anytime

---

## NEXT STEP

When user selects [1-8]:
- Display confirmation
- Load, read entire file, then execute appropriate sub-mode file
- Maintain current session state

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE MODE: Content Creation Hub

## STEP GOAL:

Present CREATE Mode options and route user to selected operation.

## EXECUTION:

### 1. Display Mode Welcome

```
═══════════════════════════════════════════════════════════════

           📝 CREATE MODE: Collaborative Content Creation

═══════════════════════════════════════════════════════════════

Здесь ты создаёшь новый контент, я помогаю:
  ✅ Добавляю идеи в inbox
  ✅ Исследую с разными углами
  ✅ Пишу варианты постов
  ✅ Помогу найти и редактировать старые
  ✅ Объединяю посты по темам
  ✅ Показываю аналитику и insights
  ✅ Управляю базой (backup, export)

Взаимодействие: 50/50 (ты выбираешь, я создаю)
Время цикла: 2-3 часа на 3 поста
Качество: 85-95% (высокое)

═══════════════════════════════════════════════════════════════
```

### 2. Present Sub-Mode Menu

```
ВЫБЕРИ ЧТО ДЕЛАТЬ:

[1] 💡 ADD IDEA — Добавить новую идею
    Просто описание идеи → добавляю в inbox

[2] 🔍 RESEARCH — Исследовать идею
    Выбери идею → 5-8 углов найду → вариации

[3] ✍️  WRITE POST — Написать пост
    Выбери идею & угол → 3 варианта текста → одобрение

[4] 🔎 SEARCH POST — Поиск по постам
    Найти пост по автору/дате/теме/ключевому слову

[5] ✏️  EDIT POST — Редактировать пост
    Быстрые улучшения одного поста

[6] 🔗 MERGE POSTS — Объединить посты
    Несколько постов → одна большая статья

[7] 📊 ANALYTICS — Аналитика и insights
    Какие посты работают, топ углы, рекомендации

[8] 💾 MANAGE BASE — Управление базой
    Backup, export, архивирование, очистка

[?] HELP — Показать справку
[A] Advanced Elicitation — Глубокое изучение
[P] Party Mode — Мультиперспективное обсуждение
[M] Back to MENU — Вернуться в главное меню

═══════════════════════════════════════════════════════════════
```

### 3. Handle User Selection

**[1] ADD IDEA:**
```
Переходим к добавлению новой идеи...
```
Load, read entire file, then execute `./c-01-add-idea.md`

**[2] RESEARCH:**
```
Переходим к исследованию идеи...
```
Load, read entire file, then execute `./c-02a-load-ideas.md`

**[3] WRITE POST:**
```
Переходим к написанию поста...
```
Load, read entire file, then execute `./c-03a-select-idea.md`

**[4] SEARCH POST:**
```
Переходим к поиску постов...
```
Load, read entire file, then execute `./c-04a-search-criteria.md`

**[5] EDIT POST:**
```
Переходим к редактированию поста...
```
Load, read entire file, then execute `./c-05a-select-post.md`

**[6] MERGE POSTS:**
```
Переходим к объединению постов...
```
Load, read entire file, then execute `./c-06a-select-posts.md`

**[7] ANALYTICS:**
```
Переходим к аналитике...
```
Load, read entire file, then execute `./c-07a-dashboard.md`

**[8] MANAGE BASE:**
```
Переходим к управлению базой...
```
Load, read entire file, then execute `./c-08a-backup.md`

**[?] HELP:**
Return to step 1 (redisplay this menu)

**[A] Advanced Elicitation:**
Execute Advanced Elicitation workflow, then return to this menu

**[P] Party Mode:**
Execute Party Mode workflow, then return to this menu

**[M] Back to MENU:**
Load step-00-menu.md (back to 4-mode selection)

---

## CRITICAL RULES

- 🛑 ALWAYS halt and wait for user input
- 📋 ONLY proceed when user selects [1-8]
- 💬 If user selects [A] or [P], return to menu after completion
- 🚫 NEVER force user into a sub-mode

---

## SUCCESS CRITERIA

- ✅ All 8 CREATE sub-modes clearly explained
- ✅ User understands which sub-mode fits their need
- ✅ Selection handled correctly and routed properly
- ✅ Can return to main menu anytime

---

## NEXT STEP

When user selects [1-8]:
- Display confirmation
- Load, read entire file, then execute appropriate sub-mode file
- Maintain current session state
