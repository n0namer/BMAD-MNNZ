---
name: 'step-03-orchestration-plan'
description: 'Build dependency graph, detect conflicts, and mark parallel execution zones'

nextStepFile: './step-04-execution-loop.md'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
planTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/orchestration-plan-template.md'
conflictPatterns: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/data/conflict-detection-patterns.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Orchestration Plan

## STEP GOAL:

To build a dependency graph of workflows, detect read/write conflicts, mark safe parallel execution zones, and select the runtime environment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an orchestration architect
- ✅ Analyze dependencies and conflicts systematically
- ✅ Present execution plan with clear parallel/sequential zones
- ✅ Let user confirm or adjust the plan

### Step-Specific Rules:

- 🎯 Focus ONLY on orchestration planning
- 🚫 FORBIDDEN to execute workflows yet (that's step 4)
- 💬 Present dependency graph and conflict analysis
- 🚪 User must confirm plan before proceeding

## EXECUTION PROTOCOLS:

- 🎯 Analyze workflow dependencies
- 💬 Detect conflicts (read-after-write, write-after-write)
- 📖 Mark parallel vs sequential zones
- 🚫 FORBIDDEN to load next step until plan confirmed

## CONTEXT BOUNDARIES:

- Workflows selected from Step 2
- Files identified from Step 1
- Now we plan execution order and parallelization
- Don't execute yet

## YOLO MODE AUTO-PLANNING

**CRITICAL: Check YOLO configuration BEFORE user menu:**

```
IF yolo_level >= 3:
  → Auto-generate orchestration plan
  → Default strategy: parallel where safe, sequential otherwise
  → Auto-select runtime (typically Claude Code for best compatibility)
  → Skip user confirmation menus
  → Auto-proceed to step-04
  → Log: "YOLO Level {level} - Auto-generated plan: {parallel_zones} parallel zones, {sequential_deps} dependencies"

IF yolo_level < 3:
  → Show dependency graph with [A/P/C] menu as normal
  → Wait for user confirmation before proceeding
```

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Build Dependency Graph

"**Building orchestration plan...**

Analyzing workflows: [list selected workflows]
Target files: [list files from discovery]

**Dependency Analysis:**"

For each workflow, identify inputs, outputs, dependencies.
See `/data/conflict-detection-patterns.md` for examples.

### 2. Conflict Detection

"**Conflict Detection Analysis:**

Checking for read-after-write and write-after-write conflicts..."

See `/data/conflict-detection-patterns.md` for conflict types and examples.

### 3. Mark Parallel Zones

"**Parallel Execution Zones:**

Based on conflict analysis, create execution plan diagram."

See `/data/conflict-detection-patterns.md` for parallel zone example.

### 4. Runtime Selection

"**Select Runtime Environment:**

Where will this orchestration run?

**[C]line** — Local with use_subagents for parallel execution
**[L]aude Code** — Cloud with MCP subagents
**[D]ex** — OpenAI Codex with subagents
**[A]uto** — Detect based on environment

Which runtime? [C/L/D/A]"

Handle selection and document.

### 5. Present Complete Plan

"**ORCHESTRATION PLAN SUMMARY**

**Execution Flow:**
[Show visual diagram from step 3]

**Parallel Zones:** [N zones identified]
**Sequential Dependencies:** [M dependencies]
**Estimated Phases:** [K phases]

**Runtime:** [Selected runtime]
**Conflict Risk:** [Low/Medium/High with explanation]

See `/data/conflict-detection-patterns.md` for large file and safety strategies.

**Does this plan look correct? Any adjustments needed?**"

### 6. Handle User Feedback

**IF user approves:** Document and proceed
**IF user wants changes:** Adjust plan, re-present
**IF user has concerns:** Address with alternatives

### 7. Update Plan Document

Update `{workflowPlanFile}` with orchestration plan:

```markdown
## Orchestration Plan

**Dependency Graph:**
```
[Visual representation]
```

**Parallel Zones:**
- Zone 1: [workflows that can run in parallel]
- Zone 2: [workflows that can run in parallel]

**Sequential Dependencies:**
- [Workflow A] → [Workflow B] (reason: read-after-write)

**Execution Phases:**
1. Phase 1: [description]
2. Phase 2: [description]
...

**Runtime:** [Cline/Claude/Codex/Auto]

**Conflict Analysis:**
- Conflicts detected: [N]
- Mitigation: [strategy]

**Large File Handling:**
- Range read threshold: [X] lines
- Append-only building: [Yes/No]

**Safety Measures:**
- Backup before writes: [Yes/No]
- Checkpoint frequency: [every phase/step]
```

Update frontmatter: `stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection', 'step-03-orchestration-plan']`

### 8. Create Orchestration Plan Intermediate File

Create orchestration plan file in `{intermediateFolder}`:

**File:** `orchestration-plan-{sessionId}.md`

Use template `{planTemplate}` and populate with:
- sessionId: From session
- timestamp: Current date/time
- totalWorkflows: Count of selected workflows
- parallelZones: Number of parallel zones identified
- sequentialDeps: Number of sequential dependencies
- estimatedPhases: Estimated number of execution phases
- dependencyGraph: Visual/text representation
- parallelZones: List of parallel zones with workflows
- sequentialZones: List of sequential phases
- conflicts: Any conflicts detected with resolutions
- runtime: Selected runtime environment
- safetyMeasures: Large file handling, backup, checkpoint settings

Also create conflict analysis file:
**File:** `conflict-analysis-{sessionId}.md`
- Detailed conflict analysis
- Resolution strategies
- Risk assessment

### 9. Transition to Execution

"Excellent! Orchestration plan is ready. Now we'll execute the workflows according to this plan — parallel zones will use subagents, sequential phases will run in order."

### 10. Present MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 3:
  → Auto-proceed to step-04 (no menu)
  → Update plan: stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection', 'step-03-orchestration-plan']
  → Load: {nextStepFile}
  → Log: "YOLO Level {level} - Auto-proceeding to execution (parallel zones: {N}, sequential deps: {M})"
  → No approval needed

IF yolo_level < 3:
  → Display: **Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue
  → ALWAYS halt and wait for user input
```

#### EXECUTION RULES (Manual Mode - yolo_level < 3):

- ALWAYS halt and wait for user input
- ONLY proceed to next step when user selects 'C'
- User can chat or ask questions - always respond and redisplay menu

#### Menu Handling Logic (For Manual Mode):

- IF A: Execute {advancedElicitationTask} for deeper exploration
- IF P: Execute {partyModeWorkflow} for multi-agent discussion
- IF C: Update plan frontmatter, then load `{nextStepFile}`
- IF Any other: Help user, then redisplay menu

#### YOLO Mode Auto-Proceed (level >= 3):

- Update plan: stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection', 'step-03-orchestration-plan']
- Load: `{nextStepFile}` (step-04-execution-loop.md)
- Log action with timestamp and plan metrics

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Dependency graph built
- Conflicts detected and documented
- Parallel zones marked clearly
- Execution plan visualized
- Runtime selected
- User confirmed plan
- Ready for execution

### ❌ SYSTEM FAILURE:

- Missing conflict detection
- No parallel zone analysis
- User didn't confirm plan
- Not documenting the orchestration

**Master Rule:** Plan thoroughly, detect conflicts, mark parallel zones, get confirmation, then execute.
