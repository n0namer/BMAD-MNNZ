---
name: 'step-08b-milestone-planning'
description: 'Create project milestones with dependencies and target dates'
stepType: Create
estimatedMinutes: 20
trackApplicable: [Deep]
prerequisites: [step-08, step-08.5]
outputs: [project-XXX/milestones.md, project-XXX/gantt.md]
nextStepFile: './step-08c-gantt-generation.md'
projectPlanFile: '{bmb_creations_output_folder}/life-os/plans/{project_id}-plan.md'
milestonesFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}/milestones.md'
snapshotFile: '{bmb_creations_output_folder}/life-os/snapshots/{project_id}.md'
journalFile: '{bmb_creations_output_folder}/life-os/journal/{project_id}.md'
capacityRef: '../data/foundation-examples/capacity.example.yaml'
dependencyPatterns: '../data/milestone-dependency-patterns.md'
criticalPathAlgorithm: '../data/milestone-critical-path.md'
gateCriteria: '../data/milestone-gate-criteria.md'
---

# Step 8b: Milestone Planning

## STEP GOAL

Decompose project into 3-5 milestones with target dates, dependencies, and critical path analysis.

**Quality Reference:** `../data/validation-examples.md` | **Patterns:** `{dependencyPatterns}` | **Algorithm:** `{criticalPathAlgorithm}` | **Gates:** `{gateCriteria}`

**Quality Standards:**
- **Milestones:** 3-5 per project (min 3, max 7 for complex projects)
- **Dependencies:** Every milestone except first must have at least 1 dependency (see patterns in `{dependencyPatterns}`)
- **Dates:** Target dates based on estimates + available capacity
- **Coverage:** Milestones must cover 100% of L2 phases from Deep Plan

## EXECUTION RULES

- 🛑 Facilitator role only - no auto-generation without user input
- 📖 Read complete step file first
- 💬 Ask 1-2 questions at a time, confirm each milestone
- 📊 Use capacity from Foundation Steps (0.6) for date calculations
- ✅ Use `{communication_language}` for all output
- 🎯 Use subprocess for dependency analysis (Pattern 3: Data Operations)
- 💬 Return structured milestone map with critical path highlighted

## EXECUTION PROTOCOLS

Load {projectPlanFile}, {snapshotFile}, {journalFile}. Extract Deep Plan L2 phases. Calculate realistic dates using capacity multiplier from Foundation Steps. Apply patterns from `{dependencyPatterns}`.

---

## MANDATORY SEQUENCE

### 1. Load Context & Extract L2 Phases

Open {projectPlanFile}. Extract:
- **L2 Phases** from Deep Plan (major work areas)
- **L3 Milestones** if already defined (from step-08)
- **Capacity data** from Foundation Steps (hours/week, speed multiplier)

```
📊 DEEP PLAN SUMMARY
Project: {project_name}
L2 Phases identified: {count}
  1. {phase_1_name} - {estimate_hours}h
  2. {phase_2_name} - {estimate_hours}h
  ...
Capacity: {hours_per_week}h/week
Speed Multiplier: {speed_multiplier}x

Ready to create milestones from these phases?
[Y]es / [M]odify phases first
```

**IF M selected:** Return to step-08 for phase adjustment.

### 2. Milestone Creation Algorithm

**Algorithm (executed by AI facilitator):**

```
INPUT: L2_phases[], capacity_hours_per_week, speed_multiplier, start_date
OUTPUT: milestones[]

FOR each phase IN L2_phases:
  1. Calculate adjusted_hours = phase.estimate_hours / speed_multiplier
  2. Calculate duration_weeks = adjusted_hours / capacity_hours_per_week
  3. Suggest milestone name (semantic grouping if phases small)
  4. Propose target_date = previous_milestone.end_date + duration_weeks

GROUPING RULES:
  - IF phase.hours < 8: Merge with adjacent phase
  - IF phase.hours > 40: Split into sub-milestones
  - Target: 3-5 milestones per project (optimal cognitive load)

DEPENDENCY DETECTION:
  - Apply patterns from {dependencyPatterns}
  - Sequential, Parallel, Convergent patterns
  - Validate: no circular dependencies

OUTPUT: milestones[] with {id, name, target_date, estimate_hours, dependencies[], stories[]}
```

### 3. Present Milestone Proposal

Display proposed milestones for user confirmation:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 MILESTONE PROPOSAL

Project: {project_name}
Timeline: {start_date} → {end_date} ({total_weeks} weeks)
Capacity: {hours_per_week}h/week × {speed_multiplier}x multiplier

┌─────────┬──────────────────────────────┬────────────┬───────────┬──────────────┐
│ ID      │ Milestone Name               │ Est. Hours │ Duration  │ Target Date  │
├─────────┼──────────────────────────────┼────────────┼───────────┼──────────────┤
│ M1      │ {milestone_1_name}           │ {hours}h   │ {weeks}w  │ {YYYY-MM-DD} │
│ M2      │ {milestone_2_name}           │ {hours}h   │ {weeks}w  │ {YYYY-MM-DD} │
│ M3      │ {milestone_3_name}           │ {hours}h   │ {weeks}w  │ {YYYY-MM-DD} │
│ M4      │ {milestone_4_name}           │ {hours}h   │ {weeks}w  │ {YYYY-MM-DD} │
└─────────┴──────────────────────────────┴────────────┴───────────┴──────────────┘

Dependencies (see patterns: {dependencyPatterns}):
  M1 → (none, start milestone)
  M2 → M1 (sequential)
  M3 → M1 (parallel with M2)
  M4 → M2, M3 (convergent)

Critical Path: M1 → M2 → M4 (longest chain: {critical_path_weeks} weeks)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A]ccept milestones
[E]dit milestone (specify ID)
[M]erge two milestones
[S]plit milestone into sub-milestones
[D]ependencies - modify

Choice: [A/E/M/S/D]
```

### 4. Critical Path Analysis (Subprocess)

**Launch subprocess that applies algorithm from `{criticalPathAlgorithm}`:**
1. Builds dependency graph from milestones
2. Calculates earliest/latest times (ES, EF, LS, LF)
3. Identifies critical path: milestones where ES = LS (no slack)
4. Calculates total float for non-critical milestones

**Display results (format from `{criticalPathAlgorithm}`):**
```
🎯 CRITICAL PATH ANALYSIS

Critical Path (no slack - delays here delay entire project):
  M1 (2w) → M2 (3w) → M4 (2w) = 7 weeks total

Non-Critical (has slack - can absorb delays):
  M3: 1.5 weeks slack (can start 2026-02-21 to 2026-03-07)

Project Risk Assessment:
  - Critical path length: 7 weeks (70% of total)
  - Buffer available: M3 slack = 1.5 weeks
  - Recommendation: Focus resources on M1, M2, M4

Understood? [Y]es / [E]xplain more
```

### 5. Generate Milestones File

**Save to {milestonesFile} (include gate criteria from `{gateCriteria}`):**

```yaml
# Project Milestones - {project_name}
# Generated: {ISO_datetime}
# Critical Path: {critical_path_ids}

project_id: {project_id}
project_name: "{project_name}"
created_date: "{YYYY-MM-DD}"
speed_multiplier: {speed_multiplier}
capacity_hours_per_week: {hours_per_week}

milestones:
  - id: M1
    name: "{milestone_1_name}"
    target_date: "{YYYY-MM-DD}"
    estimate_hours: {hours}
    dependencies: []
    stories: [story-001, story-002]
    success_criteria: # From {gateCriteria}
      - "{criterion_1}"
      - "{criterion_2}"
    status: PLANNED
    on_critical_path: true
    slack_weeks: 0

  - id: M2
    name: "{milestone_2_name}"
    target_date: "{YYYY-MM-DD}"
    estimate_hours: {hours}
    dependencies: [M1]
    stories: [story-003, story-004]
    success_criteria:
      - "{criterion_1}"
    status: PLANNED
    on_critical_path: true
    slack_weeks: 0

summary:
  total_milestones: {count}
  critical_path_weeks: {critical_weeks}
  project_end_date: "{YYYY-MM-DD}"
  risk_level: "{LOW|MEDIUM|HIGH}"
```

### 6. Update Project Plan & Journal

**Append to {projectPlanFile}:**

```markdown
## Milestone Planning (Generated {YYYY-MM-DD})

### Milestones Overview
| ID | Name | Target Date | Hours | Dependencies | Critical Path |
|----|------|-------------|-------|--------------|---------------|
| M1 | {name} | {date} | {h} | - | YES |
| M2 | {name} | {date} | {h} | M1 | YES |
| M3 | {name} | {date} | {h} | M1 | NO (1.5w slack) |
| M4 | {name} | {date} | {h} | M2, M3 | YES |

### Critical Path
M1 → M2 → M4 = {weeks} weeks

See full analysis: {criticalPathAlgorithm}
```

**Append to {journalFile}:**

```markdown
## {YYYY-MM-DD} - Milestone Planning

**Action:** Created {count} milestones with dependencies
**Critical Path:** {milestone_ids} ({weeks} weeks)
**References:** Dependency patterns ({dependencyPatterns}), Critical path algorithm ({criticalPathAlgorithm})
**Next Step:** Generate Gantt chart (step-08c)
```

---

### 7. Menu Options

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MILESTONE PLANNING COMPLETE

✅ {count} milestones created
✅ Dependencies mapped (see: {dependencyPatterns})
✅ Critical path identified: {weeks} weeks (algorithm: {criticalPathAlgorithm})
✅ Gate criteria defined (see: {gateCriteria})
✅ Files saved:
   - {milestonesFile}
   - {projectPlanFile} (updated)
   - {journalFile} (updated)

[G] Generate Gantt Chart (proceed to step-08c)
[R] Revise milestones
[V] View critical path details
[E] Export milestones (CSV/JSON)

Choice: [G/R/V/E]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Menu Logic:**
- **G:** Execute {nextStepFile} (step-08c-gantt-generation.md)
- **R:** Return to Section 3 (Milestone Proposal)
- **V:** Display detailed critical path analysis from `{criticalPathAlgorithm}`
- **E:** Export milestones to CSV or JSON format

**RULES:** Wait for user input. Only proceed when G selected.

---

## Quick Feedback

How was this step? 👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or Enter to skip]

**Save to memory:**
```bash
npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-08b-milestone-planning:{timestamp}" --content "{\"step\":\"step-08b-milestone-planning\",\"rating\":\"{rating}\",\"milestones_count\":{count},\"critical_path_weeks\":{weeks},\"timestamp\":\"{ISO_datetime}\"}"
```

---

## SUCCESS/FAILURE METRICS

**SUCCESS:**
- 3-5 milestones created with valid dependencies (patterns from `{dependencyPatterns}`)
- Critical path identified and documented (algorithm from `{criticalPathAlgorithm}`)
- Target dates realistic (based on capacity)
- Gate criteria defined (standards from `{gateCriteria}`)
- All L2 phases covered by milestones
- Files saved: milestones.md, project plan updated, journal updated

**FAILURE:**
- Skipping dependency validation
- Dates not based on capacity (wishful thinking)
- Critical path not calculated
- Circular dependencies created (violates `{dependencyPatterns}`)
- Less than 3 or more than 7 milestones
- Missing gate criteria

**Master Rule:** Milestones must be actionable, dated, and dependency-aware with clear success criteria.
