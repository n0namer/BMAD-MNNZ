---
description: Load posts with old metrics for recalculation
name: step-e-04a-load-posts
nextStepFile: ./e-04b-recalculate.md
type: load-data
---

# EDIT E-04a: Load Posts with Metrics

## STEP GOAL:

Load all published posts with current metrics and prepare for recalculation.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Loading Header

```
═══════════════════════════════════════════════════════════════

  📊 UPDATE METRICS: Обновление показателей

  Загружаю посты с текущими метриками... (5-10 сек)

═══════════════════════════════════════════════════════════════
```

### 2. Load Posts from Database

```
Загружаю из posts_main.csv...
Загружаю из metrics_tracking.csv...

✅ Загружено успешно!

📈 СТАТИСТИКА:
  • Всего опубликовано постов: 87
  • С метриками: 87 (100%)
  • Последний обновлен: 3 дня назад
  • Время сбора: 8 сек
```

### 3. Display Posts Summary

```
═══════════════════════════════════════════════════════════════

  📋 ПОСТЫ ДЛЯ ОБНОВЛЕНИЯ (87 шт)

═══════════════════════════════════════════════════════════════

ВЫБОРКА:

[1] #156 "Новое об AI" (25 янв)
    Views: 245 | CTR: 3.2% | Engagement: 4.1%
    Quality: 78/100 | Дней с публикации: 3

[2] #154 "Инсайт дня" (24 янв)
    Views: 189 | CTR: 2.8% | Engagement: 3.8%
    Quality: 72/100 | Дней с публикации: 4

[3] #152 "Как я заработал" (23 янв)
    Views: 412 | CTR: 4.1% | Engagement: 5.2%
    Quality: 85/100 | Дней с публикации: 5

... (более 84 постов)

[85] #10 "Старая идея" (15 ноя)
     Views: 1203 | CTR: 2.1% | Engagement: 2.8%
     Quality: 65/100 | Дней с публикации: 74

[86] #8 "История" (10 ноя)
     Views: 892 | CTR: 1.9% | Engagement: 2.4%
     Quality: 62/100 | Дней с публикации: 79

[87] #5 "Первый пост" (5 ноя)
     Views: 567 | CTR: 1.2% | Engagement: 1.6%
     Quality: 58/100 | Дней с публикации: 84
```

### 4. Metrics Overview

```
═══════════════════════════════════════════════════════════════

📊 ТЕКУЩИЕ МЕТРИКИ (всего 87 постов):

ПРОСМОТРЫ:
  Мин: 45 | Макс: 1203 | Среднее: 287

CTR (Click-Through Rate):
  Мин: 0.8% | Макс: 4.5% | Среднее: 2.1%

ENGAGEMENT:
  Мин: 1.2% | Макс: 5.8% | Среднее: 3.2%

QUALITY SCORE:
  Мин: 54/100 | Макс: 89/100 | Среднее: 71/100

ВОЗРАСТ ПОСТОВ:
  Самый старый: 84 дня (5 ноя)
  Самый новый: 3 дня (25 янв)
  Среднее: 32 дня

═══════════════════════════════════════════════════════════════
```

### 5. Present Update Options

```
ВЫБЕРИ ЧТО ОБНОВИТЬ:

[A] ALL POSTS — Обновить метрики для ВСЕ 87 постов
    Пересчитаю CTR, Engagement и Quality для всех

[R] RECENT — Обновить только свежие посты (последние 7 дней)
    Вариант для быстрого обновления (6 постов)

[O] OLD — Обновить старые посты (30+ дней назад)
    Для переоценки долгосрочного контента (54 поста)

[F] FILTER — Выбрать по критериям
    Только посты с CTR < 2% или другой фильтр

[M] MANUAL — Обновить конкретные посты
    Выбери номера постов вручную

[B] BACK — Вернуться в меню

═══════════════════════════════════════════════════════════════
```

Wait for user selection.

---

## SAVED DATA

Posts loaded in session:
```
posts_loaded: 87
last_update: 3 days ago
metrics_loaded:
  - all CTR values
  - all engagement values
  - all quality scores
ready_for_recalculation: true
```

---

## SUCCESS CRITERIA

- ✅ All 87 posts loaded
- ✅ Current metrics displayed
- ✅ Summary statistics shown
- ✅ User ready to select update scope

---

## NEXT STEP

Handle user selection:
- [A] → Execute `./step-e-04b-recalculate.md` (all posts)
- [R] → Filter recent, then execute `./step-e-04b-recalculate.md`
- [O] → Filter old, then execute `./step-e-04b-recalculate.md`
- [F] → Show filter options, then execute `./step-e-04b-recalculate.md`
- [M] → Show selection, then execute `./step-e-04b-recalculate.md`
- [B] → Return to `./e-00-menu.md`
