# Calendar Integration Guide

## Integration Pattern (Future Enhancement)

### Supported Calendar Systems
- Google Calendar (via API)
- Outlook/Office 365 (via Microsoft Graph API)
- iCal/CalDAV (standard protocol)
- Local calendar files (.ics format)

## Time Block Sync

**From Today View → Calendar:**
1. Generate calendar events for each time block allocation
2. Event title: `[WORK] {task_title}`
3. Event description: Project context, estimated hours, next action
4. Color coding:
   - 🔴 Red: Overdue/High Priority
   - 🟡 Yellow: Medium Priority
   - 🟢 Green: Low Priority
5. Set reminders:
   - 15 min before start
   - At start time
   - 30 min before end (wrap-up reminder)

**From Calendar → Today View:**
1. Check for conflicts with scheduled events
2. Adjust time block recommendations to avoid meetings
3. Suggest rescheduling if capacity exceeded

## Event Templates

### Work Block Event
```ics
BEGIN:VEVENT
SUMMARY:[WORK] {task_title}
DESCRIPTION:Project: {project_name}\nEstimated: {estimated_hours}h\nNext Action: {next_action}\nTracker: {task_id}
DTSTART:{iso_start_time}
DTEND:{iso_end_time}
STATUS:CONFIRMED
PRIORITY:{1=high, 5=medium, 9=low}
CATEGORIES:WORK,{project_name}
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:-PT15M
END:VALARM
END:VEVENT
```

### Blocker Alert Event
```ics
BEGIN:VEVENT
SUMMARY:⚠️ BLOCKER: {task_title}
DESCRIPTION:Blocked by: {blocker}\nSeverity: {severity}\nRecommendation: {recommendation}
DTSTART:{today_9am}
DURATION:PT0M
STATUS:TENTATIVE
PRIORITY:1
CATEGORIES:BLOCKER,ALERT
BEGIN:VALARM
ACTION:DISPLAY
TRIGGER:PT0M
END:VALARM
END:VEVENT
```

## Availability Check

**Before allocating time blocks:**
1. Query calendar for events on target date
2. Calculate available time:
   ```
   morning_available = 4h - SUM(morning_meeting_durations)
   afternoon_available = 5h - SUM(afternoon_meeting_durations)
   evening_available = 3h - SUM(evening_meeting_durations)
   ```
3. If insufficient time:
   - Suggest deferring low-priority tasks
   - Recommend rescheduling meetings
   - Flag overcommitment warning

## Auto-Adjustment Logic

**When meeting added to calendar:**
1. Detect conflict with task allocation
2. Re-run time block algorithm with reduced capacity
3. Notify user of rescheduled tasks
4. Update today view

**When meeting cancelled:**
1. Detect freed capacity
2. Suggest moving tasks from tomorrow to today
3. Re-optimize time blocks

## Privacy & Security

**Data exposure:**
- Only task titles visible in calendar (no sensitive details)
- Option to use generic titles: `[WORK] Project Task`
- Descriptions encrypted if using cloud calendar

**Access control:**
- Read-only calendar access recommended
- Write access only for creating work blocks
- Never delete/modify non-work events
