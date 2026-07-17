---
name: 'step-04-execution-loop'
description: 'Execute workflows according to plan with parallel zones and large file support'

nextStepFile: './step-05-cascade-sync.md'
workflowPlanFile: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/workflow-plan-bmad-orchestrator.md'
intermediateFolder: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate'
checkpointTemplate: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/intermediate/checkpoint-phase-template.md'
executionPatterns: '{bmb_creations_output_folder}/workflows/bmad-orchestrator/data/execution-patterns.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Execution Loop

## STEP GOAL:

To execute workflows according to the orchestration plan — parallel zones via subagents, sequential phases in order, with large file support and progress tracking.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an orchestration executor
- ✅ Follow the plan precisely
- ✅ Monitor progress and handle checkpoints
- ✅ Allow user to pause/continue at any phase

### Step-Specific Rules:

- 🎯 Execute according to orchestration plan
- 🚫 FORBIDDEN to deviate from plan without user approval
- 💬 Report progress after each phase
- 🚪 Allow [C] Continue or pause at each checkpoint

## EXECUTION PROTOCOLS:

- 🎯 Follow dependency graph from orchestration plan
- 💬 Execute parallel zones via subagents
- 📖 Update frontmatter stepsCompleted after each phase
- 🚫 FORBIDDEN to skip phases or change order

**Reference:** See `/data/manifest-integration-guide.md` for tool selection and availability checks.

## CONTEXT BOUNDARIES:

- Orchestration plan from Step 3 defines execution order
- Workflows selected from Step 2
- Files from Step 1
- Now we execute according to plan

## YOLO MODE AUTO-EXECUTION

**CRITICAL: Check YOLO configuration BEFORE checkpoints:**

```
IF yolo_level >= 5:
  → Execute all workflows continuously (no checkpoints)
  → Auto-handle minor errors
  → Only report critical issues
  → Skip all [C/P/A/S] checkpoint menus
  → Auto-proceed to step-05 when execution complete
  → Log: "YOLO Level {level} - Continuous execution, {N} phases completed"

IF yolo_level >= 3 and < 5:
  → Execute with checkpoints on phase boundaries
  → Show [C] Continue / [P] Pause options at checkpoints
  → Auto-proceed through phases if user doesn't pause
  → Skip [A/S] menu options (Advanced Elicitation / Save Report)

IF yolo_level < 3:
  → Execute with full checkpoint menu [C/P/A/S] at every phase
  → Wait for user approval to continue
```

---

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Orchestration Plan

"**Starting Execution Phase**

Loading orchestration plan...

**Plan Summary:**
- Total phases: [N]
- Parallel zones: [M]
- Runtime: [Cline/Claude/Codex]
- Estimated time: [estimate if known]

**Ready to begin execution. I'll report progress after each phase.**"

### 2. Execute Phase by Phase

For each phase in the orchestration plan:

#### **Phase Execution:**

See `/data/execution-patterns.md` for:
- Parallel zone execution pattern
- Sequential phase execution pattern
- Large file handling strategy
- Failure handling

### 2a. Initialize Swarm for Parallel Zones

If orchestration plan has parallel zones:

**1. Initialize Swarm via MCP:**

```javascript
mcp__ruv-swarm__swarm_init({
  topology: "hierarchical",        // Coordinator prevents drift
  maxAgents: 8,                    // Smaller team = less coordination overhead
  strategy: "specialized"          // Clear roles, no overlap
})
```

**Message to user:**
```
"🔄 Initializing parallel execution swarm...
- Topology: hierarchical (prevents goal drift)
- Max agents: 8 (optimal coordination)
- Strategy: specialized (clear role boundaries)

Loading parallel zone definitions from plan..."
```

**2. Load Parallel Zone Definitions:**

From orchestration plan, identify:
- Zone structure (which workflows run parallel, which sequential)
- Dependencies between zones
- Conflict analysis (read/write/resource conflicts)
- Expected outputs per zone

**Example Plan Structure:**
```
Zone 1 (Parallel - 3 workflows simultaneously):
  - Workflow A (independent)
  - Workflow B (independent)
  - Workflow C (independent)

Zone 2 (Sequential - depends on Zone 1):
  - Workflow D (uses Zone 1 outputs)
  - Workflow E (uses Workflow D output)
```

### 2b. Spawn Agents for Each Parallel Zone

For each zone, spawn via Task tool (all agents in ONE message for parallel execution):

**Zone 1 Parallel Execution (Spawn all agents simultaneously):**

```javascript
// Agent 1 - Execute Workflow A
Task({
  subagent_type: "coder",
  prompt: "Execute Workflow A with inputs: {zone1_inputs}. Output to: {zone1_output_dir}. Report results back with: status, duration, output files.",
  name: "exec-workflow-a",
  model: "sonnet"
})

// Agent 2 - Execute Workflow B
Task({
  subagent_type: "coder",
  prompt: "Execute Workflow B with inputs: {zone1_inputs}. Output to: {zone1_output_dir}. Report results back with: status, duration, output files.",
  name: "exec-workflow-b",
  model: "sonnet"
})

// Agent 3 - Execute Workflow C
Task({
  subagent_type: "tester",
  prompt: "Execute Workflow C with inputs: {zone1_inputs}. Output to: {zone1_output_dir}. Report results back with: status, duration, output files.",
  name: "exec-workflow-c",
  model: "sonnet"
})
```

**Message to user:**
```
"🚀 Launching Parallel Zone 1 (3 agents)...

▶️ Agent 1 → Workflow A
▶️ Agent 2 → Workflow B
▶️ Agent 3 → Workflow C

All three workflows executing simultaneously.
Estimated time: {max_workflow_duration}
Will report when all complete..."
```

**WAIT FOR ALL ZONE 1 AGENTS TO COMPLETE before proceeding to Zone 2.**

**Zone 2 Sequential Execution (after Zone 1 complete):**

```javascript
// Agent 4 - Execute Workflow D (uses Zone 1 results)
Task({
  subagent_type: "reviewer",
  prompt: "Execute Workflow D using these inputs from Zone 1: {zone1_results}. Output to: {zone2_output_dir}. Report results with: status, duration, output files.",
  name: "exec-workflow-d",
  model: "sonnet"
})

// After Workflow D completes:

// Agent 5 - Execute Workflow E (uses Workflow D output)
Task({
  subagent_type: "reviewer",
  prompt: "Execute Workflow E using output from Workflow D: {workflow_d_output}. Output to: {zone2_output_dir}. Report results with: status, duration, output files.",
  name: "exec-workflow-e",
  model: "sonnet"
})
```

**Message to user:**
```
"✅ Zone 1 Complete (3 workflows finished)
Results:
- Workflow A: SUCCESS (2m 15s)
- Workflow B: SUCCESS (1m 58s)
- Workflow C: SUCCESS (2m 22s)

⏭️ Proceeding to Zone 2 (sequential)...

▶️ Agent 4 → Workflow D (depends on Zone 1)
▶️ Agent 5 → Workflow E (depends on Workflow D)

Executing sequentially..."
```

### 2c. Conflict Detection & Handling

**Before spawning parallel agents, validate conflict analysis:**

```javascript
// Check for conflicts in parallel zone:
conflicts = {
  readAfterWrite: [],      // A reads file, B writes to same file
  writeAfterWrite: [],     // A and B both write to same file
  resourceConflict: [],    // A and B compete for same resource
  dependencyConflict: []   // A depends on B's output
}

// Analyze each workflow pair in parallel zone:
for (workflow_i in zone.workflows) {
  for (workflow_j in zone.workflows) {
    if (workflow_i < workflow_j) {
      // Check for conflicts
      if (hasReadWriteConflict(workflow_i, workflow_j)) {
        conflicts.readAfterWrite.push({from: workflow_i, to: workflow_j})
        // Mark as sequential instead
      }
      if (hasWriteWriteConflict(workflow_i, workflow_j)) {
        conflicts.writeAfterWrite.push({between: [workflow_i, workflow_j]})
        // Mark as sequential instead
      }
      // ... check other conflict types
    }
  }
}

// If conflicts detected:
if (conflicts.size > 0) {
  message = "⚠️ Conflicts detected - switching to sequential mode"
  // Reorder workflows to avoid conflicts
  // Or split into multiple zones
  workflows = reorderForSequential(workflows, conflicts)
} else {
  message = "✅ No conflicts - safe for parallel execution"
}
```

**Message to user:**
```
"Analyzing conflicts in Zone {N}...

Read-Write conflicts: {count}
Write-Write conflicts: {count}
Resource conflicts: {count}
Dependency conflicts: {count}

Verdict: {parallel_safe | needs_sequential_mode}"
```

### 2d. Aggregate Results from Parallel Agents

After all agents in a zone complete:

**1. Collect Results:**

```javascript
// After all Zone 1 agents report back:
zone1_results = {
  workflow_a: {
    status: "SUCCESS",
    duration: "2m 15s",
    output_files: ["file1.md", "file2.md"],
    tokens_used: 4521
  },
  workflow_b: {
    status: "SUCCESS",
    duration: "1m 58s",
    output_files: ["file3.md", "file4.md"],
    tokens_used: 3890
  },
  workflow_c: {
    status: "SUCCESS",
    duration: "2m 22s",
    output_files: ["file5.md", "file6.md"],
    tokens_used: 4103
  }
}
```

**2. Validate Results Consistency:**

```javascript
// Validate no conflicting outputs
for (each result in zone_results) {
  // Check output files don't conflict
  if (duplicate_files(result.output_files, all_zone_outputs)) {
    conflicts.push({workflow: result.name, issue: "duplicate_files"})
  }

  // Check no contradictory content
  if (conflicting_content(result.content, previous_results)) {
    conflicts.push({workflow: result.name, issue: "content_conflict"})
  }

  // Merge compatible results
  merged_outputs.add(result.output_files)
}

// If conflicts:
if (conflicts.size > 0) {
  message = "⚠️ Output conflicts detected - manual review needed"
} else {
  message = "✅ Results merged successfully"
}
```

**3. Store Aggregated Results in Checkpoint:**

Create/update checkpoint with aggregated results:

```markdown
## Phase N Checkpoint - Zone Aggregation Results

**Parallel Zone Execution:**
- Zone 1 (3 agents parallel):
  - Workflow A: ✅ SUCCESS (2m 15s) → output_files: [file1.md, file2.md]
  - Workflow B: ✅ SUCCESS (1m 58s) → output_files: [file3.md, file4.md]
  - Workflow C: ✅ SUCCESS (2m 22s) → output_files: [file5.md, file6.md]

  **Combined Result:** Merged 6 output files
  **Total Zone Time:** 2m 22s (parallel execution faster than sequential 6m 35s)
  **Tokens Used:** 12,514

**Validation:**
- Read-Write conflicts: ✅ None detected
- Write-Write conflicts: ✅ None detected
- Content conflicts: ✅ None detected
- Output integrity: ✅ All files valid

**Next Zone:** Zone 2 (Sequential, depends on Zone 1)
```

**Message to user:**
```
"✅ Zone 1 Results Aggregated:

Execution Summary:
| Workflow | Status | Duration | Output Files | Tokens |
|----------|--------|----------|--------------|--------|
| A | SUCCESS | 2m 15s | 2 files | 4,521 |
| B | SUCCESS | 1m 58s | 2 files | 3,890 |
| C | SUCCESS | 2m 22s | 2 files | 4,103 |

Zone Total: 6 files created, 12,514 tokens, 2m 22s (parallel faster than 6m 35s sequential)

Validation: ✅ No conflicts, all outputs valid

Ready for Zone 2 sequential execution..."
```

### 2e. Dynamic Load Balancing

**Monitor agent workload during execution:**

```javascript
// During parallel execution, monitor:
agent_metrics = {
  agent_1: {task: "workflow_a", progress: "65%", tokens_used: 2890, est_complete: "1m 23s"},
  agent_2: {task: "workflow_b", progress: "48%", tokens_used: 2100, est_complete: "2m 10s"},
  agent_3: {task: "workflow_c", progress: "72%", tokens_used: 3200, est_complete: "1m 05s"}
}

// If agent gets overloaded or fails:
if (agent_2.tokens_used > 60% of token_budget) {
  // Can't assign more work to agent_2
  message = "⚠️ Agent 2 approaching token limit, no new tasks"
}

if (agent_1.progress > 95% && agent_2.progress < 30%) {
  // Could rebalance, but generally avoid mid-execution
  message = "ℹ️ Agent 1 finishing early, Agent 2 behind (expected variance)"
}

if (agent_3.status == "FAILED") {
  // Redistribute its work
  remaining_work = split_workflow_task(agent_3.task)
  Task({...}) // assign remaining work to idle agent
}
```

**Message to user:**
```
"⏳ Parallel Execution In Progress...

Agent Status:
- Agent 1 (Workflow A): 65% - ~1m 23s remaining
- Agent 2 (Workflow B): 48% - ~2m 10s remaining
- Agent 3 (Workflow C): 72% - ~1m 05s remaining

Load Distribution: Balanced
ETA (max): 2m 22s"
```

**Auto-Scale Logic:**
- If agent fails → redistribute tasks to healthy agents
- If agent overloaded → mark it unavailable for new assignments
- If agent idle before zone done → optimize by reassigning lighter tasks
- Track token budget per agent to avoid exceeding limits

### 4. Checkpoint After Each Phase (YOLO-Aware)

After each phase:

**A. Create Checkpoint File**

Create checkpoint file in `{intermediateFolder}`:

**File:** `checkpoint-phase-{N}-{sessionId}.md`

Use template `{checkpointTemplate}` and populate with:
- sessionId: Current session ID
- timestamp: Current date/time
- phaseNumber: Current phase number
- checkpointId: Unique checkpoint identifier
- totalPhases: Total number of phases
- workflows: List of workflows in this phase with status
- executionType: Parallel or Sequential
- completed: List of completed workflows with outputs
- failed: List of failed workflows with errors
- skipped: List of skipped workflows with reasons
- newFiles: New files created
- modifiedFiles: Files modified
- contextUsage: Token usage statistics
- nextPhaseNumber: Next phase to execute

**B. Present Checkpoint Menu (YOLO-Aware)**

**CONDITIONAL CHECKPOINT PRESENTATION:**

```
IF yolo_level >= 5:
  → Skip checkpoint menu entirely
  → Auto-proceed to next phase
  → Only report critical issues
  → Continue until execution complete

IF yolo_level >= 3 and < 5:
  → Display simplified menu: **[C] Continue [P] Pause**
  → Show: Phase {N} complete, {files} created
  → Auto-continue if user doesn't explicitly pause

IF yolo_level < 3:
  → Display full menu: **[C] Continue [P] Pause [A] Elicitation [S] Save Report**
  → Wait for user selection
```

**Full Checkpoint Menu (Manual Mode - yolo_level < 3):**

```
**📍 CHECKPOINT: Phase {N} Complete**

Phase {N} of {Total} finished.
Workflows: {Completed}/{Total} successful
Files created: {Count}
Context usage: {Tokens} tokens

**Options:**
[C] Continue to next phase
[P] Pause orchestration (resume later)
[A] Advanced Elicitation on results
[S] Save detailed report and exit

Select: [C/P/A/S]
```

**Simplified Menu (YOLO Level 3-4):**

```
**Phase {N}/{Total} Complete** - {Count} files created

[C] Continue  [P] Pause
```

See `/data/execution-patterns.md` for checkpoint pattern.

### 5. Update Progress Document

After each phase, update `{workflowPlanFile}`:

```markdown
## Execution Progress

**Current Phase:** [X] of [N]
**Status:** [In Progress / Paused / Complete]

**Completed Workflows:**
- [Workflow name] — [result]

**Pending Workflows:**
- [Workflow name]

**Last Checkpoint:** [timestamp]
```

Update frontmatter: `stepsCompleted: ['step-01-discovery', 'step-02-workflow-selection', 'step-03-orchestration-plan', 'step-04-execution-loop']`

### 6. Handle Failures

If workflow fails, present failure menu.
See `/data/execution-patterns.md` for failure handling pattern.

### 7. Execution Complete

"**🎉 EXECUTION COMPLETE**

All phases finished successfully!

**Summary:**
- Total workflows executed: [N]
- Successful: [X]
- Failed: [Y]
- Skipped: [Z]

**Output files created/updated:**
- [list files]

Now proceeding to cascade synchronization..."

### 8. Present MENU OPTIONS (YOLO-Aware)

**CONDITIONAL MENU PRESENTATION:**

```
IF yolo_level >= 5:
  → Skip menu entirely
  → Auto-proceed to step-05
  → Update plan: stepsCompleted: [all phases complete]
  → Load: {nextStepFile}
  → Log: "YOLO Level {level} - Auto-proceeded to cascade sync"

IF yolo_level >= 3 and < 5:
  → Display simple menu: **[C] Continue to Sync**
  → Auto-proceed if user doesn't respond within timeout
  → Skip [A/P] options

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

- Update plan: stepsCompleted: [all execution phases complete]
- Load: `{nextStepFile}` (step-05-cascade-sync.md)
- Log action with execution summary

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All phases executed according to plan
- Parallel zones used subagents correctly
- Large files handled without context overflow
- Progress tracked and documented
- User could pause/continue at checkpoints
- Ready for cascade synchronization

### ❌ SYSTEM FAILURE:

- Deviating from orchestration plan
- Not handling large files properly
- No checkpoint system
- Not reporting progress

**Master Rule:** Execute plan precisely, handle large files safely, track progress, allow pauses.
