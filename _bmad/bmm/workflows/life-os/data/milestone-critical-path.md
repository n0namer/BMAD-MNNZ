# Critical Path Analysis

## Algorithm

### Step 1: Forward Pass (Earliest Times)
Calculate earliest start (ES) and earliest finish (EF) for each milestone:

```
FOR each milestone M in topological order:
  ES(M) = MAX(EF of all predecessors)
  EF(M) = ES(M) + duration(M)

For start milestone:
  ES = 0
  EF = duration
```

### Step 2: Backward Pass (Latest Times)
Calculate latest start (LS) and latest finish (LF) backwards:

```
FOR each milestone M in reverse topological order:
  LF(M) = MIN(LS of all successors)
  LS(M) = LF(M) - duration(M)

For end milestone:
  LF = EF (project deadline)
  LS = LF - duration
```

### Step 3: Calculate Slack (Float)
Total float = amount milestone can delay without delaying project:

```
Total Float = LS - ES = LF - EF

IF Total Float = 0:
  Milestone is on critical path
ELSE:
  Milestone has slack (non-critical)
```

### Step 4: Identify Critical Path
Critical path = sequence of zero-slack milestones from start to end:

```
Critical Path = {M | Total Float(M) = 0}
Path Length = SUM(duration of critical milestones)
```

## Visualization Format

### ASCII Critical Path Graph
```
CRITICAL PATH ANALYSIS

     ┌─────────┐ *** CRITICAL ***
     │   M1    │ Foundation (2w) [ES:0, EF:2, LS:0, LF:2, Slack:0]
     └────┬────┘
          │
    ┌─────┴─────┐
    │           │
    v           v
┌───────┐* ┌───────┐
│  M2   │  │  M3   │  Core (3w) [ES:2, EF:5, Slack:0] || UX (2.5w) [ES:2, EF:4.5, Slack:1.5]
└───┬───┘  └───┬───┘
    │          │
    └────┬─────┘
         │
         v
    ┌─────────┐ *** CRITICAL ***
    │   M4    │ Integration (2w) [ES:5, EF:7, Slack:0]
    └─────────┘

Legend:
  *** = Critical path milestone (zero slack)
  ES = Earliest Start, EF = Earliest Finish
  LS = Latest Start, LF = Latest Finish
  Slack = LS - ES (buffer available)
```

### Tabular Format
```
┌────┬──────────────┬──────┬──────┬──────┬──────┬───────┬──────────────┐
│ ID │ Name         │ ES   │ EF   │ LS   │ LF   │ Slack │ Critical?    │
├────┼──────────────┼──────┼──────┼──────┼──────┼───────┼──────────────┤
│ M1 │ Foundation   │ 0w   │ 2w   │ 0w   │ 2w   │ 0w    │ YES          │
│ M2 │ Core         │ 2w   │ 5w   │ 2w   │ 5w   │ 0w    │ YES          │
│ M3 │ UX Design    │ 2w   │ 4.5w │ 3.5w │ 6w   │ 1.5w  │ NO           │
│ M4 │ Integration  │ 5w   │ 7w   │ 5w   │ 7w   │ 0w    │ YES          │
└────┴──────────────┴──────┴──────┴──────┴──────┴───────┴──────────────┘

Critical Path: M1 → M2 → M4 = 7 weeks
Total Slack Available: 1.5 weeks (M3)
```

## Risk Assessment

### Critical Path Risk Levels
```
Risk = (Critical Path Duration / Total Project Duration) × 100

LOW RISK:    < 60% (significant parallel work)
MEDIUM RISK: 60-80% (balanced critical/non-critical)
HIGH RISK:   > 80% (minimal slack, delays cascade)
```

### Slack Distribution
```
Healthy Project:
  - 30-40% milestones on critical path
  - Average slack: 1-2 weeks per non-critical milestone
  - Multiple parallel tracks

Risky Project:
  - 80%+ milestones on critical path
  - Average slack: < 0.5 weeks
  - Mostly sequential dependencies
```

## Optimization Strategies

### Strategy 1: Add Parallel Tracks
**Problem:** 80% milestones on critical path
**Solution:** Split sequential work into parallel streams

Example:
```
BEFORE: M1 → M2 → M3 → M4 (all critical, 10 weeks)

AFTER:  M1 → {M2 || M3} → M4
        (M1, M4 critical = 4 weeks; M2, M3 parallel with slack)
```

### Strategy 2: Fast-Track Critical Milestones
**Problem:** Critical path too long for deadline
**Solution:** Increase resources on critical milestones only

Example:
```
M2 (critical, 3 weeks) → Assign 2x resources → 1.5 weeks
Result: Critical path reduced by 1.5 weeks
```

### Strategy 3: Crash Critical Path
**Problem:** Need to compress timeline
**Solution:** Reduce duration of critical milestones (costly)

Trade-offs:
- Increased resources (money)
- Reduced scope (features)
- Increased risk (quality)

### Strategy 4: Re-sequence Dependencies
**Problem:** Unnecessary sequential dependencies
**Solution:** Challenge assumptions, enable parallelization

Example:
```
Assumption: "Frontend needs complete backend API"
Reality: "Frontend can mock API and develop in parallel"

BEFORE: Backend → Frontend (sequential, both critical)
AFTER:  {Backend || Frontend} → Integration (parallel, less critical time)
```

## Monitoring Critical Path

### Weekly Check-In Questions
1. Are critical milestones on track?
2. Have any delays occurred on critical path?
3. Has slack on non-critical milestones been consumed?
4. Have new dependencies emerged that change the critical path?

### Early Warning Indicators
- Critical milestone delayed by 1+ day → escalate immediately
- Slack on non-critical < 20% remaining → risk of becoming critical
- New dependency added to critical milestone → recalculate critical path

### Reporting Format
```
CRITICAL PATH STATUS - Week {N}

Critical Path: M1 → M2 → M4 (7 weeks)
Current Status:
  ✅ M1: COMPLETED on time (2 weeks actual)
  🚧 M2: IN PROGRESS (60% complete, Week 4 of 5)
  ⏸️ M4: PENDING (blocked by M2)

Risks:
  ⚠️ M2 trending 0.5 weeks behind (80% confidence)
  → Mitigation: Added 1 developer to M2 this week
  → Updated ETA: Week 5.5 (0.5 week delay)

Non-Critical Status:
  ✅ M3: COMPLETED early (2 weeks vs 2.5 estimate, 0.5w slack consumed)

Revised Critical Path: 7.5 weeks (was 7 weeks)
Deadline Impact: +0.5 weeks (still within acceptable buffer)
```

## Decision Rules

### When to Adjust Critical Path
**ALWAYS recalculate when:**
- Any milestone completes early or late
- New dependencies added
- Milestone split or merged
- Resources reallocated

### When to Escalate
**ESCALATE when:**
- Critical milestone delayed by 10%+ of duration
- Critical path elongates by 2+ days
- Slack on multiple non-critical milestones consumed
- New critical milestone emerges (non-critical becomes critical)

### When to Accept Delay
**ACCEPTABLE when:**
- Delay < 5% of milestone duration
- Non-critical milestone with slack remaining
- Delay absorbed by buffer time in project
- Quality/risk trade-off justified

## Examples

### Example 1: Software Development (Healthy)
```
M1: Architecture (2w) → ES:0, EF:2, Slack:0 [CRITICAL]
M2: Backend (3w) → ES:2, EF:5, Slack:0 [CRITICAL]
M3: Frontend (3w) → ES:2, EF:5, Slack:1 [slack = 1w]
M4: Testing (2w) → ES:5, EF:7, Slack:0 [CRITICAL]

Critical Path: M1 → M2 → M4 = 7 weeks (70% of timeline)
Risk Level: MEDIUM (70% critical)
Buffer: 1 week from M3 slack
```

### Example 2: Content Creation (Risky)
```
M1: Research (1w) → ES:0, EF:1, Slack:0 [CRITICAL]
M2: Outline (0.5w) → ES:1, EF:1.5, Slack:0 [CRITICAL]
M3: Draft (4w) → ES:1.5, EF:5.5, Slack:0 [CRITICAL]
M4: Edit (2w) → ES:5.5, EF:7.5, Slack:0 [CRITICAL]
M5: Publish (0.5w) → ES:7.5, EF:8, Slack:0 [CRITICAL]

Critical Path: M1 → M2 → M3 → M4 → M5 = 8 weeks (100% of timeline)
Risk Level: HIGH (100% critical, no slack)
Recommendation: Add parallel work or accept high risk
```

### Example 3: Product Launch (Optimized)
```
M1: Product Dev (4w) → ES:0, EF:4, Slack:0 [CRITICAL]
M2: Marketing (3w) → ES:4, EF:7, Slack:2 [slack = 2w]
M3: Legal (2w) → ES:4, EF:6, Slack:3 [slack = 3w]
M4: Beta Test (3w) → ES:4, EF:7, Slack:0 [CRITICAL]
M5: Launch (1w) → ES:7, EF:8, Slack:0 [CRITICAL]

Critical Path: M1 → M4 → M5 = 8 weeks (57% of timeline)
Risk Level: LOW (57% critical, multiple parallel tracks)
Buffer: 2-3 weeks across M2, M3
```
