# Capacity Planning - Katana Vectorbt Phase 1

**Project:** Katana Vectorbt Optimizer
**Generated:** 2026-02-26

---

## Team Capacity Model

### Assumptions

| Parameter | Value | Notes |
|-----------|-------|-------|
| Team size | 2 developers | Dev A and Dev B |
| Sprint duration | 2 weeks | 10 working days per sprint |
| Daily capacity per developer | 7 hours productive | Accounting for meetings, reviews |
| Individual velocity | 10-12 points/sprint | Based on story complexity |
| Team velocity | 20-24 points/sprint | Combined |
| Overhead (meetings, reviews, planning) | 15% | Sprint planning, daily standups, reviews |
| Effective team velocity | 17-20 points/sprint | After overhead |
| Buffer sprints | 1 (Sprint 7) | Absorbs overrun from Sprint 6 |

### Velocity Calibration by Story Size

| Story Size | Points | Expected Days (1 dev) |
|------------|--------|----------------------|
| Extra Small | 1-2 | 0.5-1 day |
| Small | 3-5 | 1-2.5 days |
| Medium | 6-8 | 3-4 days |
| Large | 9-13 | 5-7 days |
| Extra Large | 13+ | 7+ days (consider splitting) |

---

## Sprint-by-Sprint Capacity

### Sprint 1 (Weeks 1-2)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 21 |
| Utilization | 105% (slightly over) |
| Dev A load | S-STRATEGY-001 (13 pts) = 6.5 days |
| Dev B load | S-JOURNAL-001 (8 pts) = 4 days |
| Buffer time | Dev B has ~4 days buffer for documentation, setup, tests |

**Note:** 105% utilization is acceptable for Sprint 1. S-STRATEGY-001 at 13 points is large; monitor daily.

### Sprint 2 (Weeks 3-4)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 23 |
| Utilization | 115% (over capacity) |
| Dev A load | S-STRATEGY-002 (8 pts) + S-STRATEGY-003 (5 pts) = 13 pts = 6.5 days |
| Dev B load | S-JOURNAL-002 (10 pts) = 5 days |
| Buffer time | Limited; Dev A has only 1 day buffer, Dev B has 3 days |

**Contingency:** If Sprint 2 is over-capacity at start, defer S-STRATEGY-003 to Sprint 3 (has S-STRATEGY-001 dependency already satisfied by then).

### Sprint 3 (Weeks 5-6)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 24 |
| Utilization | 120% (over capacity) |
| Dev A load | S-STRATEGY-004 (5 pts) + S-STRATEGY-005 (3 pts) = 8 pts = 4 days |
| Dev B load | S-JOURNAL-003 (8 pts) → S-JOURNAL-004 (8 pts) = 16 pts = 8 days sequentially |
| Buffer time | Dev A has 5 days buffer; Dev B is fully packed |

**Contingency:** Dev B must complete S-JOURNAL-003 within first 3-4 days. If S-JOURNAL-003 slips, S-JOURNAL-004 moves to Sprint 4 (pushing S-JOURNAL-005 to Sprint 5).

**Rebalancing option:** Dev A completes STRATEGY-004+005 by day 4, then assists Dev B on JOURNAL-003 code review/testing in days 5-10.

### Sprint 4 (Weeks 7-8)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 18 |
| Utilization | 90% (well-balanced) |
| Dev A load | S-JOURNAL-005 (6 pts) + S-TELEMETRY-001 (6 pts) = 12 pts = 6 days |
| Dev B load | S-TELEMETRY-002 (6 pts) = 3 days |
| Buffer time | Dev A 2 days, Dev B 5 days - Dev B picks up extra testing |

**Note:** Sprint 4 is the first sprint where telemetry work begins. Ensure Dev A finishes JOURNAL-005 early enough to start TELEMETRY-001 without context-switching mid-sprint.

### Sprint 5 (Weeks 9-10)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 19 |
| Utilization | 95% (good) |
| Dev A load | S-TELEMETRY-003 (6 pts) + S-AUDIT-001 (6 pts) = 12 pts = 6 days |
| Dev B load | S-COMPARE-001 (7 pts) = 3.5 days |
| Buffer time | Dev A limited; Dev B has 4.5 days for testing/documentation |

### Sprint 6 (Weeks 11-12)
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 24 |
| Utilization | 120% (over capacity) |
| Dev A load | S-TELEMETRY-004 (8 pts) + S-TELEMETRY-005 (4 pts) = 12 pts = 6 days |
| Dev B load | S-COMPARE-002 (5 pts) + S-AUDIT-002 (7 pts) = 12 pts = 6 days |
| Buffer time | None - both devs fully loaded |

**Contingency:** Sprint 6 is the highest-risk sprint. If S-TELEMETRY-005 (4 pts) or S-COMPARE-002 (5 pts) cannot be completed, move to Sprint 7.

### Sprint 7 (Weeks 13-14) - Buffer Sprint
| Metric | Value |
|--------|-------|
| Available points | 20 |
| Committed points | 25 |
| Utilization | 125% (over capacity, but this is the designated buffer sprint) |
| Dev A load | S-COMPARE-003 (6) + S-COMPARE-004 (4) + S-COMPARE-005 (3) = 13 pts |
| Dev B load | S-AUDIT-003 (6) + S-AUDIT-004 (4) + S-AUDIT-005 (2) = 12 pts |
| Buffer time | None initially, but Sprint 7 absorbs overruns from Sprint 6 |

**Note:** Sprint 7 is intentionally a buffer sprint. Any stories that overflow from Sprint 6 are handled here. If Sprint 6 completes on time, Sprint 7 focuses only on remaining Compare and Audit stories.

---

## Velocity Scenarios

### Optimistic (24 pts/sprint)
- All sprints complete on schedule
- Phase 1 complete end of Sprint 6 (Week 12)
- Sprint 7 is not needed

### Realistic (20 pts/sprint)
- Sprints 2, 3, 6 have minor overruns absorbed by buffer days
- Phase 1 complete end of Sprint 7 (Week 14)

### Conservative (16 pts/sprint)
- Sprint 6 spills heavily into Sprint 7
- Phase 1 complete end of Week 16
- May require a Sprint 8 for final stories

---

## Sprint Point Summary

| Sprint | Planned Points | Capacity | Utilization |
|--------|---------------|----------|-------------|
| Sprint 1 | 21 | 20 | 105% |
| Sprint 2 | 23 | 20 | 115% |
| Sprint 3 | 24 | 20 | 120% |
| Sprint 4 | 18 | 20 | 90% |
| Sprint 5 | 19 | 20 | 95% |
| Sprint 6 | 24 | 20 | 120% |
| Sprint 7 | 25 | 20 | 125% |
| **Total** | **154** | **140** | **110% avg** |

**Average utilization across all sprints: 110%** — This reflects that the team is working at full capacity with some overflow absorbed by the buffer sprint. Acceptable given the defined contingency plans.

---

*Generated by BMAD Sprint Planning Workflow*
*Date: 2026-02-26*
