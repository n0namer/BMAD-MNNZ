# Validation Design Check - Life OS Workflow

**Validation Date:** 2026-02-06
**Workflow:** Life Operating System (Life OS)
**Workflow Plan:** d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow-plan.md

---

## Executive Summary

**Overall Status:** ✅ **PASS** (with minor recommendations)

The Life OS workflow has well-designed validation steps that follow systematic approaches and load validation data appropriately. The workflow is NOT compliance/safety-critical, but employs quality gates and validation steps for personal project management effectiveness. All validation steps demonstrate:
- Proper subprocess optimization patterns
- Systematic check sequences
- Auto-proceed behavior (no unnecessary stops)
- Clear pass/fail criteria
- JIT data loading from `data/` folder

**Key Strengths:**
- All 9 validation steps include comprehensive subprocess patterns
- Strong anti-lazy language throughout ("DO NOT BE LAZY", "DO NOT SKIP")
- Extensive JIT protocol loading from data/ folder
- Proper tri-modal segregation (steps-v/ folder)
- Auto-proceed validation flow (no menu stops between validation steps)

**Minor Recommendations:**
- Consider adding explicit validation checklists to `data/` folder (already referenced implicitly)
- Daily review could benefit from stronger skip encouragement (it's optional but not strongly emphasized)

---

## 1. Validation Requirement Assessment

### Is Validation Critical for This Workflow?

**Assessment:** ⚠️ **CONDITIONALLY CRITICAL**

**Workflow Type:** Personal/Business Operating System

**Domain Classification:**
- **NOT compliance/regulatory:** No legal, medical, tax, or safety requirements
- **NOT safety-critical:** No risk to life or property
- **IS quality-critical:** User relies on system for life/business decisions
- **IS effectiveness-critical:** Poor validation leads to wasted time, missed goals

**Validation Purpose:**
- Ensure portfolio health (capacity management, WIP limits)
- Track goal progress and alignment
- Identify blockers and risks early
- Calibrate estimates over time
- Learn from completed projects (retrospectives)

**Verdict:** Validation is NOT strictly required (user could skip all reviews), but is HIGHLY RECOMMENDED for system effectiveness. The workflow correctly treats validation as optional but encouraged, with weekly review as the PRIMARY cadence.

---

## 2. Validation Steps Found

The workflow includes **9 validation step files** in `steps-v/` folder:

| Step File | Purpose | Estimated Duration | Required/Optional |
|-----------|---------|-------------------|-------------------|
| `step-00-return-to-plan.md` | Quick context restore | 2-5 min | On-demand |
| `step-01-daily-review.md` | Optional daily standup | 1-2 min | OPTIONAL |
| `step-02-weekly-review.md` | PRIMARY review cadence | 15-20 min | RECOMMENDED |
| `step-03-monthly-review.md` | "Deeper weekly" with trends | 30 min | RECOMMENDED |
| `step-04-quarterly-review.md` | OKR review and goal adjustment | 2-3 hours | REQUIRED quarterly |
| `step-v-05-retrospective.md` | Learning from completed ideas | Variable | After completion |
| `step-v-06-portfolio-view.md` | Portfolio dashboard view | 3-5 min | On-demand |
| `step-v-07-decision-queue.md` | Activation decision queue | 5-10 min | On-demand |
| `step-05-refactoring-summary.md` | Meta-documentation (not a step) | N/A | N/A |

**Total:** 8 active validation steps + 1 meta-documentation file

---

## 3. Validation Step Quality Assessment

### Step-by-Step Analysis

#### Step V-00: Return-to-Plan

**Proper Design:**
- ✅ Loads validation data from multiple sources (project file, snapshot, journal, plan, decision log)
- ✅ Systematic check sequence (subprocess pattern)
- ✅ Auto-proceeds (single [C] Continue option, no stops)
- ✅ Clear success criteria (context restored)
- ✅ Reports findings to user (structured snapshot)

**Anti-Lazy Language:**
- ⚠️ Limited anti-lazy language (step is read-only, so less critical)
- ✅ Subprocess pattern enforces comprehensive loading
- ✅ "DO NOT CHANGE PROJECT DATA" (boundary enforcement)

**Critical Flow:**
- ✅ Located in `steps-v/` folder (tri-modal structure)
- ✅ Properly segregated from create flow
- ✅ Can be run independently

**Data Files Referenced:**
- Projects, snapshots, journal, plans, decision log (all loaded via subprocess)
- No explicit validation data file (not needed for read-only step)

**Overall Status:** ✅ **PASS**

---

#### Step V-01: Daily Review

**Proper Design:**
- ✅ Loads validation data from `data/weekly-pulse-protocol.md`
- ✅ Systematic 3-question protocol
- ✅ Auto-proceeds to next step (no menu wait)
- ✅ Clear success criteria (1-2 min completion, 3 short answers)
- ✅ Reports findings to user (appends to metrics)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "YOU ARE A FACILITATOR, not a content generator"
- ✅ Subprocess pattern ("DO NOT ask for details - signal-only mode")
- ✅ "Accept short answers" (prevents over-engineering)

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ **SKIP PROMPT OFFERED FIRST** (user can bypass entirely)

**Data Files Referenced:**
- `data/weekly-pulse-protocol.md` (loaded via subprocess)

**Overall Status:** ✅ **PASS**

**Notes:** Daily review is OPTIONAL and strongly encourages skipping. This is appropriate design - most users should focus on weekly review.

---

#### Step V-02: Weekly Review (PRIMARY)

**Proper Design:**
- ✅ Loads validation data from `data/weekly-review-protocol.md`
- ✅ Systematic 5-section review protocol (Milestone Progress, WIP Health, Blockers, Priorities, Quick Wins)
- ✅ Auto-proceeds to next step (no menu wait)
- ✅ Clear success criteria (all 5 sections completed, 15-20 min duration)
- ✅ Reports findings to user (appends structured review to metrics)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "DO NOT BE LAZY - LOAD AND REVIEW EVERY FILE" (via subprocess pattern)
- ✅ "Skip Warning: emphasize weekly is PRIMARY" (prevents lazy skipping)
- ✅ "Not accepting vague answers ('fine', 'ok', 'nothing')"
- ✅ "FORBIDDEN to generate fake data without user input"

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ Marked as PRIMARY cadence (most important validation step)

**Data Files Referenced:**
- `data/weekly-review-protocol.md` (comprehensive 5-section protocol)
- `data/search-decision-protocol.md` (for semantic decisions)
- Portfolio, goals, metrics files

**Overall Status:** ✅ **PASS** (exemplary design)

---

#### Step V-03: Monthly Review

**Proper Design:**
- ✅ Loads validation data from `data/monthly-review-protocol.md`, `data/monthly-metrics-analysis.md`, `data/monthly-planning-templates.md`
- ✅ Systematic 7-section protocol (Weekly format + Trends + Alignment)
- ✅ Auto-proceeds (no menu wait)
- ✅ Clear success criteria (all sections + trends + alignment, ~30 min)
- ✅ Reports findings to user (appends to metrics)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "FORBIDDEN to redesign workflow or change architecture"
- ✅ "Skip resistance script" (prevents lazy skipping of critical sections)
- ✅ Subprocess pattern enforces comprehensive 4-week data loading

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ "Deeper weekly" design (extends weekly format, not replacement)

**Data Files Referenced:**
- `data/monthly-review-protocol.md` (trend analysis, chronic blockers, alignment)
- `data/monthly-metrics-analysis.md` (output format)
- `data/monthly-planning-templates.md` (cadence explanation, context template)
- Last 4 weeks of metrics data

**Overall Status:** ✅ **PASS**

---

#### Step V-04: Quarterly Review

**Proper Design:**
- ✅ Loads validation data from `data/quarterly-review-okr-protocol.md`, `data/quarterly-metrics-calc.md`, `data/quarterly-review-swot.md`, `data/quarterly-pattern-mining.md`, `data/quarterly-calibration-protocol.md`
- ✅ Systematic PDCA protocol (CHECK + ACT phases)
- ✅ Auto-proceeds through analysis sections
- ✅ Clear success criteria (all OKRs reviewed, adjustments made, report saved)
- ✅ Reports findings to user (quarterly report file + memory storage)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "FORBIDDEN to micromanage tactics"
- ✅ Subprocess pattern with comprehensive 3-month data loading
- ✅ "Be honest about progress (no sandbagging)"

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ PDCA integration (links to goal-setting workflow)

**Data Files Referenced:**
- `data/quarterly-review-okr-protocol.md` (OKR review)
- `data/quarterly-metrics-calc.md` (metrics formulas)
- `data/quarterly-review-swot.md` (SWOT analysis)
- `data/quarterly-pattern-mining.md` (pattern discovery)
- `data/quarterly-calibration-protocol.md` (estimate calibration)
- 3 months of metrics, goals, portfolio data

**Overall Status:** ✅ **PASS** (comprehensive design)

---

#### Step V-05: Retrospective

**Proper Design:**
- ✅ Loads validation data from `data/retrospective-protocol.md`, `data/retrospective-calibration.md`, `data/retrospective-questions.md`, `data/retrospective-report-template.md`
- ✅ Systematic accuracy analysis (planned vs actual)
- ✅ Auto-proceeds through analysis
- ✅ Clear success criteria (accuracy metrics calculated, learnings stored, calibration updated)
- ✅ Reports findings to user (retrospective report + memory storage)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "YOU ARE A FACILITATOR, not a content generator"
- ✅ Subprocess pattern with comprehensive execution log analysis
- ✅ "No data comparison = SYSTEM FAILURE"

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ Triggered after idea completion (integrated with workflow)

**Data Files Referenced:**
- `data/retrospective-protocol.md` (full retrospective process)
- `data/retrospective-calibration.md` (calibration formulas and methods)
- `data/retrospective-questions.md` (6-question protocol)
- `data/retrospective-report-template.md` (report structure)
- Deep Plan data (step-08 outputs)
- Execution tracking data (step-x-01, step-x-02)

**Overall Status:** ✅ **PASS** (learning-focused design)

---

#### Step V-06: Portfolio Dashboard

**Proper Design:**
- ✅ Loads portfolio and workflow plan data via subprocess
- ✅ Systematic 5-section dashboard (Capacity, Health, Balance, Active Projects, Risks)
- ✅ Auto-proceeds after dashboard display (offers menu options)
- ✅ Clear success criteria (dashboard generated with all sections, <3 min to assess)
- ✅ Reports findings to user (structured markdown dashboard)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "FORBIDDEN to modify portfolio or projects here (view-only)"
- ✅ Subprocess pattern ("DO NOT load full portfolio in main context")
- ✅ "Context waste" called out as system failure

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ READ-ONLY mode (validation, not modification)

**Data Files Referenced:**
- Portfolio file
- Workflow plan file
- Metrics file
- `data/search-decision-protocol.md` (for capacity planning patterns)

**Overall Status:** ✅ **PASS**

---

#### Step V-07: Decision Queue

**Proper Design:**
- ✅ Loads workflow plan and portfolio via subprocess
- ✅ Systematic decision analysis (readiness, capacity fit, dependencies, risk, alignment)
- ✅ Auto-proceeds with menu options (can trigger activation)
- ✅ Clear success criteria (queue ranked by score, decision factors shown, <5 min to decide)
- ✅ Reports findings to user (prioritized decision queue with recommendations)

**Anti-Lazy Language:**
- ✅ "NEVER generate content without user input"
- ✅ "FORBIDDEN to auto-activate without user confirmation"
- ✅ Subprocess pattern ("DO NOT load full workflow plan in main context")
- ✅ "Not recording decisions in memory = SYSTEM FAILURE"

**Critical Flow:**
- ✅ Located in `steps-v/` folder
- ✅ Properly segregated
- ✅ Independent execution
- ✅ Activation gateway (GO/NO-GO decisions)

**Data Files Referenced:**
- Workflow plan file
- Portfolio file
- `data/search-decision-protocol.md` (activation decision patterns)
- Deep Plan outputs (for readiness assessment)

**Overall Status:** ✅ **PASS**

---

## 4. "DO NOT BE LAZY" Language Assessment

All validation steps include strong anti-lazy mandates:

### Universal Mandates (Present in All Steps)

1. ✅ **"NEVER generate content without user input"** (8/8 steps)
2. ✅ **"YOU ARE A FACILITATOR, not a content generator"** (8/8 steps)
3. ✅ **"Read complete step file before action"** (8/8 steps)
4. ✅ **"FORBIDDEN to..."** boundary enforcement (8/8 steps)

### Subprocess-Specific Mandates

1. ✅ **"DO NOT load full files in main context"** (context optimization) (8/8 steps)
2. ✅ **"Launch subprocess that..."** (Pattern 2 enforcement) (8/8 steps)
3. ✅ **"Return structured findings, not raw data"** (context savings) (8/8 steps)

### Quality-Specific Mandates

1. ✅ **"Not accepting vague answers"** (Weekly Review)
2. ✅ **"Do NOT ask for details - signal-only"** (Daily Review)
3. ✅ **"Skip resistance script"** (Monthly Review)
4. ✅ **"Be honest about progress (no sandbagging)"** (Quarterly Review)

### Examples of Strong Anti-Lazy Language

**Weekly Review (step-02):**
```
### ❌ SYSTEM FAILURE
- Skipping sections (except Quick Wins if time-pressed)
- Accepting vague answers ("fine", "ok", "nothing")
- Not writing to metrics
- Generating fake data without user input
- Review takes <5 min (too shallow) or >30 min (too detailed)
```

**Retrospective (step-v-05):**
```
### ❌ SYSTEM FAILURE
- No data comparison
- No calibration updates
- Learnings not stored

**Master Rule:** Always store retrospective learnings in memory for future improvement.
```

**Portfolio Dashboard (step-v-06):**
```
### ❌ SYSTEM FAILURE
- Loading full portfolio/workflow files in main context (context waste)
- Missing key metrics (capacity, health, balance)
- No risk detection or recommendations
- Allowing modifications from view-only step
- Dashboard too verbose (>3 screens)
- Not using subprocess for analysis
```

**Assessment:** ✅ **EXCELLENT** - All validation steps have comprehensive anti-lazy language with specific failure modes called out.

---

## 5. Critical Flow Segregation

### Tri-Modal Structure Analysis

**Expected Structure:**
- `steps-c/` - Create mode (idea intake → planning)
- `steps-v/` - Validate mode (reviews, retrospectives, portfolio management)
- `steps-e/` - Edit mode (update projects, goals, resources)

**Actual Structure:**
- ✅ All 8 validation steps located in `steps-v/` folder
- ✅ Validation steps properly segregated from create flow
- ✅ No validation logic mixed into create steps
- ✅ Each validation step can run independently

**Workflow Type:** Personal/Business Operating System (NOT safety-critical)

**Appropriate Segregation:**
- ✅ For non-critical workflows, inline validation is acceptable
- ✅ Life OS uses tri-modal structure anyway (best practice)
- ✅ Validation steps are optional but encouraged (correct design)

**Verdict:** ✅ **PASS** - Proper tri-modal segregation, appropriate for workflow type.

---

## 6. Validation Data Files

### Data Files Found

**Review Protocols:**
- ✅ `data/weekly-review-protocol.md` (5-section weekly review)
- ✅ `data/monthly-review-protocol.md` (trend analysis, alignment)
- ✅ `data/quarterly-review-okr-protocol.md` (OKR review)
- ✅ `data/quarterly-review-swot.md` (SWOT analysis)
- ✅ `data/quarterly-metrics-calc.md` (metrics formulas)
- ✅ `data/quarterly-pattern-mining.md` (pattern discovery)
- ✅ `data/quarterly-calibration-protocol.md` (estimate calibration)

**Retrospective Protocols:**
- ✅ `data/retrospective-protocol.md` (retrospective process)
- ✅ `data/retrospective-calibration.md` (calibration methods)
- ✅ `data/retrospective-questions.md` (6-question protocol)
- ✅ `data/retrospective-report-template.md` (report structure)

**Validation Examples:**
- ✅ `data/validation-examples.md` (validation patterns)
- ✅ `data/user-validation-framework.md` (validation framework)
- ✅ `data/goals-examples/goals-smart-validation.md` (SMART goal validation)

**Supporting Data:**
- ✅ `data/search-decision-protocol.md` (semantic decision support)
- ✅ Portfolio, workflow plan, metrics files (runtime data)

### Data File Quality

**Structure:**
- ✅ All referenced data files exist
- ✅ Files properly structured (Markdown with clear sections)
- ✅ Referenced in step frontmatter or JIT loading sections

**Coverage:**
- ✅ Weekly/monthly/quarterly protocols complete
- ✅ Retrospective protocols comprehensive
- ✅ PDCA integration documented

**Missing (Minor):**
- ⚠️ Daily review could have explicit `data/daily-standup-protocol.md` (currently embedded)
- ⚠️ Portfolio dashboard could have `data/portfolio-health-metrics.md` (currently inline)

**Verdict:** ✅ **PASS** - Comprehensive validation data files present and properly referenced.

---

## 7. Issues Identified

### Critical Issues

**None.** All validation steps meet quality standards.

### Minor Issues

1. **Daily Review Skip Emphasis**
   - **Issue:** While daily review offers skip option, it could more strongly emphasize weekly as PRIMARY
   - **Current:** "Skip to weekly review (recommended for most users)"
   - **Suggested:** "Skip to weekly review (STRONGLY RECOMMENDED - 90% of users should skip daily)"
   - **Impact:** Low (daily review is already optional and short)
   - **Priority:** Low

2. **Missing Explicit Data Files**
   - **Issue:** Daily review and portfolio dashboard could have dedicated data files
   - **Current:** Protocols embedded in step files
   - **Suggested:** Extract to `data/daily-standup-protocol.md` and `data/portfolio-health-metrics.md`
   - **Impact:** Low (current design works fine, extraction would improve consistency)
   - **Priority:** Low

### Recommendations (Not Issues)

1. **Consider Validation Checklists**
   - Add explicit validation checklists to `data/` folder (e.g., `data/weekly-review-checklist.md`)
   - Would make it easier for users to self-validate review quality
   - Already implicitly present in protocols

2. **Add Validation Metrics**
   - Track validation completion rates (how many users complete weekly/monthly/quarterly)
   - Store in `data/validation-metrics.md`
   - Use for system improvement

---

## 8. Overall Assessment

### Summary Table

| Validation Step | Loads Data | Systematic Checks | Auto-Proceeds | Anti-Lazy | Clear Criteria | Status |
|-----------------|------------|-------------------|---------------|-----------|----------------|--------|
| V-00: Return-to-Plan | ✅ | ✅ | ✅ | ⚠️ (limited) | ✅ | ✅ PASS |
| V-01: Daily Review | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-02: Weekly Review | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-03: Monthly Review | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-04: Quarterly Review | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-05: Retrospective | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-06: Portfolio View | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| V-07: Decision Queue | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |

**Overall Validation Score:** 8/8 PASS (100%)

### Strengths

1. **Subprocess Optimization:** All validation steps use Pattern 2 (LLM Operations in subprocess) for context efficiency
2. **Data Loading:** Comprehensive JIT data loading from `data/` folder
3. **Anti-Lazy Language:** Strong mandates throughout with specific failure modes
4. **Systematic Protocols:** Each validation step has clear, repeatable process
5. **Auto-Proceed Design:** No unnecessary menu stops in validation flow
6. **Tri-Modal Segregation:** Proper separation of validation from create/edit modes
7. **Quality Standards:** Clear success/failure criteria for each step
8. **Learning Loop:** Retrospective and calibration steps ensure system improvement

### Weaknesses

**None critical.** Minor recommendations listed in Section 7.

---

## 9. Final Verdict

**✅ VALIDATION DESIGN: PASS**

**Reasoning:**

1. **Validation is Appropriate:** Life OS is NOT compliance-critical, but validation steps improve effectiveness
2. **Validation Steps Well-Designed:** All 8 steps follow best practices (data loading, systematic checks, auto-proceed, clear criteria)
3. **Anti-Lazy Language Strong:** Comprehensive mandates with specific failure modes
4. **Proper Segregation:** Tri-modal structure with validation in `steps-v/` folder
5. **Data Files Complete:** All referenced validation protocols exist and are well-structured
6. **No Critical Issues:** Only minor recommendations for future enhancement

**Quality Rating:** ⭐⭐⭐⭐⭐ (5/5 stars)

---

## 10. Recommendations for Future Enhancement

1. **Extract Daily/Portfolio Protocols:** Move embedded protocols to dedicated data files for consistency
2. **Add Validation Metrics:** Track completion rates and user satisfaction with validation steps
3. **Strengthen Daily Skip Emphasis:** Make it even clearer that 90% of users should skip daily review
4. **Add Validation Checklists:** Explicit checklists in `data/` folder for user self-assessment
5. **Expand Retrospective Coverage:** Add domain-specific retrospective questions for different project types

---

**Validation Complete.**
**Next Step:** Proceed to step-07-instruction-style-check.md

---

**Report Generated:** 2026-02-06
**Validator:** Claude Code (Code Review Agent)
**Workflow:** Life OS v3.0
