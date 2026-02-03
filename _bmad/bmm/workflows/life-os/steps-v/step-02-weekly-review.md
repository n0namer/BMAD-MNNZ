---
name: 'step-02-weekly-review'
description: 'Run a weekly portfolio review and update priorities'
nextStepFile: './step-03-monthly-review.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
---

# Validation Step 2: Weekly Review

## STEP GOAL:

Run a weekly portfolio review to assess progress, risks, and priorities.

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
- 🎯 Focus ONLY on weekly review and priorities
- 🚫 FORBIDDEN to modify project scope here

## EXECUTION PROTOCOLS:

### Proactive Advice & Best Practices (MCP)
- If the user asks for advice, best practices, or recommendations, use MCP search (if available) to retrieve current guidance.
- Summarize findings concisely and cite sources when possible.
- If MCP search is unavailable, provide best-effort guidance and note the limitation.

- 🎯 Ask weekly review questions
- 💾 Append to {metricsFile}
- 📖 Proceed to next review step

## CONTEXT BOUNDARIES:

- Available context: {portfolioFile} if exists
- Focus: weekly progress and priority shifts

## MANDATORY SEQUENCE

### 1. Ask Weekly Review Questions

Ask (1–2 at a time):
- What moved forward this week?
- What stalled and why?
- What should be top priority next week?

### 2. Append Metrics

Append:
```markdown
## Weekly Review — {today}
- Progress: {summary}
- Stalls: {issues}
- Next Week Priority: {priority}
```

### 3. Proceed to Next Review

Display: "**Proceeding to monthly review check...**"
Then load, read entire file, then execute {nextStepFile}.

#### EXECUTION RULES:
- This is an auto-proceed validation step
- Do not wait for user menu selection

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Weekly snapshot captured
- Metrics appended

### ❌ SYSTEM FAILURE:
- Skipping questions
- Not writing to metrics

**Master Rule:** Weekly review must be concise and recorded.



