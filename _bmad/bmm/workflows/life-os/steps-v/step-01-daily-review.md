---
name: 'step-01-daily-review'
description: 'Run a quick daily review of active projects and blockers'
nextStepFile: './step-02-weekly-review.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
---

# Validation Step 1: Daily Review

## STEP GOAL:

Run a quick daily review to capture current state, blockers, and tomorrow focus.

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
- 🎯 Focus ONLY on daily review signals
- 🚫 FORBIDDEN to reprioritize or rescore here

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

### Search Orchestrator Protocol (Required)
- Follow data/search-decision-protocol.md (and data/mcp_search_system_prompt_xml.md).
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Record an evidence snapshot and confidence (high/medium/low).
- If confidence is low, ask user to choose; if high, proceed and note rationale.

### Semantic Decision Support
If review prioritization or next actions are unclear, use Search Orchestrator to rank 2–3 options.

- 🎯 Ask short daily review questions
- 💾 Append to {metricsFile}
- 📖 Proceed to next review step
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES:

- Available context: {portfolioFile} if exists
- Focus: daily snapshot only

## MANDATORY SEQUENCE

### 1. Ask Daily Review Questions

Ask (1–2 at a time):
- What is in progress today?
- Any blockers?
- What is the single most important task tomorrow?

### 2. Append Metrics

Append:
```markdown
## Daily Review — {today}
- In Progress: {items}
- Blockers: {blockers}
- Tomorrow Focus: {focus}
```

If the user skips metrics, prompt once:
- "Чтобы обзор был полезнее, давайте зафиксируем хотя бы 1–2 пункта."

### 3. Proceed to Next Review

Display: "**Proceeding to weekly review check...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an auto-proceed validation step
- Do not wait for user menu selection

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Daily snapshot captured
- Metrics appended

### ❌ SYSTEM FAILURE:
- Skipping questions
- Not writing to metrics

**Master Rule:** Keep daily review lightweight and recorded.



