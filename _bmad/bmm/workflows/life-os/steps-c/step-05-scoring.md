---
name: 'step-05-scoring'
description: 'Score the project using MCDA/RICE inputs and document rationale'
nextStepFile: './step-06-integration.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
mcdaGuide: '../data/mcda-methodology.md'
stageGateMap: '../data/stage-gate-mapping.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Scoring

## STEP GOAL:

Score the project using structured criteria and document the rationale.

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
- 🎯 Focus ONLY on scoring and rationale
- 🚫 FORBIDDEN to change scope or add new features
- 💬 Use {mcdaGuide} and {stageGateMap} as reference only
- 💬 If reference files are sharded, load only the relevant part(s) listed in the index file

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

### Subprocess Data Ops (Reference Lookup)
- If subprocess is available, load only relevant part(s) from {mcdaGuide} and {stageGateMap}:
  - Use the index file to identify needed `.part-*.md` files.
  - Subprocess returns only the criteria/tables required for this step.
- If subprocess is unavailable, load only the needed part files manually.

- 🎯 Ask user for inputs per criteria
- 💾 Append scoring summary to {workflowPlanFile}
- 📖 Keep rationale explicit and concise
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES:

- Available context: workflow plan + consilium recommendations
- Focus: scoring and decision rationale
- Dependencies: step-04 consilium must be complete

## MANDATORY SEQUENCE

### 1. Load References

Briefly reference {mcdaGuide} and {stageGateMap} for criteria alignment.

### 2. Auto-Suggest: Domain-Specific Criteria (Intelligence Layer)

**AI automatically adds domain-specific scoring criteria based on selected frameworks:**

**If Business frameworks present:**
- Market Opportunity (0.10 weight)
- Competitive Advantage (0.10 weight)

**If Finance frameworks present:**
- Expected Value (0.15 weight)
- Option Value (0.10 weight)

**If Health frameworks present:**
- Readiness (HBM) (0.10 weight)
- Sustainability (0.10 weight)

**If Personal Dev frameworks present:**
- Skill Impact (0.10 weight)
- Time Commitment (0.10 weight)

**Total weights always sum to 1.0** (remaining distributed to base criteria)

**User confirmation:**
```
🎯 **Auto-Detected Domain Criteria**

I've added these criteria based on your frameworks:
- {Criterion 1}: {weight} ({reason})
- {Criterion 2}: {weight} ({reason})

Adjust weights? [Y/n]
```

### 3. Collect Scoring Inputs

Invite the user to provide values (1–5) and short rationale for:
- Impact
- Confidence
- Effort
- Strategic alignment
- Risk

If the user is unsure about weights or criteria interpretation, use Search Orchestrator to propose 2–3 scoring profiles.

Ask 1–2 questions at a time and adapt based on the user's answers.

If the user is unsure about a score, offer a quick anchor:
- 1 = низко, 3 = средне, 5 = высоко
- Suggest a default score and ask for confirmation

### 4. Calculate Summary

Compute a simple weighted summary (user-approved weights or equal weights).
Confirm the total score with the user.

### 5. Append to Workflow Plan

Append:
```markdown
## Scoring Summary

**Criteria Scores (1–5):**
- Impact: {score} — {rationale}
- Confidence: {score} — {rationale}
- Effort: {score} — {rationale}
- Strategic Alignment: {score} — {rationale}
- Risk: {score} — {rationale}

**Overall Score:** {score} (method: {weights})

**Decision Rationale:**
- {bullet}
- {bullet}
```

### 6. Stage Gate: Scoring DoD

Confirm readiness to proceed with planning:
- Scores are complete and justified
- Key risks are acknowledged
- Strategic alignment is acceptable
- User agrees to proceed

Ask the user to confirm Gate 1 (Proceed / Revise / Pause).

Append:
```markdown
## Stage Gate: Scoring

**Gate Decision:** {Proceed/Revise/Pause}
**DoD Checklist:** {met/not met}
**Notes:** {brief rationale}
```

### 7. Present MENU OPTIONS

**Choose next action:**

**[T] TRIZ** - Resolve scoring conflicts (if criteria contradict)
**[S] Rescore** - Redo scoring with different criteria
**[A] Adjust Criteria** - Modify MCDA weights
**[C] Continue** - Accept current scores

➡️ **Your choice:** [T/S/A/C]

**[T] TRIZ - Scoring Conflict Resolution (Optional)**
- **When to use:** Two criteria fundamentally conflict (e.g., High Impact but High Risk, High Confidence but High Effort)
- **What happens:** Launch Step 4.5 - TRIZ Analysis to resolve the contradiction
- **Example:** "High business impact (9/10) requires major investment (9/10 effort)" → Use TRIZ to find breakthrough that achieves high impact with low effort
- **Skip if:** Scores are balanced, or trade-off is acceptable

💡 **Additional Method Options Available:**
- **[A] Advanced Elicitation**: Deepen analysis with 50+ techniques
- **[P] Party Mode**: Creative scoring session

#### Menu Handling Logic:
- IF T: Identify scoring contradictions (e.g., High Impact ⇄ High Effort, Speed ⇄ Quality, Cost ⇄ Features), proceed to Step 4.5: TRIZ Analysis (optional step jump), return here with TRIZ-optimized approach, re-run MCDA with adjusted criteria if needed, then redisplay the menu
- IF S: Clear current scores, restart from step 2 (Collect Scoring Inputs) with fresh perspective, then redisplay the menu
- IF A: Allow user to modify MCDA weights (e.g., increase Impact weight from 0.3 to 0.5), recalculate overall score, confirm with user, then redisplay the menu
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### Additional Method Handling:
- Advanced Elicitation [A]: Read fully and follow: {advancedElicitationTask} with the current scoring rationale to refine criteria and weights, then redisplay the menu
- Party Mode [P]: Read fully and follow: {partyModeWorkflow} to gather alternative scoring perspectives, then redisplay the menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A/P execution, return and redisplay this menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Scores collected with rationale
- Overall score confirmed
- Scoring written to {workflowPlanFile}

### ❌ SYSTEM FAILURE:
- Scoring without user input
- Missing rationale
- Skipping save/update before continuing

**Master Rule:** Scoring must be explicit, justified, and recorded.




