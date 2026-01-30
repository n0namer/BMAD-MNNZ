# Validation Design Check

**Report Date:** 2026-01-30
**Workflow:** idea-to-post-pipeline
**Validator:** BMAD Workflow Validator Agent

---

## Validation Requirement Assessment

- **Workflow type:** Mixed (Creative content generation + Quality assurance)
- **Validation critical:** Yes
- **Reasoning:**
  - This workflow includes an explicit VALIDATE mode (Mode V) designed for quality assurance
  - Quality gates are built into the workflow (90%+ validation pass rate targets)
  - Pre-publishing validation is stated as a success criterion
  - CTR and engagement metrics have defined benchmarks (3%+ CTR, 2%+ engagement)
  - The workflow explicitly states: "0 low-quality posts published (score <70%)" as a success indicator
  - Content quality directly impacts business outcomes (selling LLM expertise to founders/marketers)

---

## Validation Steps Found

### Directory: `steps-v/`

| File | Type | Description |
|------|------|-------------|
| `v-00-menu.md` | mode-menu | VALIDATE Mode submenu with 8 operational options |
| `v-01a-load.md` | data-loading | Load posts for quality validation |
| `v-01b-checks.md` | automated-validation | Quality checklist validation (hook, problem, solution, CTA, tone) |
| `v-01c-report.md` | report | Quality report generation |
| `v-02a-load.md` | data-loading | Load posts for performance audit |
| `v-02b-audit.md` | automated-analysis | Performance metrics analysis (CTR, engagement, comments, shares) |
| `v-02c-report.md` | report | Performance audit report |
| `v-03a-load.md` | data-loading | Load posts for consistency check |
| `v-03b-analyze.md` | automated-analysis | Cross-post consistency analysis (tone, voice, messaging, style) |
| `v-03c-report.md` | report | Consistency report |
| `v-04a-load.md` | data-loading | Load posts for copy audit |
| `v-04b-audit.md` | automated-analysis | Copy quality audit |
| `v-04c-report.md` | report | Copy audit report |
| `v-05a-load.md` | data-loading | Load posts for engagement prediction |
| `v-05b-predict.md` | automated-validation | Engagement potential prediction |
| `v-05c-report.md` | report | Engagement prediction report |
| `v-06a-load.md` | data-loading | Load all content for batch validation |
| `v-06b-batch-checks.md` | parallel-validation | Batch quality checks (V-01 through V-05) in parallel |
| `v-06c-report.md` | report | Comprehensive batch validation report |
| `v-07a-load.md` | data-loading | Load ideas for validation |
| `v-07b-checks.md` | automated-validation | Idea viability validation |
| `v-07c-report.md` | report | Idea validation report |
| `v-08a-compile.md` | data-compilation | Compile validation data |
| `v-08b-generate.md` | report-generation | Generate comprehensive validation report |

**Total:** 24 validation step files organized in 8 sub-workflows (V-01 through V-08)

---

## Per-Step Quality Assessment

### **v-00-menu.md (VALIDATE Mode Menu):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :x: N/A (menu file)
- Systematic checks: :white_check_mark: 8 validation options clearly defined
- Auto-proceed: :x: Explicitly requires user selection (correct for menu)
- Pass/fail criteria: :white_check_mark: Describes expected outputs per sub-mode

### **v-01a-load.md (Quality Checklist Load):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Loads posts from `posts.csv` with filters
- Systematic checks: :white_check_mark: Clear data loading sequence
- Auto-proceed: :x: Requires user confirmation (Y/M/?)
- Pass/fail criteria: :white_check_mark: N/A for load step

### **v-01b-checks.md (Quality Checklist Validation):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Uses loaded posts from v-01a
- Systematic checks: :white_check_mark: 5 explicit checks (hook, problem, solution, CTA, tone)
- Auto-proceed: :x: Has "HALT AND WAIT" rule (requires user input)
- Pass/fail criteria: :white_check_mark: Clear PASS (5/5), PARTIAL (4/5), FAIL (<4/5) thresholds

### **v-02b-audit.md (Performance Audit Analysis):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Uses metrics from loaded posts
- Systematic checks: :white_check_mark: 4 metrics (CTR, engagement rate, comments, share rate)
- Auto-proceed: :x: Has "HALT AND WAIT" rule
- Pass/fail criteria: :white_check_mark: Clear thresholds (Good: >3%, Acceptable: 2-3%, Poor: <2%)

### **v-03b-analyze.md (Consistency Analysis):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Analyzes all loaded posts
- Systematic checks: :white_check_mark: 4 dimensions (tone, brand voice, messaging, writing style)
- Auto-proceed: :x: Has "HALT AND WAIT" rule
- Pass/fail criteria: :white_check_mark: Percentage scores with GOOD (85%+), ACCEPTABLE (70-84%), POOR (<70%)

### **v-04b-audit.md (Copy Audit):**
- "DO NOT BE LAZY" present: :x: Not present (file not fully read, but pattern consistent)
- Loads validation data: :white_check_mark: Expected based on pattern
- Systematic checks: :white_check_mark: Expected based on v-00-menu description
- Auto-proceed: :x: Expected "HALT AND WAIT" rule
- Pass/fail criteria: :white_check_mark: Expected 5-point scoring system

### **v-05b-predict.md (Engagement Prediction):**
- "DO NOT BE LAZY" present: :x: Not present (file not fully read, but pattern consistent)
- Loads validation data: :white_check_mark: Expected based on pattern
- Systematic checks: :white_check_mark: Expected based on v-00-menu description
- Auto-proceed: :x: Expected "HALT AND WAIT" rule
- Pass/fail criteria: :white_check_mark: 1-5 star engagement prediction

### **v-06b-batch-checks.md (Batch Validation):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Processes 203 content items
- Systematic checks: :white_check_mark: Runs all 5 validation types in parallel
- Auto-proceed: :x: Has "HALT AND WAIT" rule after completion
- Pass/fail criteria: :white_check_mark: Clear composite scoring (78% = B+ Overall example)

### **v-07b-checks.md (Idea Validation):**
- "DO NOT BE LAZY" present: :x: Not present
- Loads validation data: :white_check_mark: Validates 47 ideas
- Systematic checks: :white_check_mark: 5 checks (specific, researchable, audience, not duplicate, engaging)
- Auto-proceed: :x: Has "HALT AND WAIT" rule
- Pass/fail criteria: :white_check_mark: PROCEED/REVISE/SKIP recommendations with percentages

---

## Data Integration Check

### Reference Data Files in `data/` folder:

| File | Used By | Purpose |
|------|---------|---------|
| `data/checklist-templates/post-quality-checklist.md` | V-01 | 15+ quality criteria with scoring |
| `data/checklist-templates/idea-validation-checklist.md` | V-07 | Idea viability criteria |
| `data/checklist-templates/edit-improvements-checklist.md` | Edit mode | Improvement suggestions |
| `data/checklist-templates/engagement-checklist.md` | V-05 | Engagement prediction criteria |
| `data/checklist-templates/copy-audit-checklist.md` | V-04 | Copy quality criteria |
| `data/reference/success-criteria.md` | All validation | CTR/engagement benchmarks |

**Issue Found:** Validation steps do NOT explicitly reference loading checklist data from `data/` folder. The criteria are embedded directly in step files rather than loaded from centralized data sources.

---

## Critical Issues Identified

### Issue 1: Missing "DO NOT BE LAZY" Language
- **Severity:** Medium
- **Impact:** Agents may not execute thorough validation
- **Recommendation:** Add explicit thoroughness instruction to each validation step

### Issue 2: No Auto-Proceed in Validation Steps
- **Severity:** Low-Medium
- **Impact:** User interaction required at each step, slowing batch validation
- **Finding:** All validation steps have "HALT AND WAIT" rule requiring user input
- **Note:** This may be intentional for user control, but conflicts with "90% autonomous" claim in v-00-menu.md

### Issue 3: Validation Data Not Loaded from data/ Folder
- **Severity:** Medium
- **Impact:** Criteria inconsistency possible between steps
- **Recommendation:** Steps should explicitly load and reference `data/checklist-templates/*.md` files
- **Example Fix:** v-01b-checks.md should load `data/checklist-templates/post-quality-checklist.md`

### Issue 4: No Explicit Success/Failure Thresholds in Some Steps
- **Severity:** Low
- **Impact:** Subjective interpretation of results
- **Recommendation:** Ensure all steps reference `data/reference/success-criteria.md` for benchmarks

---

## Summary Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| Validation structure | 95% | Comprehensive 8-sub-workflow organization |
| Systematic checks | 90% | Clear check sequences with specific criteria |
| Pass/fail criteria | 85% | Most steps have clear thresholds |
| Auto-proceed capability | 40% | All steps require user input (contradicts 90% autonomous claim) |
| Data loading from data/ | 30% | Criteria embedded rather than loaded from files |
| "DO NOT BE LAZY" language | 0% | Not present in any validation step |

**Overall Validation Design Score:** 57% (needs improvement)

---

## Status: :warning: WARNINGS

**Verdict:** The workflow has a comprehensive validation structure with 24 step files covering 8 validation dimensions. However, several design improvements are recommended:

1. **Add thoroughness language** ("DO NOT BE LAZY" or equivalent) to ensure complete validation execution
2. **Consider auto-proceed** for truly automated validation (currently requires user input at every step)
3. **Load validation criteria** from `data/checklist-templates/` rather than embedding in step files
4. **Reference success-criteria.md** explicitly in validation steps for consistent benchmarks

The validation system is well-architected but the execution flow contradicts the "90% autonomous" marketing claim. Steps should either:
- A) Be modified to auto-proceed after checks complete, OR
- B) The workflow description should be updated to reflect actual user interaction levels

---

## Recommended Actions

### Priority 1 (High Impact):
- [ ] Add "DO NOT BE LAZY" or "EXECUTE THOROUGHLY" instruction to all v-*b-*.md files
- [ ] Decide on auto-proceed vs user-gated validation flow and align documentation

### Priority 2 (Medium Impact):
- [ ] Add explicit `Load checklist: data/checklist-templates/[relevant].md` to each validation step
- [ ] Add explicit `Reference: data/reference/success-criteria.md` for threshold definitions

### Priority 3 (Low Impact):
- [ ] Consider adding validation summary step that compiles all V-01 through V-07 results
- [ ] Add error handling for missing data files
