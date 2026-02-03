# Stage-Gate Process Mapping for Life OS

**Purpose:** Define the stage-gate methodology for Life OS project management with explicit go/kill/hold/recycle decisions at each critical checkpoint.

**Based on:** Robert G. Cooper's Stage-Gate® process adapted for personal and business portfolio management.

---

## GATE DEFINITIONS

| Gate | Name | Decision Options | Typical Time | Workflow Step(s) | Output |
|------|------|------------------|--------------|------------------|--------|
| **G0** | Idea Screen | GO / KILL | 5-15 min | step-01 (collect-ideas) | Idea brief (1 page) |
| **G1** | Evidence Screen | GO / KILL / HOLD / RECYCLE | 48-72 hours | step-02.5 (academic-search)<br>step-03 (consilium) | Evidence summary + recommendation |
| **G2** | Scoring Decision | GO / KILL / RECYCLE | 2-4 hours | step-04 (scoring) | Scored project with rationale |
| **G3** | Approval | GO / HOLD | 30 min | step-05 (integration) | Approved project plan |
| **G4** | In Progress | CONTINUE / PAUSE / KILL | Weekly | validate mode steps | Status update |
| **G5** | Done | ARCHIVE / ITERATE / SCALE | 1 hour | Completion retrospective | Completion report |

---

## GATE 0: IDEA SCREEN

### Purpose
Quick filter to eliminate obviously poor fits before investing time.

### Decision Criteria
✅ **Must-Have Criteria (ALL required for GO):**
- [ ] Strategic fit: Aligns with at least 1 of user's long-term goals
- [ ] Resource availability: Can start within next 90 days
- [ ] Rough effort estimate: < 100 hours OR budget available
- [ ] No fatal flaws: No legal, ethical, or health risks

❌ **Auto-KILL Triggers:**
- Legal or ethical violations
- User explicitly says "not interested"
- No alignment with any life domain (business/finance/home/health/personal)
- Required resources exceed 2x available capacity

⏸️ **HOLD Triggers:**
- Good idea but timing unclear
- Needs more information to evaluate

### Decision Logic
```
IF all_must_have_criteria == TRUE THEN
  DECISION = GO → Proceed to G1
ELSE IF fatal_flaw == TRUE THEN
  DECISION = KILL → Archive with reason
ELSE
  DECISION = HOLD → Store in idea backlog
END
```

### Workflow Mapping
- **Step**: `step-01-collect-ideas.md`
- **Input**: User's new idea or project
- **Process**: Ask clarifying questions (what, why, when, who)
- **Output**: Idea brief saved to memory (Markdown + Claude Flow)

### Time Investment
- **Target**: 5-15 minutes
- **Maximum**: 30 minutes for complex ideas

---

## GATE 1: EVIDENCE SCREEN

### Purpose
Validate that idea has merit based on evidence (market validation, technical feasibility, initial ROI).

### Decision Criteria
✅ **Must-Have Criteria (≥80% required for GO):**
- [ ] Market validation: Evidence of demand or need (3+ data points)
- [ ] Technical feasibility: No major technical blockers identified
- [ ] Initial ROI estimate: CLV/CAC ≥ 1.5 (if applicable)
- [ ] Specialist consensus: ≥70% of consilium recommends GO
- [ ] Uniqueness check: Not duplicating existing active project

❌ **Auto-KILL Triggers:**
- No market evidence after 72-hour research sprint
- CLV/CAC < 1.0 (negative unit economics)
- Consilium unanimous KILL recommendation
- Discovered as duplicate of existing active project

⏸️ **HOLD Triggers:**
- 60-79% of criteria met
- Waiting on external dependency (partner decision, regulatory approval)
- Specialist needs more information

🔄 **RECYCLE Triggers:**
- Good idea but wrong approach → Return to G0 with new angle
- Good idea but wrong timing → Store in backlog with trigger condition

### Decision Logic
```
IF criteria_met >= 80% AND no_fatal_flaws THEN
  DECISION = GO → Proceed to G2
ELSE IF criteria_met < 60% OR fatal_flaw THEN
  DECISION = KILL → Archive with evidence
ELSE IF waiting_on_dependency THEN
  DECISION = HOLD → Store with dependency tracker
ELSE IF good_idea_wrong_approach THEN
  DECISION = RECYCLE → Return to G0 with new framing
END
```

### Workflow Mapping
- **Steps**:
  - `step-02-specialist-match.md` - Match specialists
  - `step-02.5-academic-search.md` - Research evidence (Phase 2)
  - `step-03-consilium.md` - Get specialist recommendations
- **Input**: Idea brief from G0
- **Process**: Research + consilium + evidence gathering
- **Output**: Evidence summary + consilium recommendation + GO/KILL/HOLD/RECYCLE decision

### Time Investment
- **Target**: 48-72 hours research sprint
- **Maximum**: 1 week (if research extensive)

---

## GATE 2: SCORING DECISION

### Purpose
Prioritize project using quantitative scoring (RICE, MCDA) to determine if it deserves resources vs. other portfolio candidates.

### Decision Criteria
✅ **Must-Have Criteria (≥70% required for GO):**
- [ ] MCDA score: In top 50% of current portfolio (or > threshold if first project)
- [ ] D/F/V/C alignment: Desirability ≥7/10, Feasibility ≥6/10
- [ ] Unit economics: CLV/CAC ≥ 1.5 OR qualitative value clear
- [ ] Resource capacity: Available capacity ≥ required effort + 20% buffer
- [ ] WIP limit check: Current active projects ≤ 2 (or can pause one)

❌ **Auto-KILL Triggers:**
- MCDA score in bottom 20% of portfolio
- CLV/CAC < 1.5 (business projects only)
- Feasibility < 4/10 (too difficult)
- Required resources > 2x available capacity
- Cannot meet WIP limit (2 active max) and no pauseable projects

🔄 **RECYCLE Triggers:**
- Good score but wrong timing (capacity issue) → Return to G1 when capacity available
- Good score but needs rescoping → Return to G0 with adjusted scope

### Decision Logic
```
IF mcda_score >= threshold AND capacity_available AND wip_limit_ok THEN
  DECISION = GO → Proceed to G3
ELSE IF mcda_score < bottom_20% OR fatal_resource_issue THEN
  DECISION = KILL → Archive with score data
ELSE IF good_score_but_wrong_timing THEN
  DECISION = RECYCLE → Return to G1 with trigger condition
END
```

### Workflow Mapping
- **Step**: `step-04-scoring.md`
- **Input**: Evidence summary from G1
- **Process**:
  - RICE scoring (Reach, Impact, Confidence, Effort)
  - MCDA scoring across criteria
  - D/F/V/C analysis
  - Portfolio comparison
  - Capacity check
- **Output**: Scored project with quantitative rationale + GO/KILL/RECYCLE decision

### Time Investment
- **Target**: 2-4 hours scoring session
- **Maximum**: 1 day (if complex portfolio analysis)

---

## GATE 3: APPROVAL

### Purpose
Final checkpoint before committing resources - ensure sponsor (user) is committed and resources are locked.

### Decision Criteria
