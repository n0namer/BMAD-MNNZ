# Stage 5 Implementation - Code Analysis & Gaps

**Date:** 2026-01-30
**Files Analyzed:** c-03c-draft.md, c-03d-variants.md, c-03e-finalize.md

---

## ACTUAL CODE IMPLEMENTATION

### 1. c-03c-draft.md — Where Frameworks Should Be Applied

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03c-draft.md`

**What It Does:**
- Generates 3 draft post variations
- Each has different style/focus
- All include soft CTAs
- Quality scores provided

**Code Snippet (Lines 42-125):**

```markdown
### 2. Generate 3 Drafts

Using angle + research data, create 3 variations:

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
```

**DRAFT 2 - STORYTELLING (Narrative-focused)**

```markdown
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
```

**DRAFT 3 - DATA-DRIVEN (Numbers-focused)**

```markdown
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
```

---

### 2. c-03d-variants.md — Size Variants (Not Framework Variants)

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03d-variants.md`

**What It Does:**
- Takes selected draft
- Creates 500-char, 250-char, 100-char versions
- Different length targets, NOT different frameworks

**Code Snippet (Lines 49-90):**

```markdown
### 2. Generate Variants

**500-char (original):**
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

**250-char version:**
3 часа вместо недели: как ИИ подтягивает контент 👉
Писать вручную = 8 часов в день + ноль роста.
ИИ меняет всё:
✅ 3 готовых поста за 3 часа
✅ Больше времени на стратегию
✅ Масштабирование без найма
👉 Попробуй сегодня

**100-char version:**
3 часа вместо недели: как ИИ подтягивает контент 👉
Попробуй сегодня и сэкономь 7 часов в неделю!
```

**KEY INSIGHT:** These are LENGTH variants, not FRAMEWORK variants.
The same post is just shortened for different platforms.

---

### 3. c-03e-finalize.md — Quality Checks

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03e-finalize.md`

**What It Does:**
- Final review of post
- Validates components
- Checks CTA presence
- Saves to database

**Code Snippet (Lines 62-75):**

```markdown
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
```

**Editable Components (Lines 132-136):**

```markdown
Какой раздел редактировать?

[H] Hook — Первое предложение
[P] Problem — Описание проблемы
[S] Solution — Предложенное решение
[T] Trigger — Социальный proof
[C] CTA — Call-to-action
[F] Full text — Весь текст целиком
```

---

## WHAT'S MISSING

### 1. No Framework Selection Menu

**Current Flow:**
```
Select idea → Select angle → Generate 3 drafts → Choose draft → Save
```

**Should Be:**
```
Select idea → Select angle → SELECT FRAMEWORK → Generate 3 drafts → Choose draft → Save
                                 ↓
                    [1] Show Your Work
                    [2] PAS
                    [3] Hook-Story-Offer
                    [4] Behind-the-Scenes
                    [A] Auto-Select
```

**Gap:** No menu for framework selection before c-03c-draft.md

---

### 2. No Show Your Work Variants

**What Show Your Work Should Look Like:**

```markdown
DRAFT - SHOW YOUR WORK (Process-focused)
─────────────────────────────────────────
Как я генерирую 3 поста за 3 часа вместо недели

Вот мой процесс:

1️⃣ ИССЛЕДОВАНИЕ (30 мин)
   • Открываю ChatGPT
   • Ввожу тему
   • Изучу 3-5 вариантов идей
   • Выбираю угол

2️⃣ ГЕНЕРАЦИЯ (20 мин)
   • Задаю промпт с требованиями
   • ИИ генерирует 3 варианта
   • Я читаю, выбираю лучший

3️⃣ РЕДАКТИРОВАНИЕ (10 мин)
   • Делаю правки
   • Проверяю на ошибки
   • Добавляю эмодзи

Готово! 3 поста, 1 час.

Традиционно: 3 часа на пост = 9 часов на 3 поста
У меня: 1 час на 3 поста

👉 Хочешь узнать мой точный процесс? Напиши в комментариях.

Quality score: 85/100 | CTR potential: 4.1%
```

**Gap:** This variant type doesn't exist in c-03c-draft.md

---

### 3. No Behind-the-Scenes Variants

**What Behind-the-Scenes Should Look Like:**

```markdown
DRAFT - BEHIND-THE-SCENES (Authentic demonstration)
──────────────────────────────────────────────────
Ночь 2026-01-28, 23:45. Я генерирую контент для клиента.

[Вот что происходит в реальности]

Открываю Claude. Вставляю краткую идею:
"Тема: ИИ контент за 3 часа. Угол: экономия времени"

Жду 45 секунд... готово. 3 варианта.

Читаю первый. Нравится.
Читаю второй. Хм, можно лучше.
Читаю третий. Вот это!

Копирую лучший. Редактирую 7 мин. Добавляю свои цифры.

Результат? Пост готов. Качество 89/100.

За 3 часа я сделаю так 3 раза.

Это не магия. Это процесс.

👉 Попробуй то же самое прямо сейчас.

Quality score: 87/100 | CTR potential: 4.3%
```

**Gap:** This variant type doesn't exist in c-03c-draft.md

---

### 4. No PAS Framework Explicit Variant

**What Explicit PAS Should Look Like:**

```markdown
DRAFT - PAS FRAMEWORK (Problem-Agitate-Solution)
─────────────────────────────────────────────────
[PROBLEM]
Ты пишешь контент 8 часов в день.
Каждый пост — это 2-3 часа работы.
Ты устаешь. Результатов не видишь.

[AGITATE]
А давай посчитаем: 8 часов × 5 дней = 40 часов в неделю
40 часов × 4 недели = 160 часов в месяц
160 часов × $30/час = $4800 на один человека

При этом контент может не зайти. Клиент уходит. Все зря.

[SOLUTION]
ИИ меняет всё:
• 3 часа вместо недели ✅
• $20/месяц подписка вместо $4800 ✅
• Варианты, которые работают ✅

👉 Попробуй это. Вычисли свою экономию.

Quality score: 88/100 | CTR potential: 4.1%
```

**Gap:** PAS is implicit in Draft 2 "Storytelling" but not explicitly labeled or controlled by user

---

## DOCUMENTED VS IMPLEMENTED

### From workflow.md (Lines 101-107):

```markdown
**Stage 5: OUTPUT — Post Generation**
- Frameworks used:
  - **Show Your Work** (Austin Kleon): Process over product
  - **PAS** (Problem-Agitate-Solution): Pain → Amplify → Solve
  - **Hook-Story-Offer**: Attention → Narrative → CTA
  - **Behind-the-Scenes**: Authentic work demonstrations
- Output: 2-3 Telegram post variants with soft CTAs
```

### Actual Implementation Status:

| Framework | Documented? | Implemented? | Where? | Notes |
|-----------|------------|--------------|--------|-------|
| Show Your Work | ✅ YES | ❌ NO | - | No process-focused draft |
| PAS | ✅ YES | ⚠️ IMPLICIT | Draft 2 | Storytelling uses PAS elements but user doesn't know |
| Hook-Story-Offer | ✅ YES | ⚠️ IMPLICIT | All drafts | Structure is there but not labeled |
| Behind-the-Scenes | ✅ YES | ❌ NO | - | No authentic demo draft |

---

## SOFT CTA VERIFICATION

**All 3 drafts include CTAs:**

| Draft | CTA | Type | Soft? |
|-------|-----|------|-------|
| Draft 1 | "👉 Закинь пост в сохранённые и попробуй сегодня" | Action-oriented | ✅ YES |
| Draft 2 | "👉 Вот как..." | Curiosity-driven | ✅ YES |
| Draft 3 | "👉 Попробуй и вычисли сам" | Value-focused | ✅ YES |

**CTA Validation:** Present in c-03e-finalize.md (line 68):
```
║  CTA clarity:          ✅ EXPLICIT             ║
```

---

## SUMMARY OF GAPS

1. **No Framework Selection** — User can't choose which framework to use
2. **Show Your Work Missing** — No process-focused variants
3. **Behind-the-Scenes Missing** — No authentic demo variants
4. **PAS Not Explicit** — Used implicitly in Draft 2, not by name
5. **Hook-Story-Offer Not Explicit** — Present in structure, not by name
6. **No Content Machine Pipeline** — Stages 1-4 (routine → pain → offer → filter) not implemented
7. **No Framework Explanation** — Users don't know WHY a framework is used

---

## RECOMMENDED CODE CHANGES

### Change 1: Add Framework Selection to c-03b-select-angle.md (or new c-03c0-select-framework.md)

```markdown
## Framework Selection (NEW STEP)

After selecting angle, user selects framework:

[1] Show Your Work — Focus on your process
    "Step 1: ... Step 2: ... Step 3: ..."
    Best for: Building authority, demonstrating methodology

[2] PAS — Problem-Agitate-Solution
    "The problem: ... The pain: ... The solution: ..."
    Best for: Converting skeptics, pain-driven audiences

[3] Hook-Story-Offer — Attention-Narrative-CTA
    "Hook: ... Story: ... What you get: ..."
    Best for: Viral engagement, narrative-driven audiences

[4] Behind-the-Scenes — Authentic routine demonstration
    "Here's what I'm really doing: ... The results: ..."
    Best for: Trust-building, authenticity, proof

[A] AUTO-SELECT — Based on angle + audience

Selected: ___________
Proceeding to generate variants...
```

### Change 2: Update c-03c-draft.md to generate framework-specific variants

Instead of:
- Draft 1: Direct & Punchy
- Draft 2: Storytelling
- Draft 3: Data-Driven

Generate:
- Variant 1: Using selected framework
- Variant 2: Using selected framework (different angle/approach)
- Variant 3: Using selected framework (different audience)

---

## CONCLUSION

**Current Implementation: ~60% Complete**

**Working:**
- ✅ Basic post generation
- ✅ Size variants
- ✅ Soft CTAs
- ✅ Quality validation
- ✅ Multi-component editing

**Missing:**
- ❌ Framework selection menu
- ❌ Show Your Work implementation
- ❌ Behind-the-Scenes implementation
- ❌ Explicit PAS/Hook-Story-Offer labeling
- ❌ Content Machine full pipeline (c-09+)

**To Complete Stage 5:** Add framework selection menu + 2 missing framework implementations (Show Your Work, Behind-the-Scenes). PAS and Hook-Story-Offer already exist implicitly and can be explicitly labeled.

