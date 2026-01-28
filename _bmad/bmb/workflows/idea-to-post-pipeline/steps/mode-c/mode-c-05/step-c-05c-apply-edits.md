---
name: step-c-05c-apply-edits
type: action
description: Apply selected improvements to post
nextStepFile: ./step-c-05d-finalize.md
---

## NEXT STEP

When improvements applied: Load, read entire file, then execute step-c-05d-finalize.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-05: Edit Post - Apply Improvements

## STEP GOAL:

Apply selected improvements to the post with user guidance.

## EXECUTION:

### 1. Load Selected Improvements

Load the improvements checklist from previous step.
Show which ones will be applied.

### 2. Apply Each Improvement Sequentially

For each selected improvement, present editor and wait for user input.

### 3. Display Improvement Interface

```
═══════════════════════════════════════════════════════════════

  🛠️  APPLYING IMPROVEMENTS

═══════════════════════════════════════════════════════════════

Selected: 4/7 improvements to apply

Progress: ▰▰▰░░░░░░ 40%

─────────────────────────────────────────────────────════════

CURRENT TASK: [A] ADD VISUAL ELEMENTS

─────────────────────────────────────────────────────────────

Where to add: Section "Step 1: Выбери нишу"

Current text:
"Первый шаг - выбрать специфичную нишу для своего контента.
 Например: ИИ для маркетинга, ИИ для письма и т.д."

Suggestion:
➜ Add a screenshot/diagram showing "Niche Selection Matrix"
➜ Add visual examples of good vs bad niche choices

OPTIONS:
[U] UPLOAD IMAGE — Загрузить изображение
[G] GENERATE PLACEHOLDER — Создать заглушку
[S] SKIP THIS — Пропустить это улучшение
[E] EDIT TEXT INSTEAD — Отредактировать текст

_________________________________________
```

### 4. Handle Improvement Actions

**[U] UPLOAD IMAGE:**
```
Загрузи изображение (JPG, PNG, SVG):

_________________________________________

Описание изображения для alt-text:
_________________________________________

Размер: Auto / Small / Medium / Large / Full-Width

[✓] Add — Добавить изображение
[✗] Cancel — Отмена
```

After upload:
```
✓ Изображение добавлено!

Превью:
[Image preview shown]

─────────────────────────────────────────────────────────

[>] Next Improvement — Следующее улучшение
[E] EDIT — Отредактировать позицию/размер
[S] SKIP — Пропустить
```

**[G] GENERATE PLACEHOLDER:**
```
Создаю placeholder визуального элемента...

Тип: Диаграмма "Niche Selection Matrix"

Preview:
┌─────────────────────────────────┐
│ HIGH COMPETITION / HIGH DEMAND   │
│                                 │
│ Идеальные ниши для начала       │
│ • AI для маркетинга             │
│ • AI для продаж                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ LOW COMPETITION / HIGH DEMAND    │
│                                 │
│ Лучшие ниши для роста           │
│ • AI для HR                     │
│ • AI для бухгалтерии            │
└─────────────────────────────────┘

[✓] Use This — Использовать
[E] EDIT — Отредактировать
[S] SKIP — Пропустить
[>] Next — Следующее улучшение
```

**[S] SKIP THIS:**
```
Пропускаю это улучшение.

Переходим дальше...
```
Move to next improvement

**[E] EDIT TEXT INSTEAD:**
```
Отредактировать текст вместо визуала?

Текущий текст:
"Первый шаг - выбрать специфичную нишу для своего контента.
 Например: ИИ для маркетинга, ИИ для письма и т.д."

EDIT MODE:
─────────────────────────────────────────────────────────────

[Полный текст доступен для редактирования]

Предложение автора:
"Первый шаг - выбрать специфичную нишу. Начни с области,
 где высокий спрос, но низкая конкуренция:
 • ИИ для HR (зарплата тренинга)
 • ИИ для бухгалтерии (аутсорс)
 • ИИ для недвижимости
 Выбери одно из трех выше либо свой вариант."

[T] ACCEPT THIS — Принять это предложение
[M] MERGE — Объединить мой текст с предложением
[C] CUSTOM — Отредактировать вручную
[S] SKIP — Пропустить улучшение

_________________________________________
```

### 5. Progress Through Improvements

After each improvement:
```
Improvement [A/4] completed ✓

Progress: ▰▰▰▰░░░░░░ 50%

─────────────────────────────────────────────────────────────

NEXT: [B] IMPROVE HEADLINE IMPACT

[>] Continue — Продолжить
[M] Back to MENU — Вернуться в меню
[P] Preview Changes — Посмотреть изменения
```

### 6. Final Summary

After all improvements applied:
```
═══════════════════════════════════════════════════════════════

  ✓  ALL IMPROVEMENTS APPLIED

═════════════════════════════════════════════════════════════════

Progress: ▰▰▰▰▰▰▰▰▰▰ 100%

Applied improvements:
─────────────────────────────────────────────────────────────

[✓] A — Add Visual Elements (2 images added)
[✓] B — Improve Headline Impact (new title: "Создай 10 идей...")
[✓] C — Add Real-World Examples (3 case studies added)
[✓] E — Expand Call-to-Action (CTA improved)

─────────────────────────────────────────────────────────────

QUALITY IMPROVEMENT:
Before: ⭐⭐⭐⭐☆ (4.2/5)
After:  ⭐⭐⭐⭐⭐ (4.9/5)

Expected engagement boost: +35%

─────────────────────────────────────────────────────────────

WHAT'S NEXT?

[P] PREVIEW — Посмотреть готовый пост
[F] FINALIZE — Завершить редактирование
[R] REDO — Перелделать какие-то улучшения
[M] Back to MENU — Отмена, в меню

═════════════════════════════════════════════════════════════════
```

### 7. Handle Final Options

**[P] PREVIEW:**
```
═══════════════════════════════════════════════════════════════

  PREVIEW WITH IMPROVEMENTS

═════════════════════════════════════════════════════════════════

[Full post preview with all changes shown]

─────────────────────────────────────────────────────────────

[<] Back to Summary
[F] Looks Good — Завершить
[R] Need Changes — Внести еще изменения
```

**[F] FINALIZE:**
```
Переходим к завершению редактирования...

Загружу, прочту весь файл, затем выполню C-05d
```
Load, read entire file, then execute `./step-c-05d-finalize.md`

**[R] REDO:**
```
Какое улучшение переделать?

[A] [B] [C] [D] [E] [F] [G]

[A] ALL — Переделать все

_________________________________________
```
Reapply selected improvement

**[M] Back to MENU:**
```
⚠️  ВНИМАНИЕ!

Все внесенные изменения будут потеряны.

Ты уверен?

[Y] YES, DISCARD CHANGES — Да, отменить
[N] NO, KEEP EDITING — Нет, продолжить
```

---

## NEXT STEP

When improvements applied: Load, read entire file, then execute step-c-05d-finalize.md
