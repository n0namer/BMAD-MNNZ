---
name: 'step-03-monthly-review'
description: 'Run a monthly alignment review and strategic adjustments'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
---

# Validation Step 3: Monthly Review

## STEP GOAL:

Run a monthly alignment review to ensure portfolio and goals stay aligned.

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
- 🎯 Focus ONLY on alignment and strategic adjustments
- 🚫 FORBIDDEN to redesign workflow or change architecture

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
If monthly alignment is unclear, use Search Orchestrator to rank 2–3 options.

- 🎯 Ask monthly alignment questions
- 💾 Append to {metricsFile}
- 📖 Conclude validation sequence
- 🧾 Record evidence snapshot in journal or workflow plan

## CONTEXT BOUNDARIES:

- Available context: {portfolioFile} if exists
- Focus: alignment, resource allocation, strategic shifts

## MANDATORY SEQUENCE

### 1. Ask Monthly Review Questions

Ask (1–2 at a time):
- Are current projects aligned with long-term goals?
- What should be stopped or deprioritized?
- What new opportunities emerged?

### 2. Append Metrics

Append:
```markdown
## Monthly Review — {today}
- Alignment: {summary}
- Stop/Deprioritize: {items}
- New Opportunities: {items}
```

If the user skips metrics, prompt once:
- "Для месячного обзора достаточно 1–2 ключевых пункта."

### 3. Completion Message

"✅ Monthly review captured. Validation sequence complete."

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Monthly snapshot captured
- Metrics appended

### ❌ SYSTEM FAILURE:
- Skipping questions
- Not writing to metrics

**Master Rule:** Monthly review must capture alignment and strategic shifts.



