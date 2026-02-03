---
name: 'step-06-calendar-sync'
description: 'Translate the approved project into a timeline and calendar plan'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
outputProjectFile: '{bmb_creations_output_folder}/life-os/projects/{project_id}.md'
---

# Step 6: Calendar Sync

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

- 🎯 Confirm project readiness and start date
- 💾 Write a project file to {outputProjectFile}
- 📖 Append timeline summary to {workflowPlanFile}

## CONTEXT BOUNDARIES:

- Available context: workflow plan (idea, consilium, scoring)
- Focus: scheduling and calendar alignment
- Dependencies: step-05 integration must be complete

## MANDATORY SEQUENCE

### 1. Confirm Schedule Inputs

Ask for schedule inputs progressively (1–2 at a time), covering:
- Target start date
- Target end date or duration
- Weekly capacity (hours/week)
- Milestones (if any)

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

### 5. Completion Message

Inform the user the project file was created and the workflow is complete.

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



