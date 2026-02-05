# Calendar Event Templates

## Purpose
Standardized templates for creating calendar events from Life OS project milestones.

## Template 1: Milestone Event (Standard)

**Use for:** Most project milestones

```
Title: 🎯 [Project Name]: [Milestone Name]
Start: [Date] 09:00 AM
End: [Date] 11:00 AM
All-day: No
Reminder: 3 days before, 1 day before
Color: Blue (default project color)
Description:
  Project: [Project Name]
  Milestone: [Milestone Name]
  Status: PLANNED
  Effort: [hours] hours estimated
  Dependencies: [list if any]
  Success Criteria: [brief criteria]

  📁 Project File: {outputProjectFile}
  📋 Workflow Plan: {workflowPlanFile}
```

**Example:**
```
Title: 🎯 Life OS v3: Initial Prototype Complete
Start: 2026-02-15 09:00 AM
End: 2026-02-15 11:00 AM
Reminder: Feb 12 (3 days), Feb 14 (1 day)
Color: Blue
Description:
  Project: Life OS v3
  Milestone: Initial Prototype Complete
  Status: PLANNED
  Effort: 12 hours estimated
  Dependencies: None
  Success Criteria: Core workflow functional, basic UI complete
```

## Template 2: Capacity Block (Work Session)

**Use for:** Scheduled work time for projects

```
Title: 🔨 [Project Name] - Work Block
Start: [Date] [Time]
End: [Date] [Time + Duration]
Recurring: Weekly on [Days]
Reminder: 15 minutes before
Color: [Project Color]
Description:
  Allocated work time for [Project Name]
  Weekly capacity: [hours/week]
  Focus: [current phase or task]

  🚫 Protect this time - no meetings
```

**Example:**
```
Title: 🔨 Life OS v3 - Work Block
Start: Monday 09:00 AM
End: Monday 11:00 AM
Recurring: Weekly on Mon, Wed
Reminder: 15 min before
Color: Purple
Description:
  Allocated work time for Life OS v3
  Weekly capacity: 4 hours/week
  Focus: Development sprint

  🚫 Protect this time - no meetings
```

## Template 3: Deadline (Hard Date)

**Use for:** Non-negotiable deadlines, external dependencies

```
Title: ⏰ DEADLINE: [Project Name] - [Deliverable]
Start: [Date] 17:00 (end of day)
End: [Date] 17:00
All-day: No
Reminder: 1 week, 3 days, 1 day, morning of
Color: Red
Priority: High
Description:
  🚨 HARD DEADLINE 🚨
  Project: [Project Name]
  Deliverable: [What's due]
  Stakeholder: [Who's waiting]
  Consequence of miss: [Impact]

  Status: [ON TRACK / AT RISK / DELAYED]
```

**Example:**
```
Title: ⏰ DEADLINE: Life OS v3 - Beta Release
Start: 2026-03-31 17:00
Reminder: Mar 24, Mar 28, Mar 30, Mar 31 9am
Color: Red
Priority: High
Description:
  🚨 HARD DEADLINE 🚨
  Project: Life OS v3
  Deliverable: Beta version to early adopters
  Stakeholder: 50 beta testers waiting
  Consequence of miss: Lose early adopter momentum

  Status: ON TRACK
```

## Template 4: Review/Checkpoint

**Use for:** Scheduled reviews, decision points

```
Title: 📊 [Project Name] - [Review Type]
Start: [Date] [Time]
End: [Date] [Time + 30-60min]
Recurring: [If periodic, e.g., biweekly]
Reminder: 1 day before
Attendees: [Stakeholders if applicable]
Color: Green
Description:
  Review Type: [Weekly/Monthly/Phase Gate]
  Project: [Project Name]

  Agenda:
  - Review progress vs. plan
  - Surface blockers and risks
  - Adjust timeline if needed
  - Confirm next milestone

  📁 Snapshot: {snapshotsFolder}
  📓 Journal: {journalFolder}
```

**Example:**
```
Title: 📊 Life OS v3 - Sprint Review
Start: Friday 14:00
End: Friday 15:00
Recurring: Biweekly on Fridays
Reminder: Thursday 14:00
Color: Green
Description:
  Review Type: Sprint Review
  Project: Life OS v3

  Agenda:
  - Demo completed features
  - Review velocity and burndown
  - Identify blockers
  - Plan next sprint priorities
```

## Template 5: Buffer/Slack Time

**Use for:** Padding between milestones, unplanned work

```
Title: 🛡️ Buffer - [Project Name]
Start: [Date]
End: [Date + Buffer Duration]
All-day: Yes
Color: Gray
Description:
  Buffer period for [Project Name]
  Purpose: Absorb delays, handle unknowns

  Use this time for:
  - Catch-up if behind schedule
  - Quality improvements
  - Unplanned tasks
  - Testing and validation

  If not needed: Advance to next milestone early
```

**Example:**
```
Title: 🛡️ Buffer - Life OS v3
Start: 2026-02-16
End: 2026-02-19 (3 days)
All-day: Yes
Color: Gray
Description:
  Buffer after Initial Prototype milestone
  Purpose: Handle prototype issues, testing

  Use this time for:
  - Fix bugs found in prototype
  - Additional testing
  - Documentation updates

  If not needed: Start Design Phase early
```

## Template 6: Phase Transition

**Use for:** Marking transitions between project phases

```
Title: 🚀 [Project Name]: [Old Phase] → [New Phase]
Start: [Date] 16:00
End: [Date] 17:00
Color: Yellow
Description:
  Phase Transition Event
  Project: [Project Name]
  From: [Old Phase]
  To: [New Phase]

  Transition checklist:
  - [ ] [Old Phase] deliverables complete
  - [ ] [New Phase] resources ready
  - [ ] Team aligned on new objectives
  - [ ] Risks for new phase identified

  📋 Phase Plan: [Link to plan]
```

**Example:**
```
Title: 🚀 Life OS v3: Prototype → Development
Start: 2026-02-15 16:00
Color: Yellow
Description:
  Phase Transition Event
  Project: Life OS v3
  From: Prototype Phase
  To: Development Phase

  Transition checklist:
  - [ ] Prototype validated by users
  - [ ] Development environment ready
  - [ ] Team onboarded to codebase
  - [ ] Architecture decisions documented
```

## Color-Coding Convention

| Color | Meaning | Use Case |
|-------|---------|----------|
| 🔵 Blue | Standard milestone | Default for most milestones |
| 🟣 Purple | Work block | Capacity allocation |
| 🔴 Red | Hard deadline | External dependencies, non-negotiable |
| 🟢 Green | Review/checkpoint | Retrospectives, phase gates |
| ⚫ Gray | Buffer/slack | Padding, contingency |
| 🟡 Yellow | Phase transition | Workflow state changes |
| 🟠 Orange | At-risk milestone | Behind schedule, needs attention |

## Reminder Strategy

| Event Type | Reminders |
|------------|-----------|
| Milestone (3-7 days out) | 3 days, 1 day |
| Milestone (8-30 days out) | 1 week, 3 days, 1 day |
| Deadline | 1 week, 3 days, 1 day, morning of |
| Work Block | 15 minutes before |
| Review | 1 day before |
| Buffer | None (passive) |

## Event Naming Convention

**Format:** `[Emoji] [Project Name]: [Event Description]`

**Examples:**
- ✅ Good: `🎯 Life OS v3: API Integration Complete`
- ✅ Good: `🔨 Client Project - Work Block`
- ✅ Good: `⏰ DEADLINE: Report Submission`
- ❌ Bad: `Milestone` (no project context)
- ❌ Bad: `Work on stuff` (too vague)
- ❌ Bad: `Life-OS-v3-milestone-integration-api-complete` (too long, no emoji)

## Batch Event Creation

For projects with 5+ milestones, create all events at once:

1. List all milestones from project file
2. Apply appropriate template to each
3. Adjust colors based on priority/risk
4. Set reminders based on event distance
5. Create in calendar as batch (import .ics or API bulk create)
6. Review all events in calendar view
7. Validate no conflicts or overlaps

## Event Maintenance

**Weekly:**
- Update status in event descriptions
- Adjust dates if milestones slip
- Remove completed events (or mark as done)
- Add newly identified milestones

**Monthly:**
- Review color-coding (re-color at-risk items orange)
- Verify reminders still appropriate
- Clean up orphaned events from cancelled projects
- Audit capacity blocks vs. actual usage

## Integration with Life OS Files

All calendar events should reference:
- **Project File:** `{outputProjectFile}` (source of truth)
- **Workflow Plan:** `{workflowPlanFile}` (context)
- **Snapshot:** `{snapshotsFolder}` (current state)
- **Journal:** `{journalFolder}` (decision history)

Include these as links or file paths in event descriptions for quick access.
