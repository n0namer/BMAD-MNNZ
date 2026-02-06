# Content Machine Pipeline - Test Execution Guide

**For QA Teams: Step-by-Step Test Instructions**
**Version:** 1.0
**Created:** 2026-01-30

---

## Quick Start

This guide provides **ready-to-execute instructions** for testing the Content Machine Pipeline.

**Two scenarios:**
1. **TEXT Mode** - Simple text input (3 variants, no special features)
2. **ROUTINE Mode** - Demo with pain points + offers (6 variants, full CM features)

**Time Required:**
- TEXT Mode tests: 2-3 hours
- ROUTINE Mode tests: 3-4 hours
- Error scenarios: 1-2 hours
- **Total:** 6-8 hours

---

## Part 1: Environment Setup

### Step 1: Prepare Test Directory Structure

```bash
# Create test directories
mkdir -p D:\test-content-machine\data
mkdir -p D:\test-content-machine\user_preferences
mkdir -p D:\test-content-machine\test-data

# Note: Use absolute paths only, avoid relative paths
```

### Step 2: Initialize Empty CSV Files

**File: `D:\test-content-machine\data\ideas_inbox.csv`**
```csv
id,date_added,source,raw_idea,content_type,category,status,notes
```

**File: `D:\test-content-machine\data\ideas_research.csv`**
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
```

**File: `D:\test-content-machine\data\posts_content.csv`**
```csv
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,content_250_chars,content_100_chars
```

### Step 3: Verify System Ready

- [ ] Claude Flow system running
- [ ] Vision API available (for ROUTINE tests)
- [ ] Web search capability available (for research phase)
- [ ] All workflow files accessible

---

## Part 2: TEXT Mode Test Execution (Tests 1.1-1.9)

### Test 1.1: Mode Selection

**Duration:** 5 minutes

**Setup:**
- User at c-01-add-idea.md menu
- No test data loaded yet

**Steps:**
1. Present mode selection menu to user
2. **User input:** `T` (TEXT mode)
3. System should display: "Request Idea Input" prompt (no screenshot upload)

**Verification Checklist:**
- [ ] Mode menu displayed
- [ ] TEXT option clearly labeled
- [ ] User selection captured as 'T'
- [ ] System routes to text input (not screenshot upload)
- [ ] No Vision API called

**Pass Criteria:** System correctly routes to TEXT mode workflow

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.2: Idea Input & Validation

**Duration:** 10 minutes

**Setup:**
- Completed Test 1.1 (TEXT mode selected)
- Ready for text input

**Test Data:**
```
Idea: "ИИ помогает создавать контент за 3 часа вместо недели"
Type: [1] EVERGREEN
Category: Technology
```

**Steps:**
1. **User input:** Raw idea text
2. System validates against checklist:
   - Specific? YES
   - Researchable? YES
   - Audience clear? YES
   - Not duplicate? YES
3. **User selects:** Content type [1] EVERGREEN
4. **User provides:** Category (auto-detected or manual)
5. System shows idea summary
6. System routes to dedup check

**CSV Check After Step:**
```
Expected in ideas_inbox.csv:
id,date_added,source,raw_idea,content_type,category,status,notes
1,[TODAY],user_input,"ИИ помогает создавать контент за 3 часа вместо недели",evergreen,Technology,active,"[auto notes]"
```

**Verification Checklist:**
- [ ] Idea saved to CSV with ID = 1
- [ ] Date is today's date
- [ ] source = "user_input"
- [ ] content_type = "evergreen"
- [ ] No idea_metadata column (TEXT mode)
- [ ] Status = "active"

**Pass Criteria:**
- CSV row created with correct schema
- All fields populated correctly
- No extra columns added

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.3: Deduplication Check

**Duration:** 5 minutes

**Setup:**
- Completed Test 1.2
- ideas_inbox.csv has 1 row
- User proceeding to save idea

**Steps:**
1. System checks for duplicates (should find none)
2. System displays: "No duplicates detected"
3. **User action:** Confirm save
4. Idea remains active in CSV

**CSV Validation:**
- Same row as Test 1.2 (no changes)
- status remains "active"

**Verification Checklist:**
- [ ] Duplicate check executed
- [ ] No false positives reported
- [ ] CSV unchanged (idea saved)

**Pass Criteria:** Dedup logic executed correctly

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.4: Research Execution

**Duration:** 15 minutes

**Setup:**
- Completed Tests 1.2-1.3
- Idea saved to ideas_inbox.csv
- User selects [R] RESEARCH

**Steps:**
1. System loads idea from CSV
2. System executes research (web search for angles)
3. System finds 5-8 angles with sources
4. Research completes

**Expected Output:**
```
✅ RESEARCH COMPLETE
Found: 8 different angles
Sources: 32 total (average 4 per angle)
Avg relevance: 86% (GOOD)
```

**CSV Check After Step:**
```
Expected in ideas_research.csv:
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,[TODAY],"Time Saving via ИИ",8,"angle_1",[angles...],32,86
```

**Critical Validation - NO pain_points_json for TEXT:**
```
MUST NOT have: pain_points_json column
This is TEXT mode, not ROUTINE mode
```

**Verification Checklist:**
- [ ] research_date = today
- [ ] original_idea_id = 1 (matches ideas_inbox row)
- [ ] 5-8 angles found
- [ ] avg_relevance between 75-95
- [ ] sources_count >= 20
- [ ] NO pain_points_json column (critical for TEXT mode!)

**Pass Criteria:**
- Research row created correctly
- No pain points generated (TEXT mode)
- All numeric fields in valid ranges

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.5: Results Display

**Duration:** 10 minutes

**Setup:**
- Completed Test 1.4
- ideas_research.csv has valid data
- User at c-02d-results.md

**Steps:**
1. System displays all 8 angles with sources
2. User reviews angles
3. **Critical check:** No pain points section displayed

**Verification Checklist:**
- [ ] All 8 angles displayed
- [ ] Each has: name, insight, sources, facts, relevance
- [ ] NO pain points shown (TEXT mode)
- [ ] Source data is accurate and verifiable

**Pass Criteria:**
- Display matches research data
- No pain points leaked into view

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.6: Angle Selection & Routing

**Duration:** 5 minutes

**Setup:**
- Completed Test 1.5
- All angles displayed
- User selects angle

**Test Data:**
```
Selected angle: "Time Saving via ИИ"
```

**Steps:**
1. User selects angle from list
2. System checks: content_type from original idea
3. **Critical routing:**
   - Read ideas_inbox.csv row 1: content_type = "evergreen"
   - "evergreen" != "demo" → TEXT mode
   - Route to c-03c (NOT c-03b1)

**Verification Checklist:**
- [ ] System reads correct field from CSV (content_type)
- [ ] Compares: is it "demo"?
- [ ] Result: NO (it's "evergreen")
- [ ] Routes directly to c-03c (draft)
- [ ] c-03b1 (offer check) and c-03b2 skipped

**Pass Criteria:**
- Routing logic correct
- No unnecessary steps executed
- Proceeds to draft generation

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.7: Draft Generation

**Duration:** 10 minutes

**Setup:**
- Completed Test 1.6
- Routed to c-03c-draft.md
- System generating draft

**Steps:**
1. System generates 1 draft based on selected angle
2. Draft saved to posts_content.csv
3. System presents draft for review

**Expected Output:**
```
📝 WRITING POST: Time Saving via ИИ
Generated 1 draft version
Quality: 89/100
Best for: LinkedIn
[500-char draft text displayed]
```

**CSV Check After Step:**
```
Expected in posts_content.csv:
id,idea_id,research_id,angle_used,variant_type,draft_status,content_500_chars,...
1,1,1,"Time Saving","base","draft_1","[full text]",...
```

**Verification Checklist:**
- [ ] Row created with id=1, idea_id=1, research_id=1
- [ ] variant_type = "base"
- [ ] content_500_chars populated (~500 chars)
- [ ] content_250_chars = NULL (not yet)
- [ ] content_100_chars = NULL (not yet)
- [ ] draft_status = "draft_1"

**Pass Criteria:**
- Draft saved with correct schema
- Character count in expected range
- Only 500-char version exists yet

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.8: Variant Generation (3 VARIANTS)

**Duration:** 15 minutes

**Setup:**
- Completed Test 1.7
- Draft exists in posts_content.csv
- User confirms draft and proceeds to variants

**Steps:**
1. System routes to c-03d-variants.md
2. System generates shorter versions:
   - 250-char version (from 500-char)
   - 100-char version (from 500-char)
3. System displays all 3 variants

**Expected Output:**
```
✅ VARIANTS GENERATED (TEXT MODE: 3 variants)

[500 chars] — Original (487 chars)
Quality: 89/100 | Best for: LinkedIn

[250 chars] — Medium (251 chars)
Quality: 87/100 | Best for: Telegram

[100 chars] — Short (98 chars)
Quality: 85/100 | Best for: Twitter
```

**CSV Check After Step:**
```
Expected in posts_content.csv:
(Same row as 1.7, but updated with all variants)
id,idea_id,research_id,angle_used,variant_type,content_500_chars,content_250_chars,content_100_chars
1,1,1,"Time Saving","base","[text]","[text]","[text]"
```

**Critical COUNT Check - EXACTLY 3:**
```python
# In posts_content.csv, count rows with idea_id = 1
variants = posts_content.filter(idea_id == 1)
assert len(variants) == 3, f"Expected 3 variants, got {len(variants)}"
```

**Character Count Validation:**
```
500-char: 450-550 chars (actual: measure)
250-char: 200-300 chars (actual: measure)
100-char: 50-150 chars (actual: measure)
```

**Verification Checklist:**
- [ ] Exactly 3 variants created
- [ ] All have variant_type = "base"
- [ ] All have same idea_id and research_id
- [ ] Character counts in valid ranges
- [ ] All content fields populated
- [ ] No pain_embedded or offer_embedded fields
- [ ] No cm_* variant types

**Pass Criteria:**
- Exactly 3 variants
- All base type (no Content Machine variants)
- Character counts correct
- No pain/offer contamination

**Result:** ✅ PASS / ❌ FAIL

---

### Test 1.9: Finalization & Publishing

**Duration:** 10 minutes

**Setup:**
- Completed Test 1.8
- 3 variants exist and approved
- User at finalization step

**Steps:**
1. User selects: [S] SELECT
2. User chooses: [A] ALL THREE
3. System routes to c-03e-finalize.md
4. System publishes all variants

**Expected Output:**
```
✅ POST FINALIZED

All 3 variants saved:
├─ Variant 1 (500 chars): Ready
├─ Variant 2 (250 chars): Ready
└─ Variant 3 (100 chars): Ready
```

**CSV Final Check:**
```
All 3 rows in posts_content.csv:
- publish_status = "published" (for all)
- No duplicates
- All variants tied to correct idea_id and research_id
```

**Verification Checklist:**
- [ ] 3 rows in posts_content.csv
- [ ] All have publish_status = "published"
- [ ] No duplicate IDs
- [ ] All have valid content
- [ ] No orphaned rows

**Complete Test 1 Data Integrity Check:**
```
Ideas: 1 row (TEXT mode)
Research: 1 row (no pain points)
Posts: 3 variants (base type only)

No pain points in any CSV ✓
No offer filters created ✓
No workflow_state.json ✓
```

**Pass Criteria:**
- All 3 variants published
- No data contamination
- Complete TEXT mode flow executed successfully

**Result:** ✅ PASS / ❌ FAIL

---

## Part 3: ROUTINE Mode Test Execution (Tests 2.1-2.13)

### Test 2.1: Mode Selection

**Duration:** 5 minutes

**Setup:**
- IMPORTANT: Start fresh (clear all data from Part 2 or use separate DB)
- User at c-01-add-idea.md menu

**Steps:**
1. System displays mode selection menu
2. **User input:** `R` (ROUTINE mode)
3. System should display: screenshot upload + description input

**Verification Checklist:**
- [ ] Mode menu displayed
- [ ] ROUTINE/DEMO option clearly labeled as [R]
- [ ] User selection captured as 'R'
- [ ] Screenshot upload field shown
- [ ] Description text field shown
- [ ] Content type selection field NOT shown yet

**Pass Criteria:**
- System correctly routes to ROUTINE mode
- Vision API inputs ready

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.2: Vision AI Processing

**Duration:** 10 minutes

**Setup:**
- Completed Test 2.1 (ROUTINE mode selected)
- Test screenshot available

**Test Data:**
```
Screenshot: /test-data/bmad-screenshot.png
Description: "Использую BMAD для генерирования всей документации
              компании за 2 часа"
```

**Steps:**
1. User uploads screenshot
2. User provides description
3. System calls Claude Vision API
4. System extracts: visual_context, tools_used, demonstrated_result, context_type
5. System combines with description

**Expected Vision Output:**
```json
{
  "visual_context": "На скрине видна интерфейс BMAD с диалогом...",
  "tools_used": ["BMAD", "Claude", "PDF export"],
  "demonstrated_result": "80+ документов готовы к использованию",
  "context_type": "documentation generation"
}
```

**CSV Check After Step:**
```
Expected in ideas_inbox.csv:
id,date_added,source,raw_idea,content_type,idea_metadata,status,notes
1,[TODAY],routine,"Использую BMAD...",demo,"{\"visual_context\": \"...\", \"tools_used\": [...], ...}",active,"[auto]"
```

**Critical Validations for ROUTINE Mode:**
```
✓ source = "routine" (not "user_input")
✓ content_type = "demo" (auto-set, not user-selected)
✓ idea_metadata is VALID JSON
✓ idea_metadata has all 4 required fields
✓ No empty or null values in metadata
```

**Verification Checklist:**
- [ ] Vision API called successfully
- [ ] 4 context fields extracted
- [ ] Metadata is valid JSON (parseable)
- [ ] CSV row created with source="routine"
- [ ] content_type auto-set to "demo"
- [ ] All metadata fields non-empty

**Pass Criteria:**
- Vision extraction successful
- CSV row created correctly
- Metadata complete and valid

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.3: Content Type Auto-Selection

**Duration:** 5 minutes

**Setup:**
- Completed Test 2.2
- Screenshot processed and metadata extracted
- System at content type selection step

**Steps:**
1. System checks: Is this ROUTINE mode?
2. **Critical logic:** content_type == "demo"?
3. If YES → Skip manual selection
4. Proceed immediately to next step
5. No content type selection form shown to user

**Expected Output:**
```
✅ ROUTINE Mode Detected!
Content type automatically set to: DEMO

Система пропускает выбор типа контента и идёт дальше...
```

**CSV Check:**
- Row 1 in ideas_inbox.csv still has content_type = "demo"

**Verification Checklist:**
- [ ] Content type selection form NOT shown
- [ ] System proceeds without user input on type
- [ ] content_type remains "demo" in CSV
- [ ] No duplicate type selection attempts

**Pass Criteria:**
- Auto-selection works (no user prompt)
- Proceeds immediately to research

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.4: Research with Pain Point Generation

**Duration:** 20 minutes

**Setup:**
- Completed Tests 2.1-2.3
- Idea saved with content_type="demo"
- User selects [R] RESEARCH

**Steps:**
1. System loads idea from ideas_inbox.csv
2. **Critical check:** Is content_type == "demo"?
3. YES → Execute Section 2.5 (Pain Point Generation)
4. For EACH angle found, generate 3-5 pain points
5. System displays research results WITH pains
6. Save all data including pain_points_json

**Expected Research Output:**
```
✅ RESEARCH COMPLETE

Found: 8 different angles
Sources: 32 total (average 4 per angle)
Avg relevance: 86% (GOOD)

Генерирую боли предпринимателей для каждого угла...

ANGLE 1: Time Saving ⏱️
├─ Sources: 7
├─ Relevance: 92%
└─ Пains solved by this routine:
   ├─ 🔴 Медленная документация берёт 2-3 дня
   ├─ 🔴 Все процессы в голове у одного человека
   ├─ 🔴 Нельзя масштабировать без найма
   └─ 🔴 Непроцессированная информация
```

**CSV Check After Step:**
```
Expected in ideas_research.csv:
id,original_idea_id,...,pain_points_json
1,1,...,"{\"angle_1\": {\"pains\": [\"pain1\", \"pain2\", ...]}, ...}"
```

**Critical ROUTINE Validations:**
```
✓ pain_points_json column EXISTS
✓ Valid JSON structure
✓ 8 angles in pain_points_json
✓ Each angle has 3-5 pains (NOT more, NOT less)
✓ Pain descriptions in business language (not technical)
✓ Pains reference the demonstrated routine
✓ No truncated or incomplete pain text
```

**Pain Point Validation Logic:**
```python
import json

row = research_csv[0]  # First research row
pains = json.loads(row['pain_points_json'])

for angle_name, angle_data in pains.items():
    pains_list = angle_data['pains']

    # Validate count
    assert 3 <= len(pains_list) <= 5, \
        f"Angle {angle_name}: {len(pains_list)} pains (expect 3-5)"

    # Validate non-empty
    assert all(p for p in pains_list), \
        f"Angle {angle_name}: Empty pain found"

    # Validate language (business, not technical)
    for pain in pains_list:
        assert len(pain) > 10, f"Pain too short: {pain}"
        assert len(pain) < 200, f"Pain too long: {pain}"
```

**Verification Checklist:**
- [ ] pain_points_json column exists in CSV
- [ ] JSON is valid (parseable without errors)
- [ ] All 8 angles represented
- [ ] Each angle has 3-5 pains
- [ ] Pain count validation passes
- [ ] Pain text validation passes
- [ ] Pains are not technical

**Pass Criteria:**
- Research row created with pain_points_json
- Pain structure valid
- All pain counts correct
- No syntax errors in JSON

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.5: Results Display with Pain Points

**Duration:** 10 minutes

**Setup:**
- Completed Test 2.4
- ideas_research.csv has pain_points_json
- User at c-02d-results.md

**Steps:**
1. System displays all 8 angles
2. **Critical display check:** Pain points shown for EVERY angle
3. User reviews pains associated with each angle
4. Compare to TEXT mode (which had NO pains)

**Expected Output:**
```
ANGLE 1: Time Saving ⏱️
├─ Main insight: "Saves 70% of content creation time"
├─ Sources found: 7
├─ Key facts: [...]
├─ Relevance: 92%
└─ Best for: Founders, agencies

🔴 Пains this routine solves:
├─ 🔴 Медленная документация берёт 2-3 дня
├─ 🔴 Все процессы в голове у одного человека
├─ 🔴 Нельзя масштабировать без найма
└─ 🔴 Непроцессированная информация

[... 7 more angles, each with pain section ...]
```

**Verification Checklist:**
- [ ] All 8 angles displayed
- [ ] Each angle has pain points section
- [ ] Pain points match those from pain_points_json
- [ ] Pains are readable and correct
- [ ] Format consistent across all angles

**Comparison to TEXT Mode Test 1.5:**
```
TEXT mode (Test 1.5):
- NO pain points section
- Only facts and sources shown

ROUTINE mode (Test 2.5):
- Pain points shown for EVERY angle
- Pains from pain_points_json displayed
```

**Pass Criteria:**
- Pains displayed for all angles
- Pains match CSV data
- Display differs from TEXT mode

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.6: Angle Selection & Routing

**Duration:** 5 minutes

**Setup:**
- Completed Test 2.5
- All angles with pains displayed
- User selects angle

**Test Data:**
```
Selected angle: "Time Saving via BMAD"
```

**Steps:**
1. User selects angle from list
2. **Critical routing logic:**
   - Read ideas_inbox.csv row 1: content_type
   - Expected: "demo"
   - Check: content_type == "demo"?
   - Result: YES
   - Route: c-03b1 (NOT c-03c)

**Verification Checklist:**
- [ ] System reads content_type from ideas_inbox.csv
- [ ] Value is "demo"
- [ ] Routing condition: content_type == "demo" → TRUE
- [ ] Routes to c-03b1 (offer check)
- [ ] Does NOT route directly to c-03c
- [ ] c-03b1 and c-03b2 MUST be executed

**Routing Difference from TEXT Mode (Test 1.6):**
```
TEXT mode routing:
- ideas_inbox.csv content_type = "evergreen"
- "evergreen" != "demo" → Route to c-03c directly

ROUTINE mode routing:
- ideas_inbox.csv content_type = "demo"
- "demo" == "demo" → Route to c-03b1 first
```

**Pass Criteria:**
- Correct routing based on content_type
- c-03b1 executed for ROUTINE mode

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.7: Offer Filter Setup (First Run)

**Duration:** 10 minutes

**Setup:**
- Completed Test 2.6
- Routed to c-03b1
- File `user_preferences/offer_filter.csv` does NOT exist (first run)

**Steps:**
1. System checks for offer_filter.csv
2. File doesn't exist → Show first-time setup form
3. User selects offer types from options:
   - [1] Training
   - [2] Setup
   - [3] Templates
   - [4] Consulting
   - [5] Full Dev (not recommended)
4. **User input:** `1,2,3,4` (skip full dev)
5. System creates offer_filter.csv with selections
6. System stores state in workflow_state.json

**Expected Form:**
```
[X] 1. ОБУЧЕНИЕ / НАСТАВНИЧЕСТВО
[X] 2. ПРОЕКТИРОВАНИЕ ПРОЦЕССА / SETUP
[X] 3. ШАБЛОНЫ / МЕТОДИЧКИ
[X] 4. КОНСАЛТИНГ / РАЗБОР ПРОЦЕССОВ
[ ] 5. РАЗРАБОТКА ПРОДУКТА "ПОД КЛЮЧ"
```

**CSV Creation - user_preferences/offer_filter.csv:**
```csv
offer_type,willing,notes
training,true,Обучение — ОК
setup,true,Проектирование процесса — ОК
templates,true,Шаблоны — ОК
consulting,true,Консалтинг — ОК
full_dev,false,Разработка под ключ — НЕ хочу
```

**Verification Checklist:**
- [ ] File created at correct path
- [ ] CSV headers: offer_type, willing, notes
- [ ] 5 rows (all offer types)
- [ ] 4 rows with willing=true
- [ ] 1 row with willing=false (full_dev)
- [ ] Notes field populated for each
- [ ] CSV syntax correct (comma-separated, no quotes needed)

**Pass Criteria:**
- offer_filter.csv created with correct structure
- All offer types present
- User selections correctly recorded

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.8: Offer Filter Setup (Subsequent Runs)

**Duration:** 5 minutes

**Setup:**
- offer_filter.csv EXISTS from Test 2.7
- ROUTINE mode processing another demo idea
- System routing to c-03b1 again

**Steps:**
1. System checks for offer_filter.csv
2. File EXISTS → Load existing profile
3. Display loaded profile
4. **User action:** [Нет, продолжить] (No, continue)
5. Skip re-selection form
6. Use existing preferences

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

**Verification Checklist:**
- [ ] Profile loaded from CSV (no re-creation)
- [ ] Preferences match Test 2.7 settings
- [ ] User chooses [Нет, продолжить]
- [ ] No re-selection form shown
- [ ] Proceeds to c-03b2

**Pass Criteria:**
- Existing profile loaded correctly
- Preferences reused without modification

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.9: Workflow State Storage

**Duration:** 5 minutes

**Setup:**
- Completed Test 2.7 or 2.8
- Offer filter set
- System storing state

**Steps:**
1. System saves workflow state to workflow_state.json
2. Includes phase, content_type, offer preferences, timestamp

**Expected JSON:**
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

**Verification Checklist:**
- [ ] File created: workflow_state.json
- [ ] Valid JSON structure
- [ ] workflow_phase = "c-03b1-offer-check"
- [ ] content_type = "demo"
- [ ] offer_filter_configured = true
- [ ] willing_offers array has 4 elements
- [ ] unwilling_offers array has 1 element
- [ ] Timestamp in ISO format

**Pass Criteria:**
- State file created correctly
- All required fields present
- JSON valid

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.10: Offer Generation

**Duration:** 15 minutes

**Setup:**
- Completed Test 2.9
- State stored with offer preferences
- System routing to c-03b2-offer-generation.md

**Steps:**
1. System loads offer_filter.csv preferences
2. System generates 2-4 offers based on:
   - Demonstrated routine (from idea_metadata)
   - Selected angle (from previous step)
   - Willing offer types only
3. System displays generated offers
4. System saves offers to workflow_state.json
5. Routes to c-03c (draft)

**Expected Output:**
```
✅ Фильтр офферов настроен.

Система будет генерировать офферы ТОЛЬКО из:
├─ ✅ Обучение / Наставничество
├─ ✅ Проектирование Процесса / Setup
├─ ✅ Шаблоны / Методички
└─ ✅ Консалтинг / Разбор Процессов

Генерирую офферы для угла "Time Saving via BMAD"...

OFFER 1: ОБУЧЕНИЕ
  "Научу вас за 2-3 часа создавать документацию через BMAD"
  Estimated value: $300-500
  Delivery: 1x 1-on-1 session

OFFER 2: SETUP
  "Настрою BMAD-систему для вашей компании (3-5 дней)"
  Estimated value: $2,000-3,500

OFFER 3: TEMPLATES
  "Шаблон-набор для автоматизации документации"
  Estimated value: $49-99

[... possibly 1 more offer ...]
```

**workflow_state.json - Updated:**
```json
{
  ...previous fields...,
  "workflow_phase": "c-03b2-offer-generation",
  "angle_selected": "Time Saving via BMAD",
  "offers_generated": [
    {
      "offer_id": "offer_1",
      "type": "training",
      "title": "Научу создавать документацию через BMAD",
      "estimated_value": "300-500",
      "delivery_days": "1"
    },
    {
      "offer_id": "offer_2",
      "type": "setup",
      "title": "Настрою BMAD-систему",
      "estimated_value": "2000-3500",
      "delivery_days": "5"
    },
    {
      "offer_id": "offer_3",
      "type": "templates",
      "title": "Шаблон-набор документации",
      "estimated_value": "49-99",
      "delivery_days": "0"
    }
  ],
  "timestamp": "2026-01-30T10:35:00Z"
}
```

**Critical Offer Validation:**
```python
# Check offer count
assert 2 <= len(offers_generated) <= 4, \
    f"Expected 2-4 offers, got {len(offers_generated)}"

# Check only willing offer types generated
unwilling = ["full_dev"]
for offer in offers_generated:
    assert offer['type'] not in unwilling, \
        f"Offer type {offer['type']} in unwilling list!"

# Check all offers have required fields
for offer in offers_generated:
    assert offer['offer_id'], "Missing offer_id"
    assert offer['type'], "Missing type"
    assert offer['title'], "Missing title"
    assert offer['estimated_value'], "Missing estimated_value"
```

**Verification Checklist:**
- [ ] 2-4 offers generated
- [ ] All offer types in willing_offers list
- [ ] NO full_dev offers
- [ ] Each offer has: id, type, title, value, delivery_days
- [ ] Offers specific to demonstrated routine
- [ ] Offers specific to selected angle
- [ ] workflow_state.json updated with offers
- [ ] timestamp updated

**Pass Criteria:**
- 2-4 offers generated
- All offers from willing list
- workflow_state.json updated correctly

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.11: Draft Generation with Offers

**Duration:** 10 minutes

**Setup:**
- Completed Test 2.10
- Offers loaded into workflow_state.json
- System routing to c-03c-draft.md

**Steps:**
1. System checks: Are offers available?
2. YES (2-4 offers loaded)
3. Draft generated with offer context in metadata
4. Draft stored in posts_content.csv
5. Reference offers in metadata

**Expected Output:**
```
📝 WRITING POST: Time Saving via BMAD

Generated 1 draft version (with Content Machine enhancements):

[DRAFT 1] DIRECT & PUNCHY (Content Machine Framework)
Quality: 91/100
Enhancement: Content Machine + Offers
[... draft content showing offer integration points ...]
```

**CSV Check - posts_content.csv:**
```csv
id,idea_id,research_id,angle_used,variant_type,has_offer_hooks,offer_references
1,1,1,"Time Saving","base",true,"offer_1,offer_2,offer_3"
```

**Verification Checklist:**
- [ ] Offers loaded from workflow_state.json
- [ ] Draft metadata includes has_offer_hooks=true
- [ ] offer_references lists all generated offers
- [ ] CSV row created with offer hook markers
- [ ] Base content not yet modified (modifications come in variants)

**Pass Criteria:**
- Draft created with offer context
- Offers referenced in metadata
- Ready for variant generation with offer embedding

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.12: Variant Generation (6 VARIANTS - CRITICAL)

**Duration:** 20 minutes

**Setup:**
- Completed Test 2.11
- Draft exists with offer hooks
- System at c-03d-variants.md
- offers_generated in workflow_state.json

**Steps:**
1. System checks: ROUTINE mode with offers?
2. YES (content_type="demo", offers present)
3. Generate 6 variants:
   - Variants 1-3: BASIC versions (standard format, no pains/offers)
   - Variants 4-6: CONTENT MACHINE FRAMEWORK versions (with pain + offer embedding)
4. Display all 6 variants

**Expected Output:**
```
✅ VARIANTS GENERATED (ROUTINE MODE: 6 variants!)

BASIC VARIANTS (Standard format):
─────────────────────────────────
[1] 500 chars — Original
    Quality: 89/100 | Framework: Standard
    Chars: 487

CONTENT MACHINE VARIANTS (With Pains & Offers):
──────────────────────────────────────────────
[2] PAS Framework — Problem-Agitate-Solution
    Quality: 91/100 | Pains: embedded | Offers: 1-2
    Structure: Problem → Agitation → Solution → Offer CTA

[3] Hook-Story-Offer — Narrative
    Quality: 92/100 | Pains: embedded | Offers: 2-3

[4] Show Your Work — Authenticity
    Quality: 90/100 | Pains: embedded | Offers: 1-2

[5] PAS Alternative — Different angle
    Quality: 90/100 | Pains: embedded | Offers: 1-2

[6] Hook-Story-Offer Alternative — Different story
    Quality: 91/100 | Pains: embedded | Offers: 2-3
```

**CSV Check - posts_content.csv:**
```csv
id,idea_id,research_id,angle_used,variant_type,pain_embedded,offer_embedded,variant_framework
1,1,1,"Time Saving","base","false","false","standard"
2,1,1,"Time Saving","cm_pas","true","true","PAS"
3,1,1,"Time Saving","cm_hook_story_offer","true","true","Hook-Story-Offer"
4,1,1,"Time Saving","cm_show_work","true","true","Show Your Work"
5,1,1,"Time Saving","cm_pas","true","true","PAS"
6,1,1,"Time Saving","cm_hook_story_offer","true","true","Hook-Story-Offer"
```

**Critical COUNT Validation - EXACTLY 6:**
```python
# Count all variants for this idea
variants = posts_content.filter(idea_id == 1)
assert len(variants) == 6, \
    f"Expected 6 variants in ROUTINE mode, got {len(variants)}"

# Count base vs CM variants
base = variants.filter(variant_type == "base")
cm = variants.filter(variant_type.startswith("cm_"))

assert len(base) >= 1, f"Expected >=1 base, got {len(base)}"
assert len(cm) >= 3, f"Expected >=3 CM, got {len(cm)}"
```

**Critical Pain & Offer Embedding Check:**
```python
# Base variants should NOT have pain/offer embedding
for variant in base_variants:
    assert variant['pain_embedded'] == 'false', \
        "Base variant should NOT embed pains"
    assert variant['offer_embedded'] == 'false', \
        "Base variant should NOT embed offers"

# CM variants MUST have pain/offer embedding
for variant in cm_variants:
    assert variant['pain_embedded'] == 'true', \
        "CM variant MUST embed pains"
    assert variant['offer_embedded'] == 'true', \
        "CM variant MUST embed offers"
    assert variant['variant_framework'] in ['PAS', 'Hook-Story-Offer', 'Show Your Work'], \
        f"Invalid framework: {variant['variant_framework']}"
```

**Content Quality Check:**
```python
# Variants should use pains from pain_points_json
pains = json.loads(research['pain_points_json'])[selected_angle]['pains']
for cm_variant in cm_variants:
    for pain in pains:
        # At least one pain should be referenced in variant content
        # (either quoted, paraphrased, or addressed)
        pass

# Offers should appear as CTAs, not offer IDs
for cm_variant in cm_variants:
    assert 'offer_1' not in cm_variant['content'], \
        "Should not expose offer IDs (use natural CTA)"
    # Should have natural call-to-action instead
```

**Comparison to TEXT Mode Test 1.8:**
```
TEXT mode (Test 1.8):
- Exactly 3 variants
- All variant_type = "base"
- No pain_embedded or offer_embedded fields
- No Content Machine frameworks

ROUTINE mode (Test 2.12):
- Exactly 6 variants
- 1 base + 5 CM variants (with cm_ prefix)
- pain_embedded = true/false varies by type
- offer_embedded = true/false varies by type
- Multiple frameworks (PAS, HSO, SYW)
```

**Verification Checklist:**
- [ ] Exactly 6 variants created
- [ ] At least 1 base variant
- [ ] At least 3 CM variants
- [ ] CM variants have specific frameworks
- [ ] Base variants: pain_embedded=false, offer_embedded=false
- [ ] CM variants: pain_embedded=true, offer_embedded=true
- [ ] All variants have unique variant_framework values
- [ ] Character counts valid
- [ ] Pain references in CM variants
- [ ] Natural CTAs (not offer IDs)

**Pass Criteria:**
- Exactly 6 variants
- Correct type distribution
- Pain and offer embedding correct
- All frameworks applied

**Result:** ✅ PASS / ❌ FAIL

---

### Test 2.13: Finalization & Publishing

**Duration:** 10 minutes

**Setup:**
- Completed Test 2.12
- All 6 variants generated and approved
- User at finalization step

**Steps:**
1. User selects: [S] SELECT
2. User chooses: [A] ALL SIX
3. System routes to c-03e-finalize.md
4. System publishes all variants

**Expected Output:**
```
✅ POST FINALIZED (ROUTINE MODE - Full Content Machine Pipeline)

All 6 variants saved to posts_content.csv:
├─ Variant 1 (Base): Ready
├─ Variant 2 (PAS Framework): Ready
├─ Variant 3 (Hook-Story-Offer): Ready
├─ Variant 4 (Show Your Work): Ready
├─ Variant 5 (PAS Alt): Ready
└─ Variant 6 (HSO Alt): Ready

Content Machine Summary:
├─ Pain points embedded: 5 variants
├─ Offers integrated: 5 variants
├─ Frameworks applied: PAS, Hook-Story-Offer, Show Your Work
├─ Expected engagement: +35-50%
└─ Conversion opportunity: 3 offers available

[Publish All] [Save Draft] [Back to Menu]
```

**CSV Final Check:**
```
All 6 rows in posts_content.csv:
- All have publish_status = "published"
- No duplicates
- Correct pain/offer embedding
- All frameworks present
```

**Verification Checklist:**
- [ ] 6 rows in posts_content.csv
- [ ] All have publish_status = "published"
- [ ] No duplicate IDs
- [ ] Mix of base (1) and cm_ variants (5)
- [ ] Pain embedding correctly marked
- [ ] Offer embedding correctly marked
- [ ] Frameworks correctly identified

**Complete Test 2 Data Integrity Check:**
```
Ideas: 1 row (ROUTINE/demo)
  - idea_metadata present and valid ✓
Research: 1 row (with pain points)
  - pain_points_json present and valid ✓
  - 8 angles with 3-5 pains each ✓
Posts: 6 variants (mixed types)
  - 1 base variant ✓
  - 5 CM variants ✓
  - Correct pain/offer embedding ✓
State files:
  - offer_filter.csv exists ✓
  - workflow_state.json updated ✓
```

**Pass Criteria:**
- All 6 variants published
- Full Content Machine Pipeline executed
- No data contamination
- All pain points and offers properly integrated

**Result:** ✅ PASS / ❌ FAIL

---

## Part 4: Test Reporting

### Test Report Summary Template

```markdown
# Content Machine Pipeline - QA Test Report

**Test Date:** [DATE]
**Tester:** [NAME]
**Test Duration:** [HOURS]
**System Version:** [VERSION]
**Test Mode(s):** [TEXT / ROUTINE / BOTH]

---

## Executive Summary

| Category | Status | Details |
|----------|--------|---------|
| TEXT Mode | ✅/❌ | [X/9 tests passed] |
| ROUTINE Mode | ✅/❌ | [X/13 tests passed] |
| Error Scenarios | ✅/❌ | [X/4 tests passed] |
| **Overall** | **✅/❌** | **[X/26 tests passed]** |

---

## Test Results Detail

### Part 1: TEXT Mode (Expected: 9 tests)

| Test # | Name | Result | Time | Notes |
|--------|------|--------|------|-------|
| 1.1 | Mode Selection | ✅/❌ | 5min | [Notes] |
| 1.2 | Idea Input | ✅/❌ | 10min | [Notes] |
| 1.3 | Deduplication | ✅/❌ | 5min | [Notes] |
| 1.4 | Research | ✅/❌ | 15min | [Notes] |
| 1.5 | Results Display | ✅/❌ | 10min | [Notes] |
| 1.6 | Angle Selection | ✅/❌ | 5min | [Notes] |
| 1.7 | Draft Generation | ✅/❌ | 10min | [Notes] |
| 1.8 | Variants (3) | ✅/❌ | 15min | [Notes] |
| 1.9 | Finalization | ✅/❌ | 10min | [Notes] |

**TEXT Mode Result:** [PASS / FAIL]

### Part 2: ROUTINE Mode (Expected: 13 tests)

| Test # | Name | Result | Time | Notes |
|--------|------|--------|------|-------|
| 2.1 | Mode Selection | ✅/❌ | 5min | [Notes] |
| 2.2 | Vision AI | ✅/❌ | 10min | [Notes] |
| 2.3 | Content Type | ✅/❌ | 5min | [Notes] |
| 2.4 | Research + Pains | ✅/❌ | 20min | [Notes] |
| 2.5 | Results Display | ✅/❌ | 10min | [Notes] |
| 2.6 | Angle Selection | ✅/❌ | 5min | [Notes] |
| 2.7 | Offer Filter (1st) | ✅/❌ | 10min | [Notes] |
| 2.8 | Offer Filter (2nd) | ✅/❌ | 5min | [Notes] |
| 2.9 | Workflow State | ✅/❌ | 5min | [Notes] |
| 2.10 | Offer Generation | ✅/❌ | 15min | [Notes] |
| 2.11 | Draft with Offers | ✅/❌ | 10min | [Notes] |
| 2.12 | Variants (6) | ✅/❌ | 20min | [Notes] |
| 2.13 | Finalization | ✅/❌ | 10min | [Notes] |

**ROUTINE Mode Result:** [PASS / FAIL]

---

## CSV Data Validation

### ideas_inbox.csv
- [ ] Correct headers
- [ ] TEXT mode row: content_type = evergreen/topical/etc (not demo)
- [ ] ROUTINE mode row: content_type = demo
- [ ] ROUTINE mode row: idea_metadata valid JSON
- [ ] No duplicates
- [ ] All required fields populated

**Validation Result:** ✅ PASS / ❌ FAIL

### ideas_research.csv
- [ ] Correct headers
- [ ] TEXT mode row: NO pain_points_json column
- [ ] ROUTINE mode row: pain_points_json present and valid
- [ ] ROUTINE pains: 3-5 per angle, all angles covered
- [ ] avg_relevance in range 0-100
- [ ] sources_count >= 20

**Validation Result:** ✅ PASS / ❌ FAIL

### posts_content.csv
- [ ] Correct headers
- [ ] TEXT mode: exactly 3 variants, all type='base'
- [ ] ROUTINE mode: exactly 6 variants, 1 base + 5 cm_*
- [ ] TEXT variants: pain_embedded='false', offer_embedded='false'
- [ ] ROUTINE CM variants: pain_embedded='true', offer_embedded='true'
- [ ] All publish_status='published'
- [ ] No duplicate IDs
- [ ] Character counts valid

**Validation Result:** ✅ PASS / ❌ FAIL

### Additional Files
- [ ] user_preferences/offer_filter.csv: Created and valid
- [ ] workflow_state.json: Created and valid JSON

**Validation Result:** ✅ PASS / ❌ FAIL

---

## Issues Found

[List any issues, failures, or anomalies]

### Issue #1
**Severity:** [CRITICAL / HIGH / MEDIUM / LOW]
**Description:** [Detailed description]
**Steps to Reproduce:** [Steps]
**Expected:** [Expected behavior]
**Actual:** [Actual behavior]
**Workaround:** [If any]

---

## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

---

## Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| QA Tester | [Name] | [Date] | [Sig] |
| QA Lead | [Name] | [Date] | [Sig] |
| Development | [Name] | [Date] | [Sig] |

---

**Test Suite:** COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md
**Guide:** TEST-EXECUTION-GUIDE.md
**System:** Content Machine Pipeline
```

---

## Quick Reference: Common Test Checks

### DATA VALIDATION QUICK CHECKS

**After Each Test - Run These Commands:**

```bash
# Validate CSV syntax
python3 COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md --validate-text-mode
python3 COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md --validate-routine-mode

# Check file sizes (should be non-empty)
ls -lh data/ideas_inbox.csv data/ideas_research.csv data/posts_content.csv

# Count CSV rows
wc -l data/ideas_inbox.csv data/ideas_research.csv data/posts_content.csv
```

### CRITICAL FAILURE POINTS (Check These First)

1. **TEXT Mode Test 1.8:** Variant count must be exactly 3
   - If wrong: Check that cm_* variants aren't being created
   - Should only have "base" type

2. **ROUTINE Mode Test 2.4:** pain_points_json must be valid JSON
   - If parsing fails: Check for unescaped quotes
   - Each angle must have 3-5 pains

3. **ROUTINE Mode Test 2.12:** Variant count must be exactly 6
   - 1 base + 5 Content Machine variants
   - If wrong count: Check framework application logic

4. **Routing Logic (Tests 1.6 and 2.6)**
   - TEXT: content_type != "demo" → c-03c directly
   - ROUTINE: content_type == "demo" → c-03b1 first
   - Check CSV read logic

---

**END OF TEST EXECUTION GUIDE**

