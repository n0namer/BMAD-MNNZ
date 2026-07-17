# Story 3-3: Position Sizing & Risk Management System

**Status:** IN_PROGRESS

**Created:** 2026-02-28

**Updated:** 2026-03-01 (Status verified: IN_PROGRESS, AC status table added)

---

## Summary

Meta-story coordinating the implementation of position sizing algorithms and integrated risk management system for VectorBT portfolio backtesting framework.

This story spans multiple user story implementations:
- **US-PA-003**: Hard Position Limits (max position size, leverage caps)
- **US-RISK-001**: Kelly Criterion Position Sizer (optimal position sizing)
- Additional risk management features (in planning)

---

## Development Status

Current phase: **Implementation Phase** (Swarm execution active)

### Parallel Work Streams

| Component | US Story | Status | Implementation File |
|-----------|----------|--------|-------------------|
| **Hard Position Limits** | US-PA-003 | Pending | `us-pa-003-hard-limits.md` |
| **Kelly Criterion Sizer** | US-RISK-001 | Pending | `us-risk-001-kelly-sizer.md` |
| **Risk Aggregation Engine** | US-RISK-002 | Pending | `us-risk-002-aggregation.md` |
| **Exposure Monitoring** | US-RISK-003 | Pending | `us-risk-003-exposure.md` |

---

## Acceptance Criteria Status

| AC | Criteria | Status | Phase | Notes |
|-----|----------|--------|-------|-------|
| AC1 | Hard Position Limits Implementation | ⏳ Pending | Design | US-PA-003 queued for implementation |
| AC2 | Kelly Criterion Position Sizer | ⏳ Pending | Design | US-RISK-001 queued for implementation |
| AC3 | Risk Aggregation Engine | ⏳ Pending | Design Phase | Depends on AC1, AC2 completion |
| AC4 | Exposure Monitoring & Alerts | 🔄 IN_PROGRESS | Design Phase | Stream A: Risk limit enforcement in progress |

### AC1: Hard Position Limits Implementation
- **Criteria:** System enforces maximum position size per security
- **Status:** ⏳ Pending (US-PA-003 in queue)
- **File:** `us-pa-003-hard-limits.md`
- **Completion:** Not yet started

### AC2: Kelly Criterion Position Sizer
- **Criteria:** Kelly-optimal position sizing based on win/loss probability and ratio
- **Status:** ⏳ Pending (US-RISK-001 in queue)
- **File:** `us-risk-001-kelly-sizer.md`
- **Completion:** Not yet started

### AC3: Risk Aggregation Across Portfolio
- **Criteria:** System aggregates individual position risks into total portfolio risk
- **Status:** ⏳ Pending (design phase)
- **File:** `us-risk-002-aggregation.md`
- **Completion:** Not yet started

### AC4: Exposure Monitoring & Alerts
- **Criteria:** Real-time exposure monitoring with configurable alert thresholds
- **Status:** 🔄 IN_PROGRESS (Stream A: Risk limit enforcement)
- **File:** `us-risk-003-exposure.md`
- **Completion:** Risk enforcement framework in active development

---

## Technical Architecture

### Component Hierarchy

```
PositionSizingModule
├── HardLimitsEnforcer (US-PA-003)
│   ├── MaxPositionValidator
│   ├── LeverageCapChecker
│   └── LimitExceedanceHandler
│
├── KellyCriterionSizer (US-RISK-001)
│   ├── WinProbabilityCalculator
│   ├── PayoffRatioCalculator
│   ├── OptimalFractionCalculator
│   └── FractionalPositionScaler
│
├── RiskAggregator (US-RISK-002)
│   ├── PositionRiskCalculator
│   ├── CorrelationMatrix
│   ├── PortfolioVaRCalculator
│   └── AggregatedMetrics
│
└── ExposureMonitor (US-RISK-003)
    ├── ExposureCalculator
    ├── ThresholdManager
    ├── AlertSystem
    └── MetricsReporter
```

---

## Implementation Notes

### Key Design Decisions

1. **Hard Limits Priority**: Position size constraints are enforced BEFORE Kelly sizing
   - Prevents violations of position limits even if Kelly suggests larger position
   - Supports gradual sizing up to maximum allowed

2. **Kelly Criterion Adaptation**: Full Kelly divided by constant divisor (N) to reduce risk exposure
   - Supports fractional Kelly (Kelly/2, Kelly/4, etc.)
   - Adjustable based on user risk tolerance

3. **Multi-timeframe Support**: Position sizing respects signals across multiple timeframes
   - Aggregates entries from 5m, 15m, 1h, 4h, 1d signals
   - Prevents duplicate sizing on same security

4. **Risk Aggregation**: Uses correlation matrix to compute true portfolio risk
   - Not simple sum of individual position risks
   - Accounts for diversification benefits

---

## Parallel Execution Plan

### Wave 1 (Current)
- [ ] US-PA-003: Implement hard position limits enforcer
- [ ] US-RISK-001: Implement Kelly criterion position sizer

### Wave 2 (Dependent on Wave 1)
- [ ] US-RISK-002: Implement risk aggregation engine
- [ ] US-RISK-003: Implement exposure monitoring system

### Wave 3 (Integration)
- [ ] Integration tests for all components together
- [ ] End-to-end scenario testing
- [ ] Performance benchmarking

---

## Dependencies

### Blocking Dependencies
- None (design complete, can begin implementation)

### Related Stories
- Story-3-1: Signal Framework (required for signal integration)
- Story-3-2: Portfolio State Manager (required for position tracking)

---

## Linked Artifacts

- Planning: `_bmad-output/planning-artifacts/life-os-sync-plan-2026-02-08.md`
- Orchestration: `_bmad-output/orchestrator-execution/`
- Phase 1 Planning: `_bmad-output/implementation-artifacts/PHASE-1-PLANNING-BRIEF.md`

---

## Notes for Development Team

1. **This is a meta-story** - it doesn't have implementation code itself, but orchestrates multiple US stories
2. **Status = IN_PROGRESS** means swarm is working on child US stories (US-PA-003, US-RISK-001, etc.)
3. **Check linked US stories** for actual implementation progress
4. **Update this file** when:
   - New US stories added to this meta-story
   - Status of child US stories changes
   - Dependencies discovered or resolved
5. **Auto-linking**: Child story files will be created at `us-{category}-{number}-{title}.md` in this directory

---

**Last Updated:** 2026-03-01 (Stream D execution - status corrected)
**Next Review:** After first US story (US-PA-003) begins implementation
