---
name: 'step-02-weekly-review'
description: 'Run the PRIMARY weekly portfolio review (~15-20 min) - Progress, WIP, Blockers, Priorities'
nextStepFile: './step-03-monthly-review.md'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics/metrics.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
estimatedDuration: '15-20 minutes'
protocolFile: '../data/weekly-review-protocol.md'
---

# Validation Step 2: Weekly Review (PRIMARY REVIEW CADENCE)

## STEP GOAL

Run the PRIMARY weekly review (~15-20 min) to assess progress against milestones, check WIP health, identify blockers/risks, and set priorities for next week. This is the substantive review rhythm users should follow consistently.

**WHY WEEKLY IS PRIMARY:**
- **Daily** = Optional standup (1-2 min, lightweight signals)
- **Weekly** = PRIMARY substantive review (15-20 min)
- **Monthly** = Deeper weekly + trend analysis (30 min)
- **Quarterly** = Strategic goal adjustment only (OKR review)

Weekly strikes the balance: substantive without overwhelming, frequent enough to catch drift early.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with config `{communication_language}`

### Step-Specific Rules
- 🤝 Proactive guidance: highlight risks, opportunities, next best actions based on current context
- 🧭 Surface WIP/portfolio risks early with brief recommendation
- ✅ Ask for user confirmation before changing scope or priorities
- 🎯 Focus on SUBSTANTIVE weekly review: progress, WIP, blockers, priorities
- 🎯 Analyze weekly review in subprocess (Pattern 2)
- 🎯 Scan active ideas for 5+ milestones in subprocess (Pattern 1)
- 💬 Return structured review findings and milestone recommendations, not raw data
- 🚫 FORBIDDEN to modify project scope here (only flag for later decision)

## EXECUTION PROTOCOLS

**Proactive Advice & Best Practices (MCP):** Use MCP search for advice/recommendations if available. Summarize findings concisely with sources.

**Search Orchestrator Protocol:** Follow data/search-decision-protocol.md → CLI memory search → local MD (rg) → web/MCP. Convene consilium to rank 2–4 options with pros/cons. Record evidence snapshot and confidence (high/medium/low).

**Semantic Decision Support:** If weekly priorities unclear, use Search Orchestrator to rank 2–3 options.

**Output:** Ask structured questions → Append substantive review to {metricsFile} → Proceed to next step → Record evidence snapshot

## CONTEXT BOUNDARIES

- Available context: {portfolioFile}, {goalsFile} if exist
- Focus: weekly progress, WIP health, blockers, next-week priorities
- Time scope: Last 7 days + Next 7 days

## MANDATORY SEQUENCE

### 1. Context Loading & Week Overview

Display current week context:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 **Weekly Review — Week of {week_start_date}**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️  Estimated time: 15-20 minutes
📂 Context loaded:
  - Portfolio: {portfolioFile}
  - Goals: {goalsFile}
  - Metrics: {metricsFile}

This is your PRIMARY review cadence for tracking progress and adjusting priorities.
```

If {portfolioFile} exists, load and display:
- Active projects count
- Current WIP (Work In Progress)
- Projects with upcoming milestones this week

### 2. Execute 5-Section Review (Subprocess Pattern)

**JIT Reference:** See {protocolFile} for detailed questions, templates, and response patterns.

**Launch a subprocess that:**
1. Loads {protocolFile} (data/weekly-review-protocol.md)
2. Loads last 7 days of data from {portfolioFile}, {metricsFile}
3. Executes 5-section weekly review protocol
4. Scans active ideas for 5+ milestones (Pattern 1)
5. Returns structured review findings + milestone recommendations

**Subprocess executes sections:**

1. **📊 Milestone Progress Check (~5 min)**
   - For each active project: progress vs plan, behind/ahead, course correction
   - Capture: planned vs actual %, timeline delta, root cause if behind

2. **🔄 WIP Health Check (~3 min)**
   - Active projects count, WIP limit, overload check, context switching
   - Assessment: ✅ Healthy / ⚠️ Warning / 🚨 Overload
   - If overload detected: proactively suggest pause actions

3. **🚧 Blockers & Risks (~5 min)**
   - Active blockers, external dependencies, internal blockers, risk horizon
   - For each: severity, owner, resolution plan
   - Proactive flagging: chronic blockers (>7 days), critical path, external dependencies

4. **🎯 Next Week Priorities (~4 min)**
   - Top 3 focus areas with goal alignment, success criteria, effort estimates
   - Capacity check: warn if total effort > available capacity

5. **✨ Quick Wins (~2 min)**
   - Wins this week, learnings, gratitude
   - Purpose: maintain motivation, capture learnings, combat negativity bias

**Subprocess returns:**
```json
{
  "week_range": "YYYY-MM-DD to YYYY-MM-DD",
  "milestone_progress": [
    {"project": "...", "planned_pct": 75, "actual_pct": 60, "status": "behind", "reason": "..."}
  ],
  "wip_health": {
    "active_count": 3,
    "status": "healthy/warning/overload",
    "context_switches": 5,
    "action_needed": "..."
  },
  "blockers": [
    {"description": "...", "severity": "high/medium/low", "owner": "...", "days_active": 3}
  ],
  "next_week_priorities": [
    {"priority": "...", "goal_alignment": "...", "success_criteria": "...", "effort_hours": 8}
  ],
  "quick_wins": ["...", "..."],
  "milestone_recommendations": [
    {"project_id": "...", "reason": "5+ dense milestones", "action": "Step 08 (deep-plan)"}
  ]
}
```

**Context savings:** ~1,200 lines (full data + protocol) → ~80 lines (structured findings)

**Graceful fallback:** If subprocess unavailable, load protocol and data in main context.

**Skip Warning:** If user tries to skip, emphasize weekly is PRIMARY review cadence. Offer to complete at least top 3 sections (Progress, WIP, Blockers).

### 3. Append Weekly Review to Metrics

Append structured review to {metricsFile} following format in {protocolFile}:
- Milestone Progress (with planned vs actual, status, course correction)
- WIP Health (count, status, context switches, action)
- Blockers & Risks (description, affects, severity, resolution)
- Next Week Priorities (3 priorities with success criteria, capacity check)
- Quick Wins (wins, learning)

### 4. Proceed to Next Review

Display: "**Proceeding to monthly review check...**"
Then load, read entire file, then execute {nextStepFile}.

**Menu Handling Logic:** After completion, immediately load, read entire file, then execute {nextStepFile}.

**EXECUTION RULES:** This is an auto-proceed validation step. Do not wait for user menu selection.

## SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- All 5 sections completed (Progress, WIP, Blockers, Priorities, Wins)
- Substantive review captured (not just 1-word answers)
- Metrics appended with structured data
- User has clear priorities for next week
- Review completed in 15-20 minutes (not rushed, not dragged out)

### ❌ SYSTEM FAILURE
- Skipping sections (except Quick Wins if time-pressed)
- Accepting vague answers ("fine", "ok", "nothing")
- Not writing to metrics
- Generating fake data without user input
- Review takes <5 min (too shallow) or >30 min (too detailed)

**Master Rule:** Weekly review is the PRIMARY substantive review. It must be comprehensive enough to track progress and catch drift, but quick enough to do consistently every week.



