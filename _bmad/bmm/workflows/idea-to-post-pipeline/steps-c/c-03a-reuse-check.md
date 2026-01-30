---
description: Check if similar post was published recently before drafting new post
name: step-c-03a-reuse-check
nextStepFile: ./c-03c-draft.md
type: data-validation
requiredFiles:
  - posts_content.csv
  - ideas_research.csv
---

# CREATE C-03: Write Post - Reuse Check

## STEP GOAL

Before drafting a new post, check if a similar post was recently published. If yes, warn user and let them decide whether to create a variant or select a different idea.

This prevents publishing duplicate content and ensures content reuse strategy is optimized.

## EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting reuse check results.**
**ONLY proceed to next step when user provides explicit input/selection.**

---

## EXECUTION

### 1. Gather Input Data

You have:
- **Current idea_id** - The idea selected in step c-03a-select-idea.md
- **Content type** - From ideas_research.csv (main_angle field)

Example:
```
Current idea_id: 1
Content type: "ИИ экономит время"
Research date: 2026-01-27
```

### 2. Load posts_content.csv

Load all published posts (status = "ready" OR status = "published").

Focus on:
- `id` - Post ID
- `research_id` - Which research/idea this post is based on
- `publish_date` - When it was published
- `post_title_short` - Post title
- `content_250_chars` - Post preview
- `status` - Publication status

### 3. Check for Duplicate Ideas

**Search for posts where `research_id == current_idea_id`**

```
Current idea_id: 1

Posts found for idea_id=1:
  ✓ Post #1 (angle_1): "3 часа вместо недели"
    Published: 2026-01-28 (2 days ago)
    Status: ready

  ✓ Post #5 (angle_4): "ИИ контент или авторский текст?"
    Published: 2026-01-30 (0 days ago - TODAY!)
    Status: ready

  ✓ Post #7 (angle_3): "ИИ помогает взять новую высоту"
    Published: 2026-01-31 (1 day ago)
    Status: ready
```

### 4. Determine Content Type Category

Based on main_angle from ideas_research.csv, classify content type:

**Evergreen Content** (8 weeks / 56 days):
- ИИ экономит время
- Масштабирование личного бренда
- Quality vs speed
- Best practices
- Technical tutorials
- Strategy & systems

**Topical Content** (NEVER repost):
- Breaking news
- Time-sensitive topics
- Trends that are time-bound
- Event-based content

**Seasonal Content** (52 weeks / 365 days):
- Holiday-related
- Season-specific
- Annual events
- Cyclical topics

**Philosophical Content** (10 weeks / 70 days):
- Opinion pieces
- Philosophy
- Mindset shifts
- Values-based content

**Tutorial Content** (12 weeks / 84 days):
- How-to guides
- Step-by-step tutorials
- Technical guides
- Process documentation

**Content Type Detection Rules:**

```
IF main_angle contains: "экономит", "масштаб", "стратег", "система"
  → EVERGREEN (56 days)

IF main_angle contains: "тренд", "новое", "breaking", "срочно"
  → TOPICAL (NEVER)

IF main_angle contains: "новый год", "лето", "праздник", "сезон", "декабр", "январ"
  → SEASONAL (365 days)

IF main_angle contains: "философ", "мысль", "убежден", "верую", "вижу"
  → PHILOSOPHICAL (70 days)

IF main_angle contains: "как", "делай", "шаг", "инструкция", "гайд", "учебник"
  → TUTORIAL (84 days)

ELSE
  → DEFAULT EVERGREEN (56 days)
```

### 5. Calculate Days Since Last Publication

For each post found:
```
days_since_publication = TODAY - publish_date

Example:
Post #1: 2026-01-28 → 2 days ago
Post #5: 2026-01-30 → 0 days ago (TODAY!)
Post #7: 2026-01-31 → -1 days (FUTURE?! Check date)
```

### 6. Check Reuse Policy

**Get reuse window from content type:**

```
Content Type | Reuse Window | Action
─────────────────────────────────────────────────
Evergreen    | 56 days     | If < 56: warn, allow variant
Topical      | NEVER       | Always warn, strongly discourage
Seasonal     | 365 days    | If < 365: warn, allow variant
Philosophical| 70 days     | If < 70: warn, allow variant
Tutorial     | 84 days     | If < 84: warn, allow variant
```

### 7. Decision Logic - Build Reuse Decision Tree

```
IF no posts found for current_idea_id:
  → PROCEED to c-03c-draft.md (no conflicts)
  → Display: "✅ Новая идея. Создаём пост с нуля."

ELSE IF posts found AND (TODAY - latest_publish_date) < reuse_window:
  → WARN user (HALT and WAIT for response)
  → Show reuse options menu

ELSE IF posts found AND (TODAY - latest_publish_date) >= reuse_window:
  → ALLOW with note
  → Display: "✅ Последний пост был давно. Можешь создать новый."
  → PROCEED to c-03c-draft.md

ENDIF
```

---

## DISPLAY: Reuse Check Results

### SCENARIO A: No Similar Posts Found

```
═══════════════════════════════════════════════════════════════

  ✨ REUSE CHECK: No Conflicts Found

═══════════════════════════════════════════════════════════════

Идея: "ИИ экономит время"
Тип контента: Evergreen (56 дней между постами)

Результат: ✅ Похожих постов НЕ найдено

Можешь смело создавать новый пост на эту идею!

═════════════════════════════════════════════════════════════════
```

**Action:**
Load, read entire file, then execute `./c-03c-draft.md` immediately.

---

### SCENARIO B: Similar Posts Found - Within Reuse Window

```
═══════════════════════════════════════════════════════════════

  ⚠️  REUSE CHECK: Similar Posts Found

═══════════════════════════════════════════════════════════════

Идея: "ИИ экономит время"
Тип контента: Evergreen (56 дней между постами)
Статус: ⚠️ Похожие посты в течение реuse-окна!

НАЙДЕННЫЕ ПОСТЫ:

[1] Post ID #1 - "3 часа вместо недели"
    Опубликован: 2026-01-28 (2 дня назад)
    Угол: Time Saving ⏱️
    Превью: "3 часа вместо недели — вот что ИИ даёт контенту"
    Статус: ready

[2] Post ID #7 - "ИИ помогает взять новую высоту"
    Опубликован: 2026-01-31 (сегодня!)
    Угол: Growth & Scaling 📈
    Превью: "Масштабируй с ИИ умно"
    Статус: ready

─────────────────────────────────────────────────────────────

⚠️ ВНИМАНИЕ: Последний пост 0 дней назад (СЕГОДНЯ)
   Для evergreen-контента нужно 56 дней между постами.
   Осталось: 56 дней

Что ты хочешь сделать?

[V] VARIANT — Создать модифицированный вариант последнего поста
    (Обозначится как variant_of ID #7, но с новым углом/контентом)

[D] DIFFERENT IDEA — Выбрать другую идею из списка

[I] IGNORE WARNING — Создать независимый пост (на свой риск ⚠️)

[←] Back to SELECT IDEA — Вернуться к выбору идеи (c-03a-select-idea.md)

═════════════════════════════════════════════════════════════════
```

### SCENARIO C: Similar Posts Found - Outside Reuse Window

```
═══════════════════════════════════════════════════════════════

  ✅ REUSE CHECK: Safe to Create New Post

═══════════════════════════════════════════════════════════════

Идея: "ИИ экономит время"
Тип контента: Evergreen (56 дней между постами)
Статус: ✅ Reuse-окно истёк

НАЙДЕННЫЕ ПОСТЫ (архивные):

[1] Post ID #1 - "3 часа вместо недели"
    Опубликован: 2025-11-15 (77 дней назад) ✓ Safe
    Угол: Time Saving ⏱️

[2] Post ID #7 - "ИИ помогает взять новую высоту"
    Опубликован: 2025-12-10 (52 дня назад) ✓ Safe
    Угол: Growth & Scaling 📈

─────────────────────────────────────────────────────────────

✅ Достаточно времени прошло. Можешь создать новый пост!

Можешь:
• Использовать новый угол на ту же идею
• Обновить контент с новыми примерами
• Создать полностью оригинальный пост

[✅ PROCEED] — Создать новый пост (перейти к черновикам)

[↺ REVIEW PAST] — Посмотреть архивные посты для вдохновения

[←] Back to SELECT IDEA — Вернуться к выбору идеи

═════════════════════════════════════════════════════════════════
```

### SCENARIO D: Topical Content (NEVER Repost)

```
═══════════════════════════════════════════════════════════════

  🚫 REUSE CHECK: Topical Content - CANNOT REPOST

═══════════════════════════════════════════════════════════════

Идея: "Новые ИИ тренды 2026"
Тип контента: Topical (время-зависимый, НИКОГДА не переpost)
Статус: 🚫 Топик устарел, нельзя переpost!

НАЙДЕННЫЕ ПОСТЫ:

[1] Post ID #23 - "ТОП 5 ИИ трендов янв 2026"
    Опубликован: 2026-01-15 (15 дней назад)
    Статус: ready

─────────────────────────────────────────────────────────────

⚠️ ВНИМАНИЕ: Это time-sensitive контент!

Причины, почему НЕЛЬЗЯ переpost:
• Информация становится устаревшей
• Читатели потеряют доверие
• Алгоритмы штрафуют дублирующийся контент
• Твой бренд будет выглядеть ленивым

Рекомендация:
→ Выбери ДРУГУЮ идею
→ Или полностью переделай содержание (новые тренды, новые примеры)

Что ты хочешь?

[D] DIFFERENT IDEA — Выбрать другую идею

[G] GRANT EXCEPTION — Я знаю, что делаю (создать пост риск)

[←] Back to SELECT IDEA — Вернуться к выбору идеи

═════════════════════════════════════════════════════════════════
```

---

## HANDLE USER RESPONSES

### [V] VARIANT - Create Modified Variant

**Action:**
```
Выбрал: Создать модифицированный вариант

Отмечу как: variant_of Post #7

Переходим к генерации черновиков с учётом
что это будет модификация последнего поста...
```

1. Store in memory: `variant_of = 7`
2. Add note to draft generation step: "Create as variant of Post #7 - different angle/tone"
3. Load, read entire file, then execute `./c-03c-draft.md`

### [D] DIFFERENT IDEA - Return to Idea Selection

**Action:**
```
Выбрал: Выбрать другую идею

Возвращаемся к выбору идеи...
```

Load, read entire file, then execute `./c-03a-select-idea.md` (previous step)

### [I] IGNORE WARNING - Proceed at Own Risk

**Action:**
```
Выбрал: Создать независимый пост (игнорируя предупреждение)

⚠️ Риск понят. Записал в логе.

Переходим к генерации черновиков...
```

1. Log warning with timestamp
2. Create post without variant_of link
3. Add note: "Created despite recent similar post"
4. Load, read entire file, then execute `./c-03c-draft.md`

### [↺ REVIEW PAST] - Show Archive for Inspiration

**Action:**
```
Показываю архивные посты для вдохновения:

[1] Post #1 - "3 часа вместо недели" (77 дней назад)
    Угол: Time Saving ⏱️
    Текст: "3 часа вместо недели — вот что ИИ даёт контенту"

[2] Post #7 - "ИИ помогает взять новую высоту" (52 дня назад)
    Угол: Growth & Scaling 📈
    Текст: "Масштабируй с ИИ умно"

─────────────────────────────────────────────────────────────

Вдохновился? Теперь создаём новый пост с свежим взглядом!

[✅ PROCEED] — Создать новый пост (перейти к черновикам)
[←] Back to SELECT IDEA — Вернуться к выбору идеи
```

Proceed to `./c-03c-draft.md`

### [G] GRANT EXCEPTION - Override for Topical Content

**Action:**
```
Выбрал: Перепост с исключением (я знаю, что делаю)

⚠️ Риск понят. Записал в логе.

Переходим к генерации черновиков...
```

1. Log exception with timestamp and reason
2. Add strong warning note to post: "Re-posting topical content - keep content fresh!"
3. Proceed to `./c-03c-draft.md`

---

## EXECUTION RULE: HALT AND WAIT

**ALWAYS halt and wait for user input after presenting reuse check results.**

**ONLY proceed to next step when user provides explicit input/selection.**

**Do NOT auto-proceed even if only 1 option available.**

---

## NEXT STEP

**After user selection:**

- If [V] VARIANT or [I] IGNORE or [↺ REVIEW + PROCEED] → Execute `./c-03c-draft.md`
- If [D] DIFFERENT IDEA or [←] Back → Execute `./c-03a-select-idea.md`
- If [G] GRANT EXCEPTION → Execute `./c-03c-draft.md`

Load and read entire file before executing next step.

---

## DATA STORAGE

After user decision, store in session memory:

```
reuse_check_result = {
  idea_id: current_idea_id,
  content_type: detected_content_type,
  reuse_window_days: window_for_type,
  similar_posts_found: count,
  last_post_id: most_recent_post_id,
  days_since_last: days_diff,
  user_decision: "variant" | "different" | "ignore" | "exception",
  variant_of: post_id_if_variant,
  timestamp: ISO_timestamp
}
```

This data will be used in step c-03c-draft.md to:
- Mark posts as variants if applicable
- Add warnings to post metadata
- Track content reuse patterns
- Inform future reuse decisions

---

## QUALITY ASSURANCE

**Verify:**
- ✅ posts_content.csv loaded successfully
- ✅ research_id matches current_idea_id
- ✅ publish_date parsed correctly
- ✅ Content type detected correctly
- ✅ Reuse window calculated correctly
- ✅ User response captured and stored
- ✅ Next step file path correct

**If any check fails:**
```
⚠️ ERROR: [Description]

Please ensure:
- posts_content.csv exists and is readable
- dates are in YYYY-MM-DD format
- current_idea_id is set from previous step

[Retry check] [Skip reuse check and proceed] [Return to menu]
```

---

## NOTES FOR IMPLEMENTATION

1. **Date Parsing:** Use ISO format (YYYY-MM-DD) for all date calculations
2. **Null Handling:** If publish_date is NULL, treat post as draft (don't count for reuse)
3. **Case Sensitivity:** Match research_id exactly (case-sensitive)
4. **Content Type:** Use best_angle_id from ideas_research.csv for additional context
5. **Logging:** Track all reuse check decisions for analytics
6. **User Language:** Keep all user-facing text in Russian
7. **Wait Rule:** Always wait for user input - never auto-proceed
