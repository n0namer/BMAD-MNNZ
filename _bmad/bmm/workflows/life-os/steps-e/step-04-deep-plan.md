---
name: 'step-04-deep-plan'
description: 'Deepen a project plan iteratively (L1-L6)'
plansFolder: '{bmb_creations_output_folder}/life-os/plans'
snapshotsFolder: '{bmb_creations_output_folder}/life-os/snapshots'
journalFolder: '{bmb_creations_output_folder}/life-os/journal'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
deepPlanTemplatesRef: '../data/deep-plan-templates.md'
---

# Edit Step 4: Deep Plan Builder

## STEP GOAL:

Iteratively deepen a project plan to 5-6+ levels of detail.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 Focus ONLY on plan depth and clarity
- 🚫 FORBIDDEN to change scope or timeline here
- 💬 Ask 1–2 questions at a time
- 💬 Confirm each level before going deeper

## EXECUTION PROTOCOLS:

- 🎯 Identify the target project plan
- 💾 Update the Deep Plan section
- 📖 Append a journal entry about the iteration
- 🧾 Record evidence snapshot in journal or workflow plan

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

## MANDATORY SEQUENCE

### 1. Select Project

Ask for project ID/title, then locate:
- Plan file in {plansFolder}
- Snapshot file in {snapshotsFolder} (if any)
- Journal file in {journalFolder} (if any)

### 2. Confirm Iteration Mode

Ask the user for confirmation before auto‑generation:
- "Сделать авто‑генерацию глубинного плана (L1–L6) сейчас? [Да/Нет]"

If the user says **No**, ask what level of detail they want and proceed manually.

### 3. Auto-Select Iteration Mode

Automatically choose the mode:
- Default: Use template and build full depth (L1 -> L6)
- If role is unclear or user is invited without scope, use the "Invited Role" template

### 4. Update Plan (Automatic, Semantic)

Infer scenario by meaning using the Search Orchestrator:
1) CLI Claude Flow memory search to find nearest scenario template
2) Local MD search in plans/snapshots for similar cases
3) Web/MCP search only if ambiguity remains

Pick the top 1–2 scenarios and map to templates:
- Tech Expert / Architect
- Research / Discovery
- Ops / Delivery Helper
- Product / Strategy Contributor
- Invited Role (unclear contribution) as fallback

Use {deepPlanTemplatesRef} as the index and load only the relevant `.part-*.md` template file.
If subprocess is available, load the relevant part in a subprocess and return only the selected outline.

If multiple scenarios match, use a **Mixed Scenario** (combine top 2 templates).
Insert the selected template structure and auto-fill a best-effort example outline.

When mixing templates, merge unique nodes and remove duplicates.

Update the "Deep Plan (L1-L6)" section in the project plan.
Fill RACI for key L2 nodes and add 2–4 If-Then actions.
Update Plan Quality Metrics:
- Depth Covered = levels present / 6
- Nodes Count = total nodes across L1-L6
- RACI Coverage = % of L2 nodes with R and A
- If-Then Coverage = count of If-Then actions

Compute metrics explicitly:
- Levels present: count L1..L6 headers that exist in the outline
- Nodes count: count all L* lines in the outline
- RACI coverage: (L2 nodes with R and A) / (total L2 nodes)
- If-Then coverage: count of If-Then entries

Quality Gate (must pass before completion):
- L1–L4 present
- RACI Coverage >= 70%
- If-Then Coverage >= 2
If not met, extend the plan until the gate is satisfied.

### 4. Update Journal

Append entry: date, what was deepened, key decisions.

### 5. Append to Workflow Plan

Append to {workflowPlanFile}:
```markdown
## Edit: Deep Plan

**Project:** {project_id} — {title}
**Depth:** {Full/Specific}
**Summary:** {what changed}
```

### 6. Present MENU OPTIONS

Display: "**Select:** [C] Complete"

#### Menu Handling Logic:
- IF C: End this step
- IF Any other: help user respond, then redisplay menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Deep plan updated
- Journal entry appended
- Workflow plan updated

### ❌ SYSTEM FAILURE:
- Missing confirmation
- No plan update

**Master Rule:** Deep plans must be explicit, confirmed, and documented.
