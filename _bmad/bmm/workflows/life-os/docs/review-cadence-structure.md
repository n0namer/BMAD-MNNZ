# Review Cadence Structure — Life OS v3.0

**Implemented:** 2026-02-05
**Problem Solved:** Daily review too trivial (3 questions, 2 min), quarterly too complex (600+ lines, untested). No substantive middle ground.

## Overview

Life OS uses a 4-tier review system with **Weekly as the PRIMARY review cadence**:

| Cadence | Duration | Status | Purpose |
|---------|----------|--------|---------|
| **Daily** | 1-2 min | **OPTIONAL** | Lightweight standup signals |
| **Weekly** | 15-20 min | **PRIMARY** | Substantive progress tracking |
| **Monthly** | 30 min | Required | "Deeper weekly" + trends |
| **Quarterly** | 60-90 min | Required | Strategic goal adjustment |

---

## Daily Review (OPTIONAL)

**File:** `steps-v/step-01-daily-review.md`
**Duration:** 1-2 minutes
**Frequency:** Optional (skip recommended for most users)
**Format:** "Standup mode"

### Structure

1. **Skip Prompt** — ALWAYS offer skip option first
   - Most users should skip to weekly review
   - Only useful for high-discipline users

2. **3 Questions** (if not skipped):
   - What is your ONE focus today?
   - Any blockers right now?
   - What's tomorrow's top priority?

3. **Minimal Metrics**:
   ```markdown
   ## Daily Standup — {date}
   - Today: {focus}
   - Blocker: {blocker_or_none}
   - Tomorrow: {priority}
   ```

### Success Criteria

- ✅ User offered skip option FIRST
- ✅ Completed in 1-2 minutes (not longer)
- ✅ Only 3 short answers captured
- ❌ NEVER make daily feel mandatory
- ❌ NEVER ask for detailed answers

**Master Rule:** Daily is OPTIONAL and LIGHTWEIGHT. Weekly is where substantive tracking happens.

---

## Weekly Review (PRIMARY CADENCE)

**File:** `steps-v/step-02-weekly-review.md`
**Duration:** 15-20 minutes
**Frequency:** Required weekly
**Format:** Substantive progress review

### Structure (5 Sections)

#### 1. Milestone Progress Check (~5 min)

For each active project:
- **Progress vs Plan:** Planned % vs Actual %
- **Timeline Status:** Behind/On track/Ahead
- **Course Correction:** If behind, what changes this week?

**Captures:**
- Planned vs actual progress
- Timeline delta (days behind/ahead)
- Root cause of delays

#### 2. WIP Health Check (~3 min)

- **Active projects:** Count vs WIP limit
- **Capacity status:** Healthy/Warning/Overload
- **Context switching:** Frequency count

**WIP Assessment:**
- ✅ Healthy: Active ≤ WIP limit
- ⚠️ Warning: Active = WIP limit + 1
- 🚨 Overload: Active > WIP limit + 1

**Proactive overload detection:**
```
If overload → Suggest pausing (N - limit) projects
```

#### 3. Blockers & Risks (~5 min)

For each blocker:
- **Description:** What's blocking
- **Severity:** Low/Medium/High
- **Owner:** You/External/Unknown
- **Resolution:** Can this be resolved this week?

**Proactive flagging:**
- Blocker >7 days → Flag as chronic
- Affects critical path → Highlight urgency
- External dependency → Suggest follow-up

#### 4. Next Week Priorities (~4 min)

Top 3 focus areas:
- **What:** Task or milestone
- **Why:** Goal alignment
- **Success criteria:** Completion definition
- **Effort:** Hours/days estimate

**Capacity check:**
```
If total effort > capacity → Flag overcommitment
```

#### 5. Quick Wins (~2 min)

- **Wins:** Small victories this week
- **Learning:** What will help next week
- **Gratitude:** What are you grateful for

### Metrics Output

```markdown
## Weekly Review — {week_of_date}

### Milestone Progress
- **{project}**: {milestone}
  - Planned: {X}% | Actual: {Y}%
  - Status: [On Track / Behind by N days / Ahead by N days]
  - Course correction: {action}

### WIP Health
- Active: {count}/{limit}
- Status: [✅ Healthy / ⚠️ Warning / 🚨 Overload]
- Context switches: {count}
- Action: {if_overload}

### Blockers & Risks
- **{blocker}**
  - Affects: {project}
  - Severity: {level}
  - Resolution: {plan}

### Next Week Priorities
1. {priority_1} — {success_criteria}
2. {priority_2} — {success_criteria}
3. {priority_3} — {success_criteria}

Capacity: {realistic/overcommitted}

### Quick Wins
- {win_1}
- {win_2}
- Learning: {learning}
```

### Success Criteria

- ✅ All 5 sections completed
- ✅ Substantive answers (not 1-word)
- ✅ Structured metrics appended
- ✅ Clear priorities for next week
- ✅ Completed in 15-20 min
- ❌ NEVER skip sections (except Quick Wins if time-pressed)
- ❌ NEVER accept vague answers ("fine", "ok")

**Master Rule:** Weekly is the PRIMARY substantive review. Comprehensive enough to track progress and catch drift, quick enough to do consistently.

---

## Monthly Review ("Deeper Weekly")

**File:** `steps-v/step-03-monthly-review.md`
**Duration:** 30 minutes
**Frequency:** Required monthly
**Format:** Weekly structure + Trend analysis + Alignment check

### Structure (Same as Weekly + 3 Additions)

Monthly review uses **SAME 5 sections as weekly**, but adds:

#### Addition 1: Trend Analysis (for Sections 1-3)

**Milestone Progress Trends:**
```
Project: {name}
  - Week 1: {X}%
  - Week 2: {Y}%
  - Week 3: {Z}%
  - Week 4: {W}%
  - Velocity: {avg}% per week
  - Forecast: {completion_date}
  - Trend: [Improving/Declining/Stable]
```

**WIP Pattern Analysis:**
```
Average WIP: {avg} projects
  - Week 1-4: {counts}
Pattern: [Stable/Increasing/Decreasing/Chaotic]

Context switches: {avg} per week
  - Week 1-4: {counts}
```

**Chronic Blocker Detection:**
```
Blocker: {description}
  - First appeared: Week {N}
  - Weeks stuck: {count}
  - Escalation needed: {yes/no}
```

**Proactive trend detection:**
- Velocity declining 3+ weeks → Risk flag
- WIP consistently above limit → Chronic overcommitment
- Context switches increasing → Quality risk
- Blocker >2 weeks → Escalation needed

#### Addition 2: Alignment Check (~5 min)

Load goals.yaml and portfolio.md:

Ask:
1. **Alignment score:** What % of projects support top goals?
2. **Misaligned work:** Which projects NOT aligned?
3. **Stop/Deprioritize:** What should be paused?
4. **New opportunities:** What emerged that aligns?

**For each project:**
```
Project: {name}
  Supports goal: {goal_or_none}
  Strength: [Strong/Weak/None]
  Decision: [Continue/Stop/Pause]
```

**Proactive misalignment detection:**
- >30% projects with no goal → Portfolio drift
- High-priority goal with no projects → Gap
- Low-priority consuming most time → Resource misallocation

#### Addition 3: Strategic Scope

- **Next Month Priorities** (not just next week)
- **Monthly forecast** (not just weekly forecast)

### Metrics Output

Same as weekly, plus:
```markdown
### Milestone Progress & Trends
- Velocity: {avg_%} per week
- Forecast: {date}
- Trend: [Improving/Declining/Stable]

### WIP Health & Patterns
- Pattern: [Stable/Chaotic]
- Chronic overload: {yes/no}

### Blockers & Chronic Issues
- **🚨 CHRONIC**: {blocker}
  - Duration: {weeks}
  - Escalation: {action}

### Goal Alignment
- Score: {X}%
- Misaligned: {count}
- To stop: {list}
- New opportunities: {list}
```

### Success Criteria

- ✅ All weekly sections + trends + alignment
- ✅ 4-week trend analysis captured
- ✅ Chronic blockers identified
- ✅ Goal alignment % calculated
- ✅ Completed in ~30 min
- ❌ NEVER skip trend analysis
- ❌ NEVER skip alignment check

**Master Rule:** Monthly is "deeper weekly" with 4-week hindsight and strategic foresight.

---

## Quarterly Review (Strategic Only)

**File:** `steps-v/step-04-quarterly-review.md`
**Duration:** 60-90 minutes
**Frequency:** Required quarterly
**Format:** OKR review + Goal adjustment + Q+1 planning

### Purpose

Quarterly is **NOT another progress review** — it's for:
- Reviewing quarterly OKRs and Key Results
- Adjusting goals based on learnings
- Planning next quarter's theme and focus

**Progress tracking happens in weekly/monthly reviews.**

Quarterly is purely strategic:
1. **CHECK Phase:** Review OKRs, analyze actual vs planned
2. **ACT Phase:** Adjust goals, reallocate resources, update strategy

---

## Review Cadence Comparison

| Aspect | Daily | Weekly | Monthly | Quarterly |
|--------|-------|--------|---------|-----------|
| **Status** | Optional | **PRIMARY** | Required | Required |
| **Duration** | 1-2 min | 15-20 min | 30 min | 60-90 min |
| **Frequency** | Daily (skip OK) | Every week | Every month | Every quarter |
| **Focus** | Standup signals | Progress tracking | Trends + Alignment | Goal adjustment |
| **Questions** | 3 | 15+ | 20+ | 40+ |
| **Scope** | Today + Tomorrow | Last 7 + Next 7 days | Last 4 weeks | Last 90 days |
| **Metrics** | Minimal | Structured | Structured + Trends | Comprehensive |
| **Proactive** | None | Overload detection | Chronic issues | Strategic shifts |
| **Output** | 3 lines | 15-20 lines | 25-30 lines | Full report |

---

## Why This Structure Works

### Problem Before

- **Daily:** Too trivial (3 questions, auto-proceeds in 2 min)
- **Quarterly:** Too complex (600+ lines, untested, overwhelming)
- **Gap:** No substantive middle ground for regular tracking

### Solution Now

- **Daily:** Optional standup (skip recommended)
- **Weekly:** PRIMARY substantive review (15-20 min, realistic rhythm)
- **Monthly:** Deeper weekly (adds trends, not a different format)
- **Quarterly:** Strategic only (not another progress review)

### Benefits

1. **Realistic rhythm:** 15-20 min weekly is doable consistently
2. **Catch drift early:** Weekly frequency prevents 90-day blind spots
3. **Consistent structure:** Monthly uses same format as weekly (+ trends)
4. **Clear hierarchy:** Users know weekly is PRIMARY, not daily
5. **Strategic separation:** Quarterly focused on goals, not tactics

---

## User Guidance

**When starting Life OS, tell users:**

```
Your PRIMARY review cadence is WEEKLY (15-20 min).

Weekly Review covers:
1. Milestone Progress (are you on track?)
2. WIP Health (overloaded?)
3. Blockers & Risks (what's stuck?)
4. Next Week Priorities (top 3 focus areas)
5. Quick Wins (morale boost)

Daily Review is OPTIONAL (most should skip).
Monthly Review is "deeper weekly" (same format + trends).
Quarterly Review is for goal adjustment only.

Start with weekly reviews. If that works, try monthly.
Skip daily unless you want discipline signals.
```

---

## Implementation Notes

### For Claude

**At start of validation sequence:**
1. If user at step-01 (daily) → ALWAYS offer skip to weekly
2. If user accepts daily → Keep it 1-2 min MAX
3. If user at step-02 (weekly) → Emphasize this is PRIMARY
4. If user at step-03 (monthly) → Run weekly format + add trends

**Proactive suggestions:**
- If weekly review takes <5 min → "Let's add more depth to track properly"
- If weekly takes >30 min → "Let's keep this focused, save deep analysis for monthly"
- If user tries to skip weekly → "Weekly is PRIMARY — can we do at least 3 sections?"

### Success Metrics

| Metric | Target | Measures |
|--------|--------|----------|
| Weekly adoption rate | >80% | Users doing weekly consistently |
| Weekly duration | 15-20 min | Substantive but not overwhelming |
| Daily skip rate | >70% | Daily is truly optional |
| Monthly depth | Trends captured | 4-week patterns identified |
| Quarterly focus | Strategic only | Not duplicating weekly/monthly |

---

**End of Review Cadence Structure**
