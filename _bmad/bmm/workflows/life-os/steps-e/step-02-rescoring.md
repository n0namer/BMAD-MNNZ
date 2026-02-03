---
name: 'step-02-rescoring'
description: 'Re-score the updated project and document impact'
nextStepFile: './step-03-kill-project.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
mcdaGuide: '../data/mcda-methodology.md'
---

# Edit Step 2: Rescoring

## STEP GOAL:

Re-score the project after updates and capture the impact on priority.

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
- 🎯 Focus ONLY on rescoring
- 🚫 FORBIDDEN to change scope here
- 💬 Use {mcdaGuide} as reference only
- 💬 Ask 1–2 questions at a time and adapt to the user’s responses

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

- 🎯 Gather updated scoring inputs
- 💾 Append rescoring summary to {workflowPlanFile}
- 📖 Confirm priority impact with user

## CONTEXT BOUNDARIES:

- Available context: updated project details
- Focus: scoring and priority impact

## MANDATORY SEQUENCE

### 1. Collect Updated Scores

Ask for 1–5 ratings and rationale (progressively, 1–2 at a time) for:
- Impact
- Confidence
- Effort
- Strategic alignment
- Risk

### 2. Compute Summary

Compute overall score (equal weights unless user specifies).

### 3. Append to Workflow Plan

Append:
```markdown
## Edit: Rescoring

**Project:** {project_id} — {title}
**Scores (1–5):**
- Impact: {score} — {rationale}
- Confidence: {score} — {rationale}
- Effort: {score} — {rationale}
- Alignment: {score} — {rationale}
- Risk: {score} — {rationale}

**Overall Score:** {score}
**Priority Impact:** {increase/decrease/no change}
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
- Scores captured with rationale
- Priority impact confirmed
- Plan updated

### ❌ SYSTEM FAILURE:
- Rescoring without user input
- Missing rationale
- Skipping save before continue

**Master Rule:** Rescoring must be justified and recorded.



