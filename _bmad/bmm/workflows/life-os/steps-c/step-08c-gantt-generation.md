---
name: 'step-08c-gantt-generation'
description: 'Generate Gantt chart from milestones with multiple output formats'
stepType: Create
estimatedMinutes: 10
trackApplicable: [Deep]
prerequisites: [step-08b]
outputs: [project-XXX/gantt.md, project-XXX/gantt-ascii.txt]
nextStepFile: '../steps-x/step-x-01-kickoff.md'
milestonesFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}/milestones.md'
ganttFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}/gantt.md'
ganttAsciiFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}/gantt-ascii.txt'
projectPlanFile: '{bmb_creations_output_folder}/life-os/plans/{project_id}-plan.md'
journalFile: '{bmb_creations_output_folder}/life-os/journal/{project_id}.md'
chartTemplatesFile: '../data/gantt-chart-templates.md'
dependencyAlgorithmFile: '../data/dependency-graph-algorithm.md'
criticalPathMethodFile: '../data/critical-path-method.md'
---

# Step 8c: Gantt Chart Generation

## STEP GOAL

Generate visual Gantt chart from milestones in multiple formats: ASCII (terminal), Mermaid (markdown), and structured data.

**Quality Reference:** `../data/validation-examples.md`

**Algorithm References:**
- **Chart Templates:** `{chartTemplatesFile}`
- **Dependency Logic:** `{dependencyAlgorithmFile}`
- **Critical Path:** `{criticalPathMethodFile}`

**Quality Standards:**
- Clearly annotate milestone_id, critical_path flag, total slack per IDEAL 1.14 so execution reviewers can trace dependencies and risks.
- ASCII Gantt: Clear terminal-friendly visualization (80 char width)
- Mermaid Gantt: Renderable in GitHub, VS Code, Obsidian
- Critical Path: Visually highlighted in all formats
- Dependencies: Arrow/line connections between milestones

## EXECUTION RULES

- 🛑 Facilitator role only - generate from milestone data
- 📖 Read algorithm files first for calculation logic
- 📊 Load milestones from step-08b output
- ✅ Use `{communication_language}` for all output
- 🎯 Auto-generate both ASCII and Mermaid formats
- 💬 Present options for customization

## EXECUTION PROTOCOLS

Load {milestonesFile} from step-08b. Calculate timeline grid using {dependencyAlgorithmFile}. Generate visualizations per {chartTemplatesFile}. Apply critical path highlighting per {criticalPathMethodFile}. Save to multiple formats.

---

## MANDATORY SEQUENCE

### 1. Load Milestones Data

Open {milestonesFile}. Extract:
- All milestones with dates and durations
- Dependencies between milestones
- Critical path markers
- Project start and end dates

```
📊 MILESTONES LOADED

Project: {project_name}
Milestones: {count}
Timeline: {start_date} → {end_date} ({total_weeks} weeks)
Critical Path: {critical_path_ids}

Ready to generate Gantt chart?
[Y]es / [C]onfigure options first
```

**IF C selected:** Go to Section 7 (Gantt Configuration Options)

### 2. Calculate Timeline Grid

Apply algorithm from {dependencyAlgorithmFile}:
- Calculate total_weeks = (end_date - start_date) / 7
- Determine grid resolution (daily/weekly/monthly)
- Generate week_markers[] and month_markers[]
- Calculate milestone positions (start_column, width)

**Reference:** See "Timeline Grid Calculation" section in {dependencyAlgorithmFile}

### 3. Generate ASCII Gantt Chart

Apply template from {chartTemplatesFile}:
- Select ASCII format based on timeline length
- Render milestones with █ for work, ░ for slack
- Highlight critical path with bold/different characters
- Add dependency arrows with │ and ─ markers
- Include TODAY marker if project in progress

**Output to console:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          PROJECT GANTT CHART
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{ASCII_CHART_FROM_TEMPLATE}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Reference:** See "ASCII Gantt Format" section in {chartTemplatesFile}

### 4. Generate Mermaid Gantt Chart

Apply template from {chartTemplatesFile}:
- Use complete Mermaid document structure
- Mark critical path milestones with `:crit`
- Add dependency chains with `after` syntax
- Include milestone details table
- Add slack analysis table

**Save complete document to {ganttFile}**

**Reference:** See "Mermaid Gantt Format" section in {chartTemplatesFile}

### 5. Calculate Critical Path

Apply CPM algorithm from {criticalPathMethodFile}:
- Run forward pass to calculate ES/EF
- Run backward pass to calculate LS/LF
- Calculate total slack and free slack
- Identify critical path milestones (slack = 0)
- Assess risk level (LOW/MEDIUM/HIGH)

**Reference:** See "Critical Path Algorithm" section in {criticalPathMethodFile}

### 6. Save Output Files

**Save to {ganttFile}:**
- Complete Mermaid chart with documentation
- Milestone details table
- Critical path analysis
- Slack analysis table

**Save to {ganttAsciiFile}:**
- ASCII visualization with legend
- Critical path summary
- Generation timestamp

**Update {projectPlanFile}:**
```markdown
## Gantt Chart (Generated {YYYY-MM-DD})

[View interactive chart: {ganttFile}]

### ASCII Preview
{ABBREVIATED_ASCII_PREVIEW}

### Key Dates
- Project Start: {start_date}
- M1 Complete: {m1_end}
- M2 Complete: {m2_end}
- Project End: {end_date}
```

**Update {journalFile}:**
```markdown
## {YYYY-MM-DD} - Gantt Chart Generated

**Action:** Generated project timeline visualization
**Formats:** ASCII (.txt), Mermaid (.md)
**Critical Path:** {milestone_ids} ({weeks} weeks)
**Files:**
  - {ganttFile}
  - {ganttAsciiFile}
**Next Step:** Project Kickoff (step-x-01)
```

### 7. Gantt Configuration Options

**IF user selected [C]onfigure in Section 1:**

```
GANTT CONFIGURATION

Current Settings:
  1. Grid Resolution: [W]eekly / [D]aily / [M]onthly
  2. Weekend Exclusion: [Y]es / [N]o
  3. Today Marker: [S]how / [H]ide
  4. Output Formats: [A]ll / [M]ermaid only / [T]ext only
  5. Color Scheme: [D]efault / [H]igh contrast / [P]rint-friendly

Enter setting number to change, or [B]ack to generate:
```

**Configuration Schema:** See {chartTemplatesFile} "Configuration Schema" section

---

### 8. Display Final Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GANTT CHART GENERATED

✅ ASCII chart: {ganttAsciiFile}
✅ Mermaid chart: {ganttFile}
✅ Project plan updated: {projectPlanFile}
✅ Journal updated: {journalFile}

Timeline Summary:
  Start: {start_date}
  End: {end_date}
  Duration: {total_weeks} weeks
  Critical Path: {critical_weeks} weeks ({percentage}%)

{ASCII_PREVIEW_HERE}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 9. Menu Options

```
GANTT COMPLETE - What's next?

[K] Kickoff Project (proceed to execution - step-x-01)
[V] View full ASCII chart
[M] Open Mermaid file
[R] Regenerate with different options
[E] Export to additional formats (CSV, iCal)

Choice: [K/V/M/R/E]
```

**Menu Logic:**
- **K:** Execute {nextStepFile} (steps-x/step-x-01-kickoff.md)
- **V:** Display full ASCII Gantt from {ganttAsciiFile}
- **M:** Output path to {ganttFile} for opening
- **R:** Return to Section 7 (Configuration)
- **E:** Export submenu - CSV/iCal formats per {chartTemplatesFile}

**Export References:**
- **CSV Format:** See {chartTemplatesFile} "Export Formats → CSV"
- **iCal Format:** See {chartTemplatesFile} "Export Formats → iCal"

**RULES:** Wait for user input. Only proceed to Kickoff when K selected.

---

## Quick Feedback

How was this step? 👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or Enter to skip]

**Save to memory:**
```bash
npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-08c-gantt-generation:{timestamp}" --content "{\"step\":\"step-08c-gantt-generation\",\"rating\":\"{rating}\",\"formats_generated\":[\"ascii\",\"mermaid\"],\"timeline_weeks\":{weeks},\"timestamp\":\"{ISO_datetime}\"}"
```

---

## SUCCESS/FAILURE METRICS

**SUCCESS:**
- ASCII Gantt generated and readable (80 char width)
- Mermaid Gantt valid syntax (renders in GitHub/VS Code)
- Critical path visually highlighted
- Dependencies shown correctly
- All files saved: gantt.md, gantt-ascii.txt
- Project plan and journal updated

**FAILURE:**
- Gantt unreadable (formatting broken)
- Mermaid syntax errors (won't render)
- Critical path not highlighted
- Dependencies missing or incorrect
- Missing output files

**Master Rule:** Charts must be accurate, readable, and actionable for project tracking.
