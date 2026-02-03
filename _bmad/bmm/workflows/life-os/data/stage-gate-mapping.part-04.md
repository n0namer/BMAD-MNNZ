    if project.portfolio.active_count > 2 and not project.portfolio.has_pauseable_projects():
        return ("HOLD", "WIP Limit Exceeded", f"{project.portfolio.active_count} active projects exceeds WIP limit of 2")

    return ("CONTINUE", None, None)
```

---

## DECISION CRITERIA CHECKLISTS

### Gate 0: Idea Screen Checklist

```markdown
## Gate 0: Idea Screen Decision

**Project:** [Project Name]
**Date:** [Date]
**Evaluator:** [Name]

### Must-Have Criteria
- [ ] Strategic fit: Aligns with long-term goal(s): ___________
- [ ] Resource availability: Can start within 90 days
- [ ] Rough effort: < 100 hours OR budget available: ___________
- [ ] No fatal flaws: Legal, ethical, health risks cleared

### Decision
- [ ] **GO** - All criteria met → Proceed to G1
- [ ] **KILL** - Fatal flaw: ___________
- [ ] **HOLD** - Needs more info: ___________

**Rationale:** ___________________________________________

**Next Step:** ___________________________________________
```

### Gate 1: Evidence Screen Checklist

```markdown
## Gate 1: Evidence Screen Decision

**Project:** [Project Name]
**Date:** [Date]
**Evaluator:** [Name]

### Must-Have Criteria (≥80% required)
- [ ] Market validation: 3+ data points: ___________
- [ ] Technical feasibility: No major blockers
- [ ] Initial ROI: CLV/CAC ≥ 1.5 (if applicable): ___________
- [ ] Specialist consensus: ≥70% recommend GO
- [ ] Uniqueness: Not duplicating active project

**Criteria Met:** ___/5 (___%)

### Consilium Recommendation
- Specialists consulted: ___________
- Consensus view: ___________
- GO votes: ___ / ___ (___%)

### Decision
- [ ] **GO** - ≥80% criteria met → Proceed to G2
- [ ] **KILL** - <60% criteria met OR fatal flaw: ___________
- [ ] **HOLD** - Waiting on dependency: ___________
- [ ] **RECYCLE** - Return to G0 with new approach: ___________

**Rationale:** ___________________________________________

**Next Step:** ___________________________________________
```

### Gate 2: Scoring Decision Checklist

```markdown
## Gate 2: Scoring Decision

**Project:** [Project Name]
**Date:** [Date]
**Evaluator:** [Name]

### Quantitative Scores
- **MCDA Score:** ___ / 100 (Threshold: ___, Portfolio Avg: ___)
- **Desirability:** ___/10
- **Feasibility:** ___/10
- **Viability:** ___/10
- **Capability:** ___/10
- **CLV/CAC:** ___ (Target: ≥1.5)

### Must-Have Criteria (≥70% required)
- [ ] MCDA score: Top 50% of portfolio OR > threshold
- [ ] D/F/V/C: Desirability ≥7, Feasibility ≥6
- [ ] Unit economics: CLV/CAC ≥1.5 OR qualitative value clear
- [ ] Resource capacity: Available ≥ required + 20% buffer
- [ ] WIP limit: ≤2 active OR can pause one

**Criteria Met:** ___/5 (___%)

### Portfolio Comparison
- Current active projects: ___
- Required capacity: ___ hours/week
- Available capacity: ___ hours/week
- Rank vs. portfolio: ___ / ___

### Decision
- [ ] **GO** - ≥70% criteria met → Proceed to G3
- [ ] **KILL** - Bottom 20% OR fatal resource issue: ___________
- [ ] **RECYCLE** - Good score, wrong timing: ___________

**Rationale:** ___________________________________________

**Next Step:** ___________________________________________
```

### Gate 3: Approval Checklist

```markdown
## Gate 3: Approval Decision

**Project:** [Project Name]
**Date:** [Date]
**Sponsor:** [Name]

### Must-Have Criteria (ALL required)
- [ ] Resource capacity: Confirmed available (time, budget, team)
- [ ] Portfolio fit: No conflicts with active projects
- [ ] Timing: Can start within 30 days
- [ ] Sponsor commitment: Explicit "Let's do this"
- [ ] Integration plan: Standalone OR integration approach defined

**Criteria Met:** ___/5

### Resource Lock-In
- Time allocated: ___ hours/week
- Budget allocated: $ ___
- Team members: ___________
- Start date: ___________

### Integration Approach
- [ ] Standalone project
- [ ] Integrate with existing: ___________
- BMAD workflows planned: ___________

### Decision
- [ ] **GO** - All criteria met → PROJECT ACTIVE
- [ ] **HOLD** - User wants to wait: ___________

**Sponsor Signature:** ___________

**Next Step:** ___________________________________________
```

### Gate 4: In Progress Checklist

```markdown
## Gate 4: In Progress Review

**Project:** [Project Name]
**Date:** [Date]
**Reviewer:** [Name]

### CONTINUE Criteria (≥80% required)
- [ ] Progress vs. plan: ≥80% milestones on track (Actual: ___%)
- [ ] Resource burn: ≤110% of estimate (Actual: ___%)
- [ ] Early metrics: Trending positive: ___________
- [ ] No blockers: No critical blockers >3 days
- [ ] Capacity: User capacity ≥5/10 (Actual: ___/10)

**Criteria Met:** ___/5 (___%)

### Auto-Kill Triggers Check
- [ ] Time overrun: ___ / ___ hours (< 2x ✓)
- [ ] Architecture changes: ___ (< 3 ✓)
- [ ] Weeks without progress: ___ (< 2 ✓)
- [ ] Days blocked: ___ (< 3 ✓)
- [ ] Strategic alignment: ___ (≥0.5 ✓)

### Decision
- [ ] **CONTINUE** - ≥80% criteria met, no kill triggers
- [ ] **PAUSE** - Capacity overload OR external blocker: ___________
- [ ] **KILL** - Kill trigger activated: ___________

**Rationale:** ___________________________________________
