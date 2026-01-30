---
description: Generate 250-char and 100-char versions of selected post
name: step-c-03d-variants
nextStepFile: ./c-03e-finalize.md
type: variant-generation
---

## SAVED DATA

All variants saved to posts_content.csv:
```csv
id,research_id,angle_used,...,content_500_chars,content_250_chars,content_100_chars,...
[N],1,"Time Saving",...,"[500 text]","[250 text]","[100 text]",...
```

---

## NEXT STEP

When user confirms: Load, read entire file, then execute step-c-03e-finalize.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-03: Write Post - Variants

## STEP GOAL:

Generate shorter variants (250-char, 100-char) from selected post draft.

## EXECUTION:

### 1. Display Generation

```
═════════════════════════════════════════════════════════════════

  ✨ GENERATING VARIANTS

  Selected: Draft 1 (DIRECT & PUNCHY)

  Creating shorter versions...

═════════════════════════════════════════════════════════════════
```

### 2. Generate Variants

**500-char (original):**
```
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

👉 Закинь пост в сохранённые и попробуй сегодня
```

**250-char version:**
```
3 часа вместо недели: как ИИ подтягивает контент 👉

Писать вручную = 8 часов в день + ноль роста.

ИИ меняет всё:
✅ 3 готовых поста за 3 часа
✅ Больше времени на стратегию
✅ Масштабирование без найма

👉 Попробуй сегодня
```

**100-char version:**
```
3 часа вместо недели: как ИИ подтягивает контент 👉

Попробуй сегодня и сэкономь 7 часов в неделю!
```

### 3. Display All Variants

```
═════════════════════════════════════════════════════════════════

  ✅ VARIANTS GENERATED

[500 chars] — Original (full details)
  Quality: 89/100 | CTR: 4.2% | Best for: LinkedIn
  Chars: 487

[250 chars] — Medium (key points)
  Quality: 87/100 | CTR: 4.0% | Best for: Telegram
  Chars: 251

[100 chars] — Short (teaser)
  Quality: 85/100 | CTR: 3.8% | Best for: Twitter
  Chars: 98

═════════════════════════════════════════════════════════════════

Что дальше?

[S] SELECT — Выбрать вариант и сохранить
[E] EDIT — Редактировать выбранный вариант
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

**[S] SELECT:**
```
Какой вариант сохранить?

[1] 500 chars (полный)
[2] 250 chars (средний)
[3] 100 chars (короткий)
[A] ALL THREE — Сохранить все варианты
```
Load, read entire file, then execute `./step-c-03e-finalize.md` with selected variants

**[E] EDIT:**
```
Какой вариант редактировать?

[1-3] Select variant
```
Edit selected variant, then redisplay

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## SAVED DATA

All variants saved to posts_content.csv:
```csv
id,research_id,angle_used,...,content_500_chars,content_250_chars,content_100_chars,...
[N],1,"Time Saving",...,"[500 text]","[250 text]","[100 text]",...
```

---

## NEXT STEP

When user confirms: Load, read entire file, then execute step-c-03e-finalize.md
