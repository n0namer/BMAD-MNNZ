# Monthly Metrics Analysis

## Metrics Output Format

Append to {metricsFile}:

```markdown
## Monthly Review — {month} {year}

### Milestone Progress & Trends
{for each active project:}
- **{project_name}**: {milestone_title}
  - Current: {actual_%}%
  - Velocity: {avg_weekly_%}% per week
  - Forecast: {completion_date}
  - Trend: [Improving/Declining/Stable]

### WIP Health & Patterns
- Average WIP: {avg_wip}/{wip_limit}
- Pattern: [Stable/Increasing/Decreasing/Chaotic]
- Context switches: {avg_switches} per week
- Health: [✅ Healthy / ⚠️ Warning / 🚨 Chronic overload]

### Blockers & Chronic Issues
{for each blocker:}
- **{blocker_description}**
  - Duration: {weeks} weeks
  - Resolution: {plan_or_escalation}

{for each chronic blocker:}
- **🚨 CHRONIC**: {blocker}
  - Escalation: {required_action}

### Next Month Priorities
1. {priority_1} — {success_criteria}
2. {priority_2} — {success_criteria}
3. {priority_3} — {success_criteria}

### Goal Alignment
- Alignment score: {score}%
- Misaligned projects: {count}
- Projects to stop/pause: {list}
- New opportunities: {list}

### Quick Wins
- {win_1}
- {win_2}
- Learning: {key_learning}

---
```

## Analysis Patterns

### Velocity Trends
- **Improving**: Weekly progress increasing
- **Declining**: Weekly progress decreasing (risk flag)
- **Stable**: Consistent progress (healthy)

### WIP Patterns
- **Stable**: Variance ≤2 projects/week (healthy)
- **Increasing**: Growing WIP (overcommitment risk)
- **Decreasing**: Reducing WIP (focus improving)
- **Chaotic**: Variance >2 projects/week (planning issue)

### Blocker Classifications
- **Acute**: <2 weeks old
- **Chronic**: 2-4 weeks old (escalation needed)
- **Critical**: >4 weeks old (systemic issue)

### Alignment Scoring
- **Strong**: 70%+ projects aligned
- **Moderate**: 40-69% aligned
- **Weak**: <40% aligned (portfolio drift)
