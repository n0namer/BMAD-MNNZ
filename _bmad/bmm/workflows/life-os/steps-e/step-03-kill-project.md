---
name: 'step-03-kill-project'
description: 'Confirm and document project termination'
projectsFolder: '{bmb_creations_output_folder}/life-os/projects'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
decisionsLog: '{bmb_creations_output_folder}/life-os/decisions/decision-log.md'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
---

# Edit Step 3: Kill Project

## STEP GOAL:

Confirm a kill decision, document rationale, and update records.

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
- 🎯 Focus ONLY on project termination
- 🚫 FORBIDDEN to delete files without confirmation
- 💬 Confirm kill criteria explicitly
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

- 🎯 Identify the project to terminate
- 💾 Append decision to {decisionsLog}
- 📖 Update status in project record
- 🧾 Record evidence snapshot in journal or workflow plan
- 📘 Record decision in project decisions file (if exists)

## CONTEXT BOUNDARIES:

- Available context: project files in {projectsFolder} and user input
- Focus: kill decision and documentation

## MANDATORY SEQUENCE

### 1. Confirm Kill Decision

Ask (progressively):
- Which project to terminate?
- Which kill criteria are met?
- Confirm the decision and any rollback plan

If criteria are unclear, use Search Orchestrator to rank 2–3 options (pause, pivot, kill) with rationale.

### 2. Document Decision

Append to {decisionsLog}:
```markdown
## Kill Decision — {today}

**Project:** {project_id} — {title}
**Criteria Met:** {criteria}
**Rationale:** {summary}
**Decision:** KILL (confirmed)
```

### 3. Update Project Status

In the project file, update status to `KILLED` and add a brief note.

### 4. Update Snapshot and Journal

Update snapshot in {snapshotsFolder} to KILLED and record final note.
Append a journal entry in {journalFolder} with the kill decision and criteria.

### 5. Append to Workflow Plan

Append to {workflowPlanFile}:
```markdown
## Edit: Kill Project

**Project:** {project_id} — {title}
**Decision Log:** {decisionsLog}
```

### 6. Completion Message

Confirm the kill is recorded.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Kill decision confirmed
- Decision logged
- Project status updated

### ❌ SYSTEM FAILURE:
- Proceeding without explicit confirmation
- No decision log entry
- Project not updated

**Master Rule:** Kill decisions must be explicit, logged, and reversible.



