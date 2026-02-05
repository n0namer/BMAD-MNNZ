# Weekly Review Protocol

## Protocol Structure

### Section 1: Milestone Progress Check (~5 min)

**For each active project with milestones in the last/next 7 days:**

```
Project: {project_name}
Milestone: {milestone_title}
  Planned: {planned_date}
  Status: {current_status}
```

**Questions:**
1. **Progress vs Plan:** "What % complete is this milestone? (planned vs actual)"
2. **Behind/Ahead:** "Are you behind, on track, or ahead of schedule?"
3. **Course correction:** "If behind, what needs to change this week?"

**Capture:**
- Planned % complete vs Actual % complete
- Timeline delta (days behind/ahead)
- Root cause if behind (capacity, blockers, scope creep)

---

### Section 2: WIP Health Check (~3 min)

```
Current WIP: {active_project_count}/{wip_limit} projects active
Capacity status: {capacity_assessment}
```

**Questions:**
1. **Active projects:** "How many projects are you actively working on RIGHT NOW?"
2. **WIP limit:** "What's your realistic WIP limit? (recommended: 2-3 for individuals)"
3. **Overload check:** "If over WIP limit, what can be paused or finished first?"
4. **Context switching:** "How many times did you switch projects this week? (quality metric)"

**WIP Assessment:**
- ✅ Healthy: Active projects ≤ WIP limit
- ⚠️ Warning: Active projects = WIP limit + 1
- 🚨 Overload: Active projects > WIP limit + 1

**Overload Response:**
```
🚨 **WIP Overload Detected**

You're working on {N} projects simultaneously.
Recommendation: Pause {N - limit} projects to reduce context switching.

Which projects can be paused until others complete?
```

---

### Section 3: Blockers & Risks (~5 min)

**Questions:**
1. **Active blockers:** "What's currently blocking progress on any project?"
2. **External dependencies:** "Are you waiting on anyone/anything?"
3. **Internal blockers:** "What skills/resources/time are you missing?"
4. **Risk horizon:** "What risks do you see emerging in the next 2 weeks?"

**For each blocker identified:**
```
Blocker: {blocker_description}
  Affects: {project_name}
  Severity: [Low/Medium/High]
  Owner: [You/External/Unknown]

  ❓ Can this be resolved this week? If not, what's needed?
```

**Proactive risk flagging:**
- If blocker is >7 days old → Flag as chronic, suggest escalation
- If blocker affects critical path → Highlight urgency
- If external dependency → Suggest follow-up action

---

### Section 4: Next Week Priorities (~4 min)

**Questions:**
1. **Top 3 focus areas:** "What are the 3 most important things to complete NEXT WEEK?"
2. **Why these 3:** "Why are these the priorities? (link to goals/milestones)"
3. **Realistic check:** "Given current capacity and blockers, are these achievable?"
4. **Success criteria:** "How will you know these are done? (acceptance criteria)"

**Priority Template:**
```
Priority 1: {task_or_milestone}
  Why: {goal_alignment}
  Success criteria: {completion_definition}
  Est. effort: {hours/days}

Priority 2: {task_or_milestone}
  Why: {goal_alignment}
  Success criteria: {completion_definition}
  Est. effort: {hours/days}

Priority 3: {task_or_milestone}
  Why: {goal_alignment}
  Success criteria: {completion_definition}
  Est. effort: {hours/days}
```

**Capacity check:**
```
⚠️ **Capacity Warning**

Estimated effort: {total_hours}h
Available capacity: {capacity}h (realistic weekly capacity)

These priorities may not fit in one week.
What can be deferred or simplified?
```

---

### Section 5: Quick Wins (~2 min)

**Questions:**
1. **Wins this week:** "What small victories happened this week? (morale boost)"
2. **Learning:** "What did you learn that will help next week?"
3. **Gratitude:** "What are you grateful for from this week's work?"

**Purpose:**
- Maintain motivation by acknowledging progress
- Capture learnings for future reference
- Combat negativity bias (always seeing problems, missing wins)

---

## Metrics Append Format

```markdown
## Weekly Review — {week_of_date}

### Milestone Progress
{for each active project:}
- **{project_name}**: {milestone_title}
  - Planned: {planned_%}% | Actual: {actual_%}%
  - Status: [On Track / Behind by {N} days / Ahead by {N} days]
  - Course correction: {action_if_behind}

### WIP Health
- Active projects: {count}/{wip_limit}
- Status: [✅ Healthy / ⚠️ Warning / 🚨 Overload]
- Context switches: {count} this week
- Action: {action_if_overload}

### Blockers & Risks
{for each blocker:}
- **{blocker_description}**
  - Affects: {project_name}
  - Severity: {level}
  - Resolution plan: {plan}

### Next Week Priorities
1. {priority_1} — {success_criteria}
2. {priority_2} — {success_criteria}
3. {priority_3} — {success_criteria}

Capacity check: {realistic/overcommitted}

### Quick Wins
- {win_1}
- {win_2}
- Learning: {key_learning}

---
```

---

## Skip Warning

If user tries to skip the review:
```
⚠️ **Weekly Review is the PRIMARY review cadence**

This is your main progress tracking ritual (15-20 min).
Daily reviews are optional, but weekly is essential.

Can we complete at least the top 3 sections?
1. Milestone Progress (5 min)
2. WIP Health (3 min)
3. Blockers & Risks (5 min)
```
