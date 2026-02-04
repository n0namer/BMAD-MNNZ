---
template: project-snapshot
domain: project_management
framework: Project Snapshot
timeInvestment: 10-15 min per snapshot
outputs:
  - project-snapshot-{date}.md
integration_points:
  - step-09-complete.md (creates initial baseline)
  - Milestone completion (new snapshots)
  - Monthly review (monthly snapshot)
---

# Project Snapshot: {Project Name}

**Snapshot Date:** {date}
**Snapshot Type:** {Initial Baseline / Milestone / Monthly / Quarterly / Final}
**Project Status:** {Initiated / In Progress / On Track / At Risk / Blocked / Completed}

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Project Age | {days/weeks since start} |
| Completion | {%} |
| Budget Used | {if applicable - $X / $Y = Z%} |
| Time Invested | {hours total} |
| Current Phase | {L2 phase name} |
| Next Milestone | {date} |

---

## Progress Overview

**L2 Phases Status:**

| Phase (L2) | Status | Start Date | End Date | Progress |
|------------|--------|------------|----------|----------|
| {Phase 1} | Done | {date} | {date} | 100% |
| {Phase 2} | In Progress | {date} | {target} | {%} |
| {Phase 3} | Pending | - | {target} | 0% |

**L3 Activities Status:** {X}/{Y} complete

**L4 Tasks Status:** {X}/{Y} complete

---

## Metrics Snapshot

**Success Metrics Current State:**

| Metric | Baseline | Target | Current | Delta | Status |
|--------|----------|--------|---------|-------|--------|
| {Metric 1} | {value} | {value} | {value} | {+/-X} | {red/yellow/green} |
| {Metric 2} | {value} | {value} | {value} | {+/-X} | {red/yellow/green} |

**Trend:** {Improving / Stable / Declining}

---

## Domain-Specific Metrics

{If Business}
**Business Metrics:**
- Revenue: {current vs target}
- Customers: {current vs target}
- Market Share: {if applicable}

{If Finance}
**Financial Metrics:**
- Actual NPV: {value} vs Projected: {value}
- ROI: {%}
- Payback Period: {months actual vs projected}

{If Health}
**Health Metrics:**
- Weight: {kg} (target: {kg})
- Fitness Level: {metric - strength/cardio}
- Habit Adherence: {%}

{If Personal Development}
**Personal Metrics:**
- Skill Level: {1-10 or certification achieved}
- Practice Hours: {total}
- Milestones: {X}/{Y} completed

---

## Frameworks Performance

**Active Frameworks This Period:**

| Framework | Uses | Avg Effectiveness | Key Contribution |
|-----------|------|-------------------|------------------|
| {Framework 1} | {count} | {1-5}/5 | {what it helped with} |
| {Framework 2} | {count} | {1-5}/5 | {what it helped with} |

**Most Valuable Framework:** {name} - {why}

**Least Used Framework:** {name} - {why not used}

---

## Blockers & Risks

**Current Blockers:**
1. {Blocker 1} - Severity: {High/Medium/Low} - Since: {date}
2. {Blocker 2} - Severity: {High/Medium/Low} - Since: {date}

**Active Risks:**

| Risk | Probability | Impact | Mitigation Status |
|------|-------------|--------|-------------------|
| {Risk 1} | {%} | {H/M/L} | {Mitigated/In Progress/Open} |
| {Risk 2} | {%} | {H/M/L} | {Mitigated/In Progress/Open} |

---

## Resource Utilization

**Time:**
- Planned this period: {hours}
- Actual this period: {hours}
- Cumulative: {total hours}
- Efficiency: {actual/planned x 100}%

**Budget:** {if applicable}
- Planned: ${amount}
- Spent: ${amount}
- Remaining: ${amount}
- Burn Rate: ${per week}

**Team:** {if applicable}
- Active contributors: {count}
- Utilization: {%}

---

## Velocity & Predictions

**Completed Since Last Snapshot:**
- L2 Phases: {count}
- L3 Activities: {count}
- L4 Tasks: {count}

**Current Velocity:**
- Tasks per week: {avg}
- Pomodoros per week: {avg}

**Projected Completion:**
- Original target: {date}
- Current projection: {date}
- Variance: {+/- X days/weeks}

---

## Energy & Motivation

**Team Morale:** {if applicable - 1-10}

**Owner Energy Level:** {1-10}

**Motivation Trend:** {Increasing / Stable / Declining}

**Burnout Risk:** {Low / Medium / High}

{If High: Recommended actions}

---

## Adjustments Since Last Snapshot

**Changes Made:**
1. {Date}: {What changed} - {Why}
2. {Date}: {What changed} - {Why}

**Scope Changes:**
- Added: {features/tasks}
- Removed: {features/tasks}
- Deferred: {features/tasks}

---

## Insights & Patterns

**What's Working Well:**
1. {Pattern 1}
2. {Pattern 2}

**What Needs Improvement:**
1. {Issue 1}
2. {Issue 2}

**Surprising Discoveries:**
- {Discovery 1}
- {Discovery 2}

---

## Next Snapshot

**Scheduled For:** {date}
**Type:** {Milestone / Monthly / Quarterly}
**Key Questions to Answer:**
1. {Question 1}
2. {Question 2}

---

## Memory Storage

**Store this snapshot in Claude Flow Memory:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:snapshots:{project_id}:{date}" \
  --content "{
    type: '{snapshot_type}',
    completion: {%},
    metrics: {json},
    status: '{status}',
    velocity: {tasks_per_week},
    frameworks_effective: ['{top_3}'],
    insights: ['{key_insights}']
  }"
```

---

**Snapshot Version:** 1.0
**Next Review:** {date}
**Template Version:** 1.0
**Last Updated:** 2026-02-04
