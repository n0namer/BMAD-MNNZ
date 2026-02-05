# Calendar Sync Protocols

## Purpose
Step-by-step protocols for syncing Life OS project timelines with calendar systems.

## Protocol 1: Weekly Manual Sync

**Frequency:** Every Monday morning
**Duration:** 15-30 minutes
**Best for:** 1-5 active projects

### Steps:
1. Review all active projects in Life OS
2. Identify milestone changes from previous week
3. Update calendar entries for changed milestones
4. Add new milestones to calendar
5. Remove completed milestones
6. Adjust capacity blocks for upcoming week
7. Set reminders for upcoming deadlines (3-5 days out)

### Validation:
- [ ] All active projects have upcoming milestones in calendar
- [ ] Completed milestones removed from calendar
- [ ] Capacity blocks match project allocation
- [ ] Next week's milestones have reminders

## Protocol 2: iCal Export/Import

**Frequency:** On-demand or weekly
**Duration:** 5-10 minutes
**Best for:** 3-10 projects

### Steps:
1. Generate .ics file from project milestones
2. Open calendar application
3. Import .ics file (File > Import)
4. Review imported events
5. Adjust event details if needed (color, reminders)
6. Delete old project calendar if updating
7. Verify all milestones visible

### ICS File Format Example:
```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Life OS//Calendar Sync//EN
BEGIN:VEVENT
UID:milestone-1@lifeos.local
DTSTAMP:20260205T120000Z
DTSTART:20260215T090000Z
SUMMARY:Milestone: Initial Prototype
DESCRIPTION:Project: Life OS v3\nPhase: Development
END:VEVENT
END:VCALENDAR
```

### Validation:
- [ ] All milestones appear in calendar
- [ ] Dates match project file exactly
- [ ] Event titles are clear and actionable
- [ ] Reminders set appropriately

## Protocol 3: API-Based Sync

**Frequency:** Automated (every 1-24 hours)
**Duration:** Automated
**Best for:** Enterprise, 10+ projects

### Setup (One-time):
1. Obtain API credentials (Google/Microsoft)
2. Configure OAuth flow or service account
3. Map Life OS fields to calendar fields
4. Set sync frequency and conflict resolution rules
5. Test with non-critical project first
6. Enable error notifications

### Sync Logic:
```
FOR each project in Life OS:
  IF project.status == 'ACTIVE' OR 'PLANNED':
    FOR each milestone in project.milestones:
      IF milestone NOT in calendar:
        CREATE calendar event
      ELSE IF milestone date changed:
        UPDATE calendar event
      ELSE:
        SKIP (no change)

  FOR each calendar event tagged 'LifeOS':
    IF corresponding milestone NOT found:
      DELETE calendar event (milestone completed)
```

### Conflict Resolution:
- **Calendar updated externally:** Preserve calendar change, flag in Life OS
- **Both updated:** Prefer Life OS as source of truth, notify user
- **Milestone deleted:** Remove from calendar
- **Calendar event deleted:** Do NOT recreate (user intent)

### Validation:
- [ ] Sync runs without errors
- [ ] All active milestones synced to calendar
- [ ] Completed milestones removed from calendar
- [ ] Conflict logs reviewed weekly
- [ ] API quota under limits

## Protocol 4: Capacity-Based Blocking

**Frequency:** Weekly (Monday) + daily adjustments
**Duration:** 10 minutes weekly, 2 minutes daily
**Best for:** All project counts

### Weekly Setup (Monday):
1. Calculate total capacity allocation across all projects
2. Block calendar time for each project:
   - Project A: Mon/Wed 9-11am (4h/week)
   - Project B: Tue/Thu 2-5pm (6h/week)
3. Color-code blocks by project or priority
4. Leave 20-30% unscheduled for meetings/interruptions
5. Set recurring blocks for ongoing projects

### Daily Adjustments:
1. Review today's capacity blocks
2. Move blocks if meetings conflict
3. Mark completed blocks as "done"
4. Adjust tomorrow's blocks based on progress

### Validation:
- [ ] Total blocked time ≤ 70% of available time
- [ ] Each active project has allocated blocks
- [ ] Blocks don't overlap with recurring meetings
- [ ] Flexibility buffer maintained

## Emergency Sync Protocol

**When to use:** Project deadline moved, major scope change, portfolio rebalance

### Steps:
1. PAUSE all automated syncs
2. Review all affected projects in Life OS
3. Update milestone dates in project files
4. Manually update calendar for critical milestones (next 2 weeks)
5. Run full sync (Protocol 2 or 3)
6. Verify no orphaned calendar events
7. RESUME automated syncs
8. Notify stakeholders of timeline changes

## Sync Validation Checklist

Use this after ANY sync operation:

- [ ] **Completeness**: All active milestones in calendar?
- [ ] **Accuracy**: Dates match project files?
- [ ] **Cleanliness**: No orphaned events from old projects?
- [ ] **Reminders**: Upcoming milestones have notifications?
- [ ] **Capacity**: Total allocation realistic and achievable?
- [ ] **Conflicts**: No double-bookings or overlaps?

## Troubleshooting

### Issue: Calendar overloaded with milestones
**Solution:** Sync only milestones within next 90 days

### Issue: Milestones not syncing
**Solution:** Check API credentials, verify project status is 'ACTIVE'

### Issue: Duplicate events
**Solution:** Delete all Life OS events, re-run full sync

### Issue: Calendar changes overwritten
**Solution:** Adjust conflict resolution to prefer calendar updates

### Issue: Sync taking too long
**Solution:** Reduce sync frequency, sync only changed projects

## Best Practices Summary

1. **Consistency**: Choose ONE protocol and stick with it
2. **Source of Truth**: Life OS project files are master
3. **Buffer Time**: Always add 20-30% buffer
4. **Review Cadence**: Weekly review mandatory
5. **Automation**: Automate only after manual process proven
6. **Validation**: Always validate after sync
7. **Notifications**: Set reminders 3-5 days before milestones
