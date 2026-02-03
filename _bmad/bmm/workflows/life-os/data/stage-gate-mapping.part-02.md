✅ **Must-Have Criteria (ALL required for GO):**
- [ ] Resource capacity: Confirmed available (time, budget, team)
- [ ] Portfolio fit: Doesn't conflict with other active projects
- [ ] Timing: Can start within next 30 days
- [ ] Sponsor commitment: User explicitly confirms "Let's do this"
- [ ] Integration plan: Clear plan for standalone or integration with existing

⏸️ **HOLD Triggers:**
- User wants to wait (but not abandon)
- External dependency not ready (partner, vendor, etc.)
- Waiting for resource to become available (end of current project)

### Decision Logic
```
IF all_criteria_met AND sponsor_says_go THEN
  DECISION = GO → Project becomes ACTIVE
ELSE IF user_wants_to_wait THEN
  DECISION = HOLD → Store in approved backlog with trigger
ELSE
  DECISION = RECYCLE → Return to G2 if scope/timing needs adjustment
END
```

### Workflow Mapping
- **Steps**:
  - `step-05-integration.md` - Determine standalone vs. integrated
  - `step-06-calendar-sync.md` - Propose timeline and resource allocation
- **Input**: Scored project from G2
- **Process**:
  - Check WIP limit (max 2 active)
  - Suggest BMAD workflows (create-prd, dev-story, architecture)
  - Propose timeline
  - Get user confirmation
- **Output**: Approved project plan + project file with metadata

### Time Investment
- **Target**: 30 minutes review
- **Maximum**: 1 hour (if integration complex)

---

## GATE 4: IN PROGRESS

### Purpose
Monitor active projects for progress, resource burn, early metrics - decide to CONTINUE, PAUSE, or KILL.

### Decision Criteria
✅ **CONTINUE Criteria (≥80% required):**
- [ ] Progress vs. plan: ≥80% of milestones on track
- [ ] Resource burn: ≤110% of estimated burn rate
- [ ] Early metrics: Key metrics trending positive (if applicable)
- [ ] No blockers: No critical blockers lasting >3 days
- [ ] Capacity: User capacity ≥5/10 (wellness check)

⏸️ **PAUSE Triggers:**
- User capacity < 5/10 (overload, burnout risk)
- External blocker > 3 days
- Higher priority project emerges (WIP limit)

❌ **Auto-KILL Triggers:**
- Time overrun > 2x estimate
- Resource burn > budget without progress
- Architecture changes > 3 times (scope creep)
- Strategic fit lost (user goals changed)
- No progress in 2 consecutive weeks

### Decision Logic
```
IF continue_criteria >= 80% AND no_kill_triggers THEN
  DECISION = CONTINUE → Keep active
ELSE IF pause_trigger THEN
  DECISION = PAUSE → Move to ON HOLD, free up capacity
ELSE IF kill_trigger THEN
  DECISION = KILL → Archive with retrospective
END
```

### Workflow Mapping
- **Steps**:
  - `steps-v/step-01-daily-review.md` - Daily check-in (5 min)
  - `steps-v/step-02-weekly-review.md` - Weekly review (30 min)
- **Input**: Active project state from memory
- **Process**:
  - Check progress vs. milestones
  - Update metrics
  - Identify blockers
  - Assess capacity
  - Apply kill criteria automation
- **Output**: Status update + CONTINUE/PAUSE/KILL decision

### Time Investment
- **Daily**: 5 minutes per project
- **Weekly**: 30 minutes full portfolio review

---

## GATE 5: DONE

### Purpose
Retrospective after project completion - decide to ARCHIVE, ITERATE (new version), or SCALE.

### Decision Criteria

#### ARCHIVE (default)
- Project completed successfully
- No immediate follow-up needed
- Learnings captured

#### ITERATE (new version)
- Success metrics achieved but room for improvement
- User wants V2 with enhancements
- New features/scope identified

#### SCALE (expand)
- Exceeded success metrics
- Opportunity to expand to new domains
- Clear ROI justifies expansion

### Decision Logic
```
IF success_metrics >= 100% AND user_wants_more THEN
  IF new_features_defined THEN
    DECISION = ITERATE → Create V2 project (back to G0)
  ELSE IF expand_to_new_domain THEN
    DECISION = SCALE → Create expansion project (back to G0)
  END
ELSE
  DECISION = ARCHIVE → Store learnings, close project
END
```

### Workflow Mapping
- **Steps**:
  - Completion retrospective (ad-hoc)
  - `steps-v/step-03-monthly-review.md` - Strategic alignment check
- **Input**: Completed project state
- **Process**:
  - Review success metrics
  - Capture learnings
  - Identify opportunities
  - Document what worked/didn't
- **Output**: Completion report + ARCHIVE/ITERATE/SCALE decision

### Time Investment
- **Target**: 1 hour retrospective
- **Maximum**: 2 hours for major projects

---

## GO / KILL / HOLD / RECYCLE DECISION MATRIX

| Decision | When to Use | What Happens | Memory Storage |
|----------|-------------|--------------|----------------|
| **GO** | All must-have criteria met, resources available, sponsor committed | Proceed to next gate OR activate project | Store in active projects |
| **KILL** | <60% criteria met OR fatal flaw OR auto-kill trigger | Archive project with decision rationale | Store in killed projects (searchable) |
| **HOLD** | 60-80% criteria met OR waiting on dependency | Store in backlog with trigger condition | Store in on-hold projects with trigger |
| **RECYCLE** | Good idea, wrong approach/timing | Return to earlier gate with new framing | Update idea brief, return to earlier gate |

---

## WORKFLOW STEP MAPPING DIAGRAM

```mermaid
graph TD
    Start([User Idea]) --> G0{Gate 0<br>Idea Screen}

    G0 -->|GO| Step01[step-01-collect-ideas.md]
    G0 -->|KILL| Archive1[Archive: No fit]
    G0 -->|HOLD| Backlog1[Idea Backlog]

    Step01 --> G1{Gate 1<br>Evidence Screen}

    G1 -->|GO| Step02[step-02-specialist-match.md]
    G1 -->|KILL| Archive2[Archive: No evidence]
    G1 -->|HOLD| Backlog2[On Hold: Dependency]
    G1 -->|RECYCLE| G0

    Step02 --> Step025[step-02.5-academic-search.md<br>Phase 2]
    Step025 --> Step03[step-03-consilium.md]

