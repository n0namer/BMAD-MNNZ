---
name: 'step-04-scoring'
description: 'Score the project using MCDA/RICE inputs and document rationale'
nextStepFile: './step-05-integration.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
mcdaGuide: '../data/mcda-methodology.md'
stageGateMap: '../data/stage-gate-mapping.md'
---

# Step 4: Scoring

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

### Subprocess Data Ops (Reference Lookup)
- If subprocess is available, load only relevant part(s) from {mcdaGuide} and {stageGateMap}:
  - Use the index file to identify needed `.part-*.md` files.
  - Subprocess returns only the criteria/tables required for this step.
- If subprocess is unavailable, load only the needed part files manually.

- 🎯 Ask user for inputs per criteria
- 💾 Append scoring summary to {workflowPlanFile}
- 📖 Keep rationale explicit and concise

## CONTEXT BOUNDARIES:

- Available context: workflow plan + consilium recommendations
- Focus: scoring and decision rationale
- Dependencies: step-03 consilium must be complete

## MANDATORY SEQUENCE

### 1. Load References

Briefly reference {mcdaGuide} and {stageGateMap} for criteria alignment.

### 2. Collect Scoring Inputs

Invite the user to provide values (1–5) and short rationale for:
- Impact
- Confidence
- Effort
- Strategic alignment
- Risk

Ask 1–2 questions at a time and adapt based on the user’s answers.

### 3. Calculate Summary

Compute a simple weighted summary (user-approved weights or equal weights).
Confirm the total score with the user.

### 4. Append to Workflow Plan

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

### 5. Present MENU OPTIONS

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

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



