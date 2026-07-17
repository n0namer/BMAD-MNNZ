# Next Steps: Days 2-14 Implementation Roadmap

**Document:** Quick reference for implementation continuation
**Date:** 2026-02-26 (End of Day 1)
**Status:** Ready for Day 2 execution

---

## Day 2 (2026-02-27) - Testing Infrastructure & Layer 1 Design

### Morning: Test Infrastructure Setup

**Objective:** Write tests for S-STRATEGY-001 and S-JOURNAL-001

```bash
# 1. Configure TypeScript + Jest
cd implementation-code
npm install --save-dev jest ts-jest @types/jest typescript

# 2. Create test files
mkdir -p tests/features/01-strategy-lifecycle
mkdir -p tests/features/02-journal-schema
mkdir -p tests/shared

# 3. Files to create
# - tests/features/01-strategy-lifecycle/state-machine.test.ts (10+ tests)
# - tests/features/02-journal-schema/manifest.test.ts (8+ tests)
# - tests/shared/validation.test.ts (validation tests)
# - jest.config.js (already in package.json)
# - tsconfig.json (TypeScript config)
```

### Test Files to Create

#### `state-machine.test.ts` (10+ tests)

```typescript
describe('StrategyStateMachine', () => {
  describe('Basic Transitions', () => {
    test('DRAFT → SUBMITTED transition', () => {
      const machine = new StrategyStateMachine('run-1');
      const transition = machine.transitionState(
        StrategyState.SUBMITTED,
        'submit',
        {},
        'user'
      );
      expect(machine.getState()).toBe(StrategyState.SUBMITTED);
    });

    test('Invalid transition rejected', () => {
      const machine = new StrategyStateMachine('run-1', StrategyState.COMPLETED);
      expect(() => {
        machine.transitionState(StrategyState.DRAFT, 'invalid', {});
      }).toThrow('Invalid state transition');
    });
  });

  describe('Audit Trail', () => {
    test('Records all transitions in audit trail', () => {
      // Test that transitions are recorded
    });

    test('Audit trail has correct timestamps', () => {
      // Test timestamp accuracy
    });
  });

  describe('Concurrent Access', () => {
    test('Locks state during transition', () => {
      // Test concurrent transition prevention
    });

    test('Releases lock after transition', () => {
      // Test lock release
    });
  });

  describe('Rollback', () => {
    test('Rolls back from ACTIVE state', () => {
      // Test rollback logic
    });

    test('Cannot rollback from non-ACTIVE state', () => {
      // Test rollback constraints
    });
  });

  describe('Resubmit', () => {
    test('Allows resubmit from REJECTED state', () => {
      // Test resubmit counter
    });

    test('Respects max resubmit limit', () => {
      // Test max resubmit enforcement
    });
  });
});

describe('StateTimeline', () => {
  test('Maintains chronological order', () => {
    // Test timeline ordering
  });

  test('Calculates state durations', () => {
    // Test duration calculations
  });
});
```

#### `manifest.test.ts` (8+ tests)

```typescript
describe('ManifestHandler', () => {
  describe('Creation', () => {
    test('Creates valid manifest', () => {
      const manifest = ManifestHandler.createManifest(
        'run-1',
        'katana',
        StrategyProfile.STABLE,
        { rsi_period: 14 }
      );
      expect(manifest.runId).toBe('run-1');
      expect(manifest.schemaVersion).toBe('1.0.0');
    });

    test('Rejects invalid profile', () => {
      expect(() => {
        ManifestHandler.createManifest(
          'run-1',
          'katana',
          'invalid' as any,
          {}
        );
      }).toThrow();
    });
  });

  describe('Data Hash', () => {
    test('Generates reproducible hash', () => {
      const hash1 = ManifestHandler.calculateDataHash({ a: 1, b: 2 });
      const hash2 = ManifestHandler.calculateDataHash({ b: 2, a: 1 });
      expect(hash1).toBe(hash2);
    });

    test('Verifies data hash correctness', () => {
      const manifest = ManifestHandler.createManifest(
        'run-1',
        'katana',
        StrategyProfile.STABLE,
        { rsi: 14 }
      );
      expect(ManifestHandler.verifyDataHash(manifest)).toBe(true);
    });
  });

  describe('Validation', () => {
    test('Validates parameter constraints', () => {
      // Test constraint validation
    });

    test('Rejects activeParamCount > 70', () => {
      expect(() => {
        ManifestHandler.createManifest(
          'run-1',
          'katana',
          StrategyProfile.STABLE,
          Object.fromEntries(Array(71).fill(['param', 1]))
        );
      }).toThrow('exceeds maximum');
    });
  });

  describe('JSON Serialization', () => {
    test('Parses JSON manifest', () => {
      const json = JSON.stringify(generateTestManifest());
      const parsed = ManifestHandler.parseManifest(json);
      expect(parsed.runId).toBeDefined();
    });

    test('Serializes to JSON', () => {
      const manifest = generateTestManifest();
      const json = ManifestHandler.toJSON(manifest);
      expect(json).toContain('schemaVersion');
    });
  });
});
```

### Afternoon: Layer 1 Story Design

**Objective:** Design S-STRATEGY-002 and S-JOURNAL-002

Create design documents:
- `features/01-strategy-lifecycle/approval.design.md`
- `features/02-journal-schema/summary.design.md`

Review and validate:
- [ ] All acceptance criteria clear
- [ ] No blockers on Layer 0 (S-STRATEGY-001, S-JOURNAL-001)
- [ ] Dependencies resolved

---

## Day 3 (2026-02-28) - Layer 1 Implementation

### S-STRATEGY-002: Approval Workflow (8 pts)

**Files to create:**
- `features/01-strategy-lifecycle/approval.ts` (implementation)
- `features/01-strategy-lifecycle/tests/approval.test.ts` (6+ tests)

**Key classes:**
- `ApprovalManager` - Manage approval states
- `ApprovalHistory` - Track approval timeline

**Test coverage:**
- [ ] Approval state transitions
- [ ] Rejection reason capture
- [ ] Resubmit counter increments
- [ ] Operator override
- [ ] Version tracking

### S-STRATEGY-003: Kill-Switch (5 pts)

**Files to create:**
- `features/01-strategy-lifecycle/kill-switch.ts` (implementation)
- `features/01-strategy-lifecycle/tests/kill-switch.test.ts` (5+ tests)

**Key classes:**
- `KillSwitch` - Manage kill-switch states
- `KillSwitchTrigger` - Define trigger conditions

**Test coverage:**
- [ ] Kill-switch state transitions
- [ ] Trigger conditions evaluation
- [ ] Graceful shutdown
- [ ] Recovery protocol
- [ ] Audit trail recording

### S-JOURNAL-002: Summary Schema (10 pts)

**Files to create:**
- `features/02-journal-schema/summary.schema.json` (JSON Schema)
- `features/02-journal-schema/summary.ts` (implementation)
- `features/02-journal-schema/tests/summary.test.ts` (8+ tests)

**Key classes:**
- `SummaryHandler` - Create and validate summaries
- `SummaryValidator` - Validate metrics

**Test coverage:**
- [ ] Summary creation
- [ ] Metric validation
- [ ] Performance bounds checking
- [ ] JSON serialization
- [ ] Repository persistence

---

## Days 4-7 Checkpoint

### Sprint Goals by Day 7

**Completed (100%):**
- [x] S-STRATEGY-001 + tests
- [x] S-JOURNAL-001 + tests
- [x] S-STRATEGY-002 + tests
- [x] S-JOURNAL-002 + tests
- [ ] S-STRATEGY-003 + tests (60% - in progress)
- [ ] S-STRATEGY-004 + tests (40% - in progress)

**Test Metrics:**
- [ ] 20-25 tests passing
- [ ] Coverage: ~70%
- [ ] Story points: 38/154 (25%)

### Day 7 Checkpoint Checklist

```
Phase 1 Day 7 Checkpoint (2026-03-04)

✅ COMPLETED (100%):
  [x] S-STRATEGY-001: State Machine (13 pts)
  [x] S-JOURNAL-001: Manifest (8 pts)
  [x] S-STRATEGY-002: Approval (8 pts)
  [x] S-JOURNAL-002: Summary (10 pts)
  Total: 39 story points, 18+ tests

🟡 IN_PROGRESS:
  [ ] S-STRATEGY-003: Kill-Switch (5 pts) - 70% done
  [ ] S-STRATEGY-004: Timeline (5 pts) - 60% done
  [ ] S-JOURNAL-003: Events (8 pts) - 40% done

🔴 NOT STARTED:
  [ ] S-STRATEGY-005 and remaining

📊 METRICS:
  - Tests Written: 20+
  - Tests Passing: 20+
  - Code Coverage: ~70%
  - Critical Path: 45% complete
  - Story Points Completed: 39/154 (25%)

📝 ACTIONS:
  [ ] Update story-completion-summary.md
  [ ] Review test coverage gaps
  [ ] Assess velocity for remaining sprints
  [ ] Adjust Sprint 3-7 as needed
```

---

## Days 8-14 Final Sprint

### Layer 2 Completion (Sprint 3)

**Target:** S-STRATEGY-004, 005, S-JOURNAL-003, 004

- S-STRATEGY-004: State Timeline (5 pts)
- S-STRATEGY-005: Rejection/Resubmit (3 pts)
- S-JOURNAL-003: Events.ndjson (8 pts)
- S-JOURNAL-004: Postgres Schema (8 pts)

### Layer 3-7 Completion (Sprints 4-7)

**Target:** Remaining 20 stories

- S-JOURNAL-005: Reproducibility (6 pts)
- S-TELEMETRY-001, 002: Time-to-Status, MTIF (12 pts)
- S-TELEMETRY-003, 004, 005: Metrics Dashboard (18 pts)
- S-COMPARE-001 to 005: Comparison Workflow (25 pts)
- S-AUDIT-001 to 005: Audit Trail (25 pts)

### Final Validation

**Before Phase 2:**
- [ ] All 25 stories complete
- [ ] 127+ tests passing
- [ ] Code coverage ≥80%
- [ ] No critical bugs
- [ ] Documentation complete
- [ ] Ready for testarch-atdd

---

## Development Workflow

### Daily Pattern

```
9:00  - Check blockers, update story-completion-summary.md
9:15  - Code review of previous day's PRs
9:45  - Development session 1 (2 hours)
11:45 - Commit & push changes
12:00 - Lunch
13:00 - Development session 2 (2 hours)
15:00 - Testing & debugging
16:00 - Documentation update
17:00 - Daily summary, update story-completion-summary.md
```

### Git Workflow

```bash
# Before starting day
git pull origin main

# For each story
git checkout -b feature/s-{story-id}-{story-name}
# ... develop ...
git add .
git commit -m "feat: {story-id} - {description}"
git push origin feature/s-{story-id}

# Merge when complete
git checkout main
git pull origin main
git merge --squash feature/s-{story-id}
git commit -m "feat: {story-id} - complete with tests"
git push origin main
```

---

## Quality Checklist

Before committing each story:

```
Code Quality
  [ ] No TypeScript errors (npm run type-check)
  [ ] ESLint passes (npm run lint)
  [ ] Tests pass (npm test)
  [ ] Coverage >= 85% per file

Documentation
  [ ] JSDoc comments on all public APIs
  [ ] Inline comments for complex logic
  [ ] Test file examples included

Testing
  [ ] Unit tests written (TDD)
  [ ] Edge cases covered
  [ ] Integration tested with dependencies
  [ ] Error cases tested

Acceptance Criteria
  [ ] All ACs implemented
  [ ] ACs tested and passing
  [ ] Story ready for code review
```

---

## Risk Mitigation

### If Behind Schedule

**Priority order for deferral:**
1. Defer S-TELEMETRY-004, 005 (dashboard, alerts)
2. Defer S-COMPARE-003, 004, 005 (delta viz, selection, export)
3. Defer S-AUDIT-003, 004, 005 (UI, reproduce, diagnostic)

**Keep critical path:**
1. E-STRATEGY-LIFECYCLE (34 pts) - MUST complete
2. E-JOURNAL-SCHEMA (40 pts) - MUST complete
3. E-TELEMETRY-001, 002 (12 pts) - MUST complete

### If Ahead of Schedule

**Early completion activities:**
1. Add extra test coverage (P2, P3 tests)
2. Performance optimization
3. Additional validation checks
4. Documentation improvements

---

## Success Indicators

### Daily Progress

- [ ] 1-2 stories completed per day (Days 2-7)
- [ ] 2+ tests written and passing per story
- [ ] Code committed daily
- [ ] story-completion-summary.md updated

### Weekly Progress

- [ ] Week 1: 25-30 story points (Layer 0, 1)
- [ ] Week 2: 30-35 story points (Layer 1, 2)
- [ ] Critical path on track for Day 14

### End of Phase 1

- [ ] All 25 stories complete
- [ ] 127+ tests passing
- [ ] 100% of story points delivered
- [ ] Ready for Phase 2 testing

---

## References

### Files to Review

1. **IMPLEMENTATION-PLAN.md** - Overall strategy
2. **README.md** - Quick reference
3. **story-completion-summary.md** - Daily progress (keep updated!)
4. **Sprint Plan** - Detailed story acceptance criteria
5. **Test Design** - Test requirements

### Code Locations

- Types: `shared/types.ts`
- Validation: `shared/validation.ts`
- Fixtures: `shared/test-helpers.ts`
- Features: `features/*/[implementation].ts`
- Tests: `features/*/tests/[story].test.ts`

---

## Contact

**Lead:** Backend API Developer Agent (Agent-4)
**Updates:** Via story-completion-summary.md
**Escalations:** Document in IMPLEMENTATION-PLAN.md risk section

---

**Ready for Day 2!** 🚀

Next: Write tests for S-STRATEGY-001 and S-JOURNAL-001
