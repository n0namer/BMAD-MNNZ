---
description: Generate 3 draft post variations based on selected angle
name: step-c-03c-draft
nextStepFile: ./step-c-03d-variants.md
type: content-generation
Дай feedback на все варианты: 
Например: 
---

## NEXT STEP

Handle user selection (select draft → proceed to variants)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-03: Write Post - Draft

## STEP GOAL:

Generate 3 draft variations of a post for the selected angle.

## EXECUTION:

### 1. Display Generation Start

```
═══════════════════════════════════════════════════════════════

  ✍️  WRITE POST: Generating Drafts

  Идея: "ИИ контент за 3 часа"
  Угол: Time Saving ⏱️

  Создаю 3 варианта текста...

═════════════════════════════════════════════════════════════════
```

### 2. Generate 3 Drafts

Using angle + research data, create 3 variations:

```
DRAFT 1 - DIRECT & PUNCHY (Hook-focused)
─────────────────────────────────────────
3 часа вместо недели: как ИИ подтягивает контент 👉

Писать контент вручную — это 8 часов в день и ноль роста.

ИИ меняет всё. За 3 часа вместо недели ты получаешь:
✅ 3 готовых поста разных лиц
✅ Больше времени на стратегию
✅ Масштабирование без найма

Вот как это работает:
1. Даёшь ИИ тему
2. ИИ генерирует варианты (5-10 мин)
3. Ты редактируешь 20 мин
4. Готово! Публикуешь или ещё твикишь

Результат: 7 часов сэкономлено на неделю. Это весь твой рост!

👉 Закинь пост в сохранённые и попробуй сегодня

Quality score: 89/100 | CTR potential: 4.2%

─────────────────────────────────────────

DRAFT 2 - STORYTELLING (Narrative-focused)
─────────────────────────────────────────
Представь: ты писал контент 8 часов в день.
Спина болит. Голова кипит. Ты выжат.

А потом ты открыл ИИ.

Через 3 часа у тебя 3 готовых поста.
На следующий день 6 постов.
Через неделю 20 постов написано.

Всё вместе? За 15-20 часов вместо 60+.

Это не сказки. Это 2026 год.

Единственное что изменилось?
Ты научился давать правильные промпты.

👉 Вот как...

[Continue draft...]

Quality score: 84/100 | CTR potential: 3.8%

─────────────────────────────────────────

DRAFT 3 - DATA-DRIVEN (Numbers-focused)
─────────────────────────────────────────
Цифры говорят сами за себя:

Традиционно:
⏱️  2-3 часа на пост
💰 $500-1000 за статью
😩 Выгорание после недели

С ИИ:
⏱️  20-30 мин на пост (75% быстрее)
💰 $20/месяц подписка (100x дешевле)
😊 Масштабирование без стресса

Да, нужен правильный процесс.
Да, требуется редактирование.
Но экономия времени?

70-75% гарантировано.

Каковы твои цифры?

👉 Попробуй и вычисли сам

Quality score: 86/100 | CTR potential: 4.0%

─────────────────────────────────────────
```

### 3. Display Drafts & Options

```
═════════════════════════════════════════════════════════════════

  ✅ 3 DRAFT VARIANTS CREATED

  Draft 1: DIRECT & PUNCHY (89/100) ⭐
  Draft 2: STORYTELLING (84/100)
  Draft 3: DATA-DRIVEN (86/100)

═════════════════════════════════════════════════════════════════

Что дальше?

[1-3] SELECT DRAFT — Выбрать понравившийся вариант
[F] FEEDBACK — Дать feedback на все варианты
[G] GENERATE NEW — Создать новые варианты
[V] VIEW FULL — Показать полные версии (250/100 chars)
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

**[1-3] SELECT DRAFT:**
```
Выбрал Draft 1: DIRECT & PUNCHY

Переходим к генерации дополнительных вариантов...
```
Load, read entire file, then execute `./step-c-03d-variants.md` with selected draft

**[F] FEEDBACK:**
```
Дай feedback на все варианты:
[Waiting for user input...]

Например:
  • "Draft 1 лучше, но hook нужен сильнее"
  • "Мне нравится структура Draft 3"
  • Etc.
```
Re-generate with feedback

**[G] GENERATE NEW:**
Generate 3 new variations

**[V] VIEW FULL:**
Show 250-char and 100-char versions of selected draft

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

Handle user selection (select draft → proceed to variants)
