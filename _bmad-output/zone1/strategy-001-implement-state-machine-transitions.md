# Story: S-STRATEGY-001 — Implement State Machine Transitions

## Story
**Epic:** E-STRATEGY-LIFECYCLE
**Sprint:** 1
**Points:** 13
**Priority:** CRITICAL
**Dependencies:** None
**Status:** ready-for-dev

**As a** system,
**I want** a formally defined state machine governing strategy lifecycle transitions,
**So that** all state changes are validated, audited, and impossible to bypass.

---

## Acceptance Criteria

- [ ] AC-1: States defined: `DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED` and `* → CANCELLED`
- [ ] AC-2: Invalid transitions are rejected with descriptive error (e.g., `ACTIVE → DRAFT` is illegal)
- [ ] AC-3: Each transition records: `from_state`, `to_state`, `actor`, `timestamp`, `reason`
- [ ] AC-4: State machine is pure (no side effects inside transition logic)
- [ ] AC-5: 10+ unit tests covering valid transitions, invalid transitions, and audit trail
- [ ] AC-6: TypeScript types exported for all states and transitions
- [ ] AC-7: Full transition matrix documented in code (JSDoc or inline comments)

---

## Tasks / Subtasks

- [ ] T1: Define state enum and transition matrix
  - [ ] T1.1: Create `StrategyState` enum with all 6 states
  - [ ] T1.2: Define `VALID_TRANSITIONS` map (from → allowed targets)
  - [ ] T1.3: Export TypeScript types: `StrategyState`, `TransitionEvent`, `TransitionResult`

- [ ] T2: Implement `StateMachine` class
  - [ ] T2.1: Constructor accepts initial state
  - [ ] T2.2: `transition(to: StrategyState, actor: string, reason?: string): TransitionResult`
  - [ ] T2.3: Validates transition against matrix, throws `InvalidTransitionError` if illegal
  - [ ] T2.4: Returns `TransitionResult` with `success`, `event`, `newState`

- [ ] T3: Implement audit trail
  - [ ] T3.1: `getHistory(): TransitionEvent[]` returns full transition log
  - [ ] T3.2: Each event: `{ from, to, actor, timestamp, reason }`
  - [ ] T3.3: History is immutable (returns copy, not reference)

- [ ] T4: Write unit tests (RED → GREEN → REFACTOR)
  - [ ] T4.1: Test all valid transitions (at least one per state)
  - [ ] T4.2: Test all invalid transitions throw `InvalidTransitionError`
  - [ ] T4.3: Test audit trail records all transitions correctly
  - [ ] T4.4: Test initial state is correct
  - [ ] T4.5: Test history immutability

---

## Dev Notes

### Architecture
- **Pattern:** Pure state machine (no DB calls, no HTTP, no side effects)
- **File:** `lib/state-machine.ts`
- **Test file:** `lib/__tests__/state-machine.test.ts`
- **Framework:** TypeScript (strict mode), Jest for tests

### State Transition Matrix
```
DRAFT     → PENDING, CANCELLED
PENDING   → APPROVED, CANCELLED (rejection handled via reason field)
APPROVED  → ACTIVE, CANCELLED
ACTIVE    → COMPLETED, CANCELLED
COMPLETED → (terminal, no transitions)
CANCELLED → (terminal, no transitions)
```

### Key Types
```typescript
type StrategyState = 'DRAFT' | 'PENDING' | 'APPROVED' | 'ACTIVE' | 'COMPLETED' | 'CANCELLED';

interface TransitionEvent {
  from: StrategyState;
  to: StrategyState;
  actor: string;
  timestamp: Date;
  reason?: string;
}

interface TransitionResult {
  success: true;
  event: TransitionEvent;
  newState: StrategyState;
}

class InvalidTransitionError extends Error {
  constructor(from: StrategyState, to: StrategyState) {
    super(`Invalid transition: ${from} → ${to}`);
  }
}
```

### Project Structure
```
lib/
  state-machine.ts          ← main implementation
  __tests__/
    state-machine.test.ts   ← unit tests
```

### Coding Standards
- Strict TypeScript (no `any`)
- Pure functions where possible
- Immutable data structures
- JSDoc for public API
- Errors as classes (not strings)

---

## Dev Agent Record

### Implementation Plan
*(filled by dev agent during implementation)*

### Debug Log
*(filled by dev agent if issues arise)*

### Completion Notes
*(filled by dev agent upon completion)*

---

## File List
*(filled by dev agent upon completion)*

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-03-01 | Story file created from story-list.md | BMAD |

---

## Status: ready-for-dev
