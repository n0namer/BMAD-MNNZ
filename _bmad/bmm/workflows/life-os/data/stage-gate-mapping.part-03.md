    Step03 --> G2{Gate 2<br>Scoring Decision}

    G2 -->|GO| Step04[step-05-scoring.md]
    G2 -->|KILL| Archive3[Archive: Low score]
    G2 -->|RECYCLE| G1

    Step04 --> G3{Gate 3<br>Approval}

    G3 -->|GO| Step05[step-06-integration.md]
    G3 -->|HOLD| Backlog3[Approved Backlog]

    Step05 --> Step06[step-07-calendar-sync.md]
    Step06 --> ActiveProject[ACTIVE PROJECT]

    ActiveProject --> G4{Gate 4<br>In Progress<br>Weekly}

    G4 -->|CONTINUE| ActiveProject
    G4 -->|PAUSE| Backlog4[On Hold: Paused]
    G4 -->|KILL| Archive4[Archive: Criteria failed]

    ActiveProject --> Complete[Project Complete]
    Complete --> G5{Gate 5<br>Done}

    G5 -->|ARCHIVE| Archive5[Archive: Success]
    G5 -->|ITERATE| NewV2[V2 Project] --> G0
    G5 -->|SCALE| Expansion[Expansion Project] --> G0

    Backlog1 --> TriggerCheck1{Trigger Met?}
    TriggerCheck1 -->|Yes| G0

    Backlog2 --> TriggerCheck2{Dependency Ready?}
    TriggerCheck2 -->|Yes| G1

    Backlog3 --> TriggerCheck3{Resources Available?}
    TriggerCheck3 -->|Yes| G3

    Backlog4 --> TriggerCheck4{Resume Trigger?}
    TriggerCheck4 -->|Yes| G4

    style G0 fill:#ffcccc
    style G1 fill:#ffcccc
    style G2 fill:#ffcccc
    style G3 fill:#ffcccc
    style G4 fill:#ffcccc
    style G5 fill:#ffcccc

    style ActiveProject fill:#ccffcc
    style Archive1 fill:#cccccc
    style Archive2 fill:#cccccc
    style Archive3 fill:#cccccc
    style Archive4 fill:#cccccc
    style Archive5 fill:#cccccc
```

---

## AUTO-KILL CRITERIA AUTOMATION

### Trigger Logic

```yaml
auto_kill_triggers:

  # FINANCIAL TRIGGERS
  - name: "Negative Unit Economics"
    condition: "CLV / CAC < 1.5"
    gate: "G1, G2"
    action: "KILL"
    rationale: "Project will lose money at scale"

  # TIME TRIGGERS
  - name: "Time Overrun"
    condition: "actual_time > 2 * estimated_time"
    gate: "G4"
    action: "KILL"
    rationale: "Scope creep or poor estimation, resource drain"

  # ARCHITECTURE TRIGGERS
  - name: "Architecture Thrashing"
    condition: "architecture_changes > 3"
    gate: "G4"
    action: "KILL"
    rationale: "Unstable foundation, likely to continue changing"

  # PROGRESS TRIGGERS
  - name: "No Progress Streak"
    condition: "weeks_without_progress >= 2"
    gate: "G4"
    action: "KILL"
    rationale: "Persistent blocker or lost momentum"

  # BLOCKER TRIGGERS
  - name: "Critical Blocker Duration"
    condition: "days_blocked_critical > 3"
    gate: "G4"
    action: "PAUSE"
    rationale: "External dependency, free up capacity"

  # CAPACITY TRIGGERS
  - name: "Capacity Overload"
    condition: "user_capacity < 5 AND active_projects > 1"
    gate: "G4"
    action: "PAUSE lowest_priority"
    rationale: "Prevent burnout, enforce WIP limit"

  # STRATEGIC TRIGGERS
  - name: "Strategic Fit Lost"
    condition: "goals_changed AND alignment_score < 0.5"
    gate: "G4"
    action: "KILL"
    rationale: "No longer aligned with long-term goals"

  # PORTFOLIO TRIGGERS
  - name: "Low MCDA Score"
    condition: "mcda_score < bottom_20_percentile"
    gate: "G2"
    action: "KILL"
    rationale: "Better opportunities available in portfolio"

  # RESOURCE TRIGGERS
  - name: "Budget Overrun Without Progress"
    condition: "budget_spent > 1.5 * budget_planned AND progress < 50%"
    gate: "G4"
    action: "KILL"
    rationale: "Resource drain without proportional progress"

  # WIP LIMIT TRIGGERS
  - name: "WIP Limit Exceeded"
    condition: "active_projects > 2 AND no_pauseable_projects"
    gate: "G3"
    action: "HOLD"
    rationale: "Enforce focus, prevent context switching"
```

### Implementation in Code

```python
def check_auto_kill_triggers(project):
    """
    Check all auto-kill triggers for a project.
    Returns: (decision, trigger_name, rationale)
    """

    # FINANCIAL TRIGGERS
    if project.clv_cac and project.clv_cac < 1.5:
        return ("KILL", "Negative Unit Economics", "CLV/CAC ratio below 1.5")

    # TIME TRIGGERS
    if project.actual_time > 2 * project.estimated_time:
        return ("KILL", "Time Overrun", f"Actual time {project.actual_time}h > 2x estimated {project.estimated_time}h")

    # ARCHITECTURE TRIGGERS
    if project.architecture_changes > 3:
        return ("KILL", "Architecture Thrashing", f"{project.architecture_changes} architecture changes indicate unstable foundation")

    # PROGRESS TRIGGERS
    if project.weeks_without_progress >= 2:
        return ("KILL", "No Progress Streak", f"{project.weeks_without_progress} weeks without progress")

    # BLOCKER TRIGGERS
    if project.days_blocked_critical > 3:
        return ("PAUSE", "Critical Blocker Duration", f"Blocked for {project.days_blocked_critical} days on critical path")

    # CAPACITY TRIGGERS
    if project.user_capacity < 5 and project.portfolio.active_count > 1:
        return ("PAUSE", "Capacity Overload", f"User capacity {project.user_capacity}/10 too low for {project.portfolio.active_count} active projects")

    # STRATEGIC TRIGGERS
    if project.strategic_alignment < 0.5 and project.goals_changed:
        return ("KILL", "Strategic Fit Lost", f"Alignment score {project.strategic_alignment} after goal changes")

    # PORTFOLIO TRIGGERS
    if project.mcda_score < project.portfolio.bottom_20_percentile():
        return ("KILL", "Low MCDA Score", f"Score {project.mcda_score} in bottom 20% of portfolio")

    # RESOURCE TRIGGERS
    if project.budget_spent > 1.5 * project.budget_planned and project.progress < 0.5:
        return ("KILL", "Budget Overrun Without Progress", f"Spent {project.budget_spent} > 1.5x planned {project.budget_planned} with only {project.progress*100}% progress")

    # WIP LIMIT TRIGGERS

