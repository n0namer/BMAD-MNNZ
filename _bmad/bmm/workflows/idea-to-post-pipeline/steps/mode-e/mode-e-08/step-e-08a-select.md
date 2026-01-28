---
description: Select 2 posts to compare side-by-side
name: step-e-08a-select
nextStepFile: ./step-e-08b-compare.md
type: dual-selection
---

# EDIT E-08a: Select Posts to Compare

## STEP GOAL:

Select 2 posts for side-by-side comparison analysis.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Selection Header

```
═══════════════════════════════════════════════════════════════

  ⚖️  СРАВНЕНИЕ ПОСТОВ: Side-by-Side анализ

  Выбери 2 поста которые хочешь сравнить

═══════════════════════════════════════════════════════════════
```

### 2. Present Selection Options

```
КАК ВЫБРАТЬ:

[1] 🔝 TOP vs BOTTOM — Сравнить лучший и худший
    Топ пост (высокий CTR) vs слабый пост

[2] 🎯 BY CATEGORY — Сравнить в той же категории
    Два поста одной категории (какой?)

[3] 📅 BY DATE — Сравнить по дате публикации
    Два периода (когда/когда?)

[4] 🎲 CUSTOM — Выбрать самому
    Введи номера 2 постов для сравнения

[5] 📋 LIST — Показать список постов
    Выбрать из полного списка

═══════════════════════════════════════════════════════════════
```

Wait for user selection.

### 3. Present Selection Results

**[1] TOP vs BOTTOM:**
```
🔝 ТОП пост:
[1] #156 "Новое об AI" | CTR: 3.2% | Engagement: 5.3%
    Quality: 78/100 | Views: 245 | Comments: 8

🔴 BOTTOM пост:
[2] #138 "Частая ошибка #1" | CTR: 0.9% | Engagement: 2.1%
    Quality: 54/100 | Views: 189 | Comments: 0

Сравнивать эти два? [Y/N]: ___
```

**[2] BY CATEGORY:**
```
ВЫБЕРИ КАТЕГОРИЮ:
• tech (15 постов)
• business (22 постов)
• lifestyle (18 постов)
• personal-growth (25 постов)
• tutorial (12 постов)

Которую: ___

ПОСТЫ В КАТЕГОРИИ "tech":

[1] #156 "Новое об AI" | CTR: 3.2%
[2] #147 "Как начать программировать" | CTR: 2.8%
[3] #136 "Python для начинающих" | CTR: 2.1%
... (12 more)

Выбери два номера для сравнения: ___ и ___
```

**[4] CUSTOM:**
```
ВЫБЕРИ НОМЕРА ПОСТОВ ДЛЯ СРАВНЕНИЯ:

Номер первого поста: ___
Номер второго поста: ___

Загружаю...

Пост #156 "Новое об AI"
Пост #138 "Частая ошибка #1"

Сравнивать эти два? [Y] Да / [N] Нет
```

### 4. Confirm Selection

```
═══════════════════════════════════════════════════════════════

✅ ВЫБРАНЫ ДВА ПОСТА ДЛЯ СРАВНЕНИЯ:

ПОСТ 1:
#156 "Новое об AI"
  • CTR: 3.2%
  • Engagement: 5.3%
  • Quality: 78/100
  • Views: 245
  • Дата: 25 янв

ПОСТ 2:
#138 "Частая ошибка #1"
  • CTR: 0.9%
  • Engagement: 2.1%
  • Quality: 54/100
  • Views: 189
  • Дата: 15 дец

Сейчас покажу side-by-side сравнение...

═══════════════════════════════════════════════════════════════
```

---

## SAVED DATA

Selected posts stored in session:
```
post1: 156
post2: 138
comparison_ready: true
post1_details: {
  title: "Новое об AI",
  ctr: 3.2%,
  engagement: 5.3%,
  quality: 78
}
post2_details: {
  title: "Частая ошибка #1",
  ctr: 0.9%,
  engagement: 2.1%,
  quality: 54
}
```

---

## SUCCESS CRITERIA

- ✅ 2 posts selected
- ✅ Selection confirmed
- ✅ Details shown for both
- ✅ Ready for comparison

---

## NEXT STEP

Load, read entire file, then execute `./step-e-08b-compare.md`
