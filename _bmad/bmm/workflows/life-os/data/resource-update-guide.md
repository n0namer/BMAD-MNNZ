# Resource Update Guide

This document contains detailed guidance, best practices, and analysis templates for Step E-02 (Update Resources).

## Resource Management Best Practices

### Capacity Planning

**40-50 hours/week: Sustainable for 3 projects**
- Optimal work-life balance
- Allows for deep focus and context switching
- Recommended: 15-17 hours per project + 5-8 hours overhead (planning, meetings, admin)

**60+ hours/week: Unsustainable**
- High burnout risk
- Diminishing returns after 50 hours
- Recommendation: Reduce WIP or extend timelines
- Quality suffers with fatigue

**<20 hours/week: Too fragmented**
- Insufficient time for meaningful progress
- Context switch overhead dominates
- Recommendation: Consolidate portfolio to 1-2 projects

**Sweet Spot:**
- 40-45 hours/week for 3 concurrent projects
- Each project gets 12-15 hours/week (sustainable velocity)
- 5-10 hours buffer for planning, reviews, unexpected issues

---

### WIP (Work in Progress) Limits

**3 projects: Optimal for focus + progress**
- Each project gets meaningful attention
- Reduces context switching overhead (<10% time lost)
- Allows for emergency handling (1 project can absorb extra time if needed)
- Progress visible week-over-week

**4+ projects: Context switch overhead increases**
- Overhead jumps to 20-30% (meetings, status syncs, mental switching)
- Each project gets <10 hours/week (slow progress)
- Risk of projects stalling
- Only worth it for:
  - Very small tasks (<5 hours each)
  - Projects in different phases (1 active, others in review/wait)

**1-2 projects: Only for high-risk or complex work**
- Good for learning new domain
- Good for high-stakes projects (e.g., revenue-critical)
- Risk: Single point of failure (if blocked, entire capacity idle)
- Recommendation: Add 1 low-risk project as backup

**WIP Limit by Experience:**
- Junior (0-2 years): 2 projects max
- Mid (2-5 years): 3 projects optimal
- Senior (5+ years): 3-4 projects (can handle more complexity)

---

### Timeline Constraints

**Common Constraint Types:**

**1. Vacation / PTO**
- Impact: 0% capacity during dates
- Planning:
  - Mark as "blocked" in project timelines
  - Add buffer before (finish milestones early)
  - Add buffer after (re-ramp time)
- Recommendation: 1 week buffer before, 2 days buffer after

**2. Conferences / Events**
- Impact: 50% capacity during event (travel, networking, recovery)
- Planning:
  - Reduce WIP 1 week before
  - Schedule low-intensity tasks during event
  - Add 3-5 days post-event buffer

**3. Life Events (move, construction, family)**
- Impact: 20-50% capacity for extended period
- Planning:
  - Reduce WIP immediately
  - Extend all project timelines by 1.5-2x
  - Pause non-critical projects

**4. Seasonal Constraints**
- Q4 holidays: Expect 30-40% capacity loss (Nov-Dec)
- Summer: Expect 20-30% capacity loss (vacation season)
- Q1: Peak productivity (Jan-Mar, fresh motivation)

**Timeline Adjustment Formula:**
```
Adjusted Timeline = Base Timeline ÷ (1 - Constraint Impact %)

Example:
Base: 4 weeks
Constraint: 25% capacity loss (vacation 1 week)
Adjusted: 4 ÷ (1 - 0.25) = 4 ÷ 0.75 = 5.3 weeks
```

---

### Budget Allocation

**Strategic Bucket Philosophy:**
- Prevents single-domain dominance (e.g., all projects in "work", none in "health")
- Ensures balanced life/business investment
- Forces prioritization within domains

**Recommended Allocation (Balanced):**
- Work/Business: 40-50%
- Personal Development: 20-25%
- Health/Fitness: 10-15%
- Family/Relationships: 10-15%
- Home/Living: 5-10%

**Aggressive Growth Allocation:**
- Work/Business: 60-70%
- Personal Development: 20-25%
- Health: 5-10%
- Other: 5%
- Use for: Short-term sprints (3-6 months max)

**Recovery/Balance Allocation:**
- Work/Business: 25-30%
- Health/Fitness: 25-30%
- Family/Relationships: 20-25%
- Personal Development: 15-20%
- Use for: Post-burnout recovery, sabbatical

**Budget Review Frequency:**
- Monthly: Check actual vs planned spend
- Quarterly: Rebalance buckets based on progress and priorities
- Annually: Major strategic shifts

**Underfunded Bucket Warning:**
- <15% allocation → Red flag for neglect
- Example: 0% in "Health" for 3 months → High burnout risk
- Action: Reallocate or pause projects in overfunded buckets

---

## Capacity Impact Analysis Templates

### Template 1: Capacity Change Impact

```markdown
## Capacity Impact Analysis

**Current State:**
- Available: {X} hours/week
- Active Projects: {Y}
- Current Utilization: {X/Y} hours per project

**Proposed Change:**
- New Capacity: {Z} hours/week
- Change: {Z-X > 0 ? "+increase" : "-decrease"} {|Z-X|} hours/week

**Impact on Projects:**
1. {Project1}: Currently {A} hrs/week → New: {A * Z/X} hrs/week
   - Timeline impact: {change_description}
2. {Project2}: Currently {B} hrs/week → New: {B * Z/X} hrs/week
   - Timeline impact: {change_description}
3. {Project3}: Currently {C} hrs/week → New: {C * Z/X} hrs/week
   - Timeline impact: {change_description}

**Overallocation Risk:**
{if total_project_hours > Z:
  "⚠️ WARNING: Projects require {total} hours but only {Z} available.
  Recommendation: {action_plan}"
else:
  "✅ Capacity sufficient. Free capacity: {Z - total} hours/week"}

**Recommended Actions:**
- [ ] {Action 1}
- [ ] {Action 2}
- [ ] {Action 3}
```

---

### Template 2: WIP Limit Change Impact

```markdown
## WIP Limit Change Analysis

**Current WIP:**
- Limit: {X} projects
- Active: {Y} projects ({Y ≤ X ? "within limit ✅" : "exceeds limit ⚠️"})

**Proposed WIP Limit:**
- New Limit: {Z} projects

**Status Check:**
{if Y > Z:
  "⚠️ ALERT: Current WIP ({Y}) exceeds new limit ({Z}).
  Must free {Y-Z} project slots.

  **Options:**
  1. Complete {Y-Z} projects (fastest path)
  2. Pause {Y-Z} projects (move to backlog)
  3. Kill {Y-Z} projects (archive, document learnings)

  **Project Candidates for Action:**
  {list projects sorted by: lowest priority, least progress, highest risk}"
else:
  "✅ Current WIP within new limit. Free slots: {Z-Y}"}

**Active Projects:**
1. {Project1} - {priority} - {progress}% - Status: {status}
2. {Project2} - {priority} - {progress}% - Status: {status}
...

**Recommendation:**
{recommendation_based_on_analysis}
```

---

### Template 3: Timeline Constraint Impact

```markdown
## Timeline Constraint Impact Analysis

**New Constraint:**
- Type: {Vacation | Conference | Build | Other}
- Name: {event_name}
- Dates: {start_date} to {end_date}
- Duration: {days} days
- Capacity Impact: {X}% loss

**Affected Projects:**

**Project 1: {name}**
- Current timeline: {start} → {end} ({weeks} weeks)
- Constraint overlaps: {overlap_days} days
- Adjusted timeline: {new_end} (+{extension} days)
- Milestones affected: {list}

**Project 2: {name}**
- Current timeline: {start} → {end} ({weeks} weeks)
- Constraint overlaps: {overlap_days} days
- Adjusted timeline: {new_end} (+{extension} days)
- Milestones affected: {list}

**Portfolio-Level Impact:**
- Total delay: {sum_extensions} days
- Projects affected: {count}
- Projects unaffected: {count}

**Mitigation Strategies:**
1. Front-load work before constraint (finish milestones early)
2. Schedule low-intensity tasks during constraint
3. Add buffer after constraint (re-ramp period)
4. Defer non-critical projects until after constraint

**Recommended Timeline Adjustments:**
{list all timeline changes}
```

---

### Template 4: Budget Reallocation Analysis

```markdown
## Budget Reallocation Analysis

**Current Budget:**
- Total: ${X} / {period}

**Current Allocation:**
| Bucket | Allocation | Amount | Active Projects | Avg per Project |
|--------|-----------|--------|-----------------|-----------------|
| {Bucket1} | {%1} | ${amt1} | {count1} | ${avg1} |
| {Bucket2} | {%2} | ${amt2} | {count2} | ${avg2} |
| {Bucket3} | {%3} | ${amt3} | {count3} | ${avg3} |

**Proposed Reallocation:**
| Bucket | Old % | New % | Change | New Amount | Impact |
|--------|-------|-------|--------|------------|--------|
| {Bucket1} | {%1} | {%1_new} | {+/-X%} | ${amt1_new} | {description} |
| {Bucket2} | {%2} | {%2_new} | {+/-X%} | ${amt2_new} | {description} |
| {Bucket3} | {%3} | {%3_new} | {+/-X%} | ${amt3_new} | {description} |

**Impact on Projects:**
1. {Project in Bucket1}: Budget {increased|decreased} by {X%} → {impact_description}
2. {Project in Bucket2}: Budget {increased|decreased} by {X%} → {impact_description}
...

**Underfunded Buckets:**
{if any bucket < 15%:
  "⚠️ WARNING: {Bucket_name} underfunded at {X%}. Risk of neglect.
  Recommendation: {increase_allocation_or_pause_projects}"
else:
  "✅ All buckets adequately funded"}

**Overfunded Buckets:**
{if any bucket > 50%:
  "⚠️ WARNING: {Bucket_name} overfunded at {X%}. Risk of single-domain focus.
  Recommendation: {rebalance_or_justify}"
else:
  "✅ No bucket dominates portfolio"}
```

---

## Red Flag Detection

### Critical Alerts

**🔴 Utilization >100%**
- **Problem:** Projects require more capacity than available
- **Impact:** All projects delayed, quality suffers, burnout risk
- **Action:**
  1. Reduce WIP (complete or pause 1 project)
  2. Extend timelines (1.5-2x)
  3. Delegate or outsource tasks
  4. Reduce scope (MVP-only)

**🔴 WIP > Limit**
- **Problem:** Too many concurrent projects
- **Impact:** Context switching overhead >30%, slow progress
- **Action:**
  1. Complete smallest/closest project
  2. Pause lowest priority project
  3. Kill projects with <20% progress and low strategic value

**🔴 Underfunded Bucket (<15%)**
- **Problem:** Life domain neglected
- **Impact:** Imbalance, potential burnout, health risks
- **Action:**
  1. Reallocate 10-15% from overfunded bucket
  2. Pause 1 project in overfunded bucket
  3. Add project in underfunded bucket

**🔴 Budget Unallocated (>20%)**
- **Problem:** Resources idle, lost opportunity
- **Impact:** Slower progress than possible
- **Action:**
  1. Increase investment in active projects
  2. Activate deferred ideas
  3. Add buffer for experiments

---

### Warning Alerts

**🟡 Utilization 80-100%**
- **Problem:** No buffer for unexpected issues
- **Impact:** Minor delay becomes major crisis
- **Action:** Add 10-20% buffer capacity (reduce hours per project)

**🟡 Underfunded Bucket (15-25%)**
- **Problem:** Bucket under-prioritized
- **Impact:** Slow progress in that domain
- **Action:** Review quarterly, consider reallocation

**🟡 Timeline Constraint Overlap**
- **Problem:** Multiple constraints in same period
- **Impact:** Compounding delays
- **Action:** Reschedule constraints if possible, or extend all timelines

---

## Resource Management Decision Tree

```
START: What resource change?

├─ CAPACITY (hours/week)
│  ├─ Increase → Check WIP capacity
│  │  ├─ WIP < limit → Distribute extra hours across projects
│  │  └─ WIP = limit → Consider activating new project
│  └─ Decrease → Check utilization
│     ├─ New capacity < current usage → RED FLAG
│     │  └─ Action: Reduce WIP or extend timelines
│     └─ New capacity ≥ current usage → OK
│        └─ Redistribute hours across projects
│
├─ WIP LIMIT
│  ├─ Increase → Check capacity
│  │  └─ Capacity sufficient? → OK, can add projects
│  └─ Decrease → Check current WIP
│     ├─ Current WIP > new limit → Must free slots
│     │  └─ Action: Complete, pause, or kill projects
│     └─ Current WIP ≤ new limit → OK
│
├─ TIMELINE CONSTRAINT
│  ├─ Add constraint → Recalculate all project timelines
│  │  ├─ Overlap with milestones? → Extend deadlines
│  │  └─ No overlap → Mark as blocked period
│  └─ Remove constraint → Recalculate (may accelerate)
│
└─ BUDGET
   ├─ Increase total → Allocate across buckets
   │  └─ Prioritize underfunded buckets first
   └─ Reallocate → Check bucket balance
      ├─ Any bucket <15%? → RED FLAG (underfunded)
      ├─ Any bucket >50%? → WARNING (overfunded)
      └─ 15-50% all buckets → OK (balanced)

END: Document change, recalculate portfolio, update metrics
```

---

## Common Scenarios & Solutions

### Scenario 1: New Job (Capacity Drop)

**Situation:** Started full-time job, capacity drops from 60 hrs/week to 20 hrs/week

**Analysis:**
- Current: 3 projects × 20 hrs = 60 hrs/week (100% utilization)
- New: 20 hrs/week available
- Overallocation: 60 - 20 = 40 hrs/week shortage

**Solution:**
1. Pause 2 projects (move to backlog)
2. Focus on 1 highest-priority project (20 hrs/week)
3. Extend timeline 3x (was 4 weeks → now 12 weeks)

---

### Scenario 2: Vacation Planning

**Situation:** 2-week vacation in 6 weeks

**Analysis:**
- Current: 3 projects, each 15 hrs/week, 6 weeks remaining
- Vacation impact: 2 weeks × 45 hrs = 90 hrs lost
- Projects affected: All 3

**Solution:**
1. Front-load work (4 weeks before vacation):
   - Increase to 50 hrs/week (10 hrs overtime)
   - Complete critical milestones early
2. During vacation: 0 hrs (full disconnect)
3. After vacation: 2-day re-ramp (low-intensity tasks)
4. Extend timelines: 6 weeks → 8 weeks (buffer)

---

### Scenario 3: Budget Cut

**Situation:** Budget reduced from $10k/month to $5k/month

**Analysis:**
- Current: $10k across 4 buckets
- New: $5k total (50% cut)
- Must prioritize ruthlessly

**Solution:**
1. Pause lowest-priority bucket projects
2. Reallocate to critical buckets:
   - Work/Business: 50% ($2.5k) - revenue-critical
   - Health: 20% ($1k) - prevent burnout
   - Personal Dev: 20% ($1k) - skill building
   - Other: 10% ($500) - minimal
3. Review in 3 months, resume paused projects if budget recovers

---

## Metrics to Track

**Weekly:**
- Actual hours worked vs capacity
- Hours per project (are they getting minimum viable attention?)
- Utilization % (target: 70-85%)

**Monthly:**
- WIP health (count active projects, check against limit)
- Budget spend by bucket (actual vs planned)
- Timeline adherence (on track, at risk, delayed)

**Quarterly:**
- Capacity trend (increasing, stable, decreasing)
- Bucket balance (any underfunded <15%?)
- Strategic alignment (are we working on right things?)

---

**Last Updated:** 2026-02-06
**Version:** 1.0
**Purpose:** Support Step E-02 (Update Resources) with detailed analysis templates and best practices
