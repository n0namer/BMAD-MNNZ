---
name: 'step-03-consilium'
description: 'Assemble specialist consilium and capture recommendations'
nextStepFile: './step-04-scoring.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
---

# Step 3: Consilium

## STEP GOAL:

Assemble a focused consilium of specialists, capture their recommendations, and record a consensus summary.

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
- 🎯 Focus ONLY on consilium assembly and recommendations
- 🚫 FORBIDDEN to score or prioritize in this step
- 💬 Ask the user to confirm each specialist’s input

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

- 🎯 Identify the selected specialists from the workflow plan
- 💾 Append consilium notes to {workflowPlanFile}
- 📖 Keep recommendations concise and attributable

## CONTEXT BOUNDARIES:

- Available context: workflow plan content
- Focus: specialist recommendations and consensus
- Dependencies: step-02 specialist match must be complete

## MANDATORY SEQUENCE

### 1. Load Specialist List

Open {workflowPlanFile} and locate the "Specialist Matching" section.
Summarize the selected specialists to the user.

### 2. Gather Recommendations

For each specialist, guide the user to provide or confirm:
- Key risks
- Key opportunities
- Suggested approach

Ask 1–2 questions at a time and adapt based on the user’s response.

Record each recommendation as a short bullet list.

### 3. Synthesize Consensus

Ask the user to confirm a 2–4 bullet "consensus view" that captures shared guidance.

### 4. Append to Workflow Plan

Append:
```markdown
## Consilium Recommendations

**Specialists Consulted:** {list}

**Recommendations:**
- {Specialist}: {key points}
- {Specialist}: {key points}

**Consensus View:**
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
- All specialists accounted for
- Recommendations captured and confirmed
- Consensus recorded in {workflowPlanFile}

### ❌ SYSTEM FAILURE:
- Skipping specialist input
- Scoring or prioritizing prematurely
- Not appending to plan before continuing

**Master Rule:** Consilium captures expert guidance only; no scoring here.



