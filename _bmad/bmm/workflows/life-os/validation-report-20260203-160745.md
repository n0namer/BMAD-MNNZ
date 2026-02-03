---
validationDate: 2026-02-03
workflowName: life-os
workflowPath: d:\Users\NIKITA\Documents\DEV\katana-vectorbt\_bmad\bmm\workflows\life-os
validationStatus: COMPLETE
completionDate: 2026-02-03
---

# Validation Report: life-os

**Validation Started:** 2026-02-03
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

---

## File Structure & Size

**Folder structure:** PASS
- workflow.md: ✅
- workflow-plan.md: ✅
- steps-c/: ✅
- steps-e/: ✅
- steps-v/: ✅
- data/: ✅
- templates/: ✅

**Step file sizes:**
- step-01-collect-ideas.md: 184 lines (✅ Good)
- step-02-specialist-match.md: 133 lines (✅ Good)
- step-03-consilium.md: 114 lines (✅ Good)
- step-04-scoring.md: 126 lines (✅ Good)
- step-05-integration.md: 147 lines (✅ Good)
- step-06-calendar-sync.md: 119 lines (✅ Good)
- step-01-update-project.md: 106 lines (✅ Good)
- step-02-rescoring.md: 109 lines (✅ Good)
- step-03-kill-project.md: 102 lines (✅ Good)
- step-01-daily-review.md: 87 lines (✅ Good)
- step-02-weekly-review.md: 87 lines (✅ Good)
- step-03-monthly-review.md: 81 lines (✅ Good)

**Data/templates sizes:**
- mcda-methodology.part-02.md: 180 lines (✅ Good)
- mcda-methodology.part-03.md: 180 lines (✅ Good)
- mcda-methodology.part-04.md: 180 lines (✅ Good)
- five-forces-template.part-03.md: 180 lines (✅ Good)
- real-options-guide.part-04.md: 180 lines (✅ Good)
- mcda-methodology.part-01.md: 180 lines (✅ Good)
- real-options-guide.part-01.md: 180 lines (✅ Good)
- real-options-guide.part-02.md: 180 lines (✅ Good)
- real-options-guide.part-03.md: 180 lines (✅ Good)
- stage-gate-mapping.part-04.md: 180 lines (✅ Good)
- stage-gate-mapping.part-03.md: 180 lines (✅ Good)
- stage-gate-mapping.part-02.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-03.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-04.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-05.md: 180 lines (✅ Good)
- stage-gate-mapping.part-01.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-01.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-02.md: 180 lines (✅ Good)
- dfvc-criteria-rubric.part-06.md: 180 lines (✅ Good)
- five-forces-template.part-01.md: 180 lines (✅ Good)
- five-forces-template.part-02.md: 180 lines (✅ Good)
- unit-economics-calculator.part-01.md: 180 lines (✅ Good)
- unit-economics-calculator.part-02.md: 180 lines (✅ Good)
- real-options-guide.part-05.md: 134 lines (✅ Good)
- stage-gate-mapping.part-05.md: 126 lines (✅ Good)
- unit-economics-calculator.part-03.md: 94 lines (✅ Good)
- mcda-methodology.part-05.md: 82 lines (✅ Good)
- five-forces-template.part-04.md: 69 lines (✅ Good)
- strategic-buckets.md: 25 lines (✅ Good)
- workflow-plan.template.md: 23 lines (✅ Good)
- portfolio-health.md: 21 lines (✅ Good)
- bmad-workflow-mapping.md: 18 lines (✅ Good)
- dfvc-criteria-rubric.md: 16 lines (✅ Good)
- stage-gate-mapping.md: 14 lines (✅ Good)
- mcda-methodology.md: 14 lines (✅ Good)
- real-options-guide.md: 14 lines (✅ Good)
- timeline-allocation.md: 13 lines (✅ Good)
- five-forces-template.md: 13 lines (✅ Good)
- integration-patterns.md: 12 lines (✅ Good)
- unit-economics-calculator.md: 12 lines (✅ Good)
- dfvc-criteria-rubric.part-07.md: 12 lines (✅ Good)
- wip-enforcement.md: 11 lines (✅ Good)

**Issues:** None

**Overall:** PASS

## Frontmatter Validation

- step-01-collect-ideas.md: PASS
- step-02-specialist-match.md: PASS
- step-03-consilium.md: PASS
- step-04-scoring.md: PASS
- step-05-integration.md: PASS
- step-06-calendar-sync.md: PASS
- step-01-update-project.md: PASS
- step-02-rescoring.md: PASS
- step-03-kill-project.md: PASS
- step-01-daily-review.md: PASS
- step-02-weekly-review.md: PASS
- step-03-monthly-review.md: PASS

**Violations:**
None

**Overall:** PASS

## Critical Path Violations

### Config Variables (Exceptions)

The following config variables were identified from workflow.md Configuration Loading section.
Paths using these variables are valid even if not relative (they reference post-install output locations):

- user_name
- communication_language
- document_output_language
- bmb_creations_output_folder

### Content Path Violations

| File | Line | Issue | Details |
| ---- | ---- | ----- | ------- |
| (none) | - | - | - |

### Dead Links

| File | Line | Issue | Details |
| ---- | ---- | ----- | ------- |
| (none) | - | - | - |

**Note:** Output files using config variables were correctly skipped during existence checks.

### Module Awareness

No module awareness issues (workflow is in bmm module).

### Summary

- **CRITICAL:** 0 violations (must fix - workflow will break)
- **HIGH:** 0 violations (should fix)
- **MEDIUM:** 0 violations (review)

**Status:** ✅ PASS - No violations

## Menu Handling Validation

- step-01-collect-ideas.md: FAIL (menu: yes)
  - Violations: missing handler section; missing 'halt and wait' instruction
- step-02-specialist-match.md: PASS (menu: yes)
- step-03-consilium.md: PASS (menu: yes)
- step-04-scoring.md: PASS (menu: yes)
- step-05-integration.md: PASS (menu: yes)
- step-06-calendar-sync.md: PASS (menu: no)
- step-01-update-project.md: PASS (menu: yes)
- step-02-rescoring.md: PASS (menu: yes)
- step-03-kill-project.md: PASS (menu: no)
- step-01-daily-review.md: FAIL (menu: yes)
  - Violations: missing handler section; missing 'halt and wait' instruction
- step-02-weekly-review.md: FAIL (menu: yes)
  - Violations: missing handler section; missing 'halt and wait' instruction
- step-03-monthly-review.md: PASS (menu: no)

**Violations:**
- step-01-collect-ideas.md: missing handler section
- step-01-collect-ideas.md: missing 'halt and wait' instruction
- step-01-daily-review.md: missing handler section
- step-01-daily-review.md: missing 'halt and wait' instruction
- step-02-weekly-review.md: missing handler section
- step-02-weekly-review.md: missing 'halt and wait' instruction

**Overall:** FAIL

## Step Type Validation

- step-01-collect-ideas.md: PASS
  - Expected: init; Actual: unknown
- step-02-specialist-match.md: FAIL
  - Expected: middle-standard; Actual: middle-simple
  - Violations: middle-standard should include A/P/C menu
- step-03-consilium.md: FAIL
  - Expected: middle-standard; Actual: middle-simple
  - Violations: middle-standard should include A/P/C menu
- step-04-scoring.md: FAIL
  - Expected: middle-standard; Actual: middle-simple
  - Violations: middle-standard should include A/P/C menu
- step-05-integration.md: FAIL
  - Expected: middle-standard; Actual: middle-simple
  - Violations: middle-standard should include A/P/C menu
- step-06-calendar-sync.md: PASS
  - Expected: final; Actual: final/auto
- step-01-update-project.md: PASS
  - Expected: middle-simple; Actual: middle-simple
- step-02-rescoring.md: PASS
  - Expected: middle-simple; Actual: middle-simple
- step-03-kill-project.md: PASS
  - Expected: final; Actual: validation/auto
- step-01-daily-review.md: PASS
  - Expected: validation/auto; Actual: unknown
- step-02-weekly-review.md: PASS
  - Expected: validation/auto; Actual: unknown
- step-03-monthly-review.md: PASS
  - Expected: validation/auto; Actual: final/auto

**Violations:**
- step-02-specialist-match.md: middle-standard should include A/P/C menu
- step-03-consilium.md: middle-standard should include A/P/C menu
- step-04-scoring.md: middle-standard should include A/P/C menu
- step-05-integration.md: middle-standard should include A/P/C menu

**Overall:** FAIL

## Output Format Validation

**Document Production:** yes
**Template:** workflow-plan.template.md
**Template Type:** structured

**Final Polish Step:** not required for structured template (no polish step found)

**Step-to-Output Mapping:**
- step-01-collect-ideas.md: PASS (outputFile: no, used: False, C saves: True)
- step-02-specialist-match.md: PASS (outputFile: no, used: False, C saves: True)
- step-03-consilium.md: PASS (outputFile: no, used: False, C saves: True)
- step-04-scoring.md: PASS (outputFile: no, used: False, C saves: True)
- step-05-integration.md: PASS (outputFile: no, used: False, C saves: True)
- step-06-calendar-sync.md: PASS (outputFile: no, used: False, C saves: True)
- step-01-update-project.md: PASS (outputFile: no, used: False, C saves: True)
- step-02-rescoring.md: PASS (outputFile: no, used: False, C saves: True)
- step-03-kill-project.md: PASS (outputFile: no, used: False, C saves: True)
- step-01-daily-review.md: PASS (outputFile: no, used: False, C saves: True)
- step-02-weekly-review.md: PASS (outputFile: no, used: False, C saves: True)
- step-03-monthly-review.md: PASS (outputFile: no, used: False, C saves: True)

**Issues Identified:**
None

**Overall Status:** PASS

## Validation Design Check
**Validation required:** No (operational/creative workflow; no compliance/safety gates).

**Validation steps found (steps-v/):**
- step-01-daily-review.md
- step-02-weekly-review.md
- step-03-monthly-review.md

**Validation step quality:** N/A (review cadence steps, not formal validation gates).

**"DO NOT BE LAZY" language:** N/A (not a validation-gate workflow).

**Critical flow segregation:** Steps-v/ exists and is segregated; appropriate.

**Validation data files:** Present in data/ (MCDA, stage-gate, portfolio health, etc.), but not required for formal validation.

**Issues identified:** None.

**Overall status:** PASS (validation not critical; review steps exist and segregated).

## Instruction Style Check

**Workflow domain:** intent-based (personal planning / facilitation)
**Expected style:** intent-based

**Per-step classification:**
- step-01-collect-ideas.md: intent-based (PASS)
- step-02-specialist-match.md: intent-based (PASS)
- step-03-consilium.md: intent-based (PASS)
- step-04-scoring.md: intent-based (PASS)
- step-05-integration.md: intent-based (PASS)
- step-06-calendar-sync.md: intent-based (PASS)
- step-01-update-project.md: intent-based (PASS)
- step-02-rescoring.md: intent-based (PASS)
- step-03-kill-project.md: intent-based (PASS)
- step-01-daily-review.md: intent-based (PASS)
- step-02-weekly-review.md: intent-based (PASS)
- step-03-monthly-review.md: intent-based (PASS)

**Issues Identified:**
None

**Positive Findings:**
Intent-based facilitation language present in 12 steps.

**Overall Status:** PASS

## Collaborative Experience Check

**Workflow goal:** Life & Business Operating System
**User:** Individual managing personal + business projects

**Step-by-Step Analysis:**
**step-01-collect-ideas.md:**
- Question style: Laundry list
- Conversation flow: Natural
- Role clarity: ⚠️
- Status: ⚠️ NEEDS IMPROVEMENT

**step-02-specialist-match.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-03-consilium.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-04-scoring.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-05-integration.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-06-calendar-sync.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-01-update-project.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-02-rescoring.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-03-kill-project.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-01-daily-review.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-02-weekly-review.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**step-03-monthly-review.md:**
- Question style: Progressive
- Conversation flow: Mixed
- Role clarity: ⚠️
- Status: ✅ PASS

**Collaborative Strengths Found:**
- Role reinforcement and facilitation language present across steps.
- Clear progression from idea → consilium → scoring → integration → calendar.

**Collaborative Issues Found:**
- step-01-collect-ideas.md: 5 questions listed (laundry list)

**User Experience Assessment:**
- [x] A collaborative partner working WITH the user
- [ ] A form collecting data FROM the user
- [ ] An interrogation extracting information

**Overall Collaborative Rating:** ⭐⭐⭐⭐
**Status:** ✅ GOOD

## Subprocess Optimization Opportunities
**Total Opportunities:** 3 | **High Priority:** 1 | **Estimated Context Savings:** Medium

### High-Priority Opportunities

**step-04-scoring.md** - Pattern 3 (data ops)
- **Current:** Loads MCDA/stage‑gate guidance inline.
- **Suggested:** Subprocess loads `data/mcda-methodology*.md` and returns only applicable rules.
- **Impact:** Avoids loading large reference files into main context.

### Moderate/Low-Priority Opportunities

- **steps-c/*.md** - Pattern 1 (grep/regex): use a single subprocess to search for past decisions or similar projects, return only matches.
- **steps-v/*.md** - Pattern 4 (parallel): daily/weekly/monthly reviews can be run in parallel when validating historical artifacts.

### Summary by Pattern

- **Pattern 1 (grep/regex):** 1 opportunity
- **Pattern 2 (per-file):** 0 opportunities
- **Pattern 3 (data ops):** 1 opportunity
- **Pattern 4 (parallel):** 1 opportunity

### Implementation Recommendations

**Quick Wins:** Move large data lookups to subprocess (Pattern 3).  
**Strategic:** Parallelize independent checks in reviews (Pattern 4).  
**Future:** Standardize grep/regex helpers for repository-wide scans (Pattern 1).

**Status:** ⚠️ Review recommended

## Cohesive Review
**Overall Assessment:** Good, but needs work before release.

**Flow & Cohesiveness:** Logical progression from idea → specialist match → consilium → scoring → integration → calendar. Voice and tone are consistent across steps.

**Strengths:**
- Clear end‑to‑end arc that maps to the workflow plan.
- Strong role framing and facilitation language.
- Data references (MCDA, stage‑gate) exist and are well organized.

**Weaknesses:**
- Menu handling violations in key steps (missing handler + halt/wait).
- Several middle steps appear to use simple menus where A/P/C expected (per step‑type validation).
- Review steps (daily/weekly) contain menus but lack handler blocks.

**Critical Issues:** None blocking data integrity, but menu handling issues will confuse users and break standard execution flow.

**Recommendation:** **Needs work** — fix menu handling (handlers + halt/wait) and align step types/menus for steps-c middle steps. After fixes, rerun validation.

## Plan Quality Validation
**Plan file:** `workflow-plan.md` (found)  
**Requirements extracted:** 5 sections (Discovery, Classification, Requirements, Design, Tools & Data)

### Implementation Coverage

**Discovery/Vision:** ✅ Implemented (High)  
- workflow.md aligns with goal, users, success criteria.

**Classification:** ⚠️ Partially Implemented (Medium)  
- Module: bmm ✅  
- Tri‑modal: steps-c/e/v present ✅  
- Continuable: no continuation steps ✅  
- Output: plan + project file + decision log — not explicitly enforced in steps ⚠️

**Requirements:** ⚠️ Partially Implemented (Medium)  
- Intent‑based facilitation present ✅  
- “1–2 questions at a time” appears inconsistently ⚠️  
- WIP limit enforcement mentioned in data but not clearly executed in steps ⚠️

**Design:** ✅ Implemented (High)  
- All steps from plan exist and sequence matches design.

**Tools & Data:** ✅ Implemented (High)  
- Data references present in `data/` (MCDA, stage‑gate, portfolio health, integration patterns).

### Implementation Gaps

- Menu handling issues in step-01 and review steps (missing handler + halt/wait).
- Output commitments (decision log/project file) not explicitly guaranteed in step logic.

### Quality Issues

- Several middle steps lack A/P/C menus expected for collaborative refinement.

### Plan‑Reality Alignment

Overall alignment is strong on structure and domain intent, but execution details (menus, explicit output writes) need correction to fully meet plan quality.

**Implementation Score:** ~80%  
**Overall Status:** Partially Implemented (needs fixes to menu handling and output guarantees)

## Summary
**Validation Completed:** 2026-02-03  
**Overall Status:** ❌ FAIL (menu handling + step type issues)

**Step Results:**
- File Structure & Size: ✅ PASS
- Frontmatter Validation: ✅ PASS
- Critical Path Violations: ✅ PASS
- Menu Handling Validation: ❌ FAIL
- Step Type Validation: ❌ FAIL
- Output Format Validation: ✅ PASS
- Validation Design Check: ✅ PASS
- Instruction Style Check: ✅ PASS
- Collaborative Experience Check: ✅ GOOD
- Subprocess Optimization: ⚠️ Review recommended
- Cohesive Review: ⚠️ Needs work
- Plan Quality Validation: ⚠️ Partially Implemented

**Critical Issues (must fix):**
- Menu handling missing handler + halt/wait in step-01-collect-ideas, step-01-daily-review, step-02-weekly-review.

**Warnings (should address):**
- Middle steps (steps-c 02–05) expected A/P/C menus but appear to use simple menus.
- Output commitments (decision log/project file) not explicitly enforced in step logic.

**Key Strengths:**
- Solid end‑to‑end flow aligned with plan (idea → scoring → integration → calendar).
- Strong data reference library in `data/`.
- Consistent facilitation tone.

**Recommendation:** Needs tweaks before use. Fix menu handling and align middle-step menu patterns; then re-run validation.

**Next Steps:**
1. Fix menu handling in the three failing steps.
2. Update steps-c 02–05 to include full A/P/C menus or adjust expected step type.
3. Re-run validation.
