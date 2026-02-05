# Pulse Status Calculation & Alert System

## Status Formula

```
Actual Progress vs. Planned Progress (from milestones)

Status Thresholds:
- 🟢 On Track: ±20% variance from plan
- 🟡 At Risk: 20-40% behind, recoverable with action
- 🔴 Blocked: >40% behind OR critical blocker present

Trend Indicators:
- ↗️ Improving: Progress accelerating
- ➡️ Stable: Consistent pace
- ↘️ Declining: Progress slowing
```

---

## Smart Alerts System

### Alert Conditions

| Condition | Trigger | Action |
|-----------|---------|--------|
| **2+ weeks 🔴 status** | Consecutive red weeks | Escalate to step-x-04 (pivot-or-kill) |
| **Same blocker 3+ weeks** | Blocker repeats | Escalate to consilium (step-04) |
| **Milestone overdue** | Date passed, not complete | Alert + reassess plan |
| **No progress 4+ weeks** | Zero completion change | Force step-x-04 decision |
| **Trend declining 3 weeks** | ↘️ three times | Schedule deep review |

### Auto-Notification Configuration

```yaml
# Weekly pulse triggers these checks
alerts:
  - type: repeated_blocker
    threshold: 3 weeks
    action: "Schedule consilium session to solve root cause"

  - type: consecutive_red
    threshold: 2 weeks
    action: "Trigger pivot-or-kill analysis (step-x-04)"

  - type: milestone_overdue
    threshold: 1 day past due
    action: "Alert executor + update plan or extend deadline"

  - type: stagnant
    threshold: 4 weeks no progress
    action: "Force decision: continue with plan or kill"
```

---

## Integration with Other Steps

### From Weekly Review (step-v-02)

**Weekly review generates pulse list:**

```markdown
## Ideas Requiring Pulse Check

### IN_PROGRESS (3)
1. [ ] Idea-Alpha (Week 4, last pulse 7 days ago) - 🟢
2. [ ] Idea-Beta (Week 2, last pulse 8 days ago) - 🟡
3. [ ] Idea-Gamma (Week 6, **no pulse 14 days**) - ⚠️

**Recommended:** Pulse all 3 (15-20 min total)
```

### To Pivot-or-Kill (step-x-04)

**Auto-trigger when:**
- 2+ consecutive red weeks
- 4+ weeks stagnant
- Same blocker unresolved for 3+ weeks

**Handoff data:**
- Pulse history (all weeks)
- Blocker patterns
- Completion trajectory

### To Consilium (step-04)

**Escalate blockers:**
- Repeated technical blockers → TRIZ analysis
- Resource conflicts → Six Hats prioritization
- Strategic uncertainty → Full consilium session
