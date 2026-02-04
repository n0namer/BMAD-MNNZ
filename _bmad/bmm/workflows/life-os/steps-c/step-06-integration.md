---
name: 'step-06-integration'
description: 'Classify project, assess portfolio health, and define integration plan'
nextStepFile: './step-07-calendar-sync.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
decisionsLog: '{bmb_creations_output_folder}/life-os/decisions/decision-log.md'
strategicBucketsRef: '../data/strategic-buckets.md'
portfolioHealthRef: '../data/portfolio-health.md'
integrationPatternsRef: '../data/integration-patterns.md'
workflowMappingRef: '../data/bmad-workflow-mapping.md'
timelineRef: '../data/timeline-allocation.md'
wipRef: '../data/wip-enforcement.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Portfolio Integration

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
- 🚫 FORBIDDEN to change scores from step-05
- 💬 Use reference files for guidance only
- 💬 Ask 1–2 questions at a time and adapt to the user’s responses
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
- If subprocess is available, load only relevant part(s) from:
  - {strategicBucketsRef}, {portfolioHealthRef}, {integrationPatternsRef}
  - {workflowMappingRef}, {timelineRef}, {wipRef}
- Use each index file to identify needed `.part-*.md` files.
- Subprocess returns only the sections needed for the current decision.
- If subprocess is unavailable, load only the required part files manually.

- 🎯 Determine strategic bucket using {strategicBucketsRef}
- 💾 Append integration summary to {workflowPlanFile}
- 📖 Record key decisions in {decisionsLog}
- 🧾 Record evidence snapshot in journal or workflow plan
- 📘 Record decision in project decisions file (if exists)

## CONTEXT BOUNDARIES:

- Available context: workflow plan (idea + scoring)
- Focus: portfolio fit and integration plan
- Dependencies: step-05 scoring must be complete

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

If multiple patterns are plausible, use Search Orchestrator to rank 2–3 options and recommend the best fit.

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

If WIP is high and capacity is low, recommend pause or kill before proceeding.

### 7. Ensure Decision Log Exists

If {decisionsLog} does not exist, create it with:
```markdown
# Decision Log

## {today} — {project_title}
- Context: Portfolio Integration
- Decision: {bucket} / {pattern} / WIP {decision}
- Rationale: {brief rationale}
```

If it exists, append a new decision entry with the same fields.

### 8. Append Integration Summary

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

### 9. Stage Gate: Plan Readiness DoD

Confirm readiness to schedule:
- Integration summary complete
- WIP decision confirmed
- Resources and timeline agreed
- User approves moving to calendar sync

Append:
```markdown
## Stage Gate: Plan Readiness

**Gate Decision:** {Proceed/Revise/Pause}
**DoD Checklist:** {met/not met}
**Notes:** {brief rationale}
```

### 10. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue"

#### Menu Handling Logic:
- IF A: Read fully and follow: {advancedElicitationTask} with the current integration summary to refine portfolio fit, then redisplay the menu
- IF P: Read fully and follow: {partyModeWorkflow} to explore alternative integration approaches, then redisplay the menu
- IF C: Save content to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A/P execution, return and redisplay this menu

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




