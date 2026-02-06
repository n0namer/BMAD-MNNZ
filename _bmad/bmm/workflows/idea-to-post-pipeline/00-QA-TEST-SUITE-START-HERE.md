# Content Machine Pipeline - QA Test Suite

**📋 START HERE - Complete Testing Package Ready for Execution**

**Delivered:** 2026-01-30
**By:** FIXER AGENT 6 - QA Testing & Validation
**Status:** ✅ Production Ready

---

## 🎯 What You Have

A **complete, ready-to-execute QA test suite** with everything needed to validate the Content Machine Pipeline across two distinct scenarios:

### The Package

| Document | Size | Purpose |
|----------|------|---------|
| **📋 QA-TEST-SUITE-SUMMARY.md** | 17 KB | **START HERE** - Overview, quick reference, getting started |
| **📝 TEST-EXECUTION-GUIDE.md** | 42 KB | Step-by-step instructions for 26 tests (follow this to run tests) |
| **📊 COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md** | 58 KB | Complete specifications, test data, validation logic |
| **🐍 validate_data_flow.py** | 18 KB | Python script to validate CSV data after tests |

---

## 🚀 Quick Start (5 minutes)

### 1. Understand the Two Scenarios

```
TEXT MODE (Simple)
━━━━━━━━━━━━━━━━━━
User types idea
    ↓
System researches (finds 5-8 angles)
    ↓
Creates 3 blog post variants
    ↓
Publish

ROUTINE MODE (Advanced Content Machine)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User uploads screenshot + description
    ↓
Vision AI extracts context
    ↓
System researches AND generates pain points (3-5 per angle)
    ↓
System generates selling offers (2-4 offers)
    ↓
Creates 6 blog post variants (3 base + 3 with pain/offer)
    ↓
Publish
```

### 2. Choose Your Test Path

- **TEXT Mode Only:** 2-3 hours, 9 tests (basic functionality)
- **ROUTINE Mode Only:** 3-4 hours, 13 tests (Content Machine features)
- **Both Modes:** 6-8 hours, 26 tests (complete validation)

### 3. Start Testing

1. Read: **QA-TEST-SUITE-SUMMARY.md** (15 minutes)
2. Follow: **TEST-EXECUTION-GUIDE.md** (actual testing)
3. Validate: Run `validate_data_flow.py` (5 minutes)

---

## 📚 Document Guide

### 1️⃣ QA-TEST-SUITE-SUMMARY.md (Read First!)

**Purpose:** Overview and quick reference

**Contains:**
- What you're testing (30+ tests across 2 scenarios)
- Test structure and timeline
- Critical points for each mode
- Expected CSV structure
- Quick checklist
- Common questions

**Read time:** 15-20 minutes

**When to use:**
- Understand what you're testing
- Quick reference during testing
- Understand why tests matter
- Check expected data structure

**Example section:**
```
TEXT Mode - Don't Miss These:
- Variant Count: Exactly 3
- pain_points_json: ABSENT (no pains for TEXT)
- offer_filter.csv: NOT created
```

---

### 2️⃣ TEST-EXECUTION-GUIDE.md (Follow During Testing)

**Purpose:** Step-by-step testing instructions

**Contains:**
- Environment setup (15 minutes)
- 26 detailed test procedures:
  - Tests 1.1-1.9: TEXT Mode
  - Tests 2.1-2.13: ROUTINE Mode
  - Error scenarios
- For each test:
  - Duration estimate
  - Setup requirements
  - Exact steps to follow
  - Expected output
  - CSV validation checks
  - Verification checklist
  - Pass/fail criteria
- Test report template

**Read/follow time:** 6-8 hours (actual testing)

**When to use:**
- Actually running the tests
- Check what to do at each step
- See expected output
- Verify CSV data after each test

**Example test format:**
```
Test 1.8: Variant Generation (TEXT Mode)

Duration: 15 minutes
Setup: Completed Test 1.7

Test Steps:
1. User confirms draft selection
2. System routes to c-03d-variants.md
3. System generates shorter versions...

Expected Output: [Shown]

CSV Check After Step: [Validation shown]

Verification Checklist:
- [ ] Exactly 3 variants created
- [ ] All have variant_type = "base"
- [ ] Character counts in valid ranges
[... more checks ...]

Pass Criteria: All 3 variants with correct type
Result: ✅ PASS / ❌ FAIL
```

---

### 3️⃣ COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md (Reference)

**Purpose:** Complete specifications and technical details

**Contains:**
- Test data sets (JSON examples)
- Detailed specifications for all tests
- CSV validation logic (pseudo-code)
- Python validation scripts
- Error scenarios and handling
- Data integrity checks

**Read time:** Reference as needed (not front-to-back)

**When to use:**
- Understand test details deeply
- Debug test failures
- Understand validation logic
- See pseudo-code for validation
- Reference data structures

**Example section:**
```
Test 1.8: Variant Generation - TEXT Mode

Expected CSV:
┌──────────┬──────────┬──────┐
│ variant_type │ pain_embedded │ offer_embedded │
├──────────┼──────────┼──────┤
│ base     │ false    │ false │
│ base     │ false    │ false │
│ base     │ false    │ false │
└──────────┴──────────┴──────┘

Validation Logic:
```javascript
const variants = posts_content.filter(...);
assert(variants.length === 3);
variants.forEach(v => {
  assert(v.variant_type === "base");
  assert(v.pain_embedded === "false");
  assert(v.offer_embedded === "false");
});
```
```

---

### 4️⃣ validate_data_flow.py (Run After Tests)

**Purpose:** Automated validation of all CSV data

**What it checks:**
- CSV column schemas
- Numeric field ranges (relevance 0-100, counts > 0)
- TEXT mode: no pains, 3 variants
- ROUTINE mode: pain points valid, 6 variants
- No data contamination

**How to run:**
```bash
# After TEXT tests
python3 validate_data_flow.py --mode text --data-dir D:\test-content-machine\data

# After ROUTINE tests
python3 validate_data_flow.py --mode routine --data-dir D:\test-content-machine\data

# After both
python3 validate_data_flow.py --mode both --data-dir D:\test-content-machine\data
```

**Example output:**
```
CSV Files Loaded:
  - ideas_inbox.csv: 1 rows
  - ideas_research.csv: 1 rows
  - posts_content.csv: 3 rows

VALIDATING TEXT MODE DATA FLOW:
Validating idea 1...
  ✓ Correct variant count: 3

✅ ALL VALIDATIONS PASSED
```

---

## 🎬 How to Test (Step-by-Step)

### Phase 1: Setup (15 minutes)

1. Create test directory:
   ```bash
   mkdir -p D:\test-content-machine\data
   mkdir -p D:\test-content-machine\user_preferences
   ```

2. Create empty CSV files with headers (see TEST-EXECUTION-GUIDE.md)

3. Verify systems ready:
   - [ ] Claude Flow running
   - [ ] Vision API available
   - [ ] Web search working

### Phase 2: Run Tests (2-8 hours depending on mode)

1. Open: **TEST-EXECUTION-GUIDE.md**

2. Follow the tests in order:
   - **TEXT Mode:** Tests 1.1-1.9 (sequential)
   - **ROUTINE Mode:** Tests 2.1-2.13 (sequential)

3. For each test:
   - Read the test section
   - Follow the steps
   - Verify expected output
   - Check CSV data
   - Mark as ✅ PASS or ❌ FAIL
   - Move to next test

### Phase 3: Validate (5 minutes)

```bash
python3 validate_data_flow.py --mode [text|routine|both] \
  --data-dir D:\test-content-machine\data
```

Check output:
- [ ] All validations passed
- [ ] No errors (0 errors shown)
- [ ] Few or no warnings

### Phase 4: Report (10 minutes)

Use TEST-EXECUTION-GUIDE.md test report template to document results.

---

## 📊 Expected Data Structure

### After TEXT Mode Tests

```
Directory: D:\test-content-machine\

data/
  ├─ ideas_inbox.csv (1 row: TEXT mode idea)
  ├─ ideas_research.csv (1 row: NO pain_points_json)
  └─ posts_content.csv (3 rows: all base type, no pain/offer)

user_preferences/
  └─ [empty - not used in TEXT mode]

Characteristics:
✓ pain_points_json: ABSENT
✓ offer_filter.csv: NOT created
✓ Variant count: 3 (exact)
✓ All variants: variant_type="base"
```

---

### After ROUTINE Mode Tests

```
Directory: D:\test-content-machine\

data/
  ├─ ideas_inbox.csv (1 row: ROUTINE mode idea with idea_metadata)
  ├─ ideas_research.csv (1 row: WITH pain_points_json valid JSON)
  └─ posts_content.csv (6 rows: 1 base + 5 cm_* types)

user_preferences/
  └─ offer_filter.csv (5 offer types: willing/unwilling)

Additional:
  └─ workflow_state.json (offers list and state)

Characteristics:
✓ pain_points_json: PRESENT and valid (3-5 pains per angle)
✓ offer_filter.csv: CREATED
✓ workflow_state.json: CREATED with offers
✓ Variant count: 6 (exact: 1 base + 5 cm_*)
✓ CM variants: pain_embedded=true, offer_embedded=true
```

---

## 🔑 Critical Success Points

### TEXT Mode Must Have
- ❌ NO pain_points_json in research
- ❌ NO offer_filter.csv created
- ✅ EXACTLY 3 variants
- ✅ All variant_type = "base"
- ✅ Route directly to c-03c (skip c-03b1/b2)

### ROUTINE Mode Must Have
- ✅ idea_metadata with 4 fields
- ✅ pain_points_json valid JSON
- ✅ 3-5 pains for each angle
- ✅ EXACTLY 6 variants (1 base + 5 cm_*)
- ✅ offer_filter.csv created
- ✅ workflow_state.json with offers
- ✅ Route to c-03b1 first (offer check)

### If Anything Wrong
- ❌ Variant count is 3 for ROUTINE → Content Machine not activating
- ❌ Variant count is 6 for TEXT → Content Machine always on (wrong)
- ❌ TEXT has pain_points_json → Mode detection broken
- ❌ ROUTINE has no pain_points_json → Pain generation broken
- ❌ Routing goes to c-03c for ROUTINE → Skip offer filter logic broken

**Action:** Stop testing, document issue, report to dev team

---

## ✅ Checklist: Are You Ready?

Before you start:
- [ ] Read: QA-TEST-SUITE-SUMMARY.md (this document)
- [ ] Have: TEST-EXECUTION-GUIDE.md accessible
- [ ] Have: COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md available
- [ ] Have: validate_data_flow.py in test directory
- [ ] Created: D:\test-content-machine\data directory
- [ ] Created: D:\test-content-machine\user_preferences directory
- [ ] Initialized: CSV files with headers
- [ ] Verified: Claude Flow system running
- [ ] Verified: Vision API available
- [ ] Verified: Web search working
- [ ] Planned: Testing timeline (2-8 hours)
- [ ] Assigned: QA tester responsible

---

## 📞 Quick Help

### "I don't know what to do"
→ Read **QA-TEST-SUITE-SUMMARY.md** (this document)

### "Show me the exact steps for Test 1.8"
→ Go to **TEST-EXECUTION-GUIDE.md** → Search "Test 1.8"

### "What should the CSV look like?"
→ **TEST-EXECUTION-GUIDE.md** → Each test shows expected CSV

### "I found an error, now what?"
→ **COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md** → Error Scenario Tests (Part 4)

### "My CSV data doesn't match"
→ Run `validate_data_flow.py` to see what's wrong

### "How long will this take?"
→ TEXT: 2-3 hours, ROUTINE: 3-4 hours, BOTH: 6-8 hours

### "Can I test both modes at once?"
→ No, run sequentially or in separate directories (CSV conflicts)

---

## 🎓 For New Team Members

**5-Minute Training:**

This system has TWO modes:

1. **TEXT Mode** - User types idea, system makes 3 blog posts
   - No special features
   - Simple flow: input → research → 3 variants

2. **ROUTINE Mode** - User shows demo, system extracts pain points, creates 6 posts
   - Complex flow: upload → vision AI → pain generation → offers → 6 variants
   - Uses "Content Machine" framework

**Your job:** Make sure both modes work and don't mix up data.

**Critical rule:** TEXT should NEVER create 6 variants. ROUTINE should NEVER skip pain points.

---

## 📈 Success Metrics

| Metric | Target | How to Check |
|--------|--------|-----------|
| All tests pass | 26/26 (100%) | Count passed vs total |
| No errors | 0 errors | Run validate_data_flow.py |
| Correct variants | 3 for TEXT, 6 for ROUTINE | Count CSV rows with idea_id |
| No contamination | 0 cross-mode mixing | TEXT has no pains, ROUTINE has pains |
| On time | 6-8 hours total | Clock from start to validation complete |

---

## 🎉 You're Ready!

**Next Steps:**

1. ✅ You've read this file
2. → Go read: **QA-TEST-SUITE-SUMMARY.md** (detailed overview)
3. → Then follow: **TEST-EXECUTION-GUIDE.md** (actual testing)
4. → Finally run: `validate_data_flow.py` (automatic validation)

---

## 📋 Document Quick Links

All documents are in:
`D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline\`

| File | Size | Purpose |
|------|------|---------|
| `00-QA-TEST-SUITE-START-HERE.md` | ← **You are here** |
| `QA-TEST-SUITE-SUMMARY.md` | 17 KB | Read this next |
| `TEST-EXECUTION-GUIDE.md` | 42 KB | Follow this to test |
| `COMPREHENSIVE-DATA-FLOW-TEST-SUITE.md` | 58 KB | Reference for details |
| `validate_data_flow.py` | 18 KB | Run after testing |

---

**Content Machine Pipeline QA Test Suite**
**Version 1.0 - Production Ready**
**Created:** 2026-01-30
**Status:** ✅ Ready for Execution

