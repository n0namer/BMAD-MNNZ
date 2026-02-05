---
name: 'step-x-01-kickoff'
description: 'Transition idea from PLANNED to IN_PROGRESS with milestones and success metrics'
nextStepFile: './step-x-02-tracking.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
trackerTemplateFile: '../templates/project/execution-tracker.template.md'
---

# Step X-01: Project Kickoff

## STEP GOAL:

Mark idea as **IN_PROGRESS**, define 3-5 measurable milestones with dates, and set quantifiable success metrics to track execution progress.

## WHEN TO USE:

After **Step 08 (Deep Plan)** completes and user is ready to start execution. This step transitions from planning to active work.

## MANDATORY EXECUTION RULES (READ FIRST):

**Universal:** 🛑 Facilitator not generator | 📖 Read step first | 🔄 Read next step file completely | ✅ Use {communication_language}

**Step-Specific:** 🎯 Focus on kickoff only | 🚫 No plan/scoring edits | 💬 Confirm each milestone/metric | ⏰ Dates required | 📊 Quantifiable metrics only | 🎯 Use subprocess for milestone/metrics examples loading (Pattern 3: Data Operations) | 💬 Return structured examples only

## EXECUTION PROTOCOLS:

- 🎯 Load idea from memory (scoring, deep plan)
- 💾 Save kickoff data to global memory
- 📖 Create execution tracker file in output/
- 🧾 Update idea status to IN_PROGRESS
- 📘 Record kickoff decision in journal

### Search Orchestrator Protocol (Optional)
- If user needs milestone/metric examples, use Search Orchestrator (CLI memory → local MD → web/MCP)
- Retrieve successful milestone patterns from similar projects

## CONTEXT BOUNDARIES:

- Available context: workflow plan, deep plan (L1-L6), scoring results
- Focus: execution kickoff and tracking setup
- Dependencies: step-08 deep plan must be complete

## MANDATORY SEQUENCE

### 1. Load Idea Context

**Load:** {workflowPlanFile} (idea name, score, rank, Deep Plan L1-L6, status=PLANNED)
**Search:** `npx claude-flow@v3alpha memory search -q "idea:{idea-id} scoring deep-plan"`
**Summarize:** Present idea name, score/rank, L2 areas from Deep Plan, ask "Ready to transition to IN_PROGRESS?"

### 2. Confirm Kickoff Decision

**Present menu:** [S] Start execution | [P] Postpone (keep PLANNED) | [C] Cancel (archive)
**Logic:** S→Section 3 | P→status=PLANNED_PAUSED, save reason, exit | C→status=ARCHIVED, archive, exit
**CRITICAL:** Wait for user input. Do NOT auto-proceed.

### 3. Define Key Milestones (3-5) (Subprocess)

📖 **Protocol:** `data/milestone-definition-protocol.md`

**Launch a subprocess that:**
1. Loads Deep Plan L2-L4 structure from workflow plan
2. Loads milestone-definition-protocol.md with examples and templates
3. Extracts major phases (L2) and stages (L4) as milestone candidates
4. Matches similar patterns from past projects (memory search)
5. Returns 3-5 suggested milestones with:
   - Name, target date (calculated from timeline), success criteria, deliverables

**Subprocess returns:** Structured milestone suggestions (150-200 lines) instead of loading full milestone-definition-protocol.md (600+ lines).

**Graceful fallback:** If subprocess unavailable, load `data/milestone-definition-protocol.md` and manually extract 3-5 template examples relevant to project type.

### 4. Define Success Metrics (3-5 Quantifiable) (Subprocess)

📖 **Protocol:** `data/success-metrics-protocol.md`

**Launch a subprocess that:**
1. Loads scoring results and Deep Plan goals
2. Loads success-metrics-protocol.md with KPI definitions and examples
3. Auto-suggests metrics based on:
   - Project domain (Business → ROI, Health → habit streak, Personal → completion rate)
   - Scoring criteria (alignment, feasibility, impact)
   - Deep Plan L1 mission statement
4. Returns 3-5 quantifiable metrics with targets and measurement methods

**Subprocess returns:** Structured metric suggestions (150-200 lines) instead of loading full success-metrics-protocol.md (600+ lines).

**Graceful fallback:** If subprocess unavailable, load `data/success-metrics-protocol.md` and manually select 3-5 metric templates relevant to project domain.

### 5. Save Kickoff Data to Memory

**Save:** `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "execution:tracking:{idea-id}:kickoff" --content "{idea_id, idea_name, status: IN_PROGRESS, kickoff_date, milestones[], success_metrics[], timeline_estimate, variance_tolerance}"`
**Confirm:** "✅ Kickoff data saved to global memory."

### 6. Create Execution Tracker File

📖 **Template:** `../data/execution-tracker-template.md` - Read template, populate with confirmed milestones/metrics, save to `{bmb_creations_output_folder}/life-os/output/{idea-id}-execution-tracker.md`, confirm creation.

### 7. Update Workflow Plan Status

**Update {workflowPlanFile}:** Locate idea, set status=IN_PROGRESS, add kickoff_date, milestones count, metrics count, tracker file path.
**Append journal:** Add entry: "{YYYY-MM-DD} - Project Kickoff | PLANNED→IN_PROGRESS | {N} milestones | {M} metrics | Next: Step X-02"

### 8. Present Summary and Next Steps

**Show:**
- 🎉 PROJECT KICKOFF COMPLETE!
- Idea: {Name} | Status: IN_PROGRESS | Kickoff: {YYYY-MM-DD}
- Milestones: {N} (list names + dates) | Metrics: {M} (list names + targets) | Variance: ±{X}%
- ✅ Saved: memory key, tracker file, workflow plan updated
- 🚀 Next: Step X-02 for tracking, record progress weekly/at milestones, update metrics, flag blockers

### 9. Quick Feedback & MENU OPTIONS

**Ask:** 👍 Helpful | 😐 OK | 👎 Frustrating [Type feedback or skip]
**Save:** `npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-x-01-kickoff:{timestamp}" --content "{step, rating, comment, timestamp}"`

**Menu:** [T] Track Progress (Step X-02) | [E] Edit Kickoff | [R] Review Plan (Step 08) | [D] Dashboard (all IN_PROGRESS)

**Logic:**
- T: Save state, read entire `./step-x-02-tracking.md`, execute
- E: Edit milestones/metrics, re-save, redisplay menu
- R: Show Step 08, redisplay menu
- D: Show IN_PROGRESS projects, redisplay menu

**Rules:** Wait for input after menu | Only proceed when user selects action | Save before navigating

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Status updated to IN_PROGRESS
- 3-5 milestones defined with target dates and measurable criteria
- 3-5 success metrics defined with quantifiable targets
- Kickoff data saved to global memory
- Execution tracker file created
- Workflow plan updated with new status

### ❌ SYSTEM FAILURE:
- Proceeding without user confirmation
- Milestones without dates or measurable criteria
- Success metrics that are subjective (not quantifiable)
- Not saving to memory before continuing
- Creating tracker file without user-confirmed milestones

**Master Rule:** All milestones and metrics must be measurable, confirmed, and saved before proceeding to execution tracking.
