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
- 🎯 Focus ONLY on specialist matching for the current idea
- 🤖 I will suggest specialists based on roles, you confirm before proceeding
- 🚫 FORBIDDEN to save/proceed without user confirmation
- 💬 Ask clarifying questions only if needed for accurate matching
- 🎯 Use subprocess for Search Orchestrator specialist profile lookup (Pattern 3)
- 💬 Return ONLY matched specialist profiles, not full data files

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
- Present options and wait for user to choose before proceeding.

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

### 3. Draft Specialist Shortlist (I Suggest, You Confirm)

Use the Search Orchestrator to map roles -> specialists.
Prefer specialist_profile from roles-base.csv when available.
If multiple roles map to the same specialist profile, merge to avoid duplicates.
1) CLI Claude Flow memory search (nearest role templates)
2) Local MD search (existing specialist profiles)
3) Web/MCP search only if mapping is ambiguous

Build a suggested list based on the Roles section in {workflowPlanFile}.
Use one specialist per role, plus 1–2 domain specialists if needed.

#### Search Orchestrator Specialist Lookup (Subprocess - Pattern 3)

**Launch a subprocess that:**
1. Loads roles from {workflowPlanFile} (Roles section)
2. For each role, executes Search Orchestrator priority:
   - CLI memory search: `npx claude-flow@v3alpha memory search -q "specialist:{role}"`
   - Local MD search: grep {specialistsFolder} for matching profiles
   - Web/MCP: Only if ambiguous
3. Returns ONLY matched specialist names + brief scope (~50-100 lines instead of 800+ full profiles)

**Subprocess returns:** Specialist shortlist with role mapping + priority + rationale snippet

**Graceful fallback:** If subprocess unavailable, execute Search Orchestrator sequence in main context

**Context Savings:** ~800 lines (full specialist profiles → 50-100 matched excerpts)

**Present suggested specialists to user:**
```
📋 Suggested Specialists:

**Idea ID:** {IDEA_ID}
**Idea Title:** {Idea Title}

**Selected Specialists:**
- {Specialist} — {reason} (priority: {high/medium/low})
- {Specialist} — {reason} (priority: {high/medium/low})

**Notes:**
- {Any constraints or risks}

Please confirm: [A]pprove / [M]odify / [C]ontinue
```

**Wait for user response:**
- IF A or C: Proceed to save to workflow plan
- IF M: Ask what changes needed, update suggestions, re-present
- IF Any other: Help user respond, then redisplay menu

### 4. Finalize Specialist Set (After User Approval)

After user confirms, finalize the specialist set.

### 5. Save to Workflow Plan (After User Approval)

Once user approves, save to {workflowPlanFile}.
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

---

## 📊 Quick Feedback (Optional)

How was this step?

👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or press Enter to skip]

**After user responds (or skips), save to memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:step-03-specialist-match:{timestamp}" \
  --content "{\"step\": \"step-03-specialist-match\", \"rating\": \"{helpful/ok/frustrating}\", \"comment\": \"{user_comment}\", \"timestamp\": \"{ISO_datetime}\"}"
```

---

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
- Idea record identified and presented
- Specialist list suggested and confirmed by user
- Rationale documented in {workflowPlanFile} after user approval

### ❌ SYSTEM FAILURE:
- Proceeding without user confirmation
- No rationale for specialist choices
- Skipping save/update before next step

**Master Rule:** Specialist matching must be explicit, confirmed, and documented.




