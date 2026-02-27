---
remediationDate: 2026-02-06
workflowName: life-os
workflowPath: d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\
remediationStatus: PENDING
remediationStandard: IDEAL-BEHAVIOR-REFERENCE.md v2.1 (Alignment & BMAD Compliance)
severityLevels: CRITICAL (blocks execution) | HIGH (breaks features) | MEDIUM (impacts UX) | LOW (code quality)
---

# Life OS Remediation Plan
## Bringing workflow.md into BMAD-compliant alignment with IDEAL-BEHAVIOR-REFERENCE.md v2.1

**Baseline:** Validation showed 72% alignment with ideal behavior
**Target:** 100% alignment with IDEAL-BEHAVIOR-REFERENCE.md
**Execution Model:** BMAD step-file sequential architecture (no parallel work, state tracking)

---

## EXECUTIVE SUMMARY

| Severity | Count | Impact | Timeline |
|----------|-------|--------|----------|
| **CRITICAL** | 2 issues | Blocks core workflows (Quick/Standard/Deep tracks) | 1-2 days |
| **HIGH** | 5 issues | Missing features break North Star elements | 1-2 weeks |
| **MEDIUM** | 7 issues | UX gaps, incomplete workflows | 1-2 weeks |
| **LOW** | 3 issues | Code quality, frontmatter debt | 1 week |
| **TOTAL** | **17 gaps** | Full workflow dysfunction → production ready | **3-4 weeks** |

**Recommendation:** Fix CRITICAL first (1-2 days), then batch HIGH+MEDIUM (2-3 weeks), LOW last (1 week)

---

## PART 1: CRITICAL ISSUES (Must fix immediately - blocks workflows)

### CRITICAL-01: Menu Routing Gaps (5 Orphaned Steps)

**Problem:** 5 step files exist in directories but are NOT referenced in workflow.md menus.
**Location:** workflow.md lines 200-244 (track-based routing)
**Impact:** Users cannot navigate to 5 steps; entire features unreachable (e.g., Portfolio Intake batch mode)

**Affected Files:**
1. `steps-c/step-05-refactoring-summary.md` (exists, not in menu)
2. `steps-c/step-00.1-portfolio-intake.md` (referenced in code but routing not fully wired)
3. `steps-v/step-05-retrospective.md` (exists, not in menu)
4. `steps-e/step-e-*.md` (Edit mode steps - unclear routing)
5. `steps-x/step-x-04-pivot-or-kill.md` (Execution mode - missing from main workflow)

**BMAD Fix (Sequential Steps):**

**Step R-C-01.1: Update workflow.md Menu Routes**
- **Action:** Add orphaned steps to appropriate menus
- **Files to modify:** workflow.md lines 200-244
- **Specific changes:**
  ```
  Line 204: Add "IF B:" routing: "Load and execute `steps-c/step-00.1-portfolio-intake.md`"
  Line 225: Standard Track add Step 05: "Step 05 → Step 06 (before Step 06)"
  Line 235: Deep Track line 239 add: "Step 04.5 (TRIZ) → (new routing)"
  ```
- **Verification:** All 5 files should appear in at least one menu path
- **State:** Update frontmatter `stepsCompleted: [R-C-01.1]`

**Step R-C-01.2: Create Edit Mode (steps-e/*) Menu Routing**
- **Action:** Define complete Edit mode workflow (currently missing)
- **Create:** New section in workflow.md "Edit Mode Routing" (after line 360)
- **Content:**
  ```
  ## Edit Mode Routing (steps-e/)

  IF mode == edit:
    IF "edit idea" OR "update idea"
      → Load steps-e/step-e-01-select-idea.md
    IF "edit project" OR "modify project"
      → Load steps-e/step-e-02-select-project.md
    IF "edit goals"
      → Load steps-e/step-e-03-edit-goals.md
  ```
- **State:** Update frontmatter `stepsCompleted: [R-C-01.1, R-C-01.2]`

**Step R-C-01.3: Wire Execution Mode (steps-x/*) into Main Workflow**
- **Action:** Define how projects transition from PLANNED → ACTIVE → X-01 (Kickoff)
- **Modify:** workflow.md lines 337-407 (Execution Tracking section)
- **Add routing:**
  ```
  When idea activated (L2-S3 decision = GO):
  → Auto-load steps-x/step-x-01-kickoff.md
  → Create execution tracking file (project-XXX/execution-tracking.md)
  → Transition project status: PLANNED → ACTIVE
  ```
- **State:** Update frontmatter `stepsCompleted: [R-C-01.1, R-C-01.2, R-C-01.3]`

**Validation Gate:** All 5 orphaned steps now have explicit routing paths
**Duration:** 2-3 hours
**Owner:** Workflow architect (understands BMAD routing)

---

### CRITICAL-02: Step Reference Bugs (3 Broken Links)

**Problem:** Step files contain incorrect references to other steps
**Location:** Multiple step files
**Impact:** Step sequences broken; workflows fail mid-execution

**Affected References:**

**Bug A:** `steps-x/step-x-01-kickoff.md` references non-existent `./step-x-02-tracking.md`
- **Correct path:** `./step-x-02-weekly-pulse.md`
- **Line number:** Unknown (need to locate in file)
- **Impact:** After kickoff, workflow cannot proceed to weekly pulse

**Bug B:** Quick Track routing error in workflow.md
- **Location:** workflow.md line 207 or nearby
- **Current:** `Step 05 → Step 06` (skips Step 09)
- **Should be:** `Step 05 → Step 09` (Complete)
- **Impact:** Quick Track users stuck after scoring

**Bug C:** Step-05 (Scoring) routing in Standard Track
- **Issue:** Not clear if it advances to Step 06 or Step 08
- **Clarify:** Add explicit nextStepFile in step-05 frontmatter

**BMAD Fix (Sequential Steps):**

**Step R-C-02.1: Fix step-x-01-kickoff.md Reference**
- **Action:** Locate and fix broken step reference
- **Search:** Find "step-x-02-tracking.md" in step-x-01-kickoff.md
- **Replace with:** `./step-x-02-weekly-pulse.md`
- **Verify:** step-x-02-weekly-pulse.md exists and is loadable
- **State:** Update step-x-01-kickoff.md frontmatter `correctedReferences: [step-x-02]`

**Step R-C-02.2: Fix Quick Track Routing in workflow.md**
- **Action:** Correct Step 05 → Step 09 routing
- **Location:** workflow.md line ~207 (Quick Track section)
- **Current code:**
  ```
  Step 01 → Step 04-consilium-lite → Step 05 → Step 09
  ```
- **Verify:** Matches IDEAL-BEHAVIOR-REFERENCE.md section 1.2 (USE CASE 1: Quick Track)
- **State:** Update workflow.md frontmatter with revision

**Step R-C-02.3: Add Explicit Track Routing in All Step Files**
- **Action:** Every step file should have `nextStepFile:` in frontmatter
- **Files to update:** step-01, step-02, step-03, step-04, step-04-lite, step-05, step-06, step-08, step-09
- **Format:**
  ```yaml
  nextStepFile: ./step-XX.md  # or depends on track (Quick/Standard/Deep)
  ```
- **Conditional routing example for step-05:**
  ```yaml
  nextStepFile_quick: ./step-09-complete.md
  nextStepFile_standard: ./step-06-portfolio-integration.md
  nextStepFile_deep: ./step-06-portfolio-integration.md
  ```
- **State:** Update frontmatter for all affected steps

**Validation Gate:** All step cross-references validated; no broken links
**Duration:** 3-4 hours (requires reading each step file)
**Owner:** Quality assurance / QA engineer

---

**END OF CRITICAL SECTION**

After completing both CRITICAL issues, workflow core functionality restored.
Proceed to HIGH priority issues for feature completeness.

---

## PART 2: HIGH-PRIORITY ISSUES (Feature Gaps - 1-2 weeks)

### HIGH-01: Missing Portfolio Dashboard Step

**Problem:** IDEAL-BEHAVIOR-REFERENCE.md 1.3 PERSPECTIVE 1-5 requires Portfolio Dashboard, but no step implements it
**Specification:** IDEAL v2.1, lines 449-450 (monitoring capacity: "3/5 projects")
**Impact:** North Star element #3 incomplete: "monitoring capacity" not implemented

**Requirements from IDEAL:**
```
Portfolio Dashboard should show:
- Active projects count (X/5)
- Capacity utilization percentage
- Current sprints/milestones
- Health status per project
- Synergies between projects
```

**BMAD Implementation (Create New Step):**

**Step R-H-01.1: Create step-06.5-portfolio-dashboard.md**
- **Purpose:** Display portfolio overview (dashboard generation)
- **Location:** Create new file `steps-c/step-06.5-portfolio-dashboard.md`
- **Frontmatter:**
  ```yaml
  name: Portfolio Dashboard
  description: "View and manage portfolio capacity, active projects, synergies"
  stepType: Execute
  estimatedMinutes: 15
  trackApplicable: [Deep]  # Deep Track only
  prerequisites: [step-06]
  outputs: [portfolio-overview.md]
  ```
- **Content (5 sections):**
  1. **Load Portfolio State** → Read all projects and count active
  2. **Calculate Capacity** → X/5 active, show percentage
  3. **Identify Synergies** → Find projects that share goals/domains
  4. **Generate Dashboard View** → Create markdown summary
  5. **Prompt for Action** → "View portfolio" / "Modify" / "Continue"
- **Output file:** `_output/portfolio-overview-{date}.md`
- **State:** Update workflow.md Deep Track routing (add after step-06)

**Step R-H-01.2: Update Deep Track Routing**
- **Modify:** workflow.md line 239 (Deep Track routing)
- **Add:** Step 06.5 before Step 07
- **New sequence:**
  ```
  Step 06 → Step 06.5 (Portfolio Dashboard) → Step 07 (Calendar Sync) → ...
  ```
- **State:** Verify routing works end-to-end

**Validation Gate:** Portfolio Dashboard step complete, Deep Track routing updated
**Duration:** 4-6 hours
**Owner:** Backend developer (understands project structure)

---

### HIGH-02: Missing Daily TODO Generation (Task Layer)

**Problem:** IDEAL-BEHAVIOR-REFERENCE.md 1.12 Task Layer specifies daily TODO algorithm, but NOT IMPLEMENTED in steps
**Specification:** IDEAL v2.1, lines 1213-1244 (daily TODO generation algorithm)
**Impact:** Users cannot get auto-generated daily task lists (critical for execution phase)

**Algorithm from IDEAL:**
```
Parse week plan → fetch active tasks → sort by priority + due_date → filter by capacity
→ balance energy levels → output to daily-todos/YYYY-MM-DD.md
```

**BMAD Implementation (Create New Step):**

**Step R-H-02.1: Create step-x-01b-daily-todos.md**
- **Purpose:** Generate daily TODO list from week plan + task database
- **Location:** Create `steps-x/step-x-01b-daily-todos.md`
- **When triggered:** After step-x-01-kickoff.md, or daily at 8am
- **Frontmatter:**
  ```yaml
  name: Generate Daily TODOs
  description: "Auto-generate daily task list from week plan, respecting capacity and energy"
  stepType: Execute
  estimatedMinutes: 5
  trackApplicable: [all]
  prerequisites: [step-x-01]
  dataInputs: [week-plan.md, tasks/*, resource-assessment.md]
  outputs: [daily-todos/YYYY-MM-DD.md]
  ```
- **Content (6 sections):**
  1. **Load Week Plan** → Read project/project-XXX/week-plan.md
  2. **Fetch Active Tasks** → Filter: status=todo AND project.status=ACTIVE AND (due_date<=today OR in_week_plan)
  3. **Sort Tasks** → By priority (critical→low), then due_date, then energy_level
  4. **Filter by Capacity** → Sum estimate_hours <= 4-6 hours/day
  5. **Balance Energy** → Morning (high), Afternoon (medium), Evening (low)
  6. **Output & Notify** → Create YYYY-MM-DD.md, show to user
- **Output format (markdown):**
  ```markdown
  # Daily TODO - 2026-02-07

  ## Morning (High Energy) - 2 tasks
  - [ ] Task 1 (1.5h, critical)
  - [ ] Task 2 (2h, high)

  ## Afternoon (Medium) - 3 tasks
  - [ ] Task 3 (1h, medium)
  ...

  ## Completed so far: 0/5
  ```
- **State:** Frontmatter tracks `generatedDates: [2026-02-07, ...]`

**Step R-H-02.2: Add Daily TODO to Execution Workflow**
- **Modify:** workflow.md (Execution section, lines 337-407)
- **Add routing:** After step-x-01, immediately call step-x-01b
- **Also add:** Daily cronjob trigger (8am) → auto-generate if new day
- **State:** Update workflow.md with daily trigger logic

**Step R-H-02.3: Link Daily TODOs to Calendar**
- **Modify:** step-x-01b output
- **Action:** For each task with estimate_hours, create calendar event
- **Format:** Add calendar-event links to daily-todos output
- **Integration:** Sync to Google Calendar (Phase 2) if available

**Validation Gate:** Daily TODOs generate correctly, respecting capacity and energy levels
**Duration:** 8-10 hours (complex algorithm)
**Owner:** Backend developer + algorithm designer

---

### HIGH-03: Missing Planning Model Integration (L1-L6)

**Problem:** IDEAL-BEHAVIOR-REFERENCE.md 1.14 specifies comprehensive planning model (milestones, Gantt, critical path), but NOT integrated
**Specification:** IDEAL v2.1, lines 1300+ (Planning Model section - if visible)
**Impact:** Deep Track planning incomplete; users cannot see full project roadmap

**Missing Components:**
1. Milestone creation algorithm
2. Gantt chart generation
3. Critical path analysis
4. Task dependency visualization

**BMAD Implementation (Create Multiple Steps):**

**Step R-H-03.1: Create step-08b-milestone-planning.md**
- **Purpose:** Decompose project into milestones with target dates
- **Location:** Create `steps-c/step-08b-milestone-planning.md`
- **When:** After step-08 (Deep Plan), before step-x-01 (Kickoff)
- **Frontmatter:**
  ```yaml
  name: Milestone Planning
  description: "Create project milestones with dependencies and target dates"
  stepType: Create
  estimatedMinutes: 20
  trackApplicable: [Deep]
  prerequisites: [step-08]
  outputs: [project-XXX/milestones.md, project-XXX/gantt.md]
  ```
- **Content:**
  1. **Extract Epics from Plan** → From step-08 output
  2. **Group into Milestones** → 3-5 milestones per project
  3. **Assign Target Dates** → Based on total estimate_hours + capacity
  4. **Define Dependencies** → Which milestones block which
  5. **Generate Gantt** → Create gantt.md with ASCII visualization
  6. **Output Milestones File** → Store in project-XXX/milestones.md
- **Output format (YAML milestones.md):**
  ```yaml
  milestones:
    - id: milestone-1
      name: "Foundation (Database + Auth)"
      target_date: "2026-03-15"
      estimate_hours: 40
      dependencies: []
      stories: [story-001, story-002, story-003]
    - id: milestone-2
      name: "MVP Features"
      target_date: "2026-04-15"
      estimate_hours: 60
      dependencies: [milestone-1]
      stories: [story-004, story-005]
  ```

**Step R-H-03.2: Create step-08c-gantt-generation.md**
- **Purpose:** Generate Gantt chart from milestones
- **Location:** Create `steps-c/step-08c-gantt-generation.md`
- **Content:**
  1. **Load Milestones** → From step-08b output
  2. **Calculate Timeline** → Date range from today to last milestone
  3. **Generate ASCII Gantt** → ASCII art visualization
  4. **Generate Mermaid Gantt** → For markdown/web rendering
  5. **Output Options** → Show to user, save to gantt.md
- **Output format (gantt.md):**
  ```markdown
  # Project Gantt Chart

  ```mermaid
  gantt
    title Life OS Project Timeline
    dateFormat YYYY-MM-DD

    section Milestones
    Foundation :m1, 2026-02-07, 2026-03-15
    MVP Features :m2, after m1, 2026-04-15
    ...
  ```
  ```

**Step R-H-03.3: Update Deep Track Routing**
- **Modify:** workflow.md Deep Track (line 238-244)
- **New sequence:**
  ```
  Step 08 → Step 08.5 (Polish) → Step 08b (Milestone Planning) → Step 08c (Gantt) → Step X-01 (Kickoff)
  ```
- **State:** Verify new routing chain

**Validation Gate:** Milestones created, Gantt charts generated, Deep Track complete
**Duration:** 12-15 hours (3 complex steps)
**Owner:** Backend developer + UX designer

---

### HIGH-04: Missing UI Screens for Portfolio Views

**Problem:** IDEAL-BEHAVIOR-REFERENCE.md describes 5 UI screens but only 2-3 have step implementations
**Screens missing:**
1. **Portfolio Dashboard** (capacity 3/5, health checks)
2. **Decision Queue** (evaluated ideas awaiting GO/NO-GO)
3. **Today View** (daily TODOs with progress)
4. **Calendar Integration** (time blocks visualization)
5. **Goal Tree** (nested year→quarter→month→week goals)

**Currently implemented:**
- ✅ Idea Collection form (step-01)
- ✅ Scoring interface (step-05)
- ❌ Portfolio Dashboard
- ❌ Decision Queue
- ❌ Today View
- ⚠️ Calendar (planned, not implemented)
- ❌ Goal Tree

**BMAD Implementation:**

This is a **web UI phase** (Phase 2 in IDEAL), NOT directly part of CLI workflow steps.
However, we need **CLI equivalents** that generate markdown reports.

**Step R-H-04.1: Create step-v-06-portfolio-view.md (Validate Mode)**
- **Purpose:** Display portfolio overview with health checks
- **Location:** Create `steps-v/step-v-06-portfolio-view.md`
- **When:** Daily/weekly review, or on-demand
- **Output:** Markdown portfolio report

**Step R-H-04.2: Create step-v-07-decision-queue.md (Validate Mode)**
- **Purpose:** Show evaluated ideas pending activation
- **Location:** Create `steps-v/step-v-07-decision-queue.md`
- **Output:** Markdown list of decisions needing action

**Step R-H-04.3: Create step-x-01c-today-view.md (Execution Mode)**
- **Purpose:** Show today's TODOs with progress tracking
- **Location:** Create `steps-x/step-x-01c-today-view.md`
- **Output:** Markdown daily progress view

**Validation Gate:** All 3 new view steps created and routed
**Duration:** 10-12 hours
**Owner:** UX/Product designer + frontend developer

---

### HIGH-05: SaaS Autonomy Gate Not Wired (criterion #6)

**Problem:** IDEAL-BEHAVIOR-REFERENCE.md 1.10 specifies SaaS Autonomy Gate (4 pillars), but step-05 scoring doesn't implement it
**Specification:** IDEAL v2.1, lines 678-800 (SaaS Autonomy Gate)
**Impact:** SaaS/software ideas not properly evaluated on autonomy dimension

**Requirements:**
- Detect if `domain = 'saas'` or `domain = 'software'`
- If yes, add 6th criterion: SaaS Autonomy (4 sub-criteria)
- Score: Self-Signup, Self-Billing, Self-Service Support, Autonomous Operation
- Weight normalization: 70/30 (positive/negative)

**BMAD Implementation:**

**Step R-H-05.1: Update step-05-scoring.md**
- **Modify:** scoring step to detect SaaS domains
- **Add section:** "SaaS Autonomy Scoring (if applicable)"
- **Content:**
  1. **Detect Domain** → Check if domain='saas' or 'software'
  2. **If SaaS:** Present 4 autonomy pillars (1-5 scale each)
  3. **Calculate Score** → (S_Signup×0.25) + (S_Billing×0.30) + (S_Service×0.30) + (Autonomous×0.15)
  4. **Apply Weight** → Add as 6th base criterion (0.15 weight in final score)
  5. **Flag Risks** → If Autonomy < 3.0, warn about support costs
- **Cross-reference:** IDEAL v2.1 lines 745-762 (Integration with Scoring)
- **Output:** Add `saaS_autonomy_score: X.X/5.0` to scored ideas

**Step R-H-05.2: Create scoring-rubric-saas-autonomy.md**
- **Purpose:** Detailed rubric for SaaS Autonomy Gate
- **Location:** Create `data/scoring-rubric-saas-autonomy.md`
- **Content:** 4 pillars with detailed scoring anchors (from IDEAL v2.1 lines 696-723)
- **Reference:** Referenced from step-05-scoring.md

**Validation Gate:** SaaS ideas scored with autonomy criterion; weight normalization working
**Duration:** 4-6 hours
**Owner:** Scoring specialist / domain expert

---

**END OF HIGH-PRIORITY SECTION**

After completing HIGH issues, workflow features complete.
Proceed to MEDIUM issues for UX polish.

---

## PART 3: MEDIUM-PRIORITY ISSUES (UX & Workflow Polish - 1-2 weeks)

### MEDIUM-01: Output Format Gaps (missing templates)

**Problem:** IDEAL specifies output formats but template files missing
**Missing Templates:**
1. `decision-log.template.md` (decisions made + reasoning)
2. `metrics.template.md` (project success metrics)
3. `ideas-bank/structure.md` (ideas organization)

**BMAD Implementation:**
- Create each missing template file in `templates/`
- Reference in workflow.md
- Include examples in each template

**Duration:** 3-4 hours

---

### MEDIUM-02: Track Escalation Logic Not Fully Implemented

**Problem:** IDEAL section 1.5 specifies automatic escalation (Quick→Standard→Deep), but logic incomplete
**Missing:** Complexity score calculation, escalation triggers

**BMAD Implementation:**
- Create `data/track-escalation-rules.md` with all triggers
- Implement complexity scoring in step-02 or step-04

**Duration:** 5-6 hours

---

### MEDIUM-03: Goals Integration Incomplete

**Problem:** IDEAL shows Goals→Ideas→Projects→Tasks cascade, but goal data flow not wired
**Missing:** Goals Discovery step routing, goal-to-idea alignment checking

**BMAD Implementation:**
- Implement `step-00-goals-discovery.md` properly
- Add goal alignment check in step-05 scoring
- Link `goals.yaml` to Strategic Alignment criterion

**Duration:** 6-8 hours

---

### MEDIUM-04: Memory Integration (Dual Storage) Partial

**Problem:** IDEAL specifies "Markdown + Claude Flow memory" but only Markdown implemented
**Missing:** Hook triggers to save patterns to Claude Flow HNSW

**BMAD Implementation:**
- Add memory storage instructions to each step
- Create post-step hook that saves to Claude Flow memory
- Add retrieval logic ("found similar idea...")

**Duration:** 4-6 hours

---

### MEDIUM-05: Track Detection Algorithm Not Documented

**Problem:** IDEAL references complexity scoring, but algorithm not detailed in workflow
**Missing:** `data/track-detection-algorithm.md`

**BMAD Implementation:**
- Create algorithm spec (complexity 0-20 scale)
- Define Quick (<8), Standard (8-15), Deep (>15)
- Implement in step-02 or step-04

**Duration:** 3-4 hours

---

### MEDIUM-06: Specialist Role Matching Not Detailed

**Problem:** IDEAL shows "AI suggests roles based on keywords", but no algorithm
**Missing:** `data/role-matching-algorithm.md`

**BMAD Implementation:**
- Define role suggestion logic
- Create role database (50+ specialist types)
- Implement in step-02

**Duration:** 4-5 hours

---

### MEDIUM-07: TRIZ Auto-Trigger Incomplete

**Problem:** IDEAL specifies TRIZ auto-trigger (step-04.5), but conditions not clear
**Missing:** Disagreement detection, conflict identification logic

**BMAD Implementation:**
- Define TRIZ trigger conditions clearly
- Create step-04.5 with full TRIZ analysis
- Wire into Deep Track routing

**Duration:** 6-8 hours

---

**END OF MEDIUM-PRIORITY SECTION**

---

## PART 4: LOW-PRIORITY ISSUES (Code Quality - 1 week)

### LOW-01: Frontmatter Design Debt (12 unused variables)

**Problem:** workflow.md frontmatter has 12/15 unused variables (80% unused)
**Variables:**
- `trackDetectionAlgorithm` → hardcoded in code, not used
- `executionKickoff` → should reference `steps-x/step-x-01-kickoff.md` but hardcoded
- Others defined but not referenced

**BMAD Implementation:**
- **Option A:** Remove all 12 unused variables (clean)
- **Option B:** Complete refactor using all variables
- **Recommendation:** Option A (DRY principle)

**Duration:** 1-2 hours

---

### LOW-02: Missing Documentation in Data Files

**Problem:** IDEAL references files that don't exist or are incomplete
**Files:**
- `data/track-detection-algorithm.md` (partially exists)
- `data/track-escalation-rules.md` (missing)
- `data/role-matching-algorithm.md` (missing)
- `data/scoring-rubric-saas-autonomy.md` (missing)

**BMAD Implementation:**
- Create/complete all 4 files with detailed specs

**Duration:** 4-6 hours

---

### LOW-03: Step File Size Optimization

**Problem:** Some steps are too long (>250 lines recommended max)
**Large steps:**
- step-01 (idea collection - probably >200 lines)
- step-04 (consilium - complex)
- step-08 (deep plan - comprehensive)

**BMAD Implementation:**
- Break into smaller micro-steps if needed
- Maintain sequential flow

**Duration:** 3-4 hours

---

**END OF LOW-PRIORITY SECTION**

---

## IMPLEMENTATION ROADMAP

### Week 1: CRITICAL Issues (Days 1-5)
```
Day 1-2: R-C-01 (Menu routing + orphaned steps) - 3-4 hours/day
Day 3-4: R-C-02 (Fix broken references) - 3-4 hours/day
Day 5: Validation & testing - 4 hours
Total: ~20 hours
Result: Core workflow functional
```

### Week 2-3: HIGH Issues (Days 6-20)
```
Day 6-7: R-H-01 (Portfolio Dashboard) - 4-5 hours/day
Day 8-9: R-H-02 (Daily TODOs) - 4-5 hours/day
Day 10-12: R-H-03 (Planning Model) - 4-5 hours/day
Day 13-14: R-H-04 (UI Screens) - 4-5 hours/day
Day 15: R-H-05 (SaaS Autonomy) - 4-5 hours
Total: ~45-50 hours
Result: All features implemented
```

### Week 3-4: MEDIUM + LOW Issues (Days 21-28)
```
Day 21-24: MEDIUM-01 through MEDIUM-07 - 3-4 hours/day
Day 25-26: LOW-01 through LOW-03 - 3-4 hours/day
Day 27: Final validation & cleanup
Day 28: Documentation + handoff
Total: ~25-30 hours
Result: Production-ready, 100% IDEAL aligned
```

**Total Timeline: 3-4 weeks (90-100 hours)**

---

## EXECUTION PROTOCOL (BMAD-Compliant)

### Sequential, No-Skip Rules:
1. ✅ **READ this entire remediation plan** before starting
2. ✅ **START with CRITICAL issues only** (do not skip to HIGH)
3. ✅ **Complete each step sequentially** (no parallel work)
4. ✅ **Update frontmatter** after each step (stepsCompleted array)
5. ✅ **Test routing** after each modification
6. ✅ **Document changes** in git commit messages
7. ✅ **Validation gate** after each section (CRITICAL → HIGH → MEDIUM → LOW)

### State Tracking:
Each major remediation step updates a tracking file:
```yaml
# .bmad/remediation-progress.md

stepsCompleted:
  - R-C-01.1 (2026-02-07 14:00)
  - R-C-01.2 (2026-02-07 16:30)
  - R-C-02.1 (2026-02-08 10:00)
  - ...

nextStep: R-H-01.1
lastValidated: 2026-02-08T16:00:00Z
```

### Validation Gates:
After each priority level, test:
1. ✅ All referenced files exist and are loadable
2. ✅ Routing links work end-to-end
3. ✅ Frontmatter updates complete
4. ✅ Step sequences follow BMAD rules
5. ✅ No broken references remain

---

## SUMMARY: Bringing Life OS to 100% IDEAL Alignment

| Phase | Work | Hours | Timeline | Result |
|-------|------|-------|----------|--------|
| **CRITICAL** | Fix 2 core issues | 20 | 1-2 days | Core functional |
| **HIGH** | Add 5 missing features | 45-50 | 2-3 weeks | Features complete |
| **MEDIUM** | Polish 7 UX items | 20-25 | 1-2 weeks | UX refined |
| **LOW** | Clean 3 code items | 8-10 | 1 week | Production-ready |
| **TOTAL** | Full remediation | **93-105** | **3-4 weeks** | **100% IDEAL v2.1 aligned** |

**Start date:** 2026-02-07
**Target completion:** 2026-02-28

---

*Document created: 2026-02-06*
*Standards: BMAD Workflow Standards v6.0.0-Beta.5 + IDEAL-BEHAVIOR-REFERENCE.md v2.1*
