# Today View Templates

## Report Template Structure

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 **TODAY: {date}**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated: {timestamp}

## 📊 TODAY'S PROGRESS

┌────────────────────────────────────────┐
│ Completion: {completed}/{total} ({completion_rate}%)  │
│ Time Remaining: ~{estimated_hours}h    │
│ Overdue: {overdue} tasks              │
└────────────────────────────────────────┘

**Status Breakdown:**
- ✅ Completed: {completed}
- 🔄 In Progress: {in_progress}
- ⏸️  Not Started: {not_started}
- 🔴 Overdue: {overdue}

---

## 🎯 RECOMMENDED FOCUS

**What to tackle now:**
{focus_recommendation}

**Suggested time blocks:**
- 🌅 **Morning:** {morning_tasks}
- ☀️ **Afternoon:** {afternoon_tasks}
- 🌙 **Evening:** {evening_tasks}

---

## 📋 TODAY'S TASKS

{IF overdue > 0: "
### 🔴 OVERDUE (Do First!)

{FOR EACH overdue task:}
**[{task_id}] {title}** (Originally due: {due_date})
- 📦 Project: {project_name}
- ⏱️  Estimated: {estimated_hours}h
- 🚫 Blocker: {blockers}
- 💡 Next Action: {recommendation}

---
"}

{IF high_priority_count > 0: "
### 🔥 HIGH PRIORITY

{FOR EACH high_priority task:}
**[{status_emoji}] [{task_id}] {title}**
- 📦 Project: {project_name} (Milestone: {milestone})
- ⏱️  Estimated: {estimated_hours}h {IF time_spent: "| Spent: {time_spent_hours}h"}
- 🔗 Dependencies: {
    IF dependencies.length == 0: "None"
    ELSE: dependencies.join(", ") + " (must complete first)"
  }
- {IF blockers: "🚫 Blocker: {blockers}"}
- 💡 Next Action: {next_action}

---
"}

{IF medium_priority_count > 0: "
### ⚡ MEDIUM PRIORITY

{FOR EACH medium_priority task:}
**[{status_emoji}] [{task_id}] {title}**
- 📦 Project: {project_name}
- ⏱️  Estimated: {estimated_hours}h

---
"}

{IF low_priority_count > 0: "
### 📝 LOW PRIORITY (If time permits)

{FOR EACH low_priority task:}
- [{status_emoji}] [{task_id}] {title} ({estimated_hours}h)

---
"}

## 🚨 BLOCKERS

{IF blockers_summary.length > 0: "
{FOR EACH blocker:}
- **{task_id}:** {blocker}
  - Severity: {severity_emoji} {severity}
  - 💡 Recommendation: {recommendation}

"}
{ELSE: "
✅ No active blockers
"}

---

## 💡 PRODUCTIVITY TIPS

- Focus on completing **{overdue + high_priority}** critical tasks first
- Batch similar tasks together (e.g., all design tasks, then all reviews)
- Take breaks every 90 minutes
- Block distractions during deep work tasks

---
```

## Emoji Reference

### Status Indicators
- `✅` - Completed
- `🔄` - In Progress
- `⏸️` - Not Started
- `🔴` - Overdue

### Priority Markers
- `🔴` - Overdue section
- `🔥` - High Priority
- `⚡` - Medium Priority
- `📝` - Low Priority

### Time Blocks
- `🌅` - Morning (8am-12pm)
- `☀️` - Afternoon (12pm-5pm)
- `🌙` - Evening (5pm-9pm)

### Severity Levels
- `🔴` - High severity blocker
- `🟡` - Medium severity blocker
- `🟢` - Low severity blocker

## Subprocess Return Schema

```json
{
  "today_summary": {
    "date": "YYYY-MM-DD",
    "total_tasks": 0,
    "completed": 0,
    "in_progress": 0,
    "not_started": 0,
    "overdue": 0,
    "completion_rate": 0,
    "estimated_time_remaining_hours": 0
  },
  "focus_recommendation": "string",
  "time_allocation": {
    "morning": ["task-id"],
    "afternoon": ["task-id"],
    "evening": ["task-id"]
  },
  "tasks": [
    {
      "id": "task-id",
      "project_id": "idea-id",
      "project_name": "string",
      "title": "string",
      "status": "IN_PROGRESS|NOT_STARTED|COMPLETED|OVERDUE",
      "priority": "HIGH|MEDIUM|LOW",
      "estimated_hours": 0,
      "time_spent_hours": 0,
      "due_date": "YYYY-MM-DD",
      "is_overdue": false,
      "blockers": ["string"],
      "next_action": "string",
      "dependencies": ["task-id"],
      "milestone": "string"
    }
  ],
  "blockers_summary": [
    {
      "task_id": "task-id",
      "blocker": "string",
      "severity": "HIGH|MEDIUM|LOW",
      "recommendation": "string"
    }
  ],
  "portfolio_context": {
    "active_projects": 0,
    "projects_with_tasks_today": 0
  }
}
```
