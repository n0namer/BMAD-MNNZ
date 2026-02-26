---
mode: edit
targetWorkflowPath: 'D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md'
workflowName: 'life-os'
editSessionDate: '2026-02-05'
stepsCompleted:
  - step-e-01-assess-workflow.md
  - step-e-02-discover-edits.md (SKIPPED - edit goal already clear)
hasValidationReport: true
validationStatus: COMPLETE (47 warnings, 0 critical)
validationDate: 2026-02-04T23:59:30
---

# Edit Plan: life-os

## Workflow Snapshot

**Path:** D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os
**Format:** BMAD Compliant ✅
**Step Folders:** steps-c/, steps-e/, steps-v/
**Data Folder:** Yes (58 files)
**Templates Folder:** Yes (44 files)

## Validation Status

**Validation Report:** validation-report-20260204-235500.md
- **Status:** COMPLETE ✅
- **Critical Issues:** 0 (all resolved through refactoring)
- **Warnings:** 47 (subprocess optimization opportunities)
- **Key Achievement:** 3 critical file size violations RESOLVED using Subprocess Data Ops Pattern
  - step-04-consilium.md: 585→237 lines ✅
  - step-04.5-triz-analysis.md: 327→242 lines ✅
  - step-08-deep-plan.md: 311→181 lines ✅

**Pattern Used:** Subprocess Data Ops Pattern
- Extract reference content to `data/` files
- JIT loading from step files
- Keeps step files < 250 lines

## New Files Since Validation (Not Yet Validated)

**Foundation Steps (Created 2026-02-05):**
1. step-00.5-project-stage.md (430 lines) ❌ +72% over limit
2. step-00.6-resource-assessment.md (488 lines) ❌ +95% over limit
3. step-00.7-optimization-intelligence.md (522 lines) ❌ +109% over limit
4. step-00-foundation-check.md (414 lines) ❌ +66% over limit

**Total:** 4 files violating BMAD size limit (250 lines max)

---

## Edit Goals

### REQ-019: Refactor Foundation Steps to Meet BMAD Size Limits

**Priority:** 🟡 HIGH (Technical Debt)

**Goal:** Apply same Subprocess Data Ops Pattern used for step-04/04.5/08 to Foundation Steps

**Target Files:**
- [ ] step-00.5-project-stage.md (430 → < 250 lines)
- [ ] step-00.6-resource-assessment.md (488 → < 250 lines)
- [ ] step-00.7-optimization-intelligence.md (522 → < 250 lines)
- [ ] step-00-foundation-check.md (414 → < 250 lines)

**Refactoring Approach:**
1. **Extract to Data Files:**
   - Examples → `data/foundation-examples/`
   - Detailed explanations → `data/foundation-explanations/`
   - Templates and patterns → existing YAML files

2. **Keep in Step Files:**
   - Core execution logic
   - Menu handling
   - User interaction flow
   - Success/failure metrics

3. **Load via Subprocess Pattern:**
   - Reference data files from frontmatter
   - JIT loading when needed
   - Maintain full functionality

**Success Criteria:**
- ✅ All 4 foundation steps < 250 lines (ideally < 200)
- ✅ Full functionality preserved
- ✅ Same user experience
- ✅ Reusable pattern for future steps

**Estimated Time:** 3-4 hours (refactor 4 files in parallel)

---

## User Decision

**[S] Skip to Refactoring** - Selected at 2026-02-05
- Edit goal already clear (REQ-019 from REQUIREMENTS-REGISTRY)
- No additional discovery needed
- Proceeding directly to parallel refactoring

## Edits Applied

### ✅ COMPLETE: REQ-019 Refactoring (4 parallel agents)

**Execution Method:** BMAD edit mode with 4 concurrent Task agents (sonnet model)
**Duration:** 2.5 hours (parallel execution)
**Pattern:** Subprocess Data Ops Pattern (extract to data/, JIT loading)

**Results:**

| Agent | File | Before | After | Reduction | Status |
|-------|------|--------|-------|-----------|--------|
| 1 | step-00.5-project-stage.md | 430 | 248 | -42% | ✅ 1% under |
| 2 | step-00.6-resource-assessment.md | 488 | 245 | -50% | ✅ 2% under |
| 3 | step-00.7-optimization-intelligence.md | 522 | 232 | -56% | ✅ 7% under |
| 4 | step-00-foundation-check.md | 414 | 213 | -49% | ✅ 15% under |

**Total:** 1854 lines → 938 lines (-49% average reduction)

**Data Files Created:**
- `data/foundation-examples/foundation-check-examples.md` (20 KB)
- `data/foundation-examples/optimization-examples.md` (13 KB)
- `data/foundation-examples/project-stage-examples.md` (9.9 KB)
- `data/foundation-examples/resource-assessment-examples.md` (14 KB)

**All Foundation Steps Now BMAD Compliant ✅**

**Completion Date:** 2026-02-05

---

## Phase 2 Edit Goals (Core Workflow Fixes)

**Priority:** 🟡 HIGH
**Requirements:** REQ-010, REQ-011, REQ-012, REQ-013

### REQ-010: Fix Step-02/03 Contradictions
**Target Files:**
- `steps-c/step-02-roles-discovery.md`
- `steps-c/step-03-specialist-match.md`

**Issue:** Instructions say "automatic" but menus present → confusing
**Fix:** Make explicit: "I suggest, you confirm"

### REQ-011: Quality Gates to Prevent Rushing
**Target Files:**
- `steps-c/step-05-scoring.md`
- `steps-c/step-08-deep-plan.md`

**Issue:** No inline validation checkpoints
**Fix:** Add quality checkpoints before menus: "Does this output match expectations? [Y/N]"

### REQ-012: Search Orchestrator Fallback
**Target File:** Create new data file
**Location:** `data/search-orchestrator-fallback.yaml`

**Issue:** Required protocol with no fallback if fails
**Fix:** Add explicit fallback chain: MCP → CLI memory → manual

### REQ-013: Final Polish Step (step-08.5)
**Target File:** Create new step
**Location:** `steps-c/step-08.5-final-polish.md`

**Issue:** No final review step before completion
**Fix:** Add step for coherence review, consistency check, final refinements

---

**Status:** Phase 1 Complete, Starting Phase 2
**Next Step:** Spawn 4 parallel agents for Core Workflow Fixes
