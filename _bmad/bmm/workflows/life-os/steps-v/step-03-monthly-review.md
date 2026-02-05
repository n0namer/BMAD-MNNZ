---
name: 'step-03-monthly-review'
description: '"Deeper Weekly" (~30 min) - Weekly review format + Trend Analysis + Alignment Check'
portfolioFile: '{bmb_creations_output_folder}/life-os/portfolio.md'
metricsFile: '{bmb_creations_output_folder}/life-os/metrics.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
estimatedDuration: '30 minutes'
references:
  protocol: 'data/monthly-review-protocol.md'
  metrics: 'data/monthly-metrics-analysis.md'
  templates: 'data/monthly-planning-templates.md'
---

# Validation Step 3: Monthly Review ("Deeper Weekly")

## STEP GOAL

Run a "Deeper Weekly" review (~30 min) that adds trend analysis and alignment checks to the standard weekly review format. Same structure as weekly, but with 4-week trend perspective.

**WHY "DEEPER WEEKLY":** Monthly = Weekly format + Trend analysis (4 weeks) + Alignment check + Resource allocation review.

📖 **JIT Reference:** See data/monthly-planning-templates.md for full cadence explanation.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 Read complete step file before action
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ SPEAK in Agent communication style with `{communication_language}`

### Step-Specific Rules
- 🎯 Focus on TRENDS and ALIGNMENT (not just current week)
- 🎯 Analyze monthly review in subprocess (Pattern 2)
- 💬 Return structured trend analysis and alignment findings, not raw 4-week data
- 🤝 Proactive guidance: highlight risks, opportunities, next actions
- 🧭 Surface WIP/kill criteria or portfolio risks early with brief recommendation
- ✅ Ask confirmation before changing scope or priorities
- 🚫 FORBIDDEN to redesign workflow or change architecture

## EXECUTION PROTOCOLS

**Proactive Advice (MCP):** If user asks for advice, use MCP search to retrieve guidance. Cite sources. Note limitations if unavailable.

**Search Orchestrator:** Follow data/search-decision-protocol.md → CLI memory → local MD (rg) → web/MCP. Convene consilium for 2-4 ranked options. Record evidence snapshot with confidence.

**Semantic Decision Support:** If alignment unclear, use Search Orchestrator to rank 2-3 options.

**Context:** {portfolioFile} if exists. Focus: alignment, resource allocation, strategic shifts.

## MANDATORY SEQUENCE

### 1. Context Loading & Month Overview (Subprocess Pattern)

**Launch a subprocess that:**
1. Loads data/monthly-review-protocol.md
2. Loads last 4 weeks of data from {metricsFile}
3. Loads {portfolioFile} and {goalsFile}
4. Performs trend and alignment analysis
5. Returns structured monthly findings

Display current month context:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 **Monthly Review (Deeper Weekly) — {month} {year}**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️  Estimated time: 30 minutes
📂 Context loaded:
  - Portfolio: {portfolioFile}
  - Goals: {goalsFile}
  - Metrics: {metricsFile}
  - Last 4 weeks of data

This is a "deeper weekly" review with trend analysis.
Same structure as weekly, plus alignment and trends.
```

📖 **JIT:** See data/monthly-planning-templates.md for context template.

**Subprocess analyzes:**
- Last 4 weekly reviews from {metricsFile}
- Milestone velocity trends
- WIP patterns (stable/increasing/chaotic)
- Chronic blockers (2+ weeks)
- Goal alignment percentages

### 2. Milestone Progress Check (~7 min) — SAME AS WEEKLY + TRENDS

Run the same milestone progress check as weekly review, then ADD trend analysis.

📖 **JIT Reference:** See data/monthly-review-protocol.md Section 1 for:
- Trend analysis template (4-week progress tracking)
- Velocity calculation formula
- Proactive trend detection rules (declining/stagnant/improving)

**Key questions:**
- Is velocity trending up, down, or flat? Why?
- Forecast completion date based on current velocity

### 3. WIP Health Check (~5 min) — SAME AS WEEKLY + HISTORICAL PATTERN

Run the same WIP health check as weekly review, then ADD pattern analysis.

📖 **JIT Reference:** See data/monthly-review-protocol.md Section 2 for:
- WIP pattern analysis template (4-week WIP tracking)
- Context switches tracking
- Pattern classification (Stable/Increasing/Decreasing/Chaotic)
- Proactive pattern detection rules

**Key questions:**
- Is WIP trending healthier or worse?
- What's causing the pattern?

### 4. Blockers & Risks (~7 min) — SAME AS WEEKLY + CHRONIC BLOCKERS

Run the same blockers & risks check as weekly review, then ADD chronic blocker analysis.

📖 **JIT Reference:** See data/monthly-review-protocol.md Section 3 for:
- Chronic blocker identification (2+ weeks)
- Escalation criteria
- Systemic fix detection
- Proactive chronic blocker detection rules

**Key questions:**
- Which blockers are chronic (2+ weeks)?
- What's preventing resolution?
- Escalation needed?

### 5. Next Month Priorities (~6 min) — SAME AS WEEKLY BUT MONTHLY SCOPE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 Section 4: Next Month Priorities
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

📖 **JIT Reference:** See data/monthly-planning-templates.md for:
- Next month priorities template
- 4 key questions (top 3 focus areas, why, realistic check, success criteria)

**Ask (MONTH scope, not week):**
1. Top 3 focus areas for NEXT MONTH
2. Why these 3 (link to goals/milestones)
3. Realistic check (given trends, achievable?)
4. Success criteria (how will you know done?)

### 6. Alignment Check (~5 min) — NEW SECTION

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧭 Section 5: Goal Alignment Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Load {goalsFile} and {portfolioFile}, then analyze alignment.

📖 **JIT Reference:** See data/monthly-review-protocol.md Section 4 for:
- Goal alignment check template
- Project-goal mapping format
- Alignment strength classification (Strong/Weak/None)
- 4 key alignment questions
- Proactive misalignment detection rules (>30% misaligned, high-priority gaps, resource misallocation)

**For each active project, assess:**
- Supports which goal? (or "No clear goal alignment")
- Alignment strength: [Strong/Weak/None]
- Should continue or is it a distraction?

### 7. Quick Wins (~2 min) — SAME AS WEEKLY

Same as weekly review format.

### 8. Append Monthly Review to Metrics

**Subprocess returns:**
```json
{
  "month": "YYYY-MM",
  "milestone_trends": {
    "velocity_trend": "improving/declining/flat",
    "forecast_completion": "YYYY-MM-DD",
    "projects": [...]
  },
  "wip_patterns": {
    "pattern": "stable/increasing/chaotic",
    "avg_wip": 3.5,
    "context_switches_trend": "improving/worsening"
  },
  "chronic_blockers": [
    {"blocker": "...", "days_active": 14, "escalation_needed": true}
  ],
  "goal_alignment": {
    "aligned_pct": 75,
    "misaligned_projects": [...],
    "gaps": [...]
  },
  "next_month_priorities": [...],
  "quick_wins": [...]
}
```

**Context savings:** ~1,200 lines (4-week data + protocol) → ~100 lines (structured trends)

**Graceful fallback:** If subprocess unavailable, load 4-week data in main context.

📖 **JIT Reference:** See data/monthly-metrics-analysis.md for complete output format.

Append to {metricsFile} with sections:
- Milestone Progress & Trends
- WIP Health & Patterns
- Blockers & Chronic Issues
- Next Month Priorities
- Goal Alignment
- Quick Wins

**If user tries to skip sections:**

📖 **JIT Reference:** See data/monthly-review-protocol.md for skip resistance script.

```
⚠️ **Monthly Review adds trend analysis to weekly format**

This is your chance to spot patterns over 4 weeks.
Can we at least complete:
1. Trend Analysis (7 min)
2. Chronic Blockers (7 min)
3. Alignment Check (5 min)

Then you'll have strategic clarity for next month.
```

### 9. Completion Message

📖 **JIT Reference:** See data/monthly-planning-templates.md for completion template.

```
✅ **Monthly review captured**

Validation sequence complete.

Next steps:
- Continue weekly reviews (PRIMARY cadence)
- Quarterly review in {weeks_until_quarter} weeks
```

## MENU OPTIONS

**Available commands:**
- `start` - Begin monthly review sequence
- `skip [section]` - Skip section (will show warning if critical)
- `help [section]` - Show detailed guidance for section
- `trends` - Show 4-week trend analysis only
- `alignment` - Show goal alignment check only
- `complete` - Mark review complete and save to metrics

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- All sections completed (weekly format + trends + alignment)
- 4-week trend analysis captured
- Chronic blockers identified and escalated
- Goal alignment assessed (% calculated)
- User has strategic clarity for next month
- Review completed in ~30 minutes

### ❌ SYSTEM FAILURE
- Skipping trend analysis (that's the point of monthly)
- Not identifying chronic blockers
- Not checking goal alignment
- Treating this as "just another weekly" (missing the depth)
- Taking <15 min (too shallow) or >45 min (too detailed)

**Master Rule:** Monthly review is a "deeper weekly" that adds trend perspective and alignment checks. Same structure as weekly, but with 4-week hindsight and strategic foresight.

📖 **FULL PROTOCOLS:** See data/ folder for complete templates, metrics formats, and detection rules.
