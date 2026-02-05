---
name: 'step-x-02-weekly-pulse'
description: 'Quick 3-question weekly status check for IN_PROGRESS ideas to track progress, detect blockers early, and maintain momentum'
category: 'execution'
duration: '5-7 min'
frequency: 'weekly'
required: false
---

# Step X-02: Weekly Pulse Check

## STEP GOAL

Quick 3-question status check for IN_PROGRESS ideas to:
- Track weekly progress against milestones
- Detect blockers and risks early
- Maintain momentum and accountability
- Prevent silent drift or abandonment

**Time investment:** 5-7 minutes per idea
**Value:** Early warning system prevents catastrophic delays

---

## WHEN TO USE

### Automatic Triggers
- **Weekly Review (step-v-02)**: Presents all IN_PROGRESS ideas for pulse check
- **Milestone Approaching**: 7 days before deadline
- **Status Change**: When idea moves to IN_PROGRESS

### Manual Triggers
- Command: `/pulse {idea-id}`
- Feeling stuck or uncertain about progress
- Before team sync or stakeholder update

### Skip Conditions
- Idea on planned pause (documented reason)
- No expected progress this week (dependencies)
- Completed or killed status

---

## MANDATORY EXECUTION RULES

1. **Complete all 3 questions** - No partial pulses
2. **Honest status assessment** - Red weeks are data, not failure
3. **Single next-week priority** - Focus on ONE objective
4. **Save to all 3 locations** - Tracker + Memory + Metadata
5. **Use subprocess for IN_PROGRESS ideas grep** (Pattern 1: Grep)
6. **Return structured pulse tracker only**

---

## MANDATORY SEQUENCE

### 1. Load IN_PROGRESS Ideas & Pulse Protocol (Subprocess)

📖 **Protocol:** data/weekly-pulse-protocol.md

**Launch a subprocess that:**
1. Greps all workflow plan files for `status: IN_PROGRESS` (Pattern 1: Grep)
2. Loads pulse tracker history for each IN_PROGRESS idea
3. Loads weekly-pulse-protocol.md with 3-question template
4. Returns:
   - List of IN_PROGRESS ideas with last pulse date
   - Ideas needing pulse (>7 days since last check)
   - Pre-filled context (last week's Q3 → this week's Q1 context)

**Subprocess returns:** Focused IN_PROGRESS list + pulse context (200-300 lines) instead of scanning all projects + loading full weekly-pulse-protocol.md (1800+ lines).

**Graceful fallback:** If subprocess unavailable, manually grep for `status: IN_PROGRESS` and load `data/weekly-pulse-protocol.md`.

Guide user through 3-question template:
- Q1: Progress This Week (what got done + completion %)
- Q2: Blockers/Risks (severity + resolution plan)
- Q3: Next Week Priority (one clear objective)

### 2. Calculate Status

📖 **Status Logic:** data/pulse-status-calc.md

#### Pulse Status Calculation Loading (Subprocess)

**Launch a subprocess that:**
1. Loads data/pulse-status-calc.md
2. Extracts status formula section only
3. Applies variance calculation to actual progress
4. Returns status + alert trigger (typically 20-30 lines instead of 120)

**Subprocess returns:** Calculated status (🟢/🟡/🔴) + alert condition

**Graceful fallback:** If subprocess unavailable, use manual threshold comparison in main context.

Apply formula and check alert conditions:
- 🟢 On Track: ±20% variance
- 🟡 At Risk: 20-40% behind
- 🔴 Blocked: >40% behind OR critical blocker

**Alert System:** Auto-trigger escalations based on patterns

### 3. Save Results

📖 **Save Protocol:** data/pulse-tracker-update.md

#### Pulse Tracker Update Loading (Subprocess)

**Launch a subprocess that:**
1. Loads data/pulse-tracker-update.md
2. Extracts save protocol section matching project type
3. Filters to 3-location save procedure
4. Returns applicable formatting rules (typically 30-50 lines instead of 180)

**Subprocess returns:** Formatted pulse entry template ready to save

**Graceful fallback:** If subprocess unavailable, save pulse status + timestamp + status + notes to tracking file manually.

Update 3 locations:
1. Append to execution tracker file
2. Store in memory (execution:tracking namespace)
3. Update goals.yaml metadata

---

## MENU OPTIONS

After loading files above, present:

```
Weekly Pulse for {Idea Name}

1. [Start Pulse] - Answer 3 questions
2. [View History] - Past pulse reports
3. [Check Alerts] - Active warnings
4. [Skip (explain)] - Document reason
```

**If alerts active:** Display warning before proceeding

---

## SUCCESS CRITERIA

✅ **Complete pulse:**
- All 3 questions answered
- Status calculated and assigned
- Saved to all 3 locations
- Alerts checked and handled

✅ **Quality indicators:**
- Specific accomplishments in Q1
- Actionable resolution plans in Q2
- Clear success criteria in Q3
- Honest status assessment

---

## FAILURE CONDITIONS

❌ **Incomplete pulse:**
- Missing questions
- Vague answers ("made progress")
- No completion percentage
- Status not updated

❌ **Ignored alerts:**
- Repeated blockers not escalated
- Consecutive red weeks without action
- Stagnant progress without decision

---

## COMMANDS

```bash
# Manual pulse trigger
/pulse {idea-id}

# Pulse all IN_PROGRESS ideas
/pulse --all

# View pulse history
/pulse {idea-id} --history

# Check alerts
/pulse --alerts
```

---

## DATA FILES REFERENCE

| File | Purpose | Load When |
|------|---------|-----------|
| data/weekly-pulse-protocol.md | 3-question template + examples | Step 1 (always) |
| data/pulse-status-calc.md | Status formula + alerts | Step 2 (always) |
| data/pulse-tracker-update.md | Save locations + format | Step 3 (always) |

---

**Next Step:** If 🔴 status → Consider [Step X-04: Pivot or Kill](step-x-04-pivot-or-kill.md)

**Related:** [Weekly Review](../steps-v/step-v-02-weekly-review.md) | [Execution Tracker](../data/execution-tracker-template.md)
