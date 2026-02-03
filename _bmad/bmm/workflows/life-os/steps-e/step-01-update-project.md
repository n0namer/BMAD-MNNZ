---
name: 'step-01-update-project'
description: 'Update an existing project status, timeline, or resources'
nextStepFile: './step-02-rescoring.md'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
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

- 🎯 Identify the target project in {projectsFolder}
- 💾 Append update notes to {workflowPlanFile}
- 📖 Do not rescore here (rescoring happens in next step)

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

### 2. Capture Updates

Ask for updates to (progressively, 1–2 at a time):
- Статус (PLANNED / ACTIVE / BLOCKED / DONE)
- Таймлайн (даты / длительность)
- Ресурсы (время, бюджет, команда)

### 3. Append to Workflow Plan

Append:
```markdown
## Edit: Update Project

**Project:** {project_id} — {title}
**Changes:**
- Status: {from} → {to}
- Timeline: {from} → {to}
- Resources: {from} → {to}
```

### 4. Present MENU OPTIONS

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



