---
name: 'step-01-update-project'
description: 'Update an existing project status, timeline, or resources'
nextStepFile: './step-02-rescoring.md'
deepPlanStepFile: './step-04-deep-plan.md'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
plansFolder: '{bmb_creations_output_folder}/life-os/plans'
---

# Edit Step 1: Update Project

## STEP GOAL:

Select a project to update and capture changes to status, timeline, or resources.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight risks, opportunities, and next best actions based on current context
- 🧭 If WIP/kill criteria or portfolio risks appear, surface them early with a brief recommendation
- ✅ Ask for user confirmation before taking any proactive action that changes scope or priorities
- 🎯 Focus ONLY on updates to an existing project
- 🚫 FORBIDDEN to create new projects here
- 💬 Confirm all edits with the user
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

- 🎯 Identify the target project in {projectsFolder}
- 💾 Append update notes to {workflowPlanFile}
- 📖 Do not rescore here (rescoring happens in next step)
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES:

- Available context: project files in {projectsFolder}
- Focus: status, timeline, resources updates
- Dependencies: edit mode invoked by workflow routing

## MANDATORY SEQUENCE

### 1. Select Project

Ask:
"Какой проект вы хотите обновить?  
Если есть ID/название — укажите.  
Если нет — опишите, я помогу найти."

If multiple projects match or the user is unsure:
- Provide up to 5 closest matches and ask to choose by number
- Offer to filter by status (PLANNED / ACTIVE / BLOCKED / DONE)

### 2. Auto-Select Action

Default to Update (status/timeline/resources).
After updates, auto-trigger Deep Plan refresh using {deepPlanStepFile}.

If update options are unclear, use Search Orchestrator to propose 2–3 update strategies.

### 3. Capture Updates

Ask for updates to (progressively, 1–2 at a time):
- Статус (PLANNED / ACTIVE / BLOCKED / DONE)
- Таймлайн (даты / длительность)
- Ресурсы (время, бюджет, команда)

### 4. Append to Workflow Plan

Append:
```markdown
## Edit: Update Project

**Project:** {project_id} — {title}
**Changes:**
- Status: {from} → {to}
- Timeline: {from} → {to}
- Resources: {from} → {to}
```

### 5. Update Snapshot and Journal

Update the project snapshot in {snapshotsFolder} (status, dates, next actions).
Append a journal entry in {journalFolder} summarizing the change and rationale.
Update the project plan in {plansFolder} with an iteration entry and revised fields if needed.

### 6. Auto-Refresh Deep Plan

Load and execute {deepPlanStepFile} after updates are saved.

### 7. Present MENU OPTIONS

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Project identified
- Updates captured and confirmed
- Plan updated

### ❌ SYSTEM FAILURE:
- Updating without confirmation
- Creating new project
- Skipping save before continue

**Master Rule:** Capture only confirmed updates.



