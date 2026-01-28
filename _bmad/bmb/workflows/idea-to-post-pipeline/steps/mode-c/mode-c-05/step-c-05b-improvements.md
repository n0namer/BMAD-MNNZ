---
description: Display suggested improvements for selected post
name: step-c-05b-improvements
nextStepFile: ./step-c-05c-apply-edits.md
type: analysis
---

# CREATE C-05: Edit Post - Suggested Improvements

## STEP GOAL:

Analyze selected post and suggest specific improvements with checklist.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Load Post Content

Load full post text and metadata for selected post.

### 2. Analyze and Generate Suggestions

Evaluate post for:
- Structure and flow
- Grammar and readability
- SEO optimization
- Engagement factors
- Content completeness
- Visual formatting

### 3. Display Analysis

```
═══════════════════════════════════════════════════════════════

  📊  IMPROVEMENT SUGGESTIONS

═══════════════════════════════════════════════════════════════

POST: "ИИ контент за 3 часа"
CURRENT QUALITY: ⭐⭐⭐⭐☆ (4.2/5 - Very Good)

─────────────────────────────────────────────────────────────

🎯 SUGGESTED IMPROVEMENTS (6 suggestions):

─────────────────────────────────────────────────────────────

PRIORITY: HIGH (Критично)

[A] ✓ ADD VISUAL ELEMENTS
    Добавить изображения/диаграммы

    Почему: Посты с визуалом имеют на 40% выше engagement
    Где: В разделах "Step 1", "Step 3", "Results"
    Примеры: скриншоты инструментов, блок-схемы

[B] ✓ IMPROVE HEADLINE IMPACT
    Сделать заголовок более привлекательным

    Текущий: "ИИ контент за 3 часа"
    Вариант: "Создай 10 идей для постов за 3 часа (ИИ способ)"
    Бонус: +23% CTR по исследованиям

─────────────────────────────────────────────────────────────

PRIORITY: MEDIUM (Желательно)

[C] ✓ ADD REAL-WORLD EXAMPLES
    Добавить конкретные примеры использования

    Что добавить: 2-3 case-study или сценария
    Где: После каждого основного раздела
    Результат: +15% времени на чтение

[D] ✓ OPTIMIZE FOR SEO
    Добавить SEO оптимизацию

    Нужно: улучшить keyword density
    Добавить: meta-description, alt-text для изображений
    Проверить: H2/H3 структура заголовков

[E] ✓ EXPAND CALL-TO-ACTION
    Усилить заключение и призыв к действию

    Текущее: "Попробуй инструменты"
    Вариант: "Начни с ChatGPT бесплатно [ссылка]"
    Добавить: варианты для разного уровня читателя

─────────────────────────────────────────────────────────────

PRIORITY: LOW (Опционально)

[F] ✓ ADD INTERNAL LINKS
    Добавить ссылки на другие посты

    Связанные посты: "Speech-to-Text для блогеров"
    Где разместить: в конце, в контексте текста

[G] ⚠️  CONSIDER STRUCTURE REORGANIZATION
    Пересмотреть порядок секций (опционально)

    Текущий порядок логичен, но можно переместить
    примеры раньше для лучшего engagement

─────────────────────────────────────────────────────────────

ESTIMATED IMPACT:
  • Time to implement: ~15 minutes
  • Expected quality improvement: ⭐⭐⭐⭐⭐ (5.0/5)
  • Expected engagement boost: +25-40%

═════════════════════════════════════════════════════════════════
```

### 4. Display Improvement Checklist

```
CHOOSE IMPROVEMENTS TO APPLY:

Suggestions:
─────────────────────────────────────────────────────────────

☐ [A] Add Visual Elements
☐ [B] Improve Headline Impact
☐ [C] Add Real-World Examples
☐ [D] Optimize for SEO
☐ [E] Expand Call-to-Action
☐ [F] Add Internal Links
☐ [G] Consider Structure Reorganization

─────────────────────────────────────────────────────────────

SELECT TO APPLY:
[A] [B] [C] [D] [E] [F] [G] — каждую букву для выбора

QUICK ACTIONS:
─────────────────────────────────────────────────────────────

[A] APPLY ALL — Применить все предложения
[C] CUSTOM — Выбрать конкретные улучшения
[R] REVIEW — Подробный обзор каждого

─────────────────────────────────────────────────────────────

[!] AUTO-ENHANCE (AI) — Автоматически применить улучшения
    ⚠️  Проверь результат перед сохранением!

[V] VIEW POST — Посмотреть текущий пост
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

### 5. Handle Selection

**[A-G] Select individual improvements:**
```
Отмечено: A, B, C, E

Готов к применению 4 улучшений?

[Y] Continue — Да, применить
[M] Back to MENU — Отмена, в меню
```

If [Y]: Save selections, execute step-c-05c-apply-edits.md

**[A] APPLY ALL:**
```
Применяю все 7 предложений...

Это займет несколько минут.

Ожидай...
```
Apply all improvements, then execute step-c-05c-apply-edits.md

**[C] CUSTOM:**
```
Выбери какие улучшения применить (через пробел):

Пример: A B D E

_________________________________________
```
Wait for input, save selections, execute step-c-05c-apply-edits.md

**[R] REVIEW:**
```
═══════════════════════════════════════════════════════════════

  DETAILED REVIEW

═════════════════════════════════════════════════════════════════

[A] ADD VISUAL ELEMENTS
─────────────────────────────────────────────────────────────

Полное объяснение:
Визуальные элементы значительно улучшают восприятие...

[Подробный текст для каждого улучшения]

─────────────────────────────────────────────────────────────

[<] Back to Improvements — Назад
[Y] Ready to Apply — Готов применять
```

**[!] AUTO-ENHANCE:**
```
Применяю автоматические улучшения ИИ...

Это займет ~30 секунд...

✓ Завершено!

Проверь результаты перед сохранением.

Переходим к применению улучшений...
```
Apply all improvements via AI, then execute step-c-05c-apply-edits.md

**[V] VIEW POST:**
```
═══════════════════════════════════════════════════════════════

  CURRENT POST TEXT

═════════════════════════════════════════════════════════════════

[Full post content displayed]

─────────────────────────────────────────────────────────────

[<] Back to Improvements
[M] Back to MENU
```

**[M] Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

When improvements selected: Load, read entire file, then execute step-c-05c-apply-edits.md

### Menu Handling Logic

**IF [A]: APPLY ALL:**
```
Применяю все 7 предложений...

Это займет несколько минут.

Ожидай...
```
Apply all improvements, then execute step-c-05c-apply-edits.md

**IF [C]: CUSTOM:**
```
Выбери какие улучшения применить (через пробел):

Пример: A B D E

_________________________________________
```
Wait for input, save selections, execute step-c-05c-apply-edits.md

**IF [R]: REVIEW:**
```
═══════════════════════════════════════════════════════════════

  DETAILED REVIEW

═════════════════════════════════════════════════════════════════

[A] ADD VISUAL ELEMENTS
─────────────────────────────────────────────────────────────

Полное объяснение:
Визуальные элементы значительно улучшают восприятие...

[Подробный текст для каждого улучшения]

─────────────────────────────────────────────────────────────

[<] Back to Improvements — Назад
[Y] Ready to Apply — Готов применять
```

**IF [V]: VIEW POST:**
```
═══════════════════════════════════════════════════════════════

  CURRENT POST TEXT

═════════════════════════════════════════════════════════════════

[Full post content displayed]

─────────────────────────────────────────────────────────────

[<] Back to Improvements
[M] Back to MENU
```

**IF [M]: Back to MENU:**
Load `../mode-c-00-menu.md`

---

## NEXT STEP

When improvements selected: Load, read entire file, then execute step-c-05c-apply-edits.md

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.
