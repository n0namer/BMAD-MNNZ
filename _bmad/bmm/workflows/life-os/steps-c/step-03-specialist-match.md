---
name: 'step-03-specialist-match'
description: 'Match specialists to the captured idea and document the selection'
nextStepFile: './step-04-consilium.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
ideasFolder: '{bmb_creations_output_folder}/life-os/ideas'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Specialist Match

## STEP GOAL:

Identify the most relevant specialists for the captured idea, confirm with the user, and record the selection.

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
- 🎯 Focus ONLY on specialist matching for the current idea
- 🚫 FORBIDDEN to proceed without user confirmation
- 💬 Ask clarifying questions only if needed for accurate matching

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

- 🎯 Load the most recent idea record or ask the user for the idea ID
- 💾 Record specialist matches in {workflowPlanFile}
- 📖 Ensure the plan includes rationale for each specialist

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

## CONTEXT BOUNDARIES:

- Available context: idea record in {ideasFolder}, user clarifications
- Focus: matching specialists, not scoring or integration
- Dependencies: step-01 idea capture must exist

## MANDATORY SEQUENCE

### 1. Locate the Idea Record

Ask the user:

"Какую идею мы сейчас оцениваем?  
Если ID известен — пришлите его.  
Если нет — я могу взять самый свежий файл из {ideasFolder}."

If user confirms the latest idea, proceed with that.

### 2. Summarize the Idea (Brief)

Summarize in 2–4 bullets:
- Title
- Domain
- Goal / Motivation
- Timeline expectation

Confirm: "Верно ли я понял(а) идею?"

### 3. Draft Specialist Shortlist (Automatic, Semantic)

Use the Search Orchestrator to map roles -> specialists.
Prefer specialist_profile from roles-base.csv when available.
If multiple roles map to the same specialist profile, merge to avoid duplicates.
1) CLI Claude Flow memory search (nearest role templates)
2) Local MD search (existing specialist profiles)
3) Web/MCP search only if mapping is ambiguous

Build a list automatically based on the Roles section in {workflowPlanFile}.
Use one specialist per role, plus 1–2 domain specialists if needed.

Do NOT ask the user to confirm or change the list.

### 4. Finalize Specialist Set (Automatic)

Finalize without user confirmation.

### 5. Save to Workflow Plan

If {workflowPlanFile} does not exist, create it from the template used in step-01.

Append:
```markdown
## Specialist Matching

**Idea ID:** {IDEA_ID}
**Idea Title:** {Idea Title}

**Selected Specialists:**
- {Specialist} — {reason} (priority: {high/medium/low})
- {Specialist} — {reason} (priority: {high/medium/low})

**Notes:**
- {Any constraints or risks}
```

Update frontmatter in {workflowPlanFile} to append this step to
`stepsCompleted` (add `step-03-specialist-match`).

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue"

#### Menu Handling Logic:
- IF A: Read fully and follow: {advancedElicitationTask} with the current specialist shortlist to refine choices, then redisplay the menu
- IF P: Read fully and follow: {partyModeWorkflow} to explore alternative perspectives, then redisplay the menu
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A/P execution, return and redisplay this menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Idea record identified
- Specialist list confirmed by user
- Rationale documented in {workflowPlanFile}

### ❌ SYSTEM FAILURE:
- Proceeding without user confirmation
- No rationale for specialist choices
- Skipping save/update before next step

**Master Rule:** Specialist matching must be explicit, confirmed, and documented.




