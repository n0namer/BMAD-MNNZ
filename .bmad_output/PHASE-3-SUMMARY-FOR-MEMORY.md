# Phase 3 Test Deferral Planning - Summary for Global Memory

**Date:** 2026-03-01
**Project:** BMAD-MNNZ (katana-vectorbt)
**Status:** ✅ PLANNING COMPLETE
**Deliverables:** 3 comprehensive planning documents

---

## Quick Summary

**53 failing tests** identified and categorized into 6 groups with priority assessment.

### Key Numbers
- **32 FAILED tests** (known issues, debuggable)
- **21 ERROR tests** (missing fixtures, setup issues)
- **Estimated fix time:** 8-10 hours total
- **Recommended phases:** 3 phases over 7 days
- **Success metrics:** 100% of 53 tests passing

### Test Breakdown by Priority & Component

| Group | Component | Count | Priority | Time | Status |
|-------|-----------|-------|----------|------|--------|
| 1 | Callback Manager | 11 | HIGH | 2-3h | [ ] |
| 2 | Dashboard Panels | 19 | MEDIUM | 3-4h | [ ] |
| 3 | Position Sizing | 1 | MEDIUM | 1-2h | [ ] |
| 4 | Imports & Deps | 2 | MEDIUM | 1-2h | [ ] |
| 5 | Build Config | 1 | LOW | 0.5h | [ ] |
| 6 | Infrastructure | 21 | LOW | 3-4h | [ ] |
| **TOTAL** | **All components** | **55** | **Mixed** | **11-15h** | **[ ]** |

---

## Three Comprehensive Documents Created

### 1. PHASE-3-TEST-ROADMAP.md (18 KB)
**Purpose:** Strategic overview and scheduling
**Contains:**
- Executive summary
- Complete test categorization with root cause analysis
- 3-phase implementation timeline (Days 1-7)
- Dependency graph and critical path
- Risk assessment and mitigation strategies
- Success criteria per group
- BMAD skills required per group
- Recommended workflow: bmad-tea-testarch-test-design

**Key Feature:** Groups tests by component impact and provides 3-day + 4-day phased approach

### 2. PHASE-3-QUICK-START.md (13 KB)
**Purpose:** Day 1 execution guide with first 5 tests
**Contains:**
- Why these 5 tests first (lowest complexity, highest momentum)
- Detailed step-by-step fix for each of 5 tests:
  1. Kelly Criterion Import (30 min)
  2. GitHub Actions Workflow (20 min)
  3. Poetry Build Backend (15 min)
  4. Position Sizing Constraint (45 min)
  5. Callback Manager Async (45 min)
- 3-day execution plan with hourly breakdown
- Success metrics per day
- Debugging tips
- Progress tracking template

**Key Feature:** Actionable, immediate fixes with copy-paste ready code

### 3. PHASE-3-IMPLEMENTATION-CHECKLIST.md (32 KB)
**Purpose:** Comprehensive line-by-line fix reference for all 55 tests
**Contains:**
- Every failing test with:
  - File location and line number
  - Exact error message
  - Root cause analysis
  - Fix location in source code
  - Copy-paste ready fix code
  - Verification command
  - Status checkbox
- Organized by group (1-6)
- Summary statistics table
- Progress tracking section

**Key Feature:** No guessing - every test has exact fix location and code

---

## Recommended Execution Sequence

### Phase 3-A: Foundation (Days 1-2) → 15 tests (28%)
1. **Day 1:** Groups 1, 4, 5 (Callbacks, Imports, Config)
   - 11 callback tests (Group 1)
   - 2 import tests (Group 4)
   - 1 build test (Group 5)
   - Result: 14/53 passing

2. **Day 2:** Group 3 (Position Sizing) - 1 test
   - Result: 15/53 passing

### Phase 3-B: Features (Days 2-4) → 20 tests (38%)
1. **Days 2-4:** Group 2 (Dashboard Panels - 19 tests)
   - Depends on Group 1 (callbacks) working first
   - Result: 35/53 passing

### Phase 3-C: Infrastructure (Days 4-7) → 21 tests (40%)
1. **Days 4-7:** Group 6 (Story Acceptance - 21 tests)
   - Can run in parallel with Group 2
   - Requires documentation creation + CI/CD setup
   - Result: 56/53 passing (all done)

**Critical Path:** Group 1 → Group 2 → Group 3 → Full Validation
**Optional Path:** Group 6 (CI/Infrastructure) runs in parallel with Group 2

---

## BMAD Skills Recommended

All tests use primary skill: **bmad-tea-testarch-test-design**
- Test Design Architecture workflow
- Focus on understanding test requirements
- Analyze failures systematically
- Implement fixes to match test expectations
- Validate with test suite

Optional secondary: **bmad-bmm-qa-automate** (for Group 6 CI/CD setup)

---

## How to Use These Documents

1. **Start with PHASE-3-QUICK-START.md**
   - First 5 tests are quick wins
   - Builds momentum and understanding
   - ~2.5 hours to first checkpoint

2. **Refer to PHASE-3-TEST-ROADMAP.md**
   - For strategic overview
   - To understand dependencies
   - To stay on schedule
   - To track overall progress

3. **Use PHASE-3-IMPLEMENTATION-CHECKLIST.md**
   - When fixing each test
   - For exact line numbers and fixes
   - To verify you're in right location
   - To copy code directly

---

## Key Success Factors

### 1. Start with Group 1 (Callbacks)
- Foundation for all other fixes
- Relatively small group (11 tests)
- All tests follow same pattern
- Builds understanding of test framework

### 2. Keep Implementation Narrow
- Focus on making tests pass
- Don't over-engineer
- Fix exactly what test expects
- Verify with `pytest -v` after each fix

### 3. Use Checklist Religiously
- Follow exact line numbers
- Copy code patterns provided
- Mark tests as completed
- Track progress hourly

### 4. Test in Isolation First
- Test one fix at a time
- Run individual test: `pytest path::test::name -v`
- Then run full group
- Finally run all tests

---

## Critical Dependencies & Blockers

### Must-Complete First
- Group 1: Callback Manager (blocks Group 2)
- Event object standardization (blocks all dashboard tests)

### Can Run in Parallel
- Group 3 (Position Sizing) - independent
- Group 4 (Imports) - independent
- Group 5 (Config) - independent
- Group 6 (Infrastructure) - independent

### Will Need External Support
- Group 6 tests may need GitHub API access
- Security tests may need tool setup (bandit, etc.)
- CI tests may need poetry.lock generation

---

## Metrics & Validation

### Success Criteria (All Required)
- ✓ 55/55 tests passing
- ✓ Test coverage > 90%
- ✓ No integration failures
- ✓ No performance regressions
- ✓ All documentation complete
- ✓ CI/CD pipeline green

### Verification Commands
```bash
# After fixing each group:
python -m pytest src/tests/test_group_name.py -v

# After each phase:
python -m pytest src/tests/ -v --tb=short

# Check coverage:
python -m pytest src/tests/ --cov=src/bmad --cov-report=term-missing
```

---

## Document Locations

**All files saved to:** `d:/Users/NIKITA/Documents/DEV/BMAD-MNNZ/.bmad_output/planning-artifacts/`

1. **PHASE-3-TEST-ROADMAP.md** - Strategic overview
2. **PHASE-3-QUICK-START.md** - First 5 tests guide
3. **PHASE-3-IMPLEMENTATION-CHECKLIST.md** - Complete line-by-line fixes

**Total Documentation:** ~63 KB, fully actionable with exact code snippets

---

## Cross-Project Value

This planning is stored in global memory for potential reuse:
- Test categorization patterns
- Root cause analysis methods
- Fix implementation strategies
- BMAD workflow application

Key learning: Use bmad-tea-testarch-test-design for systematic test debugging.

---

## Next Steps

1. **Immediate:** Review PHASE-3-QUICK-START.md
2. **Day 1 Morning:** Start Test 1 (Kelly Criterion - 30 min)
3. **Day 1 Checkpoint:** 5/53 tests passing
4. **Day 2-3:** Complete Groups 1-3
5. **Day 4-7:** Complete Group 6 (Infrastructure)
6. **Final:** 55/55 tests passing ✓

---

**End of Summary**

*Full planning documentation ready for immediate execution.*
