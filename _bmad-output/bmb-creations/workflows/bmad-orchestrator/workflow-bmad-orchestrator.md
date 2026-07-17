---
name: bmad-orchestrator
description: Meta-workflow that dynamically selects and orchestrates BMAD workflows with parallel execution, conflict detection, and large file support
createWorkflow: './steps-c/step-01-discovery.md'
conversionWorkflow: './steps-c/step-00-conversion.md'
yolo_mode: false
yolo_level: 1
approval_method: "party-mode"
fallback_on_ambiguity: "ask-user"
parallel_execution: true
save_checkpoints: "on-error"
csvIntegration: true
mcpSearchEnabled: true
yoloModeSupported: true
parallelExecutionSupported: true
supportedModules: [bmm, bmb, tea, cis, core]
workflowCount: 52
maxParallelAgents: 8
estimatedDuration: "varies"
---

# BMAD Orchestrator

**Goal:** Dynamically orchestrate BMAD workflows with intelligent selection, parallel execution, conflict detection, and large file support.

**Your Role:** You are an orchestration architect that analyzes tasks, selects appropriate BMAD workflows, plans execution (sequential vs parallel), and synchronizes documents across the entire cascade.

**Advanced Features:**
- CSV-driven workflow selection (52 workflows indexed in workflow-manifest.csv)
- MCP search integration (Memory + OctoCode + Brave/Tavily + Context7)
- YOLO mode auto-execution (configurable automation levels 1-5)
- Parallel swarm execution (automatic conflict detection and dynamic load balancing)
- Cascade synchronization (multi-document sync with consistency verification)
- Traceability matrix (complete workflow audit trail and requirements coverage)

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** with TRI approach (Analyze → Plan → Execute):

### Core Principles

- **Dynamic Workflow Selection:** Analyzes task and selects appropriate BMAD workflows from library
- **Parallel Execution Zones:** Detects conflicts and marks safe parallel operations
- **Large File Safe:** Uses range read and append-only for big files
- **Multi-Runtime Support:** Cline, Claude Code, Codex with their subagent capabilities
- **Advanced Elicitation + Party Mode:** Available at every step via [A/P/C] menu

### Step Processing Rules

1. **READ COMPLETELY:** Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE:** Execute all numbered sections in order
3. **MENU AT EVERY STEP:** [A] Advanced Elicitation | [P] Party Mode | [C] Continue
4. **SAVE STATE:** Update `stepsCompleted` in frontmatter before loading next step
5. **CONFLICT DETECTION:** Analyze read/write dependencies before parallel execution

---

## YOLO MODE CONFIGURATION

**YOLO = You Only Orchestrate Once** — Automatically execute workflow without user menus or approval at each step.

### Mode Levels

| Level | Name | Control | Use Case |
|-------|------|---------|----------|
| **1** | Manual | Full user control at every step | Complex decisions, training, high uncertainty |
| **3** | Semi-Auto | Auto-proceed through steps, user confirm on ambiguous choices | Trusted workflows, some guidance needed |
| **5** | Full Auto | Continuous execution, no user interaction | Proven workflows, high confidence, batch processing |

### Configuration Parameters

```yaml
yolo_mode: false              # Enable/disable YOLO mode (default: false)
yolo_level: 1                 # 1=max control, 5=max auto (default: 1)
approval_method: "party-mode" # party-mode | advanced-elicitation | none
fallback_on_ambiguity: "ask-user"  # ask-user | pick-best | abort
parallel_execution: true      # Allow parallel execution where safe
save_checkpoints: "on-error"  # always | on-error | never
```

### Default Presets

**YOLO Level 1 (Manual Mode):**
- Full user control at every step
- [A/P/C] menus everywhere
- User confirmation required for all decisions
- Best for: Complex workflows, training, high uncertainty

**YOLO Level 3 (Semi-Auto Mode):**
- Auto-proceed through steps
- User confirmation only on ambiguous decisions
- Party Mode for difficult choices (if approval_method: party-mode)
- Best for: Trusted workflows, semi-autonomous operation

**YOLO Level 5 (Full Auto Mode):**
- Continuous execution without pauses
- No user interaction needed
- Only critical issues reported
- Best for: Proven workflows, batch processing

### Usage Examples

```bash
# Interactive mode (default)
orchestrate --task "design new feature" --yolo 1

# Semi-automatic mode (recommended)
orchestrate --task "implement feature" --yolo 3 --approval-method party-mode

# Full automation
orchestrate --task "refactor service" --yolo 5 --approval-method none
```

### Behavior Per YOLO Level

```
Step Execution:
  Level 1: Show menu [A/P/C] → Wait for user
  Level 3: Auto-proceed → Show menu only on ambiguity
  Level 5: Auto-proceed continuously → No menus

Decision Making:
  Level 1: All decisions require user input
  Level 3: Auto-decide if clear, ask if ambiguous
  Level 5: Auto-pick best option using fallback_on_ambiguity

Checkpoints:
  Level 1: Checkpoint after every step
  Level 3: Checkpoint on phase boundaries
  Level 5: Checkpoint on errors only (or not at all)

Reporting:
  Level 1: Detailed output at each step
  Level 3: Summary at phase boundaries
  Level 5: Final summary only
```

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/bmb/config.yaml

### 2. Mode Selection

"**BMAD Orchestrator** — Dynamic workflow orchestration with parallel execution.

**[F]rom scratch** — Start new orchestration
**[C]ontinue** — Resume from previous session (step-01b-continue.md)

Please select: [F]rom scratch / [C]ontinue"

### 3. Route to First Step

- **IF F:** Load, read completely, then execute `{createWorkflow}` (steps-c/step-01-discovery.md)
- **IF C:** Load, read completely, then execute `step-01b-continue.md`

---

## WORKFLOW PHASES (TRI Approach)

### PHASE 1: ANALYZE
- **step-01-discovery:** Understand task and files
- **step-02-workflow-selection:** Propose BMAD workflows from library

### PHASE 2: PLAN
- **step-03-orchestration-plan:** Build dependency graph, detect conflicts, mark parallel zones

### PHASE 3: EXECUTE
- **step-04-execution-loop:** Execute workflows (parallel via subagents, sequential as needed)
- **step-05-cascade-sync:** Synchronize related documents
- **step-06-validation:** Verify integrity, generate traceability matrix

---

## CRITICAL FEATURES

### Parallel Execution
- **Conflict Detection:** Analyzes read-after-write, write-after-write dependencies
- **Safe Zones:** Independent operations marked for parallel execution
- **Subagent Dispatch:** Uses platform-specific subagents (Cline use_subagents, Claude MCP, Codex subagents)

### Large File Support
- **Range Read:** Read only necessary file ranges, never entire large files
- **Append-Only Building:** Build output documents incrementally
- **Context Management:** Monitor and control context window usage

### Menu System (Every Step)
**[A]** Advanced Elicitation — Deep exploration with 50+ methods
**[P]** Party Mode — Multi-agent discussion
**[C]** Continue — Proceed to next step

---

## OUTPUT

**Primary:** Orchestrated documents synchronized across cascade
**Secondary:** Traceability matrix, execution log, conflict analysis report
