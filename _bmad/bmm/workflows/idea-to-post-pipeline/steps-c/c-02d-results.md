---
description: Display detailed research results (all angles with sources)
name: step-c-02d-results
nextStepFile: ./c-03a-select-idea.md
type: results-display
---

## DATA REFERENCE

All angles accessible from ideas_research.csv for future use.

---

## NEXT STEP

Handle user selection and route to writing step

**EXECUTION RULE:**
ALWAYS halt and wait for user input after presenting menu. ONLY proceed when user makes a selection.

---

# CREATE C-02: Research - Results

## STEP GOAL:

Display detailed research results with all angles, sources, and facts.

## EXECUTION:

### 1. Display Results Header

```
═══════════════════════════════════════════════════════════════

  📊 RESEARCH RESULTS: "ИИ контент за 3 часа"

═══════════════════════════════════════════════════════════════

Total angles found: 8
Average relevance: 86%
Total sources: 32
Research time: 18 minutes
```

### 2. Show All Angles in Detail

```
ANGLE 1: Time Saving ⏱️  [Relevance: 92%] ⭐⭐⭐⭐⭐
─────────────────────────────────────────────────
Insight: "Saves 70% of content creation time"

Key Facts:
  • Traditional copywriter: 2-3 hours per post
  • With ИИ assistance: 20-30 minutes per post
  • Productivity gain: 70-75% time savings

Sources (7 found):
  1. "The State of AI in Content Creation 2025" - TechCrunch
  2. Case study: "How Company X Scaled with ИИ" - LinkedIn
  3. Research: "Productivity gains with generative ИИ" - McKinsey
  ... (4 more sources)

Best for: Founders, busy professionals, agencies
Post angle: "3 часа вместо недели..."

─────────────────────────────────────────────────

ANGLE 2: Quality Control 🎯  [Relevance: 88%] ⭐⭐⭐⭐
─────────────────────────────────────────────────
Insight: "ИИ content can be higher quality with proper editing"

Key Facts:
  • Quality depends heavily on prompts
  • Human editing adds personal voice
  • Hybrid approach: ИИ + editing yields best results

Sources (5 found):
  1. "Best practices for ИИ-assisted writing" - Copyblogger
  2. Study: "Quality assessment of AI-generated content" - Harvard
  ... (3 more sources)

Best for: Quality-focused brands, perfectionists
Post angle: "ИИ контент не значит плохой контент..."

─────────────────────────────────────────────────

[Continue for all 8 angles...]

═════════════════════════════════════════════════════════════════
```

---

### 2.5 Боли Предпринимателей (только для Content Machine)

**Условие:** Отображается только если `content_type == "demo"`

Система показывает боли, которые были автоматически сгенерированы на шаге c-02c (Section 2.5):

```
🔴 БОЛИ ПРЕДПРИНИМАТЕЛЕЙ (для каждого угла)

Для КАЖДОГО угла система выделила боли, которые ваша рутина решает.
Эти боли будут автоматически вшиты в черновики постов!

ANGLE 1: Time Saving ⏱️
Боли, которые эта рутина решает:
├─ 🔴 Медленная документация берёт 2-3 дня на большой объём
├─ 🔴 Все процессы в голове у одного человека
├─ 🔴 Нельзя масштабировать без найма новых специалистов
└─ 🔴 Непроцессированная информация = нельзя продать бизнес

ANGLE 2: Quality Control 🎯
Боли, которые эта рутина решает:
├─ 🔴 Качество документов зависит от того кто написал
├─ 🔴 Нет стандарта, каждый пишет по-своему
├─ 🔴 Редактирование и проверка занимают много времени
└─ 🔴 Трудно передать задачу другому

ANGLE 3: Scalability 📈
Боли, которые эта рутина решает:
├─ 🔴 Масштабирование = нанять людей, не масштабировать процесс
├─ 🔴 Зарплаты специалистов растут быстрее дохода
├─ 🔴 Бизнес привязан к конкретным людям
└─ 🔴 Потеря контекста при передаче задач

[Продолжение для всех углов...]

💡 КАК ЭТО РАБОТАЕТ:

Когда вы дойдёте до написания черновиков (шаг c-03c),
система будет генерировать 6 вариантов вместо 3:

├─ Варианты 1-3: Базовые фреймворки (как обычно)
└─ Варианты 4-6: Content Machine фреймворки с вшитыми болями!
    ├─ Вариант 4: PAS (Problem → Agitate → Solution)
    ├─ Вариант 5: Hook-Story-Offer
    └─ Вариант 6: Show Your Work (Austin Kleon)
```

---

### 3. Present Choices

```
Что дальше?

[1-8] SELECT ANGLE — Выбери угол для написания поста
[W] WRITE ANY — Напиши пост (я выберу лучший угол)
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

**[1-8] SELECT ANGLE:**
User selects which angle to use for writing. Load, read entire file, then execute `./c-03b-select-angle.md` with selected angle

**[W] WRITE ANY:**
Auto-select best angle (highest relevance) and proceed to writing. Load `./c-03b-select-angle.md`

**[M] Back to MENU:**
Load `./c-00-menu.md`

---

## DATA REFERENCE

All angles accessible from ideas_research.csv for future use.

---

## NEXT STEP

Handle user selection and route to writing step
