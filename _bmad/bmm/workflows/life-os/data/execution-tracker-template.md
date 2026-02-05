# Execution Tracker Template

## File Location

`{bmb_creations_output_folder}/life-os/output/{idea-id}-execution-tracker.md`

## Full File Structure

```markdown
---
idea_id: '{id}'
idea_name: '{name}'
status: 'IN_PROGRESS'
kickoff_date: '{YYYY-MM-DD}'
last_updated: '{YYYY-MM-DD}'
completion_percentage: 0
---

# Execution Tracker: {Idea Name}

## Project Overview
**Status:** IN_PROGRESS
**Kickoff Date:** {YYYY-MM-DD}
**Last Updated:** {YYYY-MM-DD}
**Overall Completion:** 0%

## Milestones

### Milestone 1: {Name}
**Target Date:** {YYYY-MM-DD}
**Status:** Not Started
**Progress:** 0%

**Success Criteria:**
- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

**Blocker Risks:**
- ⚠️ {Risk 1}
- ⚠️ {Risk 2}

**Actual Completion:** [TBD]
**Notes:** _[Space for execution notes]_

---

[Repeat for each milestone]

---

## Success Metrics

### Metric 1: {Name}
**Definition:** {How measured}
**Target:** {Value ± tolerance}
**Frequency:** {Weekly/Milestone/Final}
**Current Value:** [TBD]
**Status:** 🟢 On Track

**History:**
- {YYYY-MM-DD}: [Value] - {Note}

---

[Repeat for each metric]

---

## Timeline Tracking

**Variance Tolerance:** ±{X}%

| Milestone | Target Date | Forecasted Date | Actual Date | Variance |
|-----------|-------------|-----------------|-------------|----------|
| M1 | {date} | [TBD] | [TBD] | [TBD] |
| M2 | {date} | [TBD] | [TBD] | [TBD] |
| M3 | {date} | [TBD] | [TBD] | [TBD] |

## Execution Log

### {YYYY-MM-DD} - Kickoff
- Project kicked off
- Milestones and metrics defined
- Status: IN_PROGRESS

---

_[Future execution notes will be appended here during Step X-02: Tracking]_
```

## Confirmation Message

```
✅ Execution tracker created: {file_path}
```
