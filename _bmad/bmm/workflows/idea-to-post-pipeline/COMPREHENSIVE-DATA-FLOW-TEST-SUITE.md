# Content Machine Pipeline - Comprehensive Data Flow Test Suite

**QA Test Plan for Content Machine Pipeline**
**Version:** 1.0
**Last Updated:** 2026-01-30
**Test Engineer:** FIXER AGENT 6 - Data Flow Testing & Validation

---

## Executive Summary

This document contains a complete, ready-to-execute test suite for the Content Machine Pipeline covering two distinct data flows:

1. **SCENARIO 1: Normal Content Path (TEXT Mode)**
   - Simple text input → Research → Single angle draft → 3 variants → Publish
   - No pain points generation (TEXT mode doesn't use Content Machine features)
   - No offer generation

2. **SCENARIO 2: Demo Content Path (ROUTINE Mode)**
   - Screenshot + description upload → Vision AI extraction → Research with auto-generated pain points
   - User configures offer preferences (one-time setup)
   - Automatic offer generation (2-4 offers per angle)
   - 6 variants (3 base + 3 with pain/offer embedding)
   - Full Content Machine Pipeline execution

---

## Test Data Sets

### Test Data Set 1: TEXT Mode Idea

```json
{
  "content_type": "TEXT",
  "raw_idea": "ИИ помогает создавать контент за 3 часа вместо недели",
  "idea_title": "AI Content Speed",
  "category": "Technology",
  "selected_type": "evergreen",
  "selected_angle": "Time Saving via ИИ",
  "expected_variants_count": 3
}
```

### Test Data Set 2: ROUTINE Mode Idea

```json
{
  "content_type": "ROUTINE",
  "screenshot_path": "/test-data/bmad-screenshot.png",
  "description": "Использую BMAD для генерирования всей документации компании за 2 часа",
  "idea_title": "BMAD Documentation Routine",
  "category": "Process Automation",
  "auto_content_type": "demo",
  "expected_pain_points_per_angle": "3-5",
  "expected_offers_per_angle": "2-4",
  "expected_variants_count": 6
}
```

---

## Part 1: SCENARIO 1 - TEXT MODE TEST PLAN

### Test 1.1: Mode Selection - TEXT Path

**Precondition:** User at c-01-add-idea.md menu

**Test Steps:**
1. System displays mode selection menu
2. User selects [T] for TEXT mode
3. Verify system routes to "Request Idea Input"

**Expected Output:**
- Prompt for text input appears
- No screenshot upload field shown
- No vision AI processing

**Data Validation Points:**
- No `idea_metadata` field created
- No `visual_context` extracted
- No `tools_used` array created

**CSV Check After:** None yet (step 1 only)

---

### Test 1.2: Idea Input & Validation - TEXT Mode

**Precondition:** User selected [T] in c-01

**Test Steps:**
1. User enters raw idea: "ИИ помогает создавать контент за 3 часа вместо недели"
2. System validates idea against checklist:
   - Specific? ✅
   - Researchable? ✅
   - Audience clear? ✅
   - Not duplicate? ✅
3. User selects content type: [1] EVERGREEN
4. System collects category: Technology

**Expected Output:**
```
✅ PASS — Идея готова к исследованию!
Идея #N:
├─ Title: "AI Content Speed"
├─ Raw description: "ИИ помогает создавать контент за 3 часа вместо недели"
├─ Content type: evergreen
├─ Category: Technology
├─ Status: active
├─ Date added: [today]
└─ Priority: medium
```

**CSV Validation - ideas_inbox.csv:**
```csv
id,date_added,source,raw_idea,content_type,category,status,notes
[N],[today],user_input,"ИИ помогает создавать контент за 3 часа вместо недели",evergreen,Technology,active,"[auto notes]"
```

**Data Validation Points:**
- ✅ `id` is unique
- ✅ `date_added` matches today's date
- ✅ `source` = "user_input" (not "routine")
- ✅ `content_type` = "evergreen" (not "demo")
- ✅ No `idea_metadata` column present
- ✅ Status = "active"

---

### Test 1.3: Deduplication Check - TEXT Mode

**Precondition:** Idea validated and ready to save

**Test Steps:**
1. System checks existing ideas_inbox.csv for similar ideas
2. Similarity algorithm runs (cosine similarity on raw_idea text)
3. Compare against all existing rows

**Scenarios to Test:**

**Scenario 1.3a: No Duplicates Found**
- System returns: "No duplicates detected"
- Idea saved to CSV
- User proceeds to next steps

**Scenario 1.3b: Potential Duplicate Detected (>85% similarity)**
- System flags: "⚠️  Similar idea found: 'AI speeds up writing' (87% match)"
- User options: [Accept duplicate] [Modify] [Cancel]
- If [Accept]: Save anyway with `status = "duplicate_confirmed"`
- If [Modify]: Return to idea input
- If [Cancel]: Don't save, return to menu

**Data Validation Points:**
- ✅ Similarity score calculated correctly
- ✅ CSV not updated until user confirms
- ✅ Duplicate row contains `status = "duplicate_confirmed"`
- ✅ Original idea remains in CSV with original status

---

### Test 1.4: Research Execution - TEXT Mode

**Precondition:** Idea saved to ideas_inbox.csv, user selects [R] RESEARCH

**Test Steps:**
1. System loads idea from ideas_inbox.csv
2. Routes to c-02c-research.md
3. System searches for 5-8 angles with sources
4. Research completes

**Expected Output:**
```
✅ RESEARCH COMPLETE

Found: 8 different angles
Sources: 32 total (average 4 per angle)
Avg relevance: 86% (GOOD)
Time: 18 minutes

Результаты сохранены в ideas_research.csv
```

**CSV Validation - ideas_research.csv:**
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,[original_id],[today],"Time Saving via ИИ",8,"angle_1",[list of angles],32,86
```

**Data Validation Points:**
- ✅ `original_idea_id` references correct row in ideas_inbox.csv
- ✅ `research_date` = today
- ✅ Exactly 8 angles found (5-8 range)
- ✅ `sources_count` >= 20 (at least 2.5 per angle)
- ✅ `avg_relevance` >= 75%
- ✅ **NO `pain_points_json` column** (TEXT mode doesn't generate pains)
- ✅ Angles are diverse and specific

**Angles Validation:**
- Angle 1: "Time Saving ⏱️"
- Angle 2: "Quality Control 🎯"
- Angle 3: "Scalability 📈"
- Angle 4: "Learning Tool 📚"
- [5-8]: Various supporting angles

---

### Test 1.5: Results Display - TEXT Mode

**Precondition:** Research complete, user at c-02d-results.md

**Test Steps:**
1. User views all angles with sources and facts
2. User doesn't see pain points section (TEXT mode)
3. User selects angle or proceeds

**Expected Output - NO pain points shown:**
```
ANGLE 1: Time Saving ⏱️
├─ Main insight: "Saves 70% of content creation time"
├─ Sources found: 7 (news articles, blogs, studies)
├─ Key facts:
│  • Average copywriter: 2-3 hours per post
│  • With ИИ: 20-30 minutes per post
│  • Relevance: 92% (highly relevant)
└─ Best for: Founders, agencies, busy entrepreneurs

[NO PAINS SECTION - This is TEXT mode, not ROUTINE mode]
```

**Data Validation Points:**
- ✅ Pain points NOT displayed
- ✅ No pains in ideas_research.csv
- ✅ Source data intact and correct
- ✅ Relevance scores present

---

### Test 1.6: Angle Selection & Routing - TEXT Mode

**Precondition:** User viewing research results for TEXT mode idea

**Test Steps:**
1. User selects angle: "Time Saving via ИИ"
2. System checks: Is this TEXT or ROUTINE mode?
   - Read: `original_idea.content_type` from ideas_inbox.csv
   - Expected: "evergreen" or similar (not "demo")
3. Route decision: content_type != "demo" → Route to c-03c (NOT c-03b1)

**Expected Routing:**
```
✅ TEXT MODE DETECTED: content_type = "evergreen"

→ Skip c-03b1 (offer check - ROUTINE only)
→ Skip c-03b2 (offer generation - ROUTINE only)
→ Go directly to c-03c (draft)
```

**Data Validation Points:**
- ✅ Routing logic reads correct field from CSV
- ✅ No offer generation workflows triggered
- ✅ System skips c-03b1 and c-03b2 entirely
- ✅ Draft section (c-03c) loads immediately

---

### Test 1.7: Draft Generation & Storage - TEXT Mode

**Precondition:** Angle selected, system at c-03c-draft.md

**Test Steps:**
1. System generates draft based on selected angle
2. Draft saved as "Draft 1"
3. System reads draft_variations (if any)
4. Presents draft options

**Expected Output:**
```
═════════════════════════════════════════════════════════════════

  📝 WRITING POST: Time Saving via ИИ

  Generated 1 draft version:

  [DRAFT 1] DIRECT & PUNCHY
  Quality: 89/100
  Best for: LinkedIn, Twitter
  Reading time: 2 min

  3 часа вместо недели: как ИИ подтягивает контент 👉

  Писать контент вручную — это 8 часов в день и ноль роста...
  [500 chars of draft content]
```

**CSV Check - posts_content.csv (first save):**
```csv
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,content_250_chars,content_100_chars,variant_metadata
1,[idea_id],1,"Time Saving","base","draft_1","[full text]",null,null,"[metadata json]"
```

**Data Validation Points:**
- ✅ Draft content saved as "base" variant
- ✅ `content_500_chars` populated
- ✅ `content_250_chars` = null (not generated yet)
- ✅ `content_100_chars` = null (not generated yet)
- ✅ Variant metadata stored as JSON

---

### Test 1.8: Variant Generation - TEXT Mode (3 VARIANTS EXPECTED)

**Precondition:** Draft created, user at c-03d-variants.md

**Test Steps:**
1. User confirms draft selection
2. System routes to variant generation
3. System generates SHORTER VARIANTS (250-char, 100-char)
4. System validates variant count

**Expected Behavior - TEXT Mode:**
- Generate 3 variants ONLY (not 6)
- All 3 are BASIC variants (no pain/offer embedding)
- No special Content Machine frameworks applied

**CSV Validation - posts_content.csv (after variants generated):**
```csv
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,content_250_chars,content_100_chars,variant_metadata
1,[id],1,"Time Saving","base","final","[500 text]","[250 text]","[100 text]","{}"
```

**Variant Count Validation:**
```javascript
// Pseudo-code for validation
const variants = posts_content.filter(row => row.idea_id == idea_id);
assert(variants.length === 3, "Expected exactly 3 variants in TEXT mode");

// Check variant types
const variantTypes = variants.map(v => v.variant_type);
assert(variantTypes.every(t => t === "base"), "All variants should be 'base' type");

// Check no pain/offer embedding
const hasEmbeddedContent = variants.some(v =>
  v.content_500_chars.includes("pain:") ||
  v.content_500_chars.includes("offer:")
);
assert(!hasEmbeddedContent, "TEXT mode variants should NOT embed pains/offers");
```

**Output Display:**
```
═════════════════════════════════════════════════════════════════

  ✅ VARIANTS GENERATED (TEXT MODE: 3 variants only)

[500 chars] — Original (full details)
  Quality: 89/100 | CTR: 4.2% | Best for: LinkedIn
  Chars: 487

[250 chars] — Medium (key points)
  Quality: 87/100 | CTR: 4.0% | Best for: Telegram
  Chars: 251

[100 chars] — Short (teaser)
  Quality: 85/100 | CTR: 3.8% | Best for: Twitter
  Chars: 98

═════════════════════════════════════════════════════════════════
```

**Data Validation Points:**
- ✅ Exactly 3 variants (not 6)
- ✅ All variants have `variant_type = "base"`
- ✅ No `pain_points_embedded` field
- ✅ No `offer_content` field
- ✅ Character counts match expected ranges:
  - 500-char: 450-550 chars
  - 250-char: 200-300 chars
  - 100-char: 50-150 chars
- ✅ All variants are complete sentences
- ✅ No truncated or malformed content

---

### Test 1.9: Finalization & Publishing - TEXT Mode

**Precondition:** All 3 variants generated and approved

**Test Steps:**
1. User selects: [S] SELECT (save variants)
2. User chooses: [A] ALL THREE
3. System routes to c-03e-finalize.md
4. System publishes all variants

**Expected Output:**
```
✅ POST FINALIZED

All 3 variants saved to posts_content.csv:
├─ Variant 1 (500 chars): Ready to publish
├─ Variant 2 (250 chars): Ready to publish
└─ Variant 3 (100 chars): Ready to publish

[Publish] [Save Draft] [Back to Menu]
```

**CSV Final State - posts_content.csv:**
```csv
id,idea_id,research_id,angle_used,variant_type,publish_status,content_500_chars,content_250_chars,content_100_chars
1,[id],1,"Time Saving","base","published","[text]","[text]","[text]"
```

**Data Validation Points:**
- ✅ All 3 rows present in CSV
- ✅ `publish_status = "published"` for all
- ✅ No duplicate rows
- ✅ No orphaned data (all have matching idea_id and research_id)
- ✅ No pain/offer fields present
- ✅ All content fields populated

---

## Part 2: SCENARIO 2 - ROUTINE MODE TEST PLAN

### Test 2.1: Mode Selection - ROUTINE Path

**Precondition:** User at c-01-add-idea.md menu

**Test Steps:**
1. System displays mode selection menu
2. User selects [R] for ROUTINE mode
3. System routes to "Load Routine Demo"

**Expected Output:**
```
┌─────────────────────────────────────────────────────────────────┐
│            РЕЖИМ ROUTINE: ПОКАЖИТЕ ВАШУ РУТИНУ                  │
└─────────────────────────────────────────────────────────────────┘

Загрузите скриншот того, что вы демонстрируете...

1. Скриншот рутины: [прикрепить изображение]
2. Описание: что вы делаете и зачем
   (1-3 предложения)
```

**Data Validation Points:**
- ✅ Vision API field shown
- ✅ Screenshot upload field active
- ✅ Description text field active
- ✅ No content type selection shown yet

---

### Test 2.2: Vision AI Processing - ROUTINE Mode

**Precondition:** User uploaded screenshot and description

**Test Data:**
```
Screenshot: /test-data/bmad-screenshot.png
Description: "Использую BMAD для генерирования всей документации компании за 2 часа"
```

**Test Steps:**
1. System receives screenshot and description
2. Calls Claude Vision API with screenshot
3. Extracts visual context, tools used, demonstrated result
4. Combines with user description

**Expected Output:**
```
Анализирую скриншот...

✓ Извлечён контекст:
  ├─ visual_context: "На скрине видна интерфейс BMAD с диалогом..."
  ├─ tools_used: ["BMAD", "Claude", "PDF export"]
  ├─ demonstrated_result: "80+ документов готовы к использованию"
  └─ context_type: "documentation generation"
```

**CSV Validation - ideas_inbox.csv:**
```csv
id,date_added,source,raw_idea,content_type,idea_metadata,status,notes
[N],[today],routine,"Использую BMAD для генерирования...",demo,"{\"visual_context\": \"...\", \"tools_used\": [\"BMAD\", \"Claude\", \"PDF export\"], \"demonstrated_result\": \"80+ документов...\", \"context_type\": \"documentation generation\"}",active,"[auto notes]"
```

**Data Validation Points:**
- ✅ `source = "routine"` (not "user_input")
- ✅ `content_type = "demo"` (auto-set, NOT user-selected)
- ✅ `idea_metadata` is valid JSON with all 4 required fields:
  - `visual_context` (string, non-empty)
  - `tools_used` (array, non-empty)
  - `demonstrated_result` (string, non-empty)
  - `context_type` (string, specific and accurate)
- ✅ No spaces or corruption in JSON

---

### Test 2.3: Content Type Auto-Selection - ROUTINE Mode

**Precondition:** Screenshot processed, Vision AI extraction complete

**Test Steps:**
1. System skips manual content type selection
2. Auto-sets: `content_type = "demo"`
3. Proceeds to next step without user input for type

**Expected Behavior:**
```
✅ ROUTINE Mode Detected!
Content type automatically set to: DEMO

Система пропускает выбор типа контента и идёт дальше...
→ Перейти к исследованию
```

**CSV Check:**
- ✅ `content_type = "demo"` in ideas_inbox.csv
- ✅ No duplicate type selection prompts
- ✅ System proceeds immediately after Vision processing

---

### Test 2.4: Research with Pain Point Generation - ROUTINE Mode

**Precondition:** Idea saved with content_type="demo", user selects [R] RESEARCH

**Test Steps:**
1. System loads idea with `content_type="demo"`
2. Checks: Is content_type == "demo"?
3. YES → Execute Section 2.5 (Pain Point Generation)
4. For EACH angle found, generate 3-5 pain points
5. Save pain points to ideas_research.csv

**Expected Output - RESEARCH WITH PAINS:**
```
✅ RESEARCH COMPLETE

Found: 8 different angles
Sources: 32 total
Avg relevance: 86%

Генерирую боли предпринимателей для каждого угла...

ANGLE 1: Time Saving ⏱️
Боли, которые эта рутина решает:
├─ 🔴 Медленная документация берёт 2-3 дня на большой объём
├─ 🔴 Все процессы в голове у одного человека
├─ 🔴 Нельзя масштабировать без найма новых специалистов
└─ 🔴 Непроцессированная информация = нельзя продать бизнес

ANGLE 2: Quality Control 🎯
Боли, которые эта рутина решает:
├─ 🔴 Качество документов зависит от того, кто написал
├─ 🔴 Нет стандарта, каждый пишет по-своему
├─ 🔴 Редактирование и проверка занимают много времени
└─ 🔴 Трудно передать задачу другому (плохо описано)

[... 6 more angles with similar pain structures ...]
```

**CSV Validation - ideas_research.csv:**
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance,pain_points_json
1,[idea_id],[today],"Time Saving via BMAD",8,"angle_1",[list],32,86,"{\"angle_1\": {\"pains\": [\"Боль 1\", \"Боль 2\", \"Боль 3\", \"Боль 4\"]}, \"angle_2\": {\"pains\": [...]}, ...}"
```

**Data Validation Points:**
- ✅ `pain_points_json` column EXISTS (TEXT mode didn't have it)
- ✅ Valid JSON structure with all 8 angles
- ✅ Each angle has 3-5 pain points (check: min 3, max 5)
- ✅ Pain points are in business language (not technical)
- ✅ Pain points reference the specific routine demonstrated
- ✅ No truncated or incomplete pain descriptions
- ✅ JSON parses correctly without syntax errors

**Pain Point Validation Logic:**
```javascript
// Pseudo-code
const painData = JSON.parse(row.pain_points_json);
for (const angle in painData) {
  const pains = painData[angle].pains;
  assert(pains.length >= 3 && pains.length <= 5,
    `Angle ${angle}: Expected 3-5 pains, got ${pains.length}`);

  pains.forEach(pain => {
    assert(pain.length > 10, "Pain point too short");
    assert(pain.length < 200, "Pain point too long");
    assert(!pain.match(/\bAPI\b|\bcode\b|\bpython\b/i),
      "Pain point is too technical");
  });
}
```

---

### Test 2.5: Results Display with Pain Points - ROUTINE Mode

**Precondition:** Research complete, user viewing c-02d-results.md

**Test Steps:**
1. User views all 8 angles
2. For EACH angle, pain points ARE displayed (unlike TEXT mode)
3. User can see which pains each routine solves

**Expected Output - PAIN POINTS SHOWN:**
```
ANGLE 1: Time Saving ⏱️
├─ Main insight: "Saves 70% of content creation time"
├─ Sources found: 7 (news articles, blogs, studies)
├─ Key facts: [facts as before]
├─ Relevance: 92%
└─ Best for: Founders, agencies, busy entrepreneurs

🔴 Пains this routine solves:
├─ 🔴 Медленная документация берёт 2-3 дня
├─ 🔴 Все процессы в голове у одного человека
├─ 🔴 Нельзя масштабировать без найма
└─ 🔴 Непроцессированная информация = нельзя продать

[... 7 more angles, each with pain sections ...]
```

**Data Validation Points:**
- ✅ Pain points displayed for EVERY angle
- ✅ Pains are readable from `pain_points_json` from ideas_research.csv
- ✅ Format is consistent across angles
- ✅ Pains are NOT shown for TEXT mode ideas

---

### Test 2.6: Angle Selection & Routing - ROUTINE Mode

**Precondition:** User viewing research results with pain points

**Test Steps:**
1. User selects angle: "Time Saving via BMAD"
2. System checks: Is this TEXT or ROUTINE mode?
   - Read: `original_idea.content_type` from ideas_inbox.csv
   - Expected: "demo"
3. Route decision: content_type == "demo" → Route to c-03b1 (NOT c-03c directly)

**Expected Routing:**
```
✅ ROUTINE MODE DETECTED: content_type = "demo"

→ Go to c-03b1 (offer check)
→ System loads offer_filter.csv (first run or existing)
→ Skip c-03c for now
```

**Data Validation Points:**
- ✅ Routing logic reads `content_type` correctly
- ✅ System routes to c-03b1 (not c-03c)
- ✅ No draft generation until offer filter is set

---

### Test 2.7: Offer Filter Setup - ROUTINE Mode (First Run)

**Precondition:** System routing to c-03b1, file `user_preferences/offer_filter.csv` doesn't exist

**Test Steps:**
1. System checks for existing offer_filter.csv
2. File doesn't exist → Show first-time setup form
3. User selects offer types: [1] Training, [2] Setup, [3] Templates, [4] Consulting
4. System parses input: "1,2,3,4"
5. Creates offer_filter.csv

**Expected Output:**
```
┌─────────────────────────────────────────────────────────────────┐
│    🔧 ПЕРВИЧНАЯ НАСТРОЙКА: Какие Офферы Вы Готовы Продавать?   │
└─────────────────────────────────────────────────────────────────┘

Отметьте типы продуктов/услуг, которые вам ОК делать.

[X] 1. ОБУЧЕНИЕ / НАСТАВНИЧЕСТВО — ОК
[X] 2. ПРОЕКТИРОВАНИЕ ПРОЦЕССА / SETUP — ОК
[X] 3. ШАБЛОНЫ / МЕТОДИЧКИ — ОК
[X] 4. КОНСАЛТИНГ / РАЗБОР ПРОЦЕССОВ — ОК
[ ] 5. РАЗРАБОТКА ПРОДУКТА "ПОД КЛЮЧ" — НЕ хочу

Ваш выбор: 1,2,3,4
```

**CSV Creation - user_preferences/offer_filter.csv:**
```csv
offer_type,willing,notes
training,true,Обучение — ОК
setup,true,Проектирование процесса — ОК
templates,true,Шаблоны — ОК
consulting,true,Консалтинг — ОК
full_dev,false,Разработка под ключ — НЕ хочу (долго и не масштабируется)
```

**Data Validation Points:**
- ✅ File created at correct path
- ✅ All 5 offer types present
- ✅ 4 rows with `willing=true`
- ✅ 1 row with `willing=false`
- ✅ Notes field populated
- ✅ CSV format correct (no syntax errors)

---

### Test 2.8: Offer Filter Setup - ROUTINE Mode (Subsequent Runs)

**Precondition:** offer_filter.csv EXISTS from previous run

**Test Steps:**
1. System checks for offer_filter.csv
2. File exists → Load existing profile
3. Display loaded profile
4. User chooses: [Нет, продолжить] (No, continue)

**Expected Output:**
```
✅ Профиль офферов загружен (сохранен с предыдущих запусков):

Вы готовы продавать:
├─ ✅ Обучение / Наставничество
├─ ✅ Проектирование Процесса / Setup
├─ ✅ Шаблоны / Методички
├─ ✅ Консалтинг / Разбор Процессов
└─ ❌ Разработка Продукта "Под Ключ"

Хотите изменить профиль? [Да] [Нет, продолжить]
```

**User Selection:** [Нет, продолжить]

**Expected Behavior:**
- Skip re-selection form
- Load profile from CSV
- Store to workflow_state.json
- Route to c-03b2 (offer generation)

**Data Validation Points:**
- ✅ Profile loaded from CSV correctly
- ✅ All preferences match previous save
- ✅ No re-creation of CSV
- ✅ Timestamp of CSV unchanged

---

### Test 2.9: Workflow State Storage - ROUTINE Mode

**Precondition:** Offer filter profile loaded/created

**Test Steps:**
1. System saves state to workflow_state.json
2. Includes: workflow phase, content type, offer filter settings

**Expected JSON - workflow_state.json:**
```json
{
  "workflow_phase": "c-03b1-offer-check",
  "content_type": "demo",
  "offer_filter_configured": true,
  "willing_offers": ["training", "setup", "templates", "consulting"],
  "unwilling_offers": ["full_dev"],
  "timestamp": "2026-01-30T10:30:00Z"
}
```

**Data Validation Points:**
- ✅ Valid JSON structure
- ✅ `workflow_phase = "c-03b1-offer-check"`
- ✅ `content_type = "demo"`
- ✅ `willing_offers` is array with 4 elements
- ✅ `unwilling_offers` is array with 1 element
- ✅ ISO timestamp format correct
- ✅ No sensitive data exposed

---

### Test 2.10: Offer Generation - ROUTINE Mode

**Precondition:** Offer filter set, system routing to c-03b2-offer-generation.md

**Test Steps:**
1. System loads offer filter preferences from CSV
2. For selected angle, generate 2-4 offers based on:
   - Demonstrated routine (from idea_metadata)
   - Selected angle
   - Willing offer types
3. Save offers to workflow_state.json
4. Route to c-03c-draft.md

**Expected Output - OFFER GENERATION:**
```
✅ Фильтр офферов настроен.

Система будет генерировать офферы ТОЛЬКО из этих категорий:
├─ ✅ Обучение / Наставничество
├─ ✅ Проектирование Процесса / Setup
├─ ✅ Шаблоны / Методички
└─ ✅ Консалтинг / Разбор Процессов

Следующий шаг: Автоматическая генерация офферов на основе рутины.

Система автоматически придумает 2-4 оффера, которые логичны именно для вашей демонстрации.

→ Генерирую офферы для угла "Time Saving via BMAD"...

OFFER 1: ОБУЧЕНИЕ
  "Научу вас за 2-3 часа создавать документацию через BMAD как я"
  Target audience: Small business owners, technical leaders
  Estimated value: $300-500
  Delivery: 1x 1-on-1 session + materials

OFFER 2: SETUP
  "Настрою BMAD-систему для вашей компании (3-5 дней)"
  Includes: Process mapping, template creation, team training
  Estimated value: $2,000-3,500

OFFER 3: TEMPLATES
  "Шаблон-набор для автоматизации документации в BMAD"
  5 готовых схем + промпты + инструкции
  Estimated value: $49-99

[... up to 4 offers total ...]
```

**workflow_state.json - Updated with Offers:**
```json
{
  "workflow_phase": "c-03b2-offer-generation",
  "content_type": "demo",
  "angle_selected": "Time Saving via BMAD",
  "offers_generated": [
    {
      "offer_id": "offer_1",
      "type": "training",
      "title": "Научу создавать документацию через BMAD",
      "description": "2-3 часовая сессия + материалы",
      "target_audience": "Small business owners",
      "estimated_value": "300-500",
      "delivery_days": "1"
    },
    {
      "offer_id": "offer_2",
      "type": "setup",
      "title": "Настрою BMAD-систему",
      "description": "Полная настройка процессов",
      "estimated_value": "2000-3500",
      "delivery_days": "5"
    },
    {
      "offer_id": "offer_3",
      "type": "templates",
      "title": "Шаблон-набор документации",
      "description": "5 готовых схем + промпты",
      "estimated_value": "49-99",
      "delivery_days": "0"
    }
  ],
  "timestamp": "2026-01-30T10:35:00Z"
}
```

**Data Validation Points:**
- ✅ 2-4 offers generated (not more, not less)
- ✅ Each offer has valid `offer_type` from `willing_offers` list
- ✅ No offers from `unwilling_offers` list
- ✅ Each offer has minimum fields: id, type, title, value
- ✅ No `full_dev` offers present
- ✅ Offers are specific to demonstrated routine
- ✅ Offers are specific to selected angle
- ✅ workflow_state.json updated with all offer details

---

### Test 2.11: Draft Generation with Offers Available - ROUTINE Mode

**Precondition:** Offers generated, system at c-03c-draft.md

**Test Steps:**
1. System loads offers from workflow_state.json
2. System checks: Are offers available?
   - YES (2-4 offers loaded)
3. Draft generation includes offer context
4. System stores reference to offers in draft metadata

**Expected Output:**
```
═════════════════════════════════════════════════════════════════

  📝 WRITING POST: Time Saving via BMAD

  Generated 1 draft version (with Content Machine enhancements):

  [DRAFT 1] DIRECT & PUNCHY
  Quality: 91/100
  Best for: LinkedIn, Twitter
  Reading time: 2 min
  Enhancement: Content Machine Framework (PAS + Offers)

  [Draft content with offer integration points marked]
  Писать контент вручную — это 8 часов в день и ноль роста...

  💡 This draft will show opportunities for:
  - Offer 1: Training in BMAD automation
  - Offer 2: Custom setup services
  - Offer 3: Template library

═════════════════════════════════════════════════════════════════
```

**CSV Check - posts_content.csv (first save for ROUTINE):**
```csv
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,has_offer_hooks,offer_references,content_500_chars
1,[id],1,"Time Saving","base","draft_1","[full text]",true,"[offer_1,offer_2,offer_3]","[base content]"
```

**Data Validation Points:**
- ✅ Offers loaded from workflow_state.json
- ✅ Draft metadata includes `has_offer_hooks=true`
- ✅ `offer_references` array contains all 3-4 generated offers
- ✅ Offer details available for variant generation phase
- ✅ Base content NOT yet modified (offers applied at variant stage)

---

### Test 2.12: Variant Generation - ROUTINE Mode (6 VARIANTS EXPECTED)

**Precondition:** Draft created, user at c-03d-variants.md, offers available

**Test Steps:**
1. User confirms draft selection
2. System checks: Is this ROUTINE mode with offers?
   - Read content_type from ideas_inbox.csv: "demo" ✓
   - Read offers from workflow_state.json: [3+ offers] ✓
3. Generate variants:
   - Variants 1-3: BASIC versions (standard format)
   - Variants 4-6: CONTENT MACHINE FRAMEWORK versions (with pain + offer embedding)
4. Total: 6 variants

**Expected Behavior - ROUTINE Mode:**
- Generate 6 variants (not 3)
- Variants 1-3: Base versions (250, 100 chars derivatives)
- Variants 4-6: Content Machine Framework versions with:
  - PAS (Problem-Agitate-Solution) structure
  - Hook-Story-Offer framework
  - Show Your Work framework

**CSV Validation - posts_content.csv:**
```csv
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,content_250_chars,content_100_chars,pain_embedded,offer_embedded,variant_framework
1,[id],1,"Time Saving","base","final","[500]","[250]","[100]","false","false","standard"
2,[id],1,"Time Saving","cm_pas","final","[500 PAS]","[250]","[100]","true","true","PAS"
3,[id],1,"Time Saving","cm_hook_story_offer","final","[500 HSO]","[250]","[100]","true","true","Hook-Story-Offer"
4,[id],1,"Time Saving","cm_show_work","final","[500 SYW]","[250]","[100]","true","true","Show Your Work"
5,[id],1,"Time Saving","cm_pas","final","[500 PAS]","[250]","[100]","true","true","PAS"
6,[id],1,"Time Saving","cm_hook_story_offer","final","[500 HSO]","[250]","[100]","true","true","Hook-Story-Offer"
```

**Variant Count Validation:**
```javascript
// Pseudo-code for ROUTINE mode validation
const variants = posts_content.filter(row => row.idea_id == idea_id);
assert(variants.length === 6, `Expected 6 variants in ROUTINE mode, got ${variants.length}`);

// Check types
const baseVariants = variants.filter(v => v.variant_type === "base");
const cmVariants = variants.filter(v => v.variant_type.startsWith("cm_"));

assert(baseVariants.length >= 1, "Should have at least 1 base variant");
assert(cmVariants.length >= 3, "Should have at least 3 Content Machine variants");

// Check pain/offer embedding
cmVariants.forEach(v => {
  assert(v.pain_embedded === "true", `CM variant should have pain_embedded=true`);
  assert(v.offer_embedded === "true", `CM variant should have offer_embedded=true`);
  assert(v.variant_framework !== "standard", `CM variant should have specific framework`);
});
```

**Output Display:**
```
═════════════════════════════════════════════════════════════════

  ✅ VARIANTS GENERATED (ROUTINE MODE: 6 variants!)

BASIC VARIANTS (Standard format):
─────────────────────────────────
[500 chars] — Original (full details)
  Quality: 89/100 | Framework: Standard
  Chars: 487

CONTENT MACHINE VARIANTS (With Pains & Offers):
──────────────────────────────────────────────
[PAS Framework] — Problem-Agitate-Solution
  Quality: 91/100 | Pain points: embedded | Offers: 1-2
  Structure: Problem → Agitation → Your solution → Offer

[Hook-Story-Offer] — Narrative with CTA
  Quality: 92/100 | Pain points: embedded | Offers: 2-3
  Structure: Hook → Context → Demonstration → Offer CTA

[Show Your Work] — Authenticity & Process
  Quality: 90/100 | Pain points: embedded | Offers: 1-2
  Structure: Here's what I do → Why it works → How you can do it

═════════════════════════════════════════════════════════════════
```

**Example Variant 4 (PAS with Pain & Offer):**
```
🔴 PROBLEM:
Документация вашей компании живёт в головах людей.
Когда человек уходит — вся информация уходит с ним.

😤 AGITATE:
- Нельзя нанять нового специалиста быстро
- Невозможно продать бизнес без документации процессов
- Масштабирование упирается в эту боль

💡 SOLUTION:
За 2 часа я генерирую всю документацию через BMAD.
Её может использовать любой в команде.
Процессы наконец-то описаны и масштабируемы.

👉 Хотите создать документацию для своей компании?
   → Предложу вам 3 варианта (обучение, setup, шаблоны)
```

**Data Validation Points:**
- ✅ Exactly 6 variants
- ✅ Variants 1-3: `variant_type = "base"`, `pain_embedded = false`, `offer_embedded = false`
- ✅ Variants 4-6: `variant_type` starts with "cm_", `pain_embedded = true`, `offer_embedded = true`
- ✅ Each CM variant has specific `variant_framework` (PAS, Hook-Story-Offer, Show Your Work)
- ✅ Pain points correctly extracted from ideas_research.csv
- ✅ Offer references correctly embedded (no offer "IDs" leaked, natural CTA)
- ✅ All variants are complete and coherent
- ✅ No truncation or malformed content
- ✅ Pain points match those generated in Step 2.4
- ✅ Offers match those generated in Step 2.10

---

### Test 2.13: Finalization & Publishing - ROUTINE Mode

**Precondition:** All 6 variants generated and approved

**Test Steps:**
1. User selects: [S] SELECT (save variants)
2. User chooses: [A] ALL SIX (or individual selection)
3. System routes to c-03e-finalize.md
4. System publishes all variants

**Expected Output:**
```
✅ POST FINALIZED (ROUTINE MODE - Full Content Machine Pipeline)

All 6 variants saved to posts_content.csv:
├─ Variant 1 (Base): Ready to publish
├─ Variant 2 (PAS Framework): Ready to publish
├─ Variant 3 (Hook-Story-Offer): Ready to publish
├─ Variant 4 (Show Your Work): Ready to publish
├─ Variant 5 (PAS Alternative): Ready to publish
└─ Variant 6 (HSO Alternative): Ready to publish

Content Machine Summary:
├─ Pain points embedded: 4 variants
├─ Offers integrated: 4 variants
├─ Frameworks applied: PAS, Hook-Story-Offer, Show Your Work
├─ Expected engagement: +35-50% (vs basic variants)
└─ Conversion opportunity: 2-4 offers available

[Publish All] [Save Draft] [Back to Menu]
```

**CSV Final State - posts_content.csv:**
```csv
id,idea_id,research_id,angle_used,variant_type,publish_status,pain_embedded,offer_embedded,variant_framework
1,[id],1,"Time Saving","base","published","false","false","standard"
2,[id],1,"Time Saving","cm_pas","published","true","true","PAS"
3,[id],1,"Time Saving","cm_hook_story_offer","published","true","true","Hook-Story-Offer"
4,[id],1,"Time Saving","cm_show_work","published","true","true","Show Your Work"
5,[id],1,"Time Saving","cm_pas_alt","published","true","true","PAS"
6,[id],1,"Time Saving","cm_hook_story_offer_alt","published","true","true","Hook-Story-Offer"
```

**Data Validation Points:**
- ✅ All 6 rows present in CSV
- ✅ `publish_status = "published"` for all
- ✅ No duplicate rows
- ✅ No orphaned data
- ✅ Mix of base (1) and cm_ variants (5)
- ✅ Pain/offer embedding correctly marked
- ✅ Frameworks correctly identified
- ✅ All content fields populated

---

## Part 3: Data Validation Scripts

### Validation Script 1: CSV Schema Check

```python
#!/usr/bin/env python3
"""
Validate CSV schemas for Content Machine Pipeline
"""

import csv
import json
import sys
from pathlib import Path

def validate_ideas_inbox_csv(filepath):
    """Validate ideas_inbox.csv structure and data"""
    required_cols = [
        'id', 'date_added', 'source', 'raw_idea',
        'content_type', 'category', 'status', 'notes'
    ]

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        # Check headers
        if not all(col in reader.fieldnames for col in required_cols):
            return False, f"Missing required columns. Expected: {required_cols}"

        rows = list(reader)
        for i, row in enumerate(rows):
            # Check required fields not empty
            if not row['id'] or not row['raw_idea']:
                return False, f"Row {i+1}: Empty required field"

            # Validate content_type values
            valid_types = ['evergreen', 'topical', 'seasonal', 'philosophical', 'tutorial', 'demo']
            if row['content_type'] not in valid_types:
                return False, f"Row {i+1}: Invalid content_type: {row['content_type']}"

            # Check date format
            if not row['date_added'].count('-') == 2:  # Basic YYYY-MM-DD check
                return False, f"Row {i+1}: Invalid date format: {row['date_added']}"

            # If source is "routine", validate idea_metadata exists
            if row['source'] == 'routine':
                if 'idea_metadata' not in reader.fieldnames:
                    return False, f"Row {i+1}: ROUTINE source but no idea_metadata column"

    return True, "ideas_inbox.csv valid"

def validate_ideas_research_csv(filepath, expected_pain_points=False):
    """Validate ideas_research.csv structure"""
    required_cols = [
        'id', 'original_idea_id', 'research_date', 'main_angle',
        'sub_angles_count', 'best_angle_id', 'angles_list',
        'sources_count', 'avg_relevance'
    ]

    if expected_pain_points:
        required_cols.append('pain_points_json')

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        if not all(col in reader.fieldnames for col in required_cols):
            return False, f"Missing columns: {required_cols}"

        for i, row in enumerate(reader):
            # Validate numeric fields
            try:
                int(row['sub_angles_count'])
                int(row['sources_count'])
                int(row['avg_relevance'])
            except ValueError:
                return False, f"Row {i+1}: Non-numeric value in count/relevance"

            # Validate avg_relevance range
            relevance = int(row['avg_relevance'])
            if not 0 <= relevance <= 100:
                return False, f"Row {i+1}: Relevance out of range: {relevance}"

            # If pain_points expected, validate JSON
            if expected_pain_points and 'pain_points_json' in row:
                try:
                    pains = json.loads(row['pain_points_json'])
                    for angle, angle_data in pains.items():
                        if 'pains' not in angle_data:
                            return False, f"Row {i+1}: Invalid pain_points structure"
                        if not 3 <= len(angle_data['pains']) <= 5:
                            return False, f"Row {i+1}: {angle} has {len(angle_data['pains'])} pains, expected 3-5"
                except json.JSONDecodeError:
                    return False, f"Row {i+1}: Invalid JSON in pain_points_json"

    return True, "ideas_research.csv valid"

def validate_posts_content_csv(filepath, expected_variant_count=None, is_routine=False):
    """Validate posts_content.csv"""
    required_cols = ['id', 'idea_id', 'research_id', 'angle_used',
                     'variant_type', 'draft_status', 'content_500_chars']

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        if not all(col in reader.fieldnames for col in required_cols):
            return False, f"Missing columns"

        rows = list(reader)

        if expected_variant_count:
            if len(rows) != expected_variant_count:
                return False, f"Expected {expected_variant_count} variants, got {len(rows)}"

        for i, row in enumerate(rows):
            # Validate variant types
            if is_routine:
                valid_types = ['base', 'cm_pas', 'cm_hook_story_offer', 'cm_show_work']
            else:
                valid_types = ['base']

            if row['variant_type'] not in valid_types:
                return False, f"Row {i+1}: Invalid variant_type: {row['variant_type']}"

            # Validate character counts
            if 'content_500_chars' in row and row['content_500_chars']:
                if not 450 <= len(row['content_500_chars']) <= 550:
                    return False, f"Row {i+1}: 500-char variant out of range"

            if is_routine and row['variant_type'].startswith('cm_'):
                if row.get('pain_embedded') != 'true':
                    return False, f"Row {i+1}: CM variant missing pain_embedded"
                if row.get('offer_embedded') != 'true':
                    return False, f"Row {i+1}: CM variant missing offer_embedded"

    return True, "posts_content.csv valid"

# Run validations
if __name__ == "__main__":
    test_mode = "TEXT" if len(sys.argv) > 1 else "ROUTINE"

    print(f"\n=== Validating {test_mode} Mode Data ===\n")

    # Text mode validation
    if test_mode == "TEXT":
        success, msg = validate_ideas_inbox_csv("data/ideas_inbox.csv")
        print(f"ideas_inbox.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

        success, msg = validate_ideas_research_csv("data/ideas_research.csv", expected_pain_points=False)
        print(f"ideas_research.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

        success, msg = validate_posts_content_csv("data/posts_content.csv", expected_variant_count=3, is_routine=False)
        print(f"posts_content.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

    # Routine mode validation
    else:
        success, msg = validate_ideas_inbox_csv("data/ideas_inbox.csv")
        print(f"ideas_inbox.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

        success, msg = validate_ideas_research_csv("data/ideas_research.csv", expected_pain_points=True)
        print(f"ideas_research.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

        success, msg = validate_posts_content_csv("data/posts_content.csv", expected_variant_count=6, is_routine=True)
        print(f"posts_content.csv: {'✅ PASS' if success else '❌ FAIL'} - {msg}")

    print()
```

---

### Validation Script 2: Data Flow Consistency Check

```python
#!/usr/bin/env python3
"""
Validate data flow consistency across CSV files
"""

import csv
import json

def check_text_mode_flow():
    """TEXT mode: No pains, no offers, 3 variants"""

    # Load CSVs
    ideas = load_csv("data/ideas_inbox.csv")
    research = load_csv("data/ideas_research.csv")
    posts = load_csv("data/posts_content.csv")

    errors = []

    for idea in ideas:
        if idea['content_type'] == 'demo':
            continue  # Skip ROUTINE ideas

        idea_id = idea['id']

        # Check research exists for this idea
        research_row = next((r for r in research if r['original_idea_id'] == idea_id), None)
        if not research_row:
            errors.append(f"Idea {idea_id}: No research found")
            continue

        # Check NO pain_points_json for TEXT mode
        if 'pain_points_json' in research_row and research_row['pain_points_json']:
            errors.append(f"Idea {idea_id}: TEXT mode has pain_points (shouldn't!)")

        # Count variants for this idea
        variants = [p for p in posts if p['idea_id'] == idea_id]
        if len(variants) != 3:
            errors.append(f"Idea {idea_id}: Expected 3 variants, got {len(variants)}")

        # Check all variants are 'base' type
        for variant in variants:
            if variant['variant_type'] != 'base':
                errors.append(f"Idea {idea_id}: Variant {variant['id']} has type '{variant['variant_type']}' (should be 'base')")

            # Check no pain/offer embedding
            if variant.get('pain_embedded') == 'true':
                errors.append(f"Idea {idea_id}: Variant {variant['id']} has pain_embedded (shouldn't!)")
            if variant.get('offer_embedded') == 'true':
                errors.append(f"Idea {idea_id}: Variant {variant['id']} has offer_embedded (shouldn't!)")

    return errors

def check_routine_mode_flow():
    """ROUTINE mode: With pains, with offers, 6 variants"""

    ideas = load_csv("data/ideas_inbox.csv")
    research = load_csv("data/ideas_research.csv")
    posts = load_csv("data/posts_content.csv")

    errors = []

    for idea in ideas:
        if idea['content_type'] != 'demo':
            continue  # Skip TEXT ideas

        idea_id = idea['id']

        # Check idea_metadata exists
        if 'idea_metadata' not in idea or not idea['idea_metadata']:
            errors.append(f"Idea {idea_id}: ROUTINE mode missing idea_metadata")
            continue

        # Check research exists
        research_row = next((r for r in research if r['original_idea_id'] == idea_id), None)
        if not research_row:
            errors.append(f"Idea {idea_id}: No research found")
            continue

        # Check pain_points_json exists and is valid
        if 'pain_points_json' not in research_row:
            errors.append(f"Idea {idea_id}: ROUTINE mode missing pain_points_json")
            continue

        try:
            pains = json.loads(research_row['pain_points_json'])
            num_angles = len(pains)

            # Validate pain structure
            for angle, angle_data in pains.items():
                if 'pains' not in angle_data:
                    errors.append(f"Idea {idea_id}: Angle {angle} missing 'pains' field")
                elif not 3 <= len(angle_data['pains']) <= 5:
                    errors.append(f"Idea {idea_id}: Angle {angle} has {len(angle_data['pains'])} pains (expect 3-5)")
        except json.JSONDecodeError:
            errors.append(f"Idea {idea_id}: Invalid JSON in pain_points_json")
            continue

        # Count variants (should be 6)
        variants = [p for p in posts if p['idea_id'] == idea_id]
        if len(variants) != 6:
            errors.append(f"Idea {idea_id}: Expected 6 variants, got {len(variants)}")

        # Check variant composition
        base_variants = [v for v in variants if v['variant_type'] == 'base']
        cm_variants = [v for v in variants if v['variant_type'].startswith('cm_')]

        if len(base_variants) < 1:
            errors.append(f"Idea {idea_id}: Missing base variants")
        if len(cm_variants) < 3:
            errors.append(f"Idea {idea_id}: Expected >=3 CM variants, got {len(cm_variants)}")

        # Check pain/offer embedding
        for variant in cm_variants:
            if variant.get('pain_embedded') != 'true':
                errors.append(f"Idea {idea_id}: CM variant {variant['id']} missing pain_embedded")
            if variant.get('offer_embedded') != 'true':
                errors.append(f"Idea {idea_id}: CM variant {variant['id']} missing offer_embedded")

    return errors

def load_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

# Run checks
if __name__ == "__main__":
    print("\n=== TEXT Mode Flow Check ===\n")
    errors = check_text_mode_flow()
    if errors:
        print("❌ ERRORS:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ TEXT mode flow is valid")

    print("\n=== ROUTINE Mode Flow Check ===\n")
    errors = check_routine_mode_flow()
    if errors:
        print("❌ ERRORS:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("✅ ROUTINE mode flow is valid")
```

---

## Part 4: Error Scenario Tests

### Error Test 4.1: Duplicate Idea Handling

**Test Setup:** Two similar ideas submitted

**Test Steps:**
1. Submit idea #1: "ИИ помогает создавать контент быстро"
2. Submit idea #2: "ИИ ускоряет процесс написания контента" (87% similarity)
3. System should flag as duplicate

**Expected Behavior:**
```
⚠️  Potential duplicate detected: 87% match

Похожая идея уже есть: "ИИ помогает создавать контент быстро"

Ваш вариант:
[Accept] — Это другой угол той же темы (сохранить оба)
[Modify] — Изменить мою идею
[Cancel] — Отмена
```

**CSV Validation:**
- If [Accept]: Both saved with `status="active"` and note about duplication
- If [Modify]: Return to input, don't save yet
- If [Cancel]: Neither saved

---

### Error Test 4.2: Missing Pain Points in ROUTINE Mode

**Test Setup:** ROUTINE mode idea researched, but pain_points_json not generated

**Test Scenario:**
- System error during pain point generation
- ideas_research.csv saved but pain_points_json column missing

**Expected Detection:**
```javascript
// Validation should catch:
const painData = JSON.parse(row.pain_points_json); // THROWS ERROR
// "Column not found" or "null value where object expected"
```

**QA Action:**
- Flag as CRITICAL error
- Regenerate pain points for that research_id
- Re-run c-02c-research.md for that idea

---

### Error Test 4.3: Offer Filter Not Applied

**Test Setup:** ROUTINE mode, offer_filter.csv specifies ["training", "setup"]

**Test Steps:**
1. Generate offers for demo idea
2. Check generated offers

**Expected Behavior:**
- Only offers of type "training" and "setup" should be generated
- No "consulting", "templates", or "full_dev" offers

**Error Scenario:**
```
Generated offer:
{
  "type": "full_dev",  // ❌ ERROR: This is in unwilling_offers!
  "title": "Write entire app for you"
}
```

**QA Validation:**
```javascript
const willingness = load_csv("user_preferences/offer_filter.csv");
const unwilling = willingness.filter(r => r.willing === "false").map(r => r.offer_type);

generated_offers.forEach(offer => {
  if (unwilling.includes(offer.type)) {
    throw new Error(`Offer type ${offer.type} not in willing list!`);
  }
});
```

---

### Error Test 4.4: Cross-Contamination Between Modes

**Test Setup:** Process both TEXT and ROUTINE ideas in same session

**Test Scenario:**
1. Idea #1 (TEXT) → 3 variants, no pains
2. Idea #2 (ROUTINE) → 6 variants, with pains
3. Check CSV for contamination

**Error Check:**
```javascript
// Text idea should NOT have pain_points
const textIdea = ideas.filter(i => i.content_type === "evergreen")[0];
const textResearch = research.filter(r => r.original_idea_id === textIdea.id)[0];

if (textResearch.pain_points_json) {
  throw new Error("TEXT mode idea has pain_points_json!");
}

// ROUTINE idea should have pain_points
const routineIdea = ideas.filter(i => i.content_type === "demo")[0];
const routineResearch = research.filter(r => r.original_idea_id === routineIdea.id)[0];

if (!routineResearch.pain_points_json) {
  throw new Error("ROUTINE mode idea missing pain_points_json!");
}
```

---

## Part 5: Test Execution Checklist

### Pre-Test Setup

- [ ] Clear test data directory
- [ ] Initialize empty CSVs with headers:
  - `ideas_inbox.csv`
  - `ideas_research.csv`
  - `posts_content.csv`
- [ ] Initialize test directories:
  - `data/`
  - `user_preferences/`
  - `test-data/` (with sample screenshot)
- [ ] Load test data sets (from Part 1)
- [ ] Start workflow system
- [ ] Verify Vision API available (if ROUTINE tests)

### Test Execution Order

**Phase 1: TEXT Mode (2-3 hours)**
1. Test 1.1 → 1.9 (sequential, each depends on previous)
2. Run Validation Script 1 after step 1.2
3. Run Validation Script 2 after step 1.9

**Phase 2: ROUTINE Mode (3-4 hours)**
1. Clear test data (or use separate test DB)
2. Test 2.1 → 2.13 (sequential)
3. Run Validation Script 1 after step 2.2
4. Run Validation Script 1 after step 2.4
5. Run Validation Script 2 after step 2.13

**Phase 3: Error Scenarios (1-2 hours)**
1. Error Test 4.1 (duplicate handling)
2. Error Test 4.2 (missing pain points)
3. Error Test 4.3 (offer filter validation)
4. Error Test 4.4 (cross-contamination)

### Test Report Template

```markdown
# Test Execution Report
Date: [date]
Tester: [name]
System Version: [version]
Test Mode: [TEXT / ROUTINE / BOTH]

## Test Results Summary

| Test ID | Name | Status | Notes |
|---------|------|--------|-------|
| 1.1 | Mode Selection - TEXT | ✅ PASS | User routed correctly |
| 1.2 | Idea Input - TEXT | ✅ PASS | CSV saved with correct schema |
| ... | ... | ... | ... |

## CSV Data Validation

ideas_inbox.csv:
✅ Headers correct
✅ 3 rows (TEXT mode)
✅ content_type values valid
✅ No duplicate IDs

ideas_research.csv:
✅ Headers correct
✅ 1 row for TEXT mode (no pains)
✅ Avg_relevance in range 0-100
✅ Pain_points_json: ABSENT (correct for TEXT)

posts_content.csv:
✅ Headers correct
✅ 3 variants for TEXT idea (correct count)
✅ All variants type='base'
✅ No pain/offer embedding

## Cross-Scenario Validation

- [✅] TEXT and ROUTINE ideas can coexist without contamination
- [✅] Pain points only in ROUTINE research
- [✅] Variants count correct per mode (3 vs 6)
- [✅] Offer filter applied correctly in ROUTINE

## Issues Found

[List any issues found during testing]

## Recommendations

[Any recommendations for system improvement]
```

---

## Summary

This comprehensive test suite covers:

✅ **TEXT Mode:** Complete flow from input → research (no pains) → 3 variants → publish
✅ **ROUTINE Mode:** Complete flow from screenshot → pain extraction → offer generation → 6 variants → publish
✅ **Data Validation:** CSV schemas, JSON structures, field validation
✅ **Flow Consistency:** Proper routing between steps, no cross-contamination
✅ **Error Scenarios:** Duplicates, missing data, unwanted offers, mode mixing
✅ **Validation Scripts:** Ready-to-run Python scripts for CSV validation

**Total Test Cases:** 30+ individual test scenarios
**Estimated Execution Time:** 6-8 hours (can be parallelized)
**Ready for QA Team:** Yes, step-by-step instructions included

