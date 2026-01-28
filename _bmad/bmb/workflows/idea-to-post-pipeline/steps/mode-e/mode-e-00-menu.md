---
name: mode-e-00-menu
type: mode-menu
description: EDIT Mode submenu with 8 autonomous improvement options (70% AI, 30% user)
nextStepFile: ./mode-e-01/step-e-01a-select-posts.md

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

## EDIT MODE PHILOSOPHY

- **70% AI autonomy**: I analyze and recommend improvements
- **30% user approval**: You review and approve changes
- **Non-destructive**: All changes reviewable before applying
- **Batch operations**: Improve multiple posts simultaneously
- **Data preservation**: Every change logged for rollback if needed

---

## SUCCESS CRITERIA

- ✅ All 8 EDIT sub-modes clearly explained
- ✅ User understands which sub-mode fits their need
- ✅ Selection handled correctly and routed properly
- ✅ Can return to main menu anytime
- ✅ Autonomous operation maintains high quality (90%+)

---

## NEXT STEP

When user selects [1-8]:
- Display confirmation
- Load, read entire file, then execute appropriate sub-mode file
- Maintain current session state

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# EDIT MODE: Autonomous Post Improvements

## STEP GOAL:

Present EDIT Mode options and route user to selected operation.

## EXECUTION:

### 1. Display Mode Welcome

```
═══════════════════════════════════════════════════════════════

           🔧 EDIT MODE: Autonomous Post Improvements

═══════════════════════════════════════════════════════════════

Здесь я улучшаю твои посты автоматически. Я анализирую, ты одобряешь:
  ✅ Массовое редактирование (улучшаю несколько постов)
  ✅ Чек-лист улучшений (систематическое покрытие)
  ✅ A/B тестирование (генерирую варианты)
  ✅ Обновление метрик (пересчитываю KPI)
  ✅ Переписывание низких CTR (авто-спасение)
  ✅ Архивирование (перемещение в архив)
  ✅ История версий (просмотр эволюции)
  ✅ Сравнение постов (side-by-side анализ)

Взаимодействие: 70/30 (я предлагаю, ты одобряешь)
Время цикла: 30-60 минут на 10+ постов
Качество: 90-95% (очень высокое)

═══════════════════════════════════════════════════════════════
```

### 2. Present Sub-Mode Menu

```
ВЫБЕРИ ЧТО УЛУЧШАТЬ:

[1] 📦 BULK EDIT — Массовое редактирование
    Выбери посты → анализирую → предлагаю улучшения → применяю

[2] ✅ CHECKLIST EDIT — Редактирование по чек-листу
    Загружаю чек-лист → оцениваю каждый пункт → применяю улучшения

[3] 🧪 A/B TEST — Тестирование вариантов
    Выбери пост → генерирую 3 варианта → сравниваю метрики

[4] 📊 UPDATE METRICS — Обновление метрик
    Загружаю посты → пересчитываю CTR и engagement → сохраняю

[5] 🚀 REWRITE LOW CTR — Переписывание слабых постов
    Нахожу CTR < 2% → переписываю → предсказываю улучшение

[6] 📦 ARCHIVE — Архивирование старых постов
    Выбираю старые посты → переводу в архив → сохраняю

[7] 📜 HISTORY — История версий поста
    Выбери пост → показываю все версии с изменениями

[8] ⚖️  COMPARE — Сравнение двух постов
    Выбери 2 поста → сравниваю side-by-side → анализирую различия

[?] HELP — Показать справку
[A] Advanced Elicitation — Глубокое изучение
[P] Party Mode — Мультиперспективное обсуждение
[M] Back to MENU — Вернуться в главное меню

═══════════════════════════════════════════════════════════════
```

### 3. Handle User Selection

**[1] BULK EDIT:**
```
Переходим к массовому редактированию...
```
Load, read entire file, then execute `./mode-e-01/step-e-01a-select-posts.md`

**[2] CHECKLIST EDIT:**
```
Переходим к редактированию по чек-листу...
```
Load, read entire file, then execute `./mode-e-02/step-e-02a-load-checklist.md`

**[3] A/B TEST:**
```
Переходим к тестированию вариантов...
```
Load, read entire file, then execute `./mode-e-03/step-e-03a-select-post.md`

**[4] UPDATE METRICS:**
```
Переходим к обновлению метрик...
```
Load, read entire file, then execute `./mode-e-04/step-e-04a-load-posts.md`

**[5] REWRITE LOW CTR:**
```
Переходим к переписыванию слабых постов...
```
Load, read entire file, then execute `./mode-e-05/step-e-05a-identify.md`

**[6] ARCHIVE:**
```
Переходим к архивированию...
```
Load, read entire file, then execute `./mode-e-06/step-e-06a-select.md`

**[7] HISTORY:**
```
Переходим к просмотру истории...
```
Load, read entire file, then execute `./mode-e-07/step-e-07a-load-history.md`

**[8] COMPARE:**
```
Переходим к сравнению постов...
```
Load, read entire file, then execute `./mode-e-08/step-e-08a-select.md`

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

## EDIT MODE PHILOSOPHY

- **70% AI autonomy**: I analyze and recommend improvements
- **30% user approval**: You review and approve changes
- **Non-destructive**: All changes reviewable before applying
- **Batch operations**: Improve multiple posts simultaneously
- **Data preservation**: Every change logged for rollback if needed

---

## SUCCESS CRITERIA

- ✅ All 8 EDIT sub-modes clearly explained
- ✅ User understands which sub-mode fits their need
- ✅ Selection handled correctly and routed properly
- ✅ Can return to main menu anytime
- ✅ Autonomous operation maintains high quality (90%+)

---

## NEXT STEP

When user selects [1-8]:
- Display confirmation
- Load, read entire file, then execute appropriate sub-mode file
- Maintain current session state
