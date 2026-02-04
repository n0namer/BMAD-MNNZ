---
name: 'step-07-calendar-sync'
description: 'Translate the approved project into a timeline and calendar plan'
nextStepFile: './step-08-deep-plan.md'
completeStepFile: './step-09-complete.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
outputProjectFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}.md'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
snapshotTemplate: '../templates/project-snapshot.template.md'
journalTemplate: '../templates/project-journal.template.md'
plansFolder: '{bmb_creations_output_folder}/life-os/plans'
planTemplate: '../templates/project-plan.template.md'
decisionsFolder: '{bmb_creations_output_folder}/life-os/decisions'
decisionsTemplate: '../templates/project-decisions.template.md'
---

# Step 7: Calendar Sync

## STEP GOAL:

Translate the approved project into a realistic timeline and capture it in a project file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight risks, opportunities, and next best actions based on current context
- 🧭 If WIP/kill criteria or portfolio risks appear, surface them early with a brief recommendation
- ✅ Ask for user confirmation before taking any proactive action that changes scope or priorities
- 🎯 Focus ONLY on timeline and calendar alignment
- 🚫 FORBIDDEN to add new scope
- 💬 Confirm dates and capacity with the user
- 💬 Ask 1–2 questions at a time and adapt to the user’s responses

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

- 🎯 Confirm project readiness and start date
- 💾 Write a project file to {outputProjectFile}
- 📖 Append timeline summary to {workflowPlanFile}
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES:

- Available context: workflow plan (idea, consilium, scoring)
- Focus: scheduling and calendar alignment
- Dependencies: step-06 integration must be complete

## MANDATORY SEQUENCE

### 1. Confirm Schedule Inputs

Ask for schedule inputs progressively (1–2 at a time), covering:
- Target start date
- Target end date or duration
- Weekly capacity (hours/week)
- Milestones (if any)

If scheduling trade-offs are unclear, use Search Orchestrator to propose 2–3 scheduling strategies.

Validation hints:
- If end date is before start date, ask to корректировать даты.
- If capacity is 0 or unrealistically high, ask to уточнить допустимую нагрузку.

### 2. Propose Timeline

Draft a simple timeline with 3–6 milestones and confirm with the user.

### 3. Create Project File

Write to {outputProjectFile}:
```markdown
---
projectId: {project_id}
title: {project_title}
status: PLANNED
startDate: {start_date}
endDate: {end_date}
capacityPerWeek: {hours}
---

# {project_title}

## Timeline
- {milestone}: {date}
- {milestone}: {date}

## Notes
- {constraints}
```

### 4. Append to Workflow Plan

Append:
```markdown
## Calendar Sync

**Start Date:** {start_date}
**End Date:** {end_date}
**Capacity:** {hours}/week

**Milestones:**
- {milestone}: {date}
- {milestone}: {date}
```

### 5. Create Snapshot, Journal, and Project Plan

Ensure folders exist:
- {snapshotsFolder}
- {journalFolder}
- {plansFolder}
- {decisionsFolder}

Create:
- Snapshot file in {snapshotsFolder} (use {snapshotTemplate})
- Journal file in {journalFolder} (use {journalTemplate})
- Project plan file in {plansFolder} (use {planTemplate})
- Decisions file in {decisionsFolder} (use {decisionsTemplate})

Include in snapshot:
- Goal
- Current status (PLANNED)
- Next actions
- Last decision (Calendar Sync approved)

Append an initial journal entry with the scheduling decision.

Initialize the project plan with:
- Idea summary
- Consilium summary
- Scoring summary
- Integration summary
- Calendar summary

### 6. Present MENU OPTIONS

Display: "**Select:** [D] Deep Plan [C] Complete"

#### Menu Handling Logic:
- IF D: Load, read entire file, then execute {nextStepFile}
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {completeStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'D'
- If user selects 'C', ensure all outputs are saved before completion

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Timeline confirmed by user
- Project file created at {outputProjectFile}
- Plan updated with schedule

### ❌ SYSTEM FAILURE:
- Timeline without confirmation
- Project file not written
- Missing schedule in workflow plan

**Master Rule:** Scheduling must be confirmed and saved to the project file.




