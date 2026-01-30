---
name: step-c-03c-draft-enhanced
description: Load workflow state, generate 3-6 draft variations, embed pain points and offers into Content Machine frameworks, save draft metadata
type: content-generation
nextStepFile: ./c-03d-variants.md
---

<!-- METADATA
   Russian Title: Генерация Черновиков с Вшитыми Офферами (Content Machine Stage 4)
   Estimated Time: ~2-3 minutes
   Input: workflow_state.json (with generated_offers, pain_points)
   Output: 3-6 draft variations, selected_draft saved to workflow_state.json
   Stage: Content Machine Stage 4
-->

# Step C-03c: Генерация Черновиков с JSON State (Content Machine Stage 4)

**Цель:** Генерировать 3-6 вариантов черновика поста, вшивая в них боли и офферы из JSON state. Сохранить выбранный вариант обратно в state.

**Тип:** Content Generation

**Зависит от:** c-03b2 (должен создать `.workflow_state.json` с офферами)

---

## Концепция

На этом шаге система:

1. **Загружает state** из `.workflow_state.json`
2. **Генерирует 3 базовых варианта** (для всех типов контента)
   - DIRECT & PUNCHY (Hook-focused)
   - STORYTELLING (Narrative-focused)
   - DATA-DRIVEN (Numbers-focused)
3. **Генерирует 3 CM варианта** (ТОЛЬКО если `content_type == "demo"`)
   - PAS: Problem-Agitate-Solution (вшивает боли из `pain_points`)
   - Hook-Story-Offer (вшивает офферы из `generated_offers`)
   - Show Your Work (Austin Kleon, комбо боли + оффер)
4. **Сохраняет черновики** и их метаданные в state
5. **Ожидает выбора пользователя**

---

## Step 1: Load Workflow State

**Система проверяет наличие state файла:**

```bash
if [ ! -f ".workflow_state.json" ]; then
    echo "⚠️ ERROR: workflow_state.json not found"
    echo ""
    echo "workflow_state.json is created by step c-03b1 (Offer Filter Setup)"
    echo ""
    echo "Possible causes:"
    echo "1. Step c-03b1 was not run"
    echo "2. Session expired (state auto-cleaned after 8 hours)"
    echo "3. File was manually deleted"
    echo ""
    echo "Solution: Go back to c-03b1 to initialize state"
    exit 1
fi

# Load state
STATE=$(cat .workflow_state.json)

# Check expiry
EXPIRES=$(echo "$STATE" | jq -r '.state_expires_at')
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

if [ "$NOW" > "$EXPIRES" ]; then
    echo "⚠️ Workflow state has expired (created 8+ hours ago)"
    echo "Session state was auto-cleaned"
    exit 1
fi

echo "✅ State loaded from .workflow_state.json"
```

**Extract Key Data:**

```bash
IDEA_TEXT=$(echo "$STATE" | jq -r '.idea_text')
SELECTED_ANGLE=$(echo "$STATE" | jq -r '.selected_angle')
PAIN_POINTS=$(echo "$STATE" | jq -r '.pain_points | join(", ")')
GENERATED_OFFERS=$(echo "$STATE" | jq -r '.generated_offers')
WILLING_OFFERS=$(echo "$STATE" | jq -r '.willing_offers')
CONTENT_TYPE=$(echo "$STATE" | jq -r '.content_type')
```

---

## Step 2: Check if Variant of Existing Post

**Before drafting new post, check reuse:**

```bash
# Load existing published posts
if [ -f "./posts_content.csv" ]; then
    # Search for posts with similar idea/angle
    SIMILAR_POSTS=$(cat posts_content.csv | \
        grep -i "$SELECTED_ANGLE" | \
        head -5)

    if [ ! -z "$SIMILAR_POSTS" ]; then
        echo "ℹ️  Found similar published posts with this angle:"
        echo "$SIMILAR_POSTS"
        echo ""
        echo "Do you want to:"
        echo "[1] Create variant of existing post (modify 30-40%)"
        echo "[2] Create completely new post (100% new)"
        echo ""
        read -p "Choice [1-2]: " CHOICE

        if [ "$CHOICE" = "1" ]; then
            # Load base post
            BASE_POST_ID=$(echo "$SIMILAR_POSTS" | cut -d',' -f1)
            VARIANT_OF="$BASE_POST_ID"
            echo "ℹ️  Creating variant of post: $BASE_POST_ID"
        fi
    fi
fi
```

---

## Step 3: Display Generation Start

**Show user what's happening:**

```
═══════════════════════════════════════════════════════════════

  ✍️  WRITE POST: Generating Drafts

  Идея: "ИИ контент за 3 часа"
  Угол: Time Saving ⏱️
  Тип контента: demo (Content Machine)

  Создаю 6 вариантов текста...
  ├─ 3 базовых варианта (DIRECT, STORYTELLING, DATA-DRIVEN)
  └─ 3 Content Machine фреймворка (PAS, Hook-Story-Offer, Show Your Work)

═════════════════════════════════════════════════════════════════
```

---

## Step 4: Generate 3 Base Drafts

**For all content types (demo and regular):**

### Draft 1: DIRECT & PUNCHY (Hook-focused)

**LLM Prompt:**

```
You are a social media expert specializing in direct, punchy posts.

IDEA: {idea_text}
ANGLE: {selected_angle}
RESEARCH DATA: {pain_points_summary}

Write ONE post that is:
1. HOOK first (first sentence shocks or surprises)
2. DIRECT language (no fluff, short sentences)
3. SPECIFIC number or result
4. Clear ending statement

Format: 600-800 characters
Tone: Confident, direct, no hype
```

**Output Example:**

```
3 часа вместо недели.

Вот что происходит когда ты переводишь документацию
на автомат вместо ручного написания.

BMAD спрашивает вопросы.
Ты отвечаешь.
80 страниц документов готовы через 180 минут.

Нужна та же скорость? Пишите.

Quality score: 89/100 | CTR potential: 4.2%
```

---

### Draft 2: STORYTELLING (Narrative-focused)

**LLM Prompt:**

```
You are a storytelling expert for social media.

IDEA: {idea_text}
ANGLE: {selected_angle}
CONTEXT: {visual_context}

Write ONE post that:
1. OPENS with a scene/situation
2. BUILDS tension or problem
3. REVEALS solution through the idea
4. ENDS with transformation

Format: 600-800 characters
Tone: Narrative, relatable, authentic
```

**Output Example:**

```
Вчера я потратил на документацию 2 часа.

Обычно это 2 недели.

Вот как получилось:

Утром дал системе задачу: "Распиши процесс на-генери документы"
30 минут — система спрашивает, я отвечаю
Через час у меня техзадание, roadmap, и 80+ штук документов

Я только проверил 4 пункта из всего.

Остальное уже было готово.

Ищу тех, кому нужна такая же скорость.

Quality score: 84/100 | CTR potential: 3.8%
```

---

### Draft 3: DATA-DRIVEN (Numbers-focused)

**LLM Prompt:**

```
You are a data-driven content expert.

IDEA: {idea_text}
ANGLE: {selected_angle}
METRICS: {demonstrated_result}

Write ONE post that:
1. LEADS with surprising statistic
2. BREAKS DOWN the numbers
3. SHOWS the process
4. ENDS with takeaway

Format: 600-800 characters
Tone: Analytical, proof-based
```

**Output Example:**

```
80 документов за 120 минут = 1.5 документа/минуту.

Вот как это разбирается:

Без автомата:
- 2 недели на документацию
- 3-4 человека вовлечены
- 50% времени на согласования
= Месячный процесс

С BMAD:
- 2 часа на документацию
- 1 человек (я)
- Почти ноль согласований
= Полный выход за день

Разница в скорости: 10x
Разница в ресурсах: 4x

Вопрос: сколько ждёте вы?

Quality score: 86/100 | CTR potential: 4.0%
```

---

## Step 5: Generate 3 Content Machine Frameworks (Demo Only)

**Only if `content_type == "demo"` AND `generated_offers` exists:**

### Draft 4: PAS (Problem-Agitate-Solution) 🔥

**Structure with Pain Points:**

```
1️⃣ PROBLEM (2-3 sentences)
   - Start with FIRST pain point from pain_points array
   - Make it real, specific

2️⃣ AGITATE (2-3 sentences)
   - Show consequences of the problem
   - Escalate emotional impact

3️⃣ SOLUTION (3-4 sentences)
   - Show the demonstrated routine
   - Use visual_context to describe the process
   - Emphasize speed/ease

4️⃣ OFFER (1-2 sentences)
   - Embed first generated offer from offers array
   - Use {offer_title} and {offer_cta}
```

**LLM Prompt:**

```
You are an expert in PAS (Problem-Agitate-Solution) copywriting.

PAIN POINT: {pain_points[0]}
ROUTINE: {idea_text}
VISUAL CONTEXT: {visual_context}
OFFER: {generated_offers[0]['title']} — {generated_offers[0]['description']}
CTA: {generated_offers[0]['cta']}

Write a PAS post:

PROBLEM: Start with the pain. What's the specific problem?
AGITATE: Why is this a BIG problem? What are the costs?
SOLUTION: How does the demonstrated routine solve this?
OFFER: What's your offer? Make it soft and helpful.

Format: 600-800 characters
Tone: Empathetic, solution-focused, no hype

Return ONLY the post text.
```

**Output Example:**

```
Документация занимает дни, а результат плохой.

Пока ты пишешь — конкуренты уже масштабируются.
Пока согласуешь — процесс устаревает.
И всё это в голове у одного человека.

Я только что сгенерировал 80+ документов за 2 часа.

Вот как это работает:
Система задаёт вопросы → я отвечаю
Через час → техзадание, roadmap, описания ролей
Вечером → готовая документация на 90%

Научу вас генерировать документы с такой же скоростью.
Готовый workflow + шаблоны + полное понимание процесса.

Интересно? Напишите — обсудим.

Quality score: 87/100 | CTR potential: 4.1%
```

---

### Draft 5: Hook-Story-Offer 🚀

**Structure with Offers:**

```
1️⃣ HOOK (1-2 sentences)
   - Shocking number from the routine
   - Pattern interrupt

2️⃣ STORY (4-5 sentences)
   - Narrative of what happened
   - Use visual_context
   - Show the process step by step

3️⃣ NARRATIVE BRIDGE (1-2 sentences)
   - Connect to audience's problem
   - "If you have X problem, same applies"

4️⃣ OFFER (2-3 sentences)
   - Embed generated offer
   - Soft CTA
```

**LLM Prompt:**

```
You are an expert in Hook-Story-Offer copywriting.

HOOK NUMBER: {demonstrated_result}
STORY: {idea_text}
VISUAL CONTEXT: {visual_context}
OFFER: {generated_offers[0]['title']} — {generated_offers[0]['cta']}

Write a Hook-Story-Offer post:

HOOK: Start with the shocking number. Make them stop scrolling.
STORY: Tell what happened. Use details from visual context.
BRIDGE: Who else has this problem?
OFFER: What's your offer?

Format: 700-900 characters
Tone: Engaging, specific, helpful

Return ONLY the post text.
```

**Output Example:**

```
80 документов за 2 часа. Вот как.

Сегодня утром BMAD опросил меня про продукт:
- Какие боли решает?
- Для кого это полезно?
- Почему вы лучше конкурентов?

Через 30 минут система генерирует техзадание.
Я только проверяю и корректирую 3-4 пункта.
Ещё час — и у меня полный roadmap.

В итоге 80+ документов. И я написал из них максимум 10%.

Если у вас юристы, маркетологи, HR — та же боль.
Все эти процессы можно убыстрить в 10 раз.

Обучу вас этой рутине за 3 часа.
Вы получите workflow и шаблоны, которые будут работать в вашем бизнесе.

Пишите в личку — обсудим формат.

Quality score: 88/100 | CTR potential: 4.3%
```

---

### Draft 6: Show Your Work (Austin Kleon) ✨

**Structure:**

```
1️⃣ BEHIND-THE-SCENES (3-4 sentences)
   - Show the actual process
   - Use visual_context
   - Real, not polished

2️⃣ INSIGHT (2-3 sentences)
   - What did you learn?
   - Counter-intuitive discovery

3️⃣ AUTHENTICITY (1-2 sentences)
   - This is real work, not a case study
   - Not a demo for clients

4️⃣ SOFT OFFER (2-3 sentences)
   - Gentle offer
   - "If interesting" tone
```

**LLM Prompt:**

```
You are an expert in Austin Kleon's "Show Your Work" style.

ROUTINE: {idea_text}
PROCESS: {visual_context}
INSIGHT: What's counter-intuitive about this?
OFFER CTA: {generated_offers[0]['cta']}

Write a "Show Your Work" post:

BEHIND-THE-SCENES: Show the real process, not polished version
INSIGHT: What surprised you about this routine?
AUTHENTICITY: Why is this real, not a case study?
SOFT OFFER: If interested...

Format: 550-750 characters
Tone: Authentic, curious, unpolished
```

**Output Example:**

```
Вот как я работаю с документацией в этом месяце.

BMAD задаёт вопросы.
Я отвечаю (обычно одной строкой).
Система на лету строит структуру и заполняет разделы.

Результат: 80+ документов на 90% готовых.

Главное открытие: качество документации зависит не от времени,
а от качества структуры вопросов.

Спешка — вот враг. Но правильная структура + система = скорость.

Это не демонстрация для клиента.
Это именно то, как я работаю каждый день.

Если похожая задача — расскажу как это устроено.

Quality score: 85/100 | CTR potential: 3.9%
```

---

## Step 6: Display All Drafts to User

**For Content Machine (demo) content:**

```
═════════════════════════════════════════════════════════════════

  ✅ 6 DRAFT VARIANTS CREATED (Content Machine)

  БАЗОВЫЕ ВАРИАНТЫ:
  ┌─────────────────────────────────────────────────────────────┐
  │ Draft 1: DIRECT & PUNCHY (89/100) ⭐                        │
  │ Draft 2: STORYTELLING (84/100)                              │
  │ Draft 3: DATA-DRIVEN (86/100)                               │
  └─────────────────────────────────────────────────────────────┘

  CONTENT MACHINE ФРЕЙМВОРКИ (с вшитыми офферами):
  ┌─────────────────────────────────────────────────────────────┐
  │ Draft 4: PAS (Problem-Agitate-Solution) (87/100) 🔥         │
  │ Draft 5: Hook-Story-Offer (88/100) 🚀                       │
  │ Draft 6: Show Your Work (Austin Kleon) (85/100) ✨          │
  └─────────────────────────────────────────────────────────────┘

  Post type: Original
  variant_of: (none)
  pain_points embedded: ✓
  generated_offers embedded: ✓
  visual_context used: ✓

═════════════════════════════════════════════════════════════════

  Варианты 4-6 автоматически вшивают:
  ✓ Боли предпринимателей (из c-02c)
  ✓ Сгенерированные офферы (из c-03b2)
  ✓ Контекст вашей рутины (из скриншота)

Что дальше?

[1-6] SELECT DRAFT — Выбрать понравившийся вариант
[F] FEEDBACK — Дать feedback на все варианты
[G] GENERATE NEW — Создать новые варианты
[V] VIEW FULL — Показать полные версии
[M] Back to MENU

═════════════════════════════════════════════════════════════════
```

---

## Step 7: Handle User Selection

### User Selects Draft

```bash
read -p "Your choice [1-6/F/G/V/M]: " CHOICE

case $CHOICE in
    1|2|3|4|5|6)
        SELECTED_DRAFT_ID="draft-$CHOICE"
        SELECTED_DRAFT_TYPE=$(get_draft_type "$CHOICE")
        DRAFT_TEXT=$(get_draft_text "$CHOICE")

        # Update state with selection
        jq --arg draft_id "$SELECTED_DRAFT_ID" \
           --arg draft_type "$SELECTED_DRAFT_TYPE" \
           '.selected_draft_id = $draft_id |
            .selected_draft_type = $draft_type |
            .draft_created_at = now |
            .state_last_updated_at = now' \
           .workflow_state.json > .workflow_state.json.tmp && \
        mv .workflow_state.json.tmp .workflow_state.json

        echo "✅ Draft selected: $SELECTED_DRAFT_TYPE"
        echo ""
        echo "Moving to next step: Draft variants & final polish..."
        ;;

    F)
        # Handle feedback
        read -p "Your feedback: " FEEDBACK
        # Pass to LLM for regeneration
        ;;

    G)
        # Generate new variants
        # Repeat draft generation with feedback
        ;;

    V)
        # Show full versions
        ;;

    M)
        # Back to menu
        ;;
esac
```

---

## Step 8: Update State & Cleanup

**Save final draft metadata:**

```json
{
  "current_phase": "c-03c-draft",
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "selected_draft_quality_score": 89,
  "selected_draft_ctr_potential": "4.2%",
  "draft_variant_of": null,
  "draft_created_at": "2026-01-30T10:40:00Z",

  "draft_variants_generated": 6,
  "draft_variants_config": {
    "base_variants": ["DIRECT & PUNCHY", "STORYTELLING", "DATA-DRIVEN"],
    "content_machine_variants": ["PAS", "Hook-Story-Offer", "Show Your Work"],
    "framework_inputs": {
      "pain_points_embedded": true,
      "offers_embedded": true,
      "visual_context_used": true
    }
  },

  "state_last_updated_at": "2026-01-30T10:40:00Z"
}
```

**Optional: Clean up generated_offers after use:**

```bash
# Keep offers in state for audit trail, but mark as consumed
jq '.generated_offers_consumed = true' .workflow_state.json > \
   .workflow_state.json.tmp && \
mv .workflow_state.json.tmp .workflow_state.json
```

---

## Error Handling

### Missing workflow_state.json

```
⚠️ ERROR: workflow_state.json not found

This step requires state from c-03b1 and c-03b2.

Possible causes:
1. Steps c-03b1 or c-03b2 were not run
2. Session expired (8+ hours old)
3. File was deleted

Solution:
Run the workflow from c-03b1 again to create new state.

[Back to c-03b]
```

### Missing generated_offers

```
⚠️ Generated offers not found in state

This usually means step c-03b2 didn't complete successfully.

Solution:
- Draft variants 4-6 (Content Machine) will be skipped
- Only 3 base drafts (1-3) will be generated
- You can add offers manually later if needed

Continue with 3 base drafts? [Yes/No]
```

### User Selects Invalid Draft Number

```
⚠️ Invalid selection. Please choose 1-6 (or F/G/V/M)

Try again: _
```

---

## Data Flow to Next Step

**Pass to c-03d (Variants):**

```json
{
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "draft_variant_of": null,
  "draft_full_text": "[full draft text here]",
  "draft_created_at": "2026-01-30T10:40:00Z"
}
```

**Load State in c-03d:**

```bash
# Load selected draft
SELECTED_DRAFT=$(cat .workflow_state.json | \
    jq '.selected_draft_id, .selected_draft_type')

# If variant_of exists
VARIANT_OF=$(cat .workflow_state.json | jq '.draft_variant_of')

# Generate additional variants (short versions, angle variants, etc.)
```

---

## What's Next?

На следующем шаге (c-03d):

1. Загрузить выбранный черновик из state
2. Генерировать **дополнительные варианты**:
   - Укороченные версии (для комментариев)
   - Альтернативные углы (разные перспективы)
   - Вариантные хуки
3. Выбрать финальный вариант
4. Перейти к c-03e (финализация и публикация)

---

**nextStepFile:** `./c-03d-variants.md`
