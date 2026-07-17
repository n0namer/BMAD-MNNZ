# YOLO MODE QUICK REFERENCE

## What is YOLO Mode?

YOLO = **You Only Orchestrate Once** - Automatic workflow execution without user menus at each step.

## Configuration

Add to workflow frontmatter:

```yaml
yolo_mode: true            # Enable YOLO mode
yolo_level: 3              # 1=manual, 3=semi-auto, 5=full-auto
approval_method: "party-mode"
```

## Behavior by Level

### Level 1: MANUAL (Default)
- User menu [A/P/C] at every step
- Full control, no automation
- Best for: Training, complex decisions

**Checkpoints:**
- Step 1: Discovery menu
- Step 2: Workflow selection menu
- Step 3: Plan review menu
- Step 4: Execution checkpoints
- Step 5: Sync approval menus
- Step 6: Validation menu

### Level 3: SEMI-AUTOMATIC (Recommended)
- Auto-proceeds through steps
- User menu only on ambiguous decisions
- Party Mode for difficult choices
- Simplified checkpoints ([C] Continue / [P] Pause)

**Checkpoints:**
- Step 1: Skip menu, auto-proceed
- Step 2: Auto-select if confident
- Step 3: Skip menu, auto-proceed
- Step 4: Simplified checkpoints [C/P]
- Step 5: Auto-sync with logging
- Step 6: Skip menu, auto-complete

### Level 5: FULL AUTOMATION
- Continuous execution, no pauses
- No user interaction needed
- Auto-handles all decisions
- Only critical issues reported

**Checkpoints:**
- Step 1: Auto-extract task
- Step 2: Auto-select best workflow
- Step 3: Auto-generate plan
- Step 4: No checkpoints, continuous execution
- Step 5: Auto-apply all changes
- Step 6: Auto-validate and complete

## Quick Start Examples

### Run Interactive Mode
```bash
orchestrate --task "design feature" --yolo 1
```

### Run Semi-Automatic (Recommended)
```bash
orchestrate --task "implement feature" --yolo 3 --approval-method party-mode
```

### Run Full Automation
```bash
orchestrate --task "refactor code" --yolo 5 --approval-method none
```

## Step-by-Step Changes

### Step 1: Discovery
- **yolo_level < 3:** Show [A/P/C] menu
- **yolo_level >= 3:** Auto-extract task, auto-proceed

### Step 2: Workflow Selection
- **yolo_level < 3:** Show workflow options [A/P/C]
- **yolo_level >= 4:** Auto-select best workflow
- **yolo_level 3-4:** Party Mode consensus select

### Step 3: Orchestration Plan
- **yolo_level < 3:** Review plan [A/P/C]
- **yolo_level >= 3:** Auto-generate, auto-proceed

### Step 4: Execution Loop
- **yolo_level < 3:** Full checkpoint [C/P/A/S]
- **yolo_level 3-4:** Simplified [C/P]
- **yolo_level >= 5:** No checkpoints, continuous

### Step 5: Cascade Sync
- **yolo_level < 3:** [A/R/S/E] for each document
- **yolo_level >= 3:** Auto-apply all changes

### Step 6: Validation
- **yolo_level < 3:** Review report [A/P/C]
- **yolo_level >= 3:** Auto-validate, auto-complete

## Menu Behavior Matrix

| Step | Level 1 | Level 3 | Level 5 |
|------|---------|---------|---------|
| 1 | [A/P/C] | Auto | Auto |
| 2 | [A/P/C] | Auto/Party | Auto |
| 3 | [A/P/C] | Auto | Auto |
| 4 | [C/P/A/S] | [C/P] | None |
| 5 | [A/R/S/E] | Auto | Auto |
| 6 | [A/P/C] | Auto | Auto |

## Key Features

**Auto-Selection (Step 2)**
- Analyzes task against 75+ workflows
- Confidence scoring and semantic matching
- Picks best match automatically

**Auto-Planning (Step 3)**
- Generates dependency graph
- Detects parallel zones
- Selects runtime environment

**Auto-Execution (Step 4)**
- Spawns parallel agents safely
- Monitors progress
- Aggregates results

**Auto-Sync (Step 5)**
- Identifies related documents
- Propagates changes
- Maintains consistency

**Auto-Validation (Step 6)**
- Runs all checks
- Generates traceability matrix
- Auto-completes workflow

## When to Use Each Level

**Level 1 (Manual)** - Use when:
- Learning the system
- Making complex decisions
- High uncertainty
- Need full control

**Level 3 (Semi-Auto)** - Use when:
- Familiar with workflows
- Want some autonomy
- Need checkpoints
- Balanced approach

**Level 5 (Full-Auto)** - Use when:
- Proven workflows
- High confidence
- Batch processing
- Unattended execution

## Configuration Parameters

```yaml
yolo_mode: true/false           # Enable/disable YOLO mode
yolo_level: 1-5                 # Autonomy level
approval_method: "party-mode"   # party-mode | advanced-elicitation | none
fallback_on_ambiguity: "ask-user" # ask-user | pick-best | abort
parallel_execution: true/false  # Allow parallel zones
save_checkpoints: "on-error"    # always | on-error | never
```

## Logging

All YOLO decisions are logged:
- Step transitions
- Auto-selections
- Menu skips
- Decision reasoning

## File Locations

1. Workflow: `workflow-bmad-orchestrator.md`
2. Steps: `steps-c/step-0X-*.md` (6 files)
3. Report: `YOLO-MODE-IMPLEMENTATION-REPORT.md`
4. This guide: `YOLO-MODE-QUICK-REFERENCE.md`

## Implementation Status

✅ All 7 files updated
✅ Complete step coverage (1-6)
✅ Menu logic implemented
✅ Configuration documented
✅ Examples provided
✅ Ready for testing

## Next Features

- Level 4 (intermediate auto)
- Auto-timeout for unattended mode
- YOLO performance metrics
- Mid-workflow level switching
