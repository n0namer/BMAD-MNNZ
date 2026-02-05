# Monthly Review Protocol ("Deeper Weekly")

## Protocol Definition

Monthly review = Weekly review format + Trend analysis + Alignment checks

**Time allocation:**
- Milestone progress + trends: ~7 min
- WIP health + patterns: ~5 min
- Blockers + chronic issues: ~7 min
- Next month priorities: ~6 min
- Goal alignment check: ~5 min
- Total: ~30 min

## Section Details

### 1. Trend Analysis (Add to Milestone Progress)

```
📈 **Trend Analysis (Last 4 Weeks):**

{for each active project:}
Project: {project_name}
  - Week 1: {progress_%}% complete
  - Week 2: {progress_%}% complete
  - Week 3: {progress_%}% complete
  - Week 4: {progress_%}% complete
  - Velocity: {avg_weekly_progress}% per week
  - Forecast completion: {estimated_completion_date}

  ❓ Question: Is velocity trending up, down, or flat? Why?
```

**Proactive trend detection:**
- Velocity declining 3+ weeks → Flag as risk
- Consistently ahead → Highlight win
- Stagnant (same % 2+ weeks) → Suggest intervention

### 2. WIP Pattern Analysis (Add to WIP Health)

```
📊 **WIP Pattern Analysis (Last 4 Weeks):**

Average WIP: {avg_wip} projects
  - Week 1: {wip_count}
  - Week 2: {wip_count}
  - Week 3: {wip_count}
  - Week 4: {wip_count}

Pattern: [Stable / Increasing / Decreasing / Chaotic]

Context switches: {avg_switches} per week
  - Week 1: {switches}
  - Week 2: {switches}
  - Week 3: {switches}
  - Week 4: {switches}

  ❓ Question: Is WIP trending healthier or worse? What's the pattern?
```

**Proactive pattern detection:**
- WIP consistently above limit → Chronic overcommitment, suggest systemic fix
- Context switches increasing → Quality risk, suggest focus protocol
- WIP chaotic (varies >2/week) → Lack of planning, suggest batching

### 3. Chronic Blocker Analysis (Add to Blockers & Risks)

```
🚧 **Chronic Blocker Analysis (Last 4 Weeks):**

{for each blocker in 2+ weekly reviews:}
Blocker: {blocker_description}
  - First appeared: Week {N}
  - Still blocking: {yes/no}
  - Weeks stuck: {count}
  - Escalation needed: {yes/no}

  ❓ Question: This blocker is chronic. What's preventing resolution?
```

**Proactive chronic blocker detection:**
- Blocker >2 weeks → Suggest escalation
- Same type recurring → Suggest systemic fix
- External dependency >4 weeks → Suggest workaround

### 4. Goal Alignment Check (New Section)

```
🧭 **Goal Alignment Check**

{for each active project:}
Project: {project_name}
  Supports goal: {goal_name} (or "No clear goal alignment")
  Alignment strength: [Strong/Weak/None]

  ❓ Question: Should this project continue, or is it a distraction?
```

**Questions to ask:**
1. **Alignment score:** "What % of active projects support top goals?"
2. **Misaligned work:** "Which projects NOT aligned with goals?"
3. **Stop/Deprioritize:** "What should be stopped or deprioritized?"
4. **New opportunities:** "What emerged this month that aligns with goals?"

**Proactive misalignment detection:**
- >30% projects with no goal alignment → Portfolio drift warning
- High-priority goal has no active projects → Gap detection
- Low-priority projects consuming most time → Resource misallocation

## Skip Resistance Script

If user tries to skip sections:
```
⚠️ **Monthly Review adds trend analysis to weekly format**

This is your chance to spot patterns over 4 weeks.
Can we at least complete:
1. Trend Analysis (7 min)
2. Chronic Blockers (7 min)
3. Alignment Check (5 min)

Then you'll have strategic clarity for next month.
```
