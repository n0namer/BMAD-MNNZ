---
name: 'step-01-daily-review'
description: 'OPTIONAL daily standup mode (1-2 min) - Quick status check, not required'
nextStepFile: './step-02-weekly-review.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
estimatedDuration: '1-2 minutes (OPTIONAL)'
isOptional: true
---

# Validation Step 1: Daily Review (OPTIONAL "Standup Mode")

## STEP GOAL:

Run an OPTIONAL quick daily standup (1-2 min) to capture lightweight signals: today's focus, blockers, and tomorrow's priority. This is NOT required daily — weekly review is the PRIMARY cadence.

## WHY DAILY IS OPTIONAL:

- **Daily** = OPTIONAL lightweight signals (1-2 min, "standup mode")
- **Weekly** = PRIMARY substantive review (15-20 min, required for progress tracking)
- **Monthly** = "Deeper weekly" (30 min, adds trend analysis)
- **Quarterly** = Strategic goal adjustment only

Daily review is useful for high-discipline users who want daily check-ins, but most users should focus on weekly reviews instead.

## SKIP PROMPT:

**At the start of this step, always offer to skip:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Daily Review (OPTIONAL — 1-2 min)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This is a quick standup check-in. It's optional.

Your PRIMARY review cadence is **weekly** (15-20 min).
Daily is only useful if you want daily discipline signals.

Options:
1. ✅ Do quick daily standup (1-2 min)
2. ⏭️  Skip to weekly review (recommended for most users)

What would you like to do?
```

If user chooses "Skip" → immediately proceed to step-02-weekly-review.md

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
- 🎯 Focus ONLY on lightweight daily signals (not substantive review)
- 🎯 Analyze daily review in subprocess (Pattern 2)
- 💬 Return structured daily findings, not portfolio data
- 🚫 FORBIDDEN to reprioritize or rescore here
- ⏱️  Keep it FAST: 1-2 minutes maximum

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

### 1. Skip Prompt (ALWAYS SHOW FIRST)

**Before doing anything else, offer skip option:**
```
Daily Review is OPTIONAL (1-2 min).
Weekly Review is your PRIMARY cadence (15-20 min).

[✅ Do daily standup] [⏭️ Skip to weekly review]
```

If user skips → immediately load and execute {nextStepFile}

### 2. Daily Review Protocol (Subprocess)

**Launch a subprocess that:**
1. Loads data/weekly-pulse-protocol.md
2. Loads today's context ({portfolioFile} if exists)
3. Asks 3 standup questions
4. Returns structured standup summary

**Subprocess asks:**
1. "What is your ONE focus today?"
2. "Any blockers right now?"
3. "What's tomorrow's top priority?"

**Subprocess returns:**
```json
{
  "date": "YYYY-MM-DD",
  "today_focus": "...",
  "blockers": "...",
  "tomorrow_priority": "...",
  "signals": {
    "wip_warning": true/false,
    "blocker_severity": "none/low/medium/high"
  }
}
```

**Context savings:** ~400 lines (portfolio data) → ~30 lines (standup summary)

**Graceful fallback:** If subprocess unavailable, ask questions in main context.

**Do NOT ask for details** — this is signal-only mode.
Accept short answers: "Code review", "Waiting on approval", "Finish testing"

### 3. Append Metrics (Minimal Format)

Append to {metricsFile}:
```markdown
## Daily Standup — {today}
- Today: {focus}
- Blocker: {blocker_or_none}
- Tomorrow: {priority}
```

**If user tries to give long answers:**
```
⏱️  Daily standup is 1-2 min only.
Save detailed reflections for weekly review.

Short answer is fine: what's the ONE thing?
```

If the user skips metrics entirely:
- "Ничего страшного — еженедельный обзор важнее."
- Do NOT force it — proceed immediately

### 4. Proceed to Next Review

Display: "**Proceeding to weekly review (PRIMARY cadence)...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an auto-proceed validation step
- Do not wait for user menu selection

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- User offered skip option FIRST
- If done: completed in 1-2 minutes (not longer)
- Minimal metrics captured (3 short answers)
- User understands weekly is PRIMARY cadence

### ❌ SYSTEM FAILURE:
- Not offering skip option
- Making daily review feel mandatory
- Asking for detailed answers (that's weekly's job)
- Taking >3 minutes
- Making user feel guilty for skipping

**Master Rule:** Daily review is OPTIONAL and LIGHTWEIGHT. Weekly review is where substantive tracking happens. Most users should skip daily and focus on weekly.



