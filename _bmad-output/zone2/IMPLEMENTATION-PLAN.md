# Zone 2 Implementation Plan - Phase 1 Stories
## Backend API Developer Agent - Implementation Specialist

**Project:** Katana Vectorbt Optimizer
**Phase:** Phase 1 - Core Foundation
**Zone:** Zone 2 - Implementation (Days 3-14)
**Status:** INITIATED
**Date:** 2026-02-26

---

## Execution Strategy

### Critical Path Focus
1. **S-STRATEGY-001** (13 pts) - State Machine Transitions (BLOCKER)
2. **S-JOURNAL-001** (8 pts) - Manifest Schema (BLOCKER, parallel)
3. Stories cascade from these two foundations

### Implementation Approach
- **Test-Driven Development**: Write acceptance tests FIRST, then implementation
- **Dependency Chain**: Follow topological order from sprint plan
- **Swarm Coordination**: Hierarchical anti-drift via memory + hooks
- **Memory-First**: Search for patterns before coding (32-50% token savings)

### Code Organization
```
zone2/implementation-code/
├── features/
│   ├── 01-strategy-lifecycle/
│   │   ├── state-machine.ts
│   │   ├── transitions.ts
│   │   ├── approval-workflow.ts
│   │   └── tests/
│   ├── 02-journal-schema/
│   │   ├── manifest.schema.json
│   │   ├── summary-schema.ts
│   │   ├── events-ndjson.ts
│   │   └── tests/
│   ├── 03-telemetry-metrics/
│   ├── 04-compare-workflow/
│   └── 05-audit-trail/
├── shared/
│   ├── types.ts
│   ├── validation.ts
│   └── test-helpers.ts
└── package.json
```

---

## Story Breakdown & Acceptance Criteria

### CRITICAL PATH (Layer 0 - Sprint 1)

#### S-STRATEGY-001: Implement State Machine Transitions [13 pts]
**Acceptance Criteria:**
- [ ] State machine enum: DRAFT → SUBMITTED → APPROVED → ACTIVE → COMPLETED | REJECTED
- [ ] Transition function: `transitionState(current, action, metadata) → next | Error`
- [ ] Invalid transitions rejected with typed error
- [ ] Audit trail recorded for every transition
- [ ] TypeScript types generated from schema
- [ ] 10+ unit tests passing
- [ ] Handles concurrent transition attempts
- [ ] Rollback capability from ACTIVE state

**Dependencies:** None (Layer 0)

---

#### S-JOURNAL-001: Create manifest.json Structure [8 pts]
**Acceptance Criteria:**
- [ ] JSON Schema created at `src/schemas/manifest.schema.json`
- [ ] TypeScript types generated: `Manifest`, `ManifestEntry`
- [ ] Schema validates run_id, strategy_name, profile, parameters
- [ ] min/max constraints for numeric parameters
- [ ] enum validation for profile types (stable/return/rocket)
- [ ] 8+ unit tests passing
- [ ] Backward compatibility layer for v1.0 → v2.0
- [ ] Reproducible data_hash calculation

**Dependencies:** None (Layer 0)

---

### SPRINT 2 (Layer 1 - depends on Layer 0)

#### S-STRATEGY-002: Build Approval Workflow [8 pts]
**Acceptance Criteria:**
- [ ] Approval state machine: PENDING → APPROVED | REJECTED
- [ ] Approval history tracking with timestamps
- [ ] Rejection reasons capture
- [ ] Resubmit capability after rejection
- [ ] Operator override mechanism
- [ ] 6+ unit tests passing
- [ ] Integration with S-STRATEGY-001 state machine

**Dependencies:** S-STRATEGY-001

---

#### S-STRATEGY-003: Add Kill-Switch Mechanism [5 pts]
**Acceptance Criteria:**
- [ ] Kill-switch state enum: ACTIVE → PAUSED | TERMINATED
- [ ] Trigger conditions: manual, performance threshold, error rate
- [ ] Graceful shutdown logic (close open positions)
- [ ] Recovery protocol from paused state
- [ ] Audit trail for all kill-switch events
- [ ] 5+ unit tests passing

**Dependencies:** S-STRATEGY-001

---

#### S-JOURNAL-002: Create summary.json v3.0 [10 pts]
**Acceptance Criteria:**
- [ ] Schema: run summary with performance metrics
- [ ] Fields: run_id, strategy_name, profile, start_time, end_time, equity_curve_hash
- [ ] Metrics: Sharpe, Calmar, Max DD, Win Rate, Profit Factor
- [ ] Validation: performance metrics within expected ranges
- [ ] 8+ unit tests passing
- [ ] Integration with manifest.json schema

**Dependencies:** S-JOURNAL-001

---

### SPRINT 3 (Layer 2 - depends on Layer 1)

#### S-STRATEGY-004: Create State Timeline [5 pts]
**Acceptance Criteria:**
- [ ] Timeline structure: `{ timestamp: DateTime, state: StateEnum, metadata: Object }[]`
- [ ] Chronological ordering validation
- [ ] Query interface: `getTimeline(start, end)`, `getStateAt(timestamp)`
- [ ] Serialization to JSON/CSV
- [ ] 5+ unit tests passing

**Dependencies:** S-STRATEGY-001

---

#### S-STRATEGY-005: Build Rejection/Resubmit Logic [3 pts]
**Acceptance Criteria:**
- [ ] Rejection reason capture and storage
- [ ] Resubmit increments version number
- [ ] Previous version archived
- [ ] Max resubmit attempts enforced
- [ ] 4+ unit tests passing

**Dependencies:** S-STRATEGY-002

---

#### S-JOURNAL-003: Implement events.ndjson [8 pts]
**Acceptance Criteria:**
- [ ] NDJSON format: one JSON object per line
- [ ] Event types: state_changed, metric_updated, error_occurred, trade_executed
- [ ] Event schema with timestamp, event_type, payload
- [ ] Append-only semantics (immutable log)
- [ ] Read streaming interface
- [ ] 8+ unit tests passing

**Dependencies:** S-JOURNAL-001

---

#### S-JOURNAL-004: Build Database Schema (Postgres) [8 pts]
**Acceptance Criteria:**
- [ ] Schema: manifest, summary, events, audit_log tables
- [ ] Primary keys: run_id, event_id
- [ ] Indexes on timestamps and state
- [ ] Referential integrity constraints
- [ ] Up/down migration scripts
- [ ] Test on clean and existing databases
- [ ] 8+ unit tests passing

**Dependencies:** S-JOURNAL-002, S-JOURNAL-003

---

### SPRINT 4 (Layer 3 - Telemetry Foundation)

#### S-JOURNAL-005: Create Reproducibility Verifier [6 pts]
**Acceptance Criteria:**
- [ ] SHA256 hash verification of artifacts
- [ ] data_hash reproducibility across runs
- [ ] Mismatch detection and reporting
- [ ] Cross-platform hash consistency
- [ ] 6+ unit tests passing

**Dependencies:** S-JOURNAL-001, S-JOURNAL-004

---

#### S-TELEMETRY-001: Instrument Time-to-Status [6 pts]
**Acceptance Criteria:**
- [ ] Timer from state DRAFT to APPROVED
- [ ] Timer from APPROVED to ACTIVE
- [ ] Percentile tracking (p50, p95, p99)
- [ ] Integration with metrics dashboard
- [ ] 6+ unit tests passing

**Dependencies:** E-STRATEGY-LIFECYCLE complete

---

#### S-TELEMETRY-002: Implement MTIF Calculation [6 pts]
**Acceptance Criteria:**
- [ ] Mean Time In Field (MTIF): average duration in each state
- [ ] Trend analysis over time
- [ ] Anomaly detection (state duration outliers)
- [ ] 6+ unit tests passing

**Dependencies:** E-STRATEGY-LIFECYCLE complete

---

### SPRINT 5 & 6 (Layers 4-7)

Continue with comparison, audit trail, and telemetry dashboard implementations...

---

## Quality Gates

### Per-Story Definition of Done
- ✅ Code passes all acceptance criteria tests
- ✅ Unit test coverage ≥ 85%
- ✅ TypeScript strict mode enabled
- ✅ No ESLint errors
- ✅ Code review approved by second dev
- ✅ Integration tests pass with dependent stories

### Phase 1 Definition of Complete
- ✅ All 25 stories reach `done` status
- ✅ All 5 epics complete
- ✅ 127+ tests passing
- ✅ Code coverage ≥ 80%
- ✅ Critical path validated
- ✅ Ready for Phase 2 testing (testarch-atdd)

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| S-STRATEGY-001 underestimated | Split into 001a + 001b if >3 days |
| E-JOURNAL-SCHEMA complexity | Pre-define Postgres schema in Sprint 0 |
| Dependency blocking | Track weekly; escalate if >20% slippage |
| Test coverage gaps | TDD from start; write tests first |

---

## Success Metrics (Day 7 Checkpoint)

**Expected Progress (Days 1-7):**
- [ ] S-STRATEGY-001: 80% complete (state machine + tests)
- [ ] S-JOURNAL-001: 100% complete
- [ ] S-STRATEGY-002: 30% complete (design + start coding)
- [ ] S-JOURNAL-002: 20% complete (schema design)
- [ ] 20-25 tests passing
- [ ] story-completion-summary.md updated

---

## Next Steps

1. Initialize TypeScript project with test infrastructure
2. Create base types and validation helpers
3. Implement S-STRATEGY-001 state machine
4. Implement S-JOURNAL-001 manifest schema
5. Begin S-STRATEGY-002 and S-JOURNAL-002 in parallel

