# Content Machine Pipeline - QA Test Suite Summary

**Complete Testing Package for Content Machine Pipeline**
**Delivered by:** FIXER AGENT 6 - Data Flow Testing & Validation
**Date:** 2026-01-30

---

## 📋 What You Have

This is a **production-ready QA test suite** with everything needed to validate the Content Machine Pipeline.

### Deliverables

| File | Purpose | Usage |
|------|---------|-------|
| **COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md** | Complete test specifications (30+ tests) | Reference for all test details |
| **TEST-EXECUTION-GUIDE.md** | Step-by-step instructions for testers | Follow this to run tests |
| **validate_data_flow.py** | Automated validation script | Run after tests to verify data |
| **QA-TEST-SUITE-SUMMARY.md** | This file - quick reference | Overview and getting started |

---

## 🎯 Test Coverage

### Scenario 1: TEXT Mode (9 Tests)
✅ **Simple text input** → Research → Single angle → **3 variants** → Publish

**What's tested:**
- Mode selection (TEXT option)
- Raw text idea input
- Deduplication check
- Research execution (NO pain generation)
- Angle selection and routing (directly to draft)
- Draft creation
- **3 variant generation** (critical count)
- Finalization and publishing

**Data validation:**
- ✅ No pain_points_json column
- ✅ No offer_filter.csv created
- ✅ Exactly 3 variants
- ✅ All variant_type = "base"
- ✅ No pain/offer embedding

**Expected Duration:** 2-3 hours

---

### Scenario 2: ROUTINE Mode (13 Tests)
✅ **Screenshot upload** + Vision AI → Research with auto-generated pains → Offer filter → Offer generation → **6 variants** → Publish

**What's tested:**
- Mode selection (ROUTINE option)
- Screenshot upload and Vision AI extraction
- Content type auto-selection (demo)
- Research with pain point generation (Section 2.5)
- Pain points display with research results
- Angle selection and routing (to c-03b1, NOT c-03c)
- Offer filter setup (first run and subsequent)
- Offer generation
- Draft with offer context
- **6 variant generation** (critical count: 1 base + 5 Content Machine)
- Finalization and publishing

**Data validation:**
- ✅ idea_metadata valid JSON with 4 fields
- ✅ pain_points_json present and valid
- ✅ 3-5 pains per angle
- ✅ offer_filter.csv created
- ✅ workflow_state.json with offers
- ✅ Exactly 6 variants
- ✅ Correct pain/offer embedding per variant type

**Expected Duration:** 3-4 hours

---

### Error Scenarios (4 Tests)
✅ **Duplicate handling, missing data, unwanted offers, mode mixing**

**What's tested:**
- Duplicate idea detection and user options
- Missing pain points error detection
- Offer filter validation (no unwanted offers)
- Cross-mode contamination prevention

**Expected Duration:** 1-2 hours

---

## 📊 Test Structure

### Quick Reference: Text Mode (Tests 1.1-1.9)

```
1.1: Mode Selection          → User selects [T]
1.2: Idea Input & Validate  → Save to ideas_inbox.csv
1.3: Dedup Check            → Confirm no duplicates
1.4: Research Execute       → Find 5-8 angles (NO pains)
1.5: Results Display        → Show angles (NO pain section)
1.6: Angle Selection        → Route to c-03c (NOT c-03b1)
1.7: Draft Generation       → Create base draft
1.8: Variant Generation     → Create 3 variants (EXACTLY 3)
1.9: Finalization           → Publish all 3
```

**Critical Counts:**
- 1 idea in ideas_inbox.csv
- 1 research row (NO pain_points_json)
- **3 variants** (EXACT count)

---

### Quick Reference: Routine Mode (Tests 2.1-2.13)

```
2.1: Mode Selection         → User selects [R]
2.2: Vision AI Processing   → Extract metadata
2.3: Content Type Auto      → Set to "demo"
2.4: Research + Pains       → Find angles + generate 3-5 pains each
2.5: Results Display        → Show angles WITH pain sections
2.6: Angle Selection        → Route to c-03b1 (offer check)
2.7: Offer Filter (1st)     → Setup user preferences
2.8: Offer Filter (2nd)     → Load existing preferences
2.9: Workflow State         → Store state in JSON
2.10: Offer Generation      → Generate 2-4 offers
2.11: Draft with Offers     → Create draft with offer hooks
2.12: Variant Generation    → Create 6 variants (1 base + 5 CM)
2.13: Finalization          → Publish all 6
```

**Critical Counts:**
- 1 idea in ideas_inbox.csv (with idea_metadata)
- 1 research row (WITH pain_points_json)
- 8 angles with 3-5 pains each
- 2-4 generated offers
- **6 variants** (EXACT count: 1 base + 5 cm_*)

---

## 🚀 Getting Started

### Step 1: Prepare Environment (15 minutes)

```bash
# Create test directory
mkdir -p D:\test-content-machine\data
mkdir -p D:\test-content-machine\user_preferences

# Copy CSV headers
# See TEST-EXECUTION-GUIDE.md → Part 1: Environment Setup
```

### Step 2: Choose Your Test Path

**Option A: Quick Test (TEXT mode only)**
- Time: 2-3 hours
- Tests: 1.1-1.9 (9 tests)
- For: Testing basic pipeline without special features
- Run: `pytest tests/text-mode/ -v`

**Option B: Full Test (ROUTINE mode only)**
- Time: 3-4 hours
- Tests: 2.1-2.13 (13 tests)
- For: Testing Content Machine features
- Run: `pytest tests/routine-mode/ -v`

**Option C: Complete Test (Both modes)**
- Time: 6-8 hours
- Tests: 1.1-1.9 + 2.1-2.13 + Error scenarios (26 tests)
- For: Full validation before production
- Run: `pytest tests/ -v`

### Step 3: Execute Tests

Follow **TEST-EXECUTION-GUIDE.md** for detailed steps.

Each test has:
- ✅ Objective and setup
- ✅ Step-by-step instructions
- ✅ Expected output
- ✅ CSV validation checks
- ✅ Pass/fail criteria

### Step 4: Validate Data

After completing tests, run the validation script:

```bash
# For TEXT mode only
python3 validate_data_flow.py --mode text --data-dir D:\test-content-machine\data

# For ROUTINE mode only
python3 validate_data_flow.py --mode routine --data-dir D:\test-content-machine\data

# For both modes
python3 validate_data_flow.py --mode both --data-dir D:\test-content-machine\data
```

**Script checks:**
- ✅ CSV schemas
- ✅ Numeric field ranges
- ✅ TEXT mode data integrity
- ✅ ROUTINE mode data integrity
- ✅ Pain point structure
- ✅ Variant counts
- ✅ Pain/offer embedding

---

## 🔑 Critical Test Points

### TEXT Mode - Don't Miss These

| Check | Expected | Why Critical |
|-------|----------|-----------|
| **Variant Count** | Exactly 3 | System must NOT create 6 for TEXT |
| **Variant Type** | All "base" | No Content Machine variants |
| **pain_points_json** | ABSENT | TEXT mode doesn't generate pains |
| **Routing** | c-03c direct | Skip offer filters (c-03b1/b2) |
| **offer_filter.csv** | NOT created | TEXT mode doesn't need offers |

**If any fails:** Content Machine algorithm activated for wrong mode

---

### ROUTINE Mode - Don't Miss These

| Check | Expected | Why Critical |
|-------|----------|-----------|
| **Variant Count** | Exactly 6 | 1 base + 5 Content Machine |
| **Pain Points** | 3-5 per angle | Auto-generated for demos |
| **Offers** | 2-4 generated | Specific to routine + angle |
| **Routing** | c-03b1 first | Must set offer filter |
| **Variant Types** | 1 base + 5 cm_* | Framework application critical |
| **Pain Embedding** | true for CM | Content Machine features |
| **Offer Embedding** | true for CM | Natural CTAs in text |

**If any fails:** Content Machine features not activating

---

## 📈 Quick Check: CSV Structure

### After TEXT Mode Tests (Expected)

```
ideas_inbox.csv:
  1 row: content_type="evergreen", source="user_input", NO idea_metadata

ideas_research.csv:
  1 row: 8 angles, avg_relevance=86, NO pain_points_json

posts_content.csv:
  3 rows: all variant_type="base", pain_embedded="false", offer_embedded="false"

Additional files:
  - user_preferences/offer_filter.csv: ❌ NOT created
  - workflow_state.json: ❌ NOT created
```

---

### After ROUTINE Mode Tests (Expected)

```
ideas_inbox.csv:
  1 row: content_type="demo", source="routine", idea_metadata=valid_json

ideas_research.csv:
  1 row: 8 angles, avg_relevance=86, pain_points_json=valid_json with all 8 angles

posts_content.csv:
  6 rows: 1 base + 5 cm_*, pain_embedded varies by type, offer_embedded varies by type

Additional files:
  - user_preferences/offer_filter.csv: ✅ Created with 5 offer types
  - workflow_state.json: ✅ Created with offers list
```

---

## 🛠️ Tools Provided

### 1. COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md
**What it is:** Complete specifications for all 26+ tests

**Contains:**
- Test data sets (JSON examples)
- Detailed test steps for each test
- CSV validation examples (pseudo-code)
- Error scenario descriptions
- Validation scripts (Python)

**When to use:**
- Reference for test details
- Understand what each test checks
- Debug failures (specs show expected values)

**Example usage:**
```
"Test 1.8: Variant Generation - TEXT Mode"
→ Read this for expected character counts
→ Read CSV validation for exactly 3 variants
→ Check pseudo-code for variant_type="base"
```

---

### 2. TEST-EXECUTION-GUIDE.md
**What it is:** Step-by-step instructions for QA testers

**Contains:**
- Environment setup (5 minutes)
- 26 detailed test procedures
- Expected output for each test
- CSV checks after each test
- Verification checklists
- Test report template

**When to use:**
- Actually running the tests
- See what to click/enter at each step
- Know exactly what to check

**Example usage:**
```
Test 1.8: Variant Generation
Step 1: User confirms draft selection
Step 2: System routes to c-03d-variants.md
Step 3: [Expected Output shown] ← Verify you see this
Step 4: [CSV Check shown] ← Verify CSV has this data
Step 5: [Verification Checklist] ← Check all boxes
Pass Criteria: [Shown] ← If all checked, test PASSES
```

---

### 3. validate_data_flow.py
**What it is:** Automated Python script to validate all CSV data

**Validates:**
- CSV column schemas
- Numeric field ranges
- TEXT mode data integrity (9 checks)
- ROUTINE mode data integrity (13 checks)
- Pain point structure
- Variant counts and types
- Pain/offer embedding correctness

**How to run:**
```bash
# After TEXT mode tests
python3 validate_data_flow.py --mode text --data-dir D:\test-content-machine\data

# After ROUTINE mode tests
python3 validate_data_flow.py --mode routine --data-dir D:\test-content-machine\data

# After both
python3 validate_data_flow.py --mode both --data-dir D:\test-content-machine\data
```

**Output:**
```
Validation Report:
✅ ideas_inbox.csv valid (1 rows, correct schema)
✅ ideas_research.csv valid (pain_points_json valid JSON)
✅ posts_content.csv valid (6 variants, correct types)
✅ TEXT mode data integrity: PASS
✅ ROUTINE mode data integrity: PASS
```

---

## 🎓 Training for QA Team

### 1-Hour Quick Briefing

**For new QA team members:**

```markdown
# Content Machine Pipeline: 10-Minute Explainer

## What is it?
System that converts ideas into blog posts using two different modes.

## TEXT Mode (Simple)
1. User types idea (e.g., "AI is fast")
2. System researches and finds angles
3. System creates 3 blog post variants
4. User publishes

## ROUTINE Mode (Advanced)
1. User uploads screenshot + description
2. System uses Vision AI to extract context
3. System researches and ALSO generates pain points
4. System generates selling offers
5. System creates 6 blog post variants (3 base + 3 with pain/offer)
6. User publishes

## Critical Difference
TEXT mode: 3 variants, NO pains, NO offers
ROUTINE mode: 6 variants, WITH pains, WITH offers

## Your Job
Make sure both modes work correctly and don't mix data.
```

### How to Run Your First Test (15 minutes)

1. Read: TEST-EXECUTION-GUIDE.md → Part 1 (setup) - 5 min
2. Read: TEST-EXECUTION-GUIDE.md → Test 1.1 (mode selection) - 5 min
3. Do: Follow Test 1.1 steps - 5 min
4. Check: See if you got expected output
5. Pass: Move to Test 1.2

---

## 📊 Success Metrics

### Test Execution Metrics

| Metric | Target | How to Measure |
|--------|--------|--------|
| **Execution Time** | TEXT: 2-3h, ROUTINE: 3-4h | Clock time from start to finish |
| **Pass Rate** | 100% (26/26 tests) | Count passed vs total tests |
| **Data Integrity** | 0 errors, <5 warnings | Run validate_data_flow.py |
| **Coverage** | 100% (both modes tested) | Both TEXT and ROUTINE completed |

### Quality Metrics

| Metric | Target | How to Check |
|--------|--------|-----------|
| **CSV Accuracy** | 100% rows correct | Compare CSV to expected (in guide) |
| **Variant Counts** | TEXT: 3, ROUTINE: 6 | Exact, no more no less |
| **Pain Points** | 3-5 per angle, all 8 angles | Count rows in pain_points_json |
| **No Contamination** | 0 cross-mode mixing | TEXT has no pains, ROUTINE has pains |

---

## 🔴 Red Flags (Failures)

**Stop testing if you see these:**

1. ❌ **TEXT Mode showing 6 variants instead of 3**
   - Means: Content Machine always active (should be mode-dependent)
   - Action: Bug in mode detection logic

2. ❌ **ROUTINE Mode generating no pain points**
   - Means: Section 2.5 not executing
   - Action: Vision AI extraction or pain generation broken

3. ❌ **Variant count is neither 3 nor 6**
   - Means: Variant generation logic broken
   - Action: Check framework application

4. ❌ **TEXT Mode created offer_filter.csv**
   - Means: System offering filters for simple mode (wrong)
   - Action: Mode routing broken

5. ❌ **CSV data doesn't match specs**
   - Means: Data validation failed
   - Action: Check CSV save logic

**What to do:**
1. Document the exact issue
2. Note which test failed
3. Save CSV files (evidence)
4. Report to development team
5. Do NOT continue testing until fixed

---

## 📋 Test Report Template

Use this after completing tests:

```markdown
# QA Test Report - Content Machine Pipeline

**Date:** [Date]
**Tester:** [Name]
**Duration:** [X hours]
**Mode Tested:** [TEXT / ROUTINE / BOTH]

## Summary
- Total Tests: [X]
- Passed: [X] ✅
- Failed: [X] ❌
- Success Rate: [X%]

## Test Results

### TEXT Mode
- Tests 1.1-1.9: ✅ PASS (or list failures)
- Variant Count: ✅ 3 (exact)
- Pain Points: ✅ None (correct)

### ROUTINE Mode
- Tests 2.1-2.13: ✅ PASS (or list failures)
- Variant Count: ✅ 6 (exact)
- Pain Points: ✅ Present and valid

### Data Validation
- CSV Schemas: ✅ PASS
- Numeric Ranges: ✅ PASS
- Data Integrity: ✅ PASS

## Issues Found
[List any issues]

## Sign-Off
Tester: ________________
Date: ________________
```

---

## 📞 Support & Questions

### Common Questions

**Q: How long will this take?**
A: TEXT only = 2-3 hours, ROUTINE only = 3-4 hours, Both = 6-8 hours

**Q: Can I run tests in parallel?**
A: Not recommended - each test modifies CSV files. Run sequentially.

**Q: What if a test fails?**
A: Document the failure, save CSVs, report to dev team. Don't skip to next test.

**Q: Do I need to clear data between modes?**
A: Yes - use separate test directory for TEXT vs ROUTINE, or clear CSVs manually.

**Q: What if validation script shows errors?**
A: The error message shows which CSV row/field is wrong. Fix the issue and re-run.

---

## 📚 Document Navigation

```
QA-TEST-SUITE-SUMMARY.md (← You are here)
├─ Quick overview and getting started
├─ Points to TEST-EXECUTION-GUIDE.md for detailed steps
└─ Points to COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md for specifications

TEST-EXECUTION-GUIDE.md
├─ Step-by-step test procedures
├─ Environment setup
├─ 26 detailed test instructions
├─ Expected outputs and CSV checks
└─ Test report template

COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md
├─ Complete test specifications
├─ Test data sets
├─ CSV validation examples
├─ Error scenarios
├─ Python validation scripts
└─ Detailed data validation logic

validate_data_flow.py
└─ Automated validation script (run after tests)
```

---

## ✅ Pre-Test Checklist

Before starting tests, verify:

- [ ] Test directory created (D:\test-content-machine\)
- [ ] CSVs initialized with headers
- [ ] Claude Flow system running
- [ ] Vision API available (for ROUTINE tests)
- [ ] Web search capability working
- [ ] Python 3 installed (for validation script)
- [ ] All three markdown files accessible
- [ ] Python script (validate_data_flow.py) in test directory

---

## 🎉 You're Ready!

You now have:
- ✅ Complete test specifications (COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md)
- ✅ Step-by-step execution guide (TEST-EXECUTION-GUIDE.md)
- ✅ Automated validation script (validate_data_flow.py)
- ✅ This summary and quick reference (QA-TEST-SUITE-SUMMARY.md)

**Next step:** Read TEST-EXECUTION-GUIDE.md Part 1 to set up your environment.

**Questions?** Refer to the specific document for details - everything is documented with examples.

---

**Test Suite v1.0**
**Created:** 2026-01-30
**For:** QA Team
**Ready to Execute:** YES ✅

