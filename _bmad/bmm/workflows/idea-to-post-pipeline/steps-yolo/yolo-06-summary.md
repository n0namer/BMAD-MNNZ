---
description: Display final results (all posts + variants + scores) and present user choices (Accept/Select/Generate more/Back)
name: step-yolo-06-summary
nextStepFile: ../step-00-menu.md
type: results-presentation
---

# YOLO Step 6: Final Summary & Results

## STEP GOAL:

Present complete results with all created posts, variants, validation scores, and quality metrics. Give user clear choices for next action.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Results Header

```
═══════════════════════════════════════════════════════════════

           🎉 YOLO AUTOMATION COMPLETE!

═══════════════════════════════════════════════════════════════

⏱️  Total execution time: 2 мин 45 сек (вместо 6-8 часов!)

═══════════════════════════════════════════════════════════════
```

### 2. Show Content Created

```
📋 CONTENT CREATED:

  ✅ Ideas added: 3
  ✅ Research angles found: 24 (avg 8 per idea)
  ✅ Posts written: 9
  ✅ Posts improved: 7 (auto-fix applied)
  ✅ Variants generated: 36 (4 per post)

  📊 Quality Metrics:
     • Posts passing validation: 8/9 (89%)
     • Avg CTR potential: 4.1% (EXCELLENT)
     • Avg engagement score: 4.3/5 (VERY GOOD)
     • Copy quality: 92% excellent + good
```

### 3. Sample Results

```
SAMPLE: Top 3 Performing Posts

POST #1: "3 часа вместо недели: как ИИ подтягивает контент"
├─ Validation Score: ✅ 92/100
├─ CTR Potential: 4.5% (EXCELLENT)
├─ Engagement: 4.8/5 ⭐
├─ Best Variant: EMOTIONAL (engagement focus)
└─ Status: READY TO PUBLISH

POST #3: "5 успешных фаундеров уже используют этот способ"
├─ Validation Score: ✅ 91/100
├─ CTR Potential: 4.2% (EXCELLENT)
├─ Engagement: 4.5/5 ⭐
├─ Best Variant: SOCIAL PROOF (credibility focus)
└─ Status: READY TO PUBLISH

POST #8: "Вот чего ты не знаешь про ИИ и контент..."
├─ Validation Score: ✅ 94/100 ⭐ TOP PERFORMER
├─ CTR Potential: 4.8% (EXCELLENT)
├─ Engagement: 4.9/5 ⭐
├─ Best Variant: CURIOSITY (click-through focus)
└─ Status: READY TO PUBLISH

⚠️  POST #6: Quality concerns (74/100)
├─ Issue: Weak hook, unclear problem
├─ Status: NEEDS REVIEW before publishing
└─ Option: Manually rewrite or discard
```

### 4. Present User Choices

```
═══════════════════════════════════════════════════════════════

ВЫБЕРИ ЧТО ДЕЛАТЬ:

[1] ✅ ACCEPT ALL — Сохранить все посты в базу
    (8 готовых к публикации + 1 для ревью)

[2] 📝 SELECT & SAVE — Выбрать какие посты сохранить
    (Покажу список для выбора)

[3] 📊 VIEW DETAILS — Показать полный отчёт
    (Все посты, варианты, метрики)

[4] 🔄 GENERATE MORE — Создать ещё посты из этих идей
    (Новые варианты, другие углы)

[5] 🚀 NEW YOLO RUN — Запустить новый YOLO с другими идеями
    (Вернёмся к шагу 1)

[6] 📁 BACK TO MENU — Вернуться в главное меню
    (Другие режимы)

[?] HELP — Показать справку

═══════════════════════════════════════════════════════════════
```

### 5. Handle User Selection

**[1] ACCEPT ALL:**
```
✅ Сохраняю все посты в базу...

Статус:
  ✅ 8 постов сохранены (ready to publish)
  ⚠️  1 пост отмечен для ревью
  📅 Можешь публиковать по расписанию

Дальше можешь:
  • Перейти в EDIT MODE для доработок
  • Перейти в VALIDATE для финальной проверки
  • Начать новый YOLO run

Возвращаемся в меню...
```

**[2] SELECT & SAVE:**
```
Какие посты сохранить?

[✓] Post #1 (92/100) ✅ Excellent
[✓] Post #2 (84/100) ⚠️  Good
[✓] Post #3 (91/100) ✅ Excellent
[✗] Post #6 (74/100) ⚠️  Needs review
...

[S] SAVE SELECTED — Сохранить выбранные
[A] SELECT ALL — Выбрать все
[N] NONE — Ничего не сохранять
```

**[3] VIEW DETAILS:**
```
🔍 Загружаю полный отчёт...

(Display comprehensive report with all posts,
all variants, detailed metrics, recommendations)
```

**[4] GENERATE MORE:**
```
🔄 Запускаю новую генерацию с этими идеями...

Использую новые углы:
  • Для идеи #1: углы 5-7 (не использовались)
  • Для идеи #2: углы 6-8 (не использовались)
  • Для идеи #3: углы 7-9 (не использовались)

Вернусь на шаг 2 (parallel execute)...
```

**[5] NEW YOLO RUN:**
```
🚀 Готов к новому YOLO run!

Вернусь на шаг 1 (input specification)...
Скажи мне что создать дальше!
```

**[6] BACK TO MENU:**
```
📁 Возвращаемся в главное меню...

(Load step-00-menu.md)
```

### 6. Final Status Display

```
═══════════════════════════════════════════════════════════════

  📊 YOLO RUN SUMMARY:

  ✅ 9 posts created (8 ready, 1 for review)
  ✨ 36 variants generated
  🎯 Average quality: 89/100
  📈 Predicted CTR boost: +15% vs manual
  ⏱️  Execution time: 2м 45с (vs 6-8 hours manual)

═══════════════════════════════════════════════════════════════
```

---

## SUCCESS CRITERIA

- ✅ All results clearly presented
- ✅ User has clear choices for next action
- ✅ Can accept all, select specific, or generate more
- ✅ Ready to route to appropriate next step

---

## NEXT STEP

Handle user selection and route accordingly:
- [1] → Save to database → Back to step-00-menu.md
- [2] → Select subset → Save → Back to step-00-menu.md
- [3] → Show details → Return to this menu
- [4] → Generate more → Restart at step-yolo-02-parallel-execute.md
- [5] → New run → Restart at step-yolo-01-input.md
- [6] → Back → Load step-00-menu.md
