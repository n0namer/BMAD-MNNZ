---
description: Apply approved improvements to all selected posts simultaneously
name: step-e-01c-apply-edits
nextStepFile: ./e-00-menu.md
type: batch-apply-changes
---

# EDIT E-01c: Apply Batch Improvements

## STEP GOAL:

Apply approved improvements to all [N] selected posts and save changes to database.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Application Header

```
═══════════════════════════════════════════════════════════════

  ✅ ПРИМЕНЯЮ УЛУЧШЕНИЯ

  Обновляю [N] постов (займёт 10-15 сек)...

═══════════════════════════════════════════════════════════════
```

### 2. Apply Changes to Each Post

**POST #145: Applying Improvements**
```
Обновляю пост #145 "Как начать с нуля"...

OLD:
─────────────────
Как начать с нуля

Если ты только начинаешь, это может быть сложно. Вот несколько
советов которые мне помогли.
─────────────────

NEW:
─────────────────
Начни с нуля за месяц (пока конкуренты спят)
7 шагов которых они боятся

Если ты только начинаешь, это может быть сложно. Вот несколько
советов которые мне помогли.

[Оригинальный контент...]

Скачай чек-лист и начни сегодня →
─────────────────

✅ Применено!
  ✓ Заголовок улучшен
  ✓ Проблема добавлена
  ✓ CTA усилен
  ✓ История версии: v1 → v2
```

**POST #138: Applying Improvements**
```
Обновляю пост #138 "Частая ошибка #1"...

OLD:
─────────────────
Частая ошибка #1

Эту ошибку делают многие. Давай разберём.
─────────────────

NEW:
─────────────────
Это убило 90% моих результатов. Как я исправил (и ты можешь)

Эта ошибка стоит мне $1000+ в месяц. Давай разберём как её
избежать за 5 минут.

[Оригинальный контент...]

Примени сегодня же →
─────────────────

✅ Применено!
  ✓ Заголовок переписан
  ✓ Боль добавлена
  ✓ Решение уточнено
  ✓ История версии: v1 → v2
```

**POST #128: Applying Improvements**
```
Обновляю пост #128 "5 советов"...

OLD:
─────────────────
5 советов

Вот 5 советов которые помогут...
─────────────────

NEW:
─────────────────
5 советов которые дали мне 3x результаты
Применяю каждый день

Вот 5 советов которые полностью изменили мои результаты...

[Оригинальный контент...]

Начни с первого совета прямо сейчас →
─────────────────

✅ Применено!
  ✓ Заголовок улучшен
  ✓ Контекст добавлен
  ✓ CTA усилен
  ✓ История версии: v1 → v2
```

### 3. Update Metrics

```
═══════════════════════════════════════════════════════════════

📊 ОБНОВЛЕНИЕ МЕТРИК

Пересчитываю метрики для всех обновленных постов...

БЫЛО:
  #145 | CTR: 1.2% → ПРОГНОЗ: 1.8-2.0% (+50-65%)
  #138 | CTR: 0.9% → ПРОГНОЗ: 1.5-1.6% (+65-75%)
  #128 | CTR: 1.3% → ПРОГНОЗ: 1.5-1.7% (+15-25%)

СРЕДНИЙ РЕЗУЛЬТАТ:
  Было: 1.13% | Стало (прогноз): 1.6-1.77% (+42-56%)

✅ Метрики обновлены и сохранены

═══════════════════════════════════════════════════════════════
```

### 4. Save Changes

```
💾 СОХРАНЕНИЕ ИЗМЕНЕНИЙ

Сохраняю:
  ✅ Обновленные тексты постов → posts_main.csv
  ✅ Новые метрики → metrics_tracking.csv
  ✅ История версий → post_history.csv (v1 → v2)
  ✅ Лог изменений → edit_audit.log

Все изменения сохранены. Можешь откатить если что.
```

### 5. Display Summary

```
═══════════════════════════════════════════════════════════════

  ✅ УСПЕШНО! Все улучшения применены

═══════════════════════════════════════════════════════════════

📋 ИТОГИ:

ОБНОВЛЕНО ПОСТОВ: 3
  • #145 "Как начать с нуля" → v2
  • #138 "Частая ошибка #1" → v2
  • #128 "5 советов" → v2

⏱️  ВРЕМЯ ВЫПОЛНЕНИЯ: 12 сек

📊 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
  • Улучшение CTR: +42-56% (в среднем)
  • Улучшение engagement: +40-50%
  • Улучшение quality score: +15-20 пунктов

💾 СОХРАНЕНО В:
  • posts_main.csv (обновленные посты)
  • metrics_tracking.csv (новые метрики)
  • post_history.csv (версии v1 и v2)
  • edit_audit.log (полный лог)

═══════════════════════════════════════════════════════════════
```

### 6. Present Next Steps

```
ДАЛЬШЕ?

[M] MORE — Улучшить ещё посты
    Вернуться к E-01a (выбрать другие посты)

[E] EDIT MODE MENU — Другой тип улучшений
    Чек-лист, A/B тесты, метрики и т.д.

[V] VIEW CHANGES — Просмотреть все изменения детально
    Side-by-side сравнение для каждого поста

[U] UNDO — Откатить последние изменения
    Вернуть посты в исходное состояние

[MENU] Back to Main Menu

═══════════════════════════════════════════════════════════════
```

Wait for user selection.

---

## SAVED DATA

Changes logged to:
```
edit_audit.log:
- [2026-01-28 14:35:22] BULK EDIT applied
  Posts: #145, #138, #128
  Action: Hook+Problem+CTA improvements
  Expected impact: +42-56% CTR
  Status: Applied
  Version: v1 → v2

posts_main.csv:
- #145: Updated with new headline
- #138: Updated with new headline
- #128: Updated with new headline

metrics_tracking.csv:
- All posts: Metrics updated with projections
```

---

## CRITICAL RULES

- ✅ ALWAYS save to audit trail for rollback capability
- 📊 ALWAYS update metrics with projections
- 💾 ALWAYS preserve version history
- 🔄 ALWAYS allow undo for user peace of mind

---

## SUCCESS CRITERIA

- ✅ All [N] posts updated
- ✅ Changes saved to all relevant files
- ✅ Audit trail created for rollback
- ✅ New metrics calculated and displayed
- ✅ Version history preserved (v1 → v2)

---

## NEXT STEP

Handle user selection:
- [M] → Return to `./step-e-01a-select-posts.md`
- [E] → Return to `./e-00-menu.md`
- [V] → Display detailed changes
- [U] → Rollback to previous version
- [MENU] → Return to main menu
