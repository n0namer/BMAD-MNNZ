---
name: step-c-03e-finalize
description: Final approval of post and save to database
type: finalization
nextStepFile: ./c-00-menu.md
---

<!-- STORAGE NOTE: Post data saved to posts_content.csv
   Fields: id, research_id, angle_used, publish_date, platform, post_title_short,
           content_500_chars, content_250_chars, content_100_chars, quality_score,
           ctr_potential, engagement_score, status, notes
   Status for draft: SAVED (draft, not published) -->


## SAVED DATA

When [Y] confirmed, post saved to posts_content.csv:
```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
post_001,1,"Time Saving",NULL,telegram,"3 часа вместо недели","[500 text]","[250 text]","[100 text]",89,4.2,4.5,draft,"Initial draft created"
```

---

## NEXT STEP

Handle final choice (save → next operation, or back to menu)

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-03: Write Post - Finalize

## STEP GOAL:

Final review of post, validation check, and save to posts_content.csv.

## EXECUTION:

### 1. Display Post for Final Review

```
═════════════════════════════════════════════════════════════════

  ✅ FINAL REVIEW

═════════════════════════════════════════════════════════════════

Post Summary:
─────────────────────────────────────────────────

Идея: "ИИ контент за 3 часа"
Угол: Time Saving ⏱️
Версия: Draft 1 (DIRECT & PUNCHY)
Status: DRAFT (не опубликовано)

[500-char version]
3 часа вместо недели: как ИИ подтягивает контент 👉
Писать контент вручную — это 8 часов в день и ноль роста.
... [full text]

╔═════════════════════════════════════════════════╗
║  QUALITY CHECK                                  ║
╠═════════════════════════════════════════════════╣
║  Hook strength:        ✅ STRONG               ║
║  Problem clarity:      ✅ CLEAR                ║
║  Solution relevance:   ✅ RELEVANT             ║
║  CTA clarity:          ✅ EXPLICIT             ║
║  Tone consistency:     ✅ CONSISTENT           ║
║─────────────────────────────────────────────── ║
║  Quality Score:        89/100 ⭐⭐⭐⭐⭐       ║
║  CTR Potential:        4.2% (EXCELLENT)        ║
║  Engagement Score:     4.5/5 ⭐⭐⭐⭐         ║
║  Status:               ✅ READY TO PUBLISH     ║
╚═════════════════════════════════════════════════╝

═════════════════════════════════════════════════════════════════
```

### 2. Present Choices

```
Готово? Что дальше?

[Y] YES, SAVE — Сохранить пост в базу
[E] EDIT — Отредактировать текст
[R] REJECT — Отклонить и создать новый
[V] VALIDATE AGAIN — Повторить проверку качества
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

### 3. Handle Choices

**[Y] YES, SAVE:**
```
✅ Сохраняю пост...

Post ID: post_001 [assigned]
Status: SAVED (draft, not published)
Location: posts_content.csv

✅ Готово!

Варианты сохранены:
  • 500-char version
  • 250-char version
  • 100-char version
```

Save to posts_content.csv, then proceed:

```
Что дальше?

[+] ADD MORE POSTS — Создать ещё пост из этого же угла
[D] DIFFERENT IDEA — Выбрать другую идею
[P] PUBLISH — Опубликовать этот пост
[A] ANALYTICS — Посмотреть как работают твои посты
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

Handle new selection

**[E] EDIT:**
```
Какой раздел редактировать?

[H] Hook — Первое предложение
[P] Problem — Описание проблемы
[S] Solution — Предложенное решение
[T] Trigger — Социальный proof
[C] CTA — Call-to-action
[F] Full text — Весь текст целиком

[After edits, return to final review]
```

**[R] REJECT:**
```
⚠️  Отклоняю пост.

Хочешь создать новый с другим углом?

[Y] Да, новый пост
[M] Back to MENU
```

**[V] VALIDATE AGAIN:**
Re-run quality checks and display results

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## SAVED DATA

When [Y] confirmed, post saved to posts_content.csv:
```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
post_001,1,"Time Saving",NULL,telegram,"3 часа вместо недели","[500 text]","[250 text]","[100 text]",89,4.2,4.5,draft,"Initial draft created"
```

---

## NEXT STEP

Handle final choice (save → next operation, or back to menu)
