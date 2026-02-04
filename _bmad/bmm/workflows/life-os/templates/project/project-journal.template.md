---
template: project-journal
domain: project_management
framework: Project Journal
timeInvestment: 5-10 min per entry
outputs:
  - project-journal.md
integration_points:
  - step-09-complete.md (creates first entry)
  - Weekly review (new entries)
  - Monthly review (monthly summary)
---

# Project Journal: {Project Name}

**Project ID:** {id}
**Created:** {date}
**Last Entry:** {date}

---

## Purpose

This journal captures:
- Daily/weekly progress updates
- Decisions made and rationale
- Blockers encountered and resolved
- Insights and patterns discovered
- Framework effectiveness ratings

**Update frequency:** {Daily / Weekly / Per Milestone}

---

## Entry Format

### {Date} - {Entry Title}

**Status:** {On Track / At Risk / Blocked / Completed}

**Progress:**
- Completed: {what was done}
- Next: {what's coming}
- Blocked by: {if applicable}

**Time Investment:**
- Planned: {hours/pomodoros}
- Actual: {hours/pomodoros}
- Variance: {difference}

**Decisions:**
- Decision: {what was decided}
- Rationale: {why}
- Alternatives considered: {what else was considered}

**Frameworks Used This Period:**
- {Framework 1}: {effectiveness 1-5 stars} - {comment}
- {Framework 2}: {effectiveness 1-5 stars} - {comment}

**Insights:**
- {Learning 1}
- {Learning 2}

**Mood/Energy:** {1-10 scale}

---

## Entry 1: Project Initiation

**Date:** {date from Step 9}
**Status:** Initiated

**Milestone:** Project plan created and approved

**Frameworks Activated:**
- Design Thinking (Step 1): 5/5 - Empathy framing clarified problem
- Six Thinking Hats (Step 4): 4/5 - Balanced perspectives from consilium
- MCDA (Step 5): 4/5 - Clear prioritization
{List all frameworks used}

**Initial Metrics:**
{Baseline values from Success Metrics table}

**Excitement Level:** {1-10}

**Confidence Level:** {1-10}

**Key Decisions:**
1. {Decision from workflow}
2. {Decision from workflow}

---

## Entry 2: {Title}

**Date:** {date}
**Status:** {On Track / At Risk / Blocked / Completed}

**Progress:**
- Completed: {what was done}
- Next: {what's coming}
- Blocked by: {if applicable}

**Time Investment:**
- Planned: {hours/pomodoros}
- Actual: {hours/pomodoros}
- Variance: {difference}

**Decisions:**
- Decision: {what was decided}
- Rationale: {why}
- Alternatives considered: {what else was considered}

**Frameworks Used This Period:**
- {Framework 1}: {effectiveness 1-5 stars} - {comment}
- {Framework 2}: {effectiveness 1-5 stars} - {comment}

**Insights:**
- {Learning 1}
- {Learning 2}

**Mood/Energy:** {1-10 scale}

---

## Monthly Summary Template

### Month {N}: {Month Name Year}

**Overall Status:** {summary}

**Key Achievements:**
1. {Achievement 1}
2. {Achievement 2}

**Challenges:**
1. {Challenge 1} - {How addressed}
2. {Challenge 2} - {How addressed}

**Metrics Progress:**
{Updated KPI table from project plan}

**Frameworks Effectiveness This Month:**

| Framework | Uses | Avg Rating | Key Insight |
|-----------|------|------------|-------------|
| {Framework 1} | {count} | {1-5}/5 | {insight} |
| {Framework 2} | {count} | {1-5}/5 | {insight} |

**Time Tracking:**
- Planned: {hours}
- Actual: {hours}
- Efficiency: {actual/planned x 100}%

**Adjustments for Next Month:**
1. {Adjustment 1}
2. {Adjustment 2}

---

## Quarterly Summary Template

### Quarter {N}: {Q1/Q2/Q3/Q4 Year}

**OKR Progress:** {if OKRs used}
- Objective 1: {X}% complete
- Objective 2: {X}% complete

**Domain-Specific Progress:**
{Business: Revenue/customers metrics}
{Finance: ROI/NPV actual vs projected}
{Health: Weight/fitness metrics}
{Personal: Skills acquired/habits formed}

**Biggest Wins:**
1. {Win 1}
2. {Win 2}

**Biggest Lessons:**
1. {Lesson 1}
2. {Lesson 2}

**Pattern Recognition:**
{What patterns emerged - when most productive, which frameworks most useful, etc.}

---

## Annual Review Template

### Year {YYYY} Review

**Mission Alignment:**
- Original mission: {from L1}
- Still aligned: {Yes / No / Evolved}
- Evolution: {how mission has evolved, if applicable}

**Year Highlights:**
1. {Highlight 1}
2. {Highlight 2}
3. {Highlight 3}

**Year Challenges:**
1. {Challenge 1} - {Resolution}
2. {Challenge 2} - {Resolution}

**Framework Usage Summary:**

| Framework | Total Uses | Avg Effectiveness | Verdict |
|-----------|-----------|-------------------|---------|
| {Framework 1} | {count} | {1-5}/5 | {Keep / Modify / Replace} |
| {Framework 2} | {count} | {1-5}/5 | {Keep / Modify / Replace} |

**Cumulative Time Investment:**
- Total hours: {sum}
- Average hours/week: {avg}
- Most productive period: {when}

**Next Year Focus:**
1. {Priority 1}
2. {Priority 2}

---

## Template Notes

**Best Practices:**
- Write entries same day (fresher memory)
- Be honest about setbacks (learning opportunity)
- Rate frameworks after each use (improve selection)
- Review monthly summaries before planning next month
- Store in Claude Flow Memory for cross-project learning

**Memory Storage:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:journals:{project_id}:summary:{date}" \
  --content "{monthly or quarterly summary}"
```

---

**Template Version:** 1.0
**Last Updated:** 2026-02-04
