---
name: 'step-05-integration'
description: 'Classify project, assess portfolio health, and define integration plan'
nextStepFile: './step-06-calendar-sync.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
decisionsLog: '{bmb_creations_output_folder}/life-os/decisions/decision-log.md'
strategicBucketsRef: '../data/strategic-buckets.md'
portfolioHealthRef: '../data/portfolio-health.md'
integrationPatternsRef: '../data/integration-patterns.md'
workflowMappingRef: '../data/bmad-workflow-mapping.md'
timelineRef: '../data/timeline-allocation.md'
wipRef: '../data/wip-enforcement.md'
---

# Step 5: Portfolio Integration

## STEP GOAL:

Classify the project, assess portfolio health, define integration approach, and document the integration plan.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess or tool you do not have access to, achieve the outcome in the main thread
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🤝 Proactive guidance: highlight risks, opportunities, and next best actions based on current context
- 🧭 If WIP/kill criteria or portfolio risks appear, surface them early with a brief recommendation
- ✅ Ask for user confirmation before taking any proactive action that changes scope or priorities
- 🎯 Focus ONLY on integration and portfolio fit
- 🚫 FORBIDDEN to change scores from step-04
- 💬 Use reference files for guidance only
- 💬 Ask 1–2 questions at a time and adapt to the user’s responses
- 💬 If reference files are sharded, load only the relevant part(s) listed in the index file

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

### Subprocess Data Ops (Reference Lookup)
- If subprocess is available, load only relevant part(s) from:
  - {strategicBucketsRef}, {portfolioHealthRef}, {integrationPatternsRef}
  - {workflowMappingRef}, {timelineRef}, {wipRef}
- Use each index file to identify needed `.part-*.md` files.
- Subprocess returns only the sections needed for the current decision.
- If subprocess is unavailable, load only the required part files manually.

- 🎯 Determine strategic bucket using {strategicBucketsRef}
- 💾 Append integration summary to {workflowPlanFile}
- 📖 Record key decisions in {decisionsLog}

## CONTEXT BOUNDARIES:

- Available context: workflow plan (idea + scoring)
- Focus: portfolio fit and integration plan
- Dependencies: step-04 scoring must be complete

## MANDATORY SEQUENCE

### 1. Classify Strategic Bucket

Use {strategicBucketsRef} to classify the project.
Confirm with the user and capture reasoning.

### 2. Check Portfolio Health

Using {portfolioHealthRef}, estimate current allocation and WIP.
If a subprocess/tool is available, compute allocations there and return only the summary.
If unhealthy, discuss rebalancing options and user decision.

### 3. Define Integration Approach

Use {integrationPatternsRef} to decide:
- Standalone vs Platform Extension vs Bundle vs Enabler
Confirm dependencies and shared components (if any).

### 4. Suggest BMAD Workflow

Use {workflowMappingRef} to suggest the most relevant BMAD workflow.
Confirm whether to start now, defer, or skip.

### 5. Propose Timeline & Resources (High-Level)

Use {timelineRef} to propose:
- Start date
- End date or duration
- Weekly capacity
Confirm with the user.

### 6. Enforce WIP Limit

Use {wipRef} to check if WIP > 2.
If exceeded, present kill/defer/override options and confirm choice.

### 7. Append Integration Summary

Append to {workflowPlanFile}:
```markdown
## Integration Summary

**Bucket:** {bucket}
**Portfolio Health:** {healthy/imbalanced} — {notes}
**Integration Pattern:** {pattern}
**Dependencies:** {list or none}
**BMAD Workflow:** {suggested} — {start/defer/skip}
**Timeline (High-Level):** {start} → {end} ({capacity}/week)
**WIP Decision:** {allow/defer/kill/override}
```

### 8. Present MENU OPTIONS

Display: "**Select:** [C] Continue"

#### Menu Handling Logic:
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Bucket classification confirmed
- Portfolio health assessed and decision made
- Integration pattern documented
- Timeline agreed
- WIP decision captured

### ❌ SYSTEM FAILURE:
- Skipping confirmation steps
- Not appending to workflow plan
- Proceeding without WIP decision

**Master Rule:** Integration requires explicit confirmation and recorded decisions.



