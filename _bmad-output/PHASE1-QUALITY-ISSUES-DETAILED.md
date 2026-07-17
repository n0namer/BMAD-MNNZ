# Phase 1.0 Code Quality Issues - Detailed Tracking

**Generated:** 2026-02-27
**Total Issues:** 9 (2 HIGH, 4 MEDIUM, 3 LOW)
**Gate Decision:** GREEN ✅ (Launch with fixes)

---

## HIGH-PRIORITY ISSUES

### [HIGH-1] Concurrent Transition Lock Not Truly Atomic

**Status:** 🔴 BLOCKING
**Priority:** CRITICAL PATH
**Component:** `StrategyStateMachine` (state-machine.ts)
**File Location:** `/features/01-strategy-lifecycle/state-machine.ts:64-72`
**Lines:** 64-72

#### Issue Description

The concurrent transition prevention mechanism uses a simple boolean flag (`this.stateLock`) with `Promise.resolve()` yielding. This is **NOT atomically safe** in JavaScript/Node.js and could allow race conditions where multiple `transitionState()` calls enter the critical section simultaneously.

#### Current Implementation

```typescript
public async transitionState(
  nextState: StrategyState,
  trigger: string,
  metadata?: Record<string, any>,
  actor?: string
): Promise<StateTransition> {
  // Prevent concurrent transitions
  if (this.stateLock) {
    throw new Error(
      `Cannot transition from ${this.currentState}: state machine is locked (concurrent attempt detected)`
    );
  }

  this.stateLock = true;
  await Promise.resolve(); // ← This does NOT guarantee atomicity!

  try {
    // Critical section
    const transition: StateTransition = { ... };
    this.auditTrail.push(transition);
    this.currentState = nextState;
    return transition;
  } finally {
    this.stateLock = false;
  }
}
```

#### Problem Scenario

```typescript
// Two concurrent calls
const promise1 = stateMachine.transitionState(StrategyState.SUBMITTED, "submit-1");
const promise2 = stateMachine.transitionState(StrategyState.SUBMITTED, "submit-2");

// ⚠️ RACE CONDITION:
// 1. Thread A: checks stateLock (false) → passes check
// 2. Thread B: checks stateLock (false) → passes check  ← BOTH PASSED!
// 3. Thread A: sets stateLock = true
// 4. Thread B: sets stateLock = true
// 5. Both threads enter critical section → CONCURRENT STATE MODIFICATION
```

#### Risk Assessment

- **Likelihood:** MEDIUM (requires specific timing)
- **Impact:** HIGH (corrupts state machine)
- **Severity:** CRITICAL
- **Affected Scenarios:**
  - High-concurrency environments
  - Multiple webhooks triggering transitions
  - API with burst load
  - User clicking multiple times rapidly

#### Recommended Fix

Use a proper async locking mechanism:

```typescript
/**
 * Proper async locking mechanism
 */
export class StrategyStateMachine {
  private lockQueue: Promise<void> = Promise.resolve();
  private currentState: StrategyState;
  private auditTrail: StateTransition[] = [];
  private approvalMetadata: ApprovalMetadata;

  /**
   * Acquire lock and execute function atomically
   */
  private async withLock<T>(fn: () => Promise<T>): Promise<T> {
    return this.lockQueue.then(async () => {
      // No other operation can start until this completes
      return fn();
    });
  }

  /**
   * Transition to next state (FIXED VERSION)
   */
  public async transitionState(
    nextState: StrategyState,
    trigger: string,
    metadata?: Record<string, any>,
    actor?: string
  ): Promise<StateTransition> {
    return this.withLock(async () => {
      // Validate transition is allowed
      if (!this.isValidTransition(this.currentState, nextState)) {
        throw new Error(
          `Invalid state transition: ${this.currentState} → ${nextState}`
        );
      }

      // Create transition record
      const transition: StateTransition = {
        timestamp: new Date(),
        fromState: this.currentState,
        toState: nextState,
        trigger,
        actor,
        metadata,
        auditTrailId: this.generateAuditId(),
      };

      // Record in audit trail
      this.auditTrail.push(transition);

      // Update state (now guaranteed atomic)
      this.currentState = nextState;

      console.log(
        `[StateMachine:${this.runId}] Transitioned: ${transition.fromState} → ${transition.toState}`
      );

      return transition;
    });
  }

  /**
   * Rollback from ACTIVE state (FIXED VERSION)
   */
  public async rollback(reason: string): Promise<StateTransition | null> {
    return this.withLock(async () => {
      if (this.currentState !== StrategyState.ACTIVE) {
        throw new Error(
          `Cannot rollback from state ${this.currentState}: only from ACTIVE`
        );
      }

      // Find rollback target
      let rollbackTarget: StrategyState | null = null;
      for (let i = this.auditTrail.length - 2; i >= 0; i--) {
        const transition = this.auditTrail[i];
        if (transition.toState !== StrategyState.ACTIVE) {
          rollbackTarget = transition.toState;
          break;
        }
      }

      if (!rollbackTarget) {
        throw new Error("No valid rollback target found");
      }

      // Perform rollback
      const transition: StateTransition = {
        timestamp: new Date(),
        fromState: this.currentState,
        toState: rollbackTarget,
        trigger: "rollback",
        metadata: { reason },
        auditTrailId: this.generateAuditId(),
      };

      this.auditTrail.push(transition);
      this.currentState = rollbackTarget;

      return transition;
    });
  }

  // Remove old lock mechanism
  // private stateLock: boolean = false; // ← DELETE THIS
}
```

#### Test Case to Add

```typescript
describe("Concurrent Transition Safety (Stress Test)", () => {
  test("T-032: Should handle 100 concurrent transitions safely", async () => {
    const stateMachine = new StrategyStateMachine("stress-test");

    // Start with DRAFT
    expect(stateMachine.getState()).toBe(StrategyState.DRAFT);

    // Attempt 100 concurrent transitions to SUBMITTED
    const promises = [];
    for (let i = 0; i < 100; i++) {
      promises.push(
        stateMachine.transitionState(
          StrategyState.SUBMITTED,
          `submit-${i}`
        ).catch(e => ({ error: e.message }))
      );
    }

    const results = await Promise.all(promises);

    // Only ONE should succeed, 99 should fail
    const successes = results.filter(r => !r.error);
    const failures = results.filter(r => r.error);

    expect(successes).toHaveLength(1); // Only one transition allowed
    expect(failures).toHaveLength(99); // Rest blocked
    expect(stateMachine.getState()).toBe(StrategyState.SUBMITTED);
    expect(stateMachine.getAuditTrail()).toHaveLength(2); // init + 1 transition
  });

  test("T-033: Should maintain audit trail consistency under concurrency", async () => {
    const stateMachine = new StrategyStateMachine("audit-stress-test");

    // Sequential valid transitions
    await stateMachine.transitionState(StrategyState.SUBMITTED, "submit");
    await stateMachine.transitionState(StrategyState.APPROVED, "approve");

    // Now attempt concurrent rollback + activate
    const rollback = stateMachine.rollback("user-request");
    const activate = stateMachine
      .transitionState(StrategyState.ACTIVE, "activate")
      .catch(e => ({ error: e.message }));

    const results = await Promise.all([rollback, activate]);

    // One should succeed, one should fail
    const auditTrail = stateMachine.getAuditTrail();

    // Verify audit trail is valid (no duplicate states)
    let previousState = auditTrail[0].toState;
    for (let i = 1; i < auditTrail.length; i++) {
      expect(auditTrail[i].fromState).toBe(previousState);
      previousState = auditTrail[i].toState;
    }
  });
});
```

#### Effort Estimation

- **Implementation:** 2-3 hours
- **Testing:** 1-2 hours
- **Code Review:** 1 hour
- **Total:** 4-6 hours

#### Deadline

- **Must Fix By:** Before Week 1 deployment
- **Target:** End of Day 1 (2026-02-27)

#### Checklist

- [ ] Implement proper async lock queue
- [ ] Remove old stateLock mechanism
- [ ] Add stress test (T-032)
- [ ] Add concurrent safety test (T-033)
- [ ] Run full test suite (should pass 35+ tests)
- [ ] Code review approval
- [ ] Merge to main

---

### [HIGH-2] Rollback Target Validation Incomplete

**Status:** 🔴 BLOCKING
**Priority:** CRITICAL PATH
**Component:** `StrategyStateMachine` (state-machine.ts)
**File Location:** `/features/01-strategy-lifecycle/state-machine.ts:124-132`
**Lines:** 124-132

#### Issue Description

The rollback logic searches for "previous non-ACTIVE state" but doesn't validate if that state is actually a valid target to return to. In edge cases where the state machine reaches ACTIVE through an unexpected path, rolling back to the first non-ACTIVE state might violate the state machine's invariants.

#### Current Implementation

```typescript
public async rollback(reason: string): Promise<StateTransition | null> {
  if (this.currentState !== StrategyState.ACTIVE) {
    throw new Error(
      `Cannot rollback from state ${this.currentState}: Rollback only allowed from ACTIVE state.`
    );
  }

  // Find previous non-ACTIVE state in audit trail
  let rollbackTarget: StrategyState | null = null;
  for (let i = this.auditTrail.length - 2; i >= 0; i--) {
    const transition = this.auditTrail[i];
    if (transition.toState !== StrategyState.ACTIVE) {
      rollbackTarget = transition.toState;
      break; // ← PROBLEM: Takes first non-ACTIVE without validation
    }
  }

  if (!rollbackTarget) {
    throw new Error("No valid rollback target found in audit trail");
  }

  // ... performs rollback to rollbackTarget
}
```

#### Problem Scenario

**Scenario 1: Unexpected ACTIVE Entry**
```typescript
// Normal path: DRAFT → SUBMITTED → APPROVED → ACTIVE
stateMachine.transitionState(StrategyState.SUBMITTED, "submit");
stateMachine.transitionState(StrategyState.APPROVED, "approve");
stateMachine.transitionState(StrategyState.ACTIVE, "activate");

// Now audit trail has:
// [DRAFT→SUBMITTED, SUBMITTED→APPROVED, APPROVED→ACTIVE]

// Rollback would find: APPROVED (correct)
// Result: ACTIVE → APPROVED ✅ VALID

// But if somehow audit trail was modified/corrupted to:
// [DRAFT→ACTIVE (invalid transition allowed)]
// Then rollback finds: DRAFT (which is backwards!)
// Result: ACTIVE → DRAFT ❌ INVALID (skips APPROVED, SUBMITTED)
```

#### Risk Assessment

- **Likelihood:** LOW (requires state machine escape)
- **Impact:** HIGH (silent state corruption)
- **Severity:** HIGH
- **Affected Scenarios:**
  - If future code adds unsafe direct state assignment
  - If audit trail is manually edited/restored incorrectly
  - If database corruption occurs (Phase 2+)

#### Recommended Fix

Validate rollback target is safe:

```typescript
/**
 * Rollback from ACTIVE state to previous valid state
 * FIXED: Validates rollback target is safe
 */
public async rollback(reason: string): Promise<StateTransition | null> {
  if (this.currentState !== StrategyState.ACTIVE) {
    throw new Error(
      `Cannot rollback from state ${this.currentState}: only from ACTIVE`
    );
  }

  // Strategy: Rollback always goes to APPROVED (the state before ACTIVE)
  // This is the safest rollback target and matches the state machine design
  // (APPROVED is the only state that can transition to ACTIVE)
  const safeRollbackTarget = StrategyState.APPROVED;

  // Verify APPROVED is reachable in audit trail
  const hasApprovedInTrail = this.auditTrail.some(
    t => t.toState === StrategyState.APPROVED
  );

  if (!hasApprovedInTrail) {
    throw new Error(
      `Cannot rollback: APPROVED state not found in audit trail. ` +
      `Audit trail may be corrupted. Contact support.`
    );
  }

  // Perform rollback
  this.stateLock = true;
  await Promise.resolve();

  try {
    const transition: StateTransition = {
      timestamp: new Date(),
      fromState: this.currentState,
      toState: safeRollbackTarget,
      trigger: "rollback",
      metadata: { reason },
      auditTrailId: this.generateAuditId(),
    };

    this.auditTrail.push(transition);
    this.currentState = safeRollbackTarget;

    console.log(
      `[StateMachine:${this.runId}] Rolled back: ACTIVE → ${safeRollbackTarget}`
    );

    return transition;
  } finally {
    this.stateLock = false;
  }
}
```

#### Alternative Approach (More Flexible)

If you want to support rollback to multiple states, use this validation:

```typescript
/**
 * Is this a valid rollback target from ACTIVE?
 * Valid targets are states that can precede ACTIVE
 */
private isValidRollbackTarget(target: StrategyState): boolean {
  // From state machine design: ACTIVE can only come from APPROVED
  // So valid rollback target from ACTIVE is only APPROVED
  return target === StrategyState.APPROVED;
}

public async rollback(reason: string): Promise<StateTransition | null> {
  if (this.currentState !== StrategyState.ACTIVE) {
    throw new Error(`Cannot rollback: only from ACTIVE state`);
  }

  // Find most recent valid rollback target
  let rollbackTarget: StrategyState | null = null;
  for (let i = this.auditTrail.length - 2; i >= 0; i--) {
    const target = this.auditTrail[i].toState;
    if (this.isValidRollbackTarget(target)) {
      rollbackTarget = target;
      break;
    }
  }

  if (!rollbackTarget) {
    throw new Error(
      `Cannot rollback: no valid target found. Audit trail may be corrupted.`
    );
  }

  // ... continue with rollback
}
```

#### Test Cases to Add/Fix

```typescript
describe("Rollback Target Validation", () => {
  test("T-024-FIXED: Should rollback only to APPROVED state", async () => {
    const sm = new StrategyStateMachine("test");

    // Normal flow
    await sm.transitionState(StrategyState.SUBMITTED, "submit");
    await sm.transitionState(StrategyState.APPROVED, "approve");
    await sm.transitionState(StrategyState.ACTIVE, "activate");

    // Rollback should go to APPROVED
    const result = await sm.rollback("user-requested");
    expect(result?.toState).toBe(StrategyState.APPROVED);
    expect(sm.getState()).toBe(StrategyState.APPROVED);
  });

  test("T-025: Should reject rollback if APPROVED not in trail", async () => {
    const sm = new StrategyStateMachine("test");

    // Manually corrupt state to ACTIVE (shouldn't be possible normally)
    (sm as any).currentState = StrategyState.ACTIVE;
    (sm as any).auditTrail = [
      {
        timestamp: new Date(),
        fromState: StrategyState.DRAFT,
        toState: StrategyState.DRAFT,
        trigger: "init",
        auditTrailId: "test",
      },
      // Missing APPROVED in trail!
    ];

    // Rollback should fail with clear error
    await expect(sm.rollback("test")).rejects.toThrow(
      /APPROVED state not found/
    );
  });

  test("T-026: Should prevent invalid rollback targets", async () => {
    const sm = new StrategyStateMachine("test");

    // Simulate corrupted trail with DRAFT as last state before ACTIVE
    (sm as any).currentState = StrategyState.ACTIVE;
    (sm as any).auditTrail = [
      {
        timestamp: new Date(),
        fromState: StrategyState.DRAFT,
        toState: StrategyState.DRAFT,
        trigger: "init",
        auditTrailId: "test-1",
      },
      {
        timestamp: new Date(),
        fromState: StrategyState.DRAFT,
        toState: StrategyState.ACTIVE, // Invalid!
        trigger: "corrupted",
        auditTrailId: "test-2",
      },
    ];

    // Should reject invalid target (DRAFT)
    await expect(sm.rollback("test")).rejects.toThrow(
      /no valid target found/
    );
  });
});
```

#### Effort Estimation

- **Implementation:** 1-2 hours
- **Testing:** 1-2 hours
- **Code Review:** 30 minutes
- **Total:** 3-4.5 hours

#### Deadline

- **Must Fix By:** Before Week 1 deployment
- **Target:** End of Day 1 (2026-02-27)

#### Checklist

- [ ] Implement rollback target validation
- [ ] Add validation test (T-025)
- [ ] Add corruption detection test (T-026)
- [ ] Update existing test (T-024)
- [ ] Run full test suite
- [ ] Code review approval
- [ ] Merge to main

---

## MEDIUM-PRIORITY ISSUES

### [MEDIUM-1] Missing Input Validation in ManifestHandler

**Status:** 🟡 MEDIUM
**Priority:** NORMAL
**Component:** `ManifestHandler` (manifest.ts)
**File Location:** `/features/02-journal-schema/manifest.ts:32-74`
**Lines:** 32-74

#### Issue Description

The `createManifest()` method accepts `runId` and `strategyName` parameters but doesn't validate them for empty strings before creating the manifest. This allows invalid manifests with blank IDs or names.

#### Current Code

```typescript
public static createManifest(
  runId: string,
  strategyName: string,
  profile: StrategyProfile,
  parameters: Record<string, string | number | boolean>,
  constraints?: Record<string, { min?: number; max?: number }>
): Manifest {
  // ⚠️ NO VALIDATION of runId or strategyName!

  // Validate parameters
  validateParameters(parameters, constraints);

  // Count active parameters
  const activeParamCount = Object.keys(parameters).length;

  // PRD Invariant check
  if (activeParamCount > 70) {
    throw new ValidationError(
      "parameters",
      parameters,
      `Active parameter count exceeds maximum`
    );
  }

  const now = new Date();

  const manifest: Manifest = {
    schemaVersion: this.SCHEMA_VERSION,
    runId,        // ← Could be empty!
    strategyName, // ← Could be empty!
    profile,
    parameters,
    activeParamCount,
    timestamp: now,
    createdAt: now,
  };

  validateManifest(manifest); // ← This validates, but too late
  manifest.dataHash = this.calculateDataHash(parameters);

  return manifest;
}
```

#### Problem Scenarios

```typescript
// Invalid: empty runId
const manifest1 = ManifestHandler.createManifest(
  "",  // ← Empty!
  "strategy",
  StrategyProfile.STABLE,
  { param1: 10 }
);
// Currently: Allowed (but invalid)
// Expected: Throw ValidationError

// Invalid: whitespace-only strategyName
const manifest2 = ManifestHandler.createManifest(
  "run-123",
  "   ", // ← Whitespace only!
  StrategyProfile.STABLE,
  { param1: 10 }
);
// Currently: Allowed (but invalid)
// Expected: Throw ValidationError
```

#### Risk Assessment

- **Likelihood:** MEDIUM (users might pass empty strings)
- **Impact:** MEDIUM (corrupts manifest data)
- **Severity:** MEDIUM
- **Affected Scenarios:**
  - API endpoints receiving empty form fields
  - Frontend not validating inputs
  - Batch import with incomplete data

#### Recommended Fix

Add explicit input validation before manifest creation:

```typescript
public static createManifest(
  runId: string,
  strategyName: string,
  profile: StrategyProfile,
  parameters: Record<string, string | number | boolean>,
  constraints?: Record<string, { min?: number; max?: number }>
): Manifest {
  // ✅ VALIDATE INPUTS FIRST
  if (!runId || !runId.trim()) {
    throw new ValidationError(
      "runId",
      runId,
      "runId must be a non-empty string"
    );
  }

  if (!strategyName || !strategyName.trim()) {
    throw new ValidationError(
      "strategyName",
      strategyName,
      "strategyName must be a non-empty string"
    );
  }

  // Validate runId format (e.g., no special characters)
  if (!/^[a-zA-Z0-9\-_]+$/.test(runId.trim())) {
    throw new ValidationError(
      "runId",
      runId,
      "runId must contain only alphanumeric, dash, and underscore characters"
    );
  }

  // Validate runId length
  if (runId.trim().length > 100) {
    throw new ValidationError(
      "runId",
      runId,
      "runId must not exceed 100 characters"
    );
  }

  if (strategyName.trim().length > 200) {
    throw new ValidationError(
      "strategyName",
      strategyName,
      "strategyName must not exceed 200 characters"
    );
  }

  // Now validate other inputs
  validateParameters(parameters, constraints);

  const activeParamCount = Object.keys(parameters).length;

  if (activeParamCount > 70) {
    throw new ValidationError(
      "activeParamCount",
      activeParamCount,
      "Active parameter count exceeds maximum of 70"
    );
  }

  const now = new Date();

  const manifest: Manifest = {
    schemaVersion: this.SCHEMA_VERSION,
    runId: runId.trim(), // ← Trim whitespace
    strategyName: strategyName.trim(), // ← Trim whitespace
    profile,
    parameters,
    activeParamCount,
    timestamp: now,
    createdAt: now,
  };

  validateManifest(manifest);
  manifest.dataHash = this.calculateDataHash(parameters);

  return manifest;
}
```

#### Test Cases

```typescript
describe("ManifestHandler Input Validation", () => {
  test("Should reject empty runId", () => {
    expect(() => {
      ManifestHandler.createManifest(
        "",
        "strategy",
        StrategyProfile.STABLE,
        { param1: 10 }
      );
    }).toThrow(/runId must be a non-empty string/);
  });

  test("Should reject whitespace-only runId", () => {
    expect(() => {
      ManifestHandler.createManifest(
        "   ",
        "strategy",
        StrategyProfile.STABLE,
        { param1: 10 }
      );
    }).toThrow(/runId must be a non-empty string/);
  });

  test("Should reject empty strategyName", () => {
    expect(() => {
      ManifestHandler.createManifest(
        "run-123",
        "",
        StrategyProfile.STABLE,
        { param1: 10 }
      );
    }).toThrow(/strategyName must be a non-empty string/);
  });

  test("Should reject runId with special characters", () => {
    expect(() => {
      ManifestHandler.createManifest(
        "run@#$%",
        "strategy",
        StrategyProfile.STABLE,
        { param1: 10 }
      );
    }).toThrow(/alphanumeric, dash, and underscore/);
  });

  test("Should reject runId exceeding max length", () => {
    const longId = "a".repeat(101);
    expect(() => {
      ManifestHandler.createManifest(
        longId,
        "strategy",
        StrategyProfile.STABLE,
        { param1: 10 }
      );
    }).toThrow(/must not exceed 100 characters/);
  });

  test("Should trim whitespace from runId and strategyName", () => {
    const manifest = ManifestHandler.createManifest(
      "  run-123  ",
      "  my-strategy  ",
      StrategyProfile.STABLE,
      { param1: 10 }
    );

    expect(manifest.runId).toBe("run-123");
    expect(manifest.strategyName).toBe("my-strategy");
  });
});
```

#### Effort Estimation

- **Implementation:** 1 hour
- **Testing:** 1 hour
- **Code Review:** 30 minutes
- **Total:** 2.5 hours

#### Deadline

- **Target:** Week 1, Day 1 afternoon
- **Must Fix By:** Before feature development in Phase 1.0

#### Checklist

- [ ] Add input validation to `createManifest()`
- [ ] Add test cases (6 tests)
- [ ] Update manifest.test.ts
- [ ] Run test suite
- [ ] Code review
- [ ] Merge

---

### [MEDIUM-2] Data Hash Calculation Documentation Misleading

**Status:** 🟡 MEDIUM
**Priority:** DOCUMENTATION
**Component:** `validation.ts`
**File Location:** `/shared/validation.ts:427-433`
**Lines:** 427-433

#### Issue Description

The `generateDataHash()` function includes a comment "Note: Full implementation requires crypto library" suggesting it's incomplete, but the actual code correctly uses Node.js's `crypto` module. The comment is outdated and misleading.

#### Current Code

```typescript
/**
 * Generate data hash for reproducibility (S-JOURNAL-005)
 * SHA256 of JSON serialized parameters
 */
export function generateDataHash(obj: any): string {
  // Note: Full implementation requires crypto library
  // This is a placeholder signature for now
  const crypto = require("crypto");
  const serialized = JSON.stringify(obj, Object.keys(obj).sort());
  return crypto.createHash("sha256").update(serialized).digest("hex");
}
```

#### Problem

The comments suggest this is "placeholder" code, but it's actually the complete implementation. This creates confusion for developers maintaining the code.

#### Recommended Fix

Update comments to reflect reality:

```typescript
/**
 * Generate data hash for reproducibility (S-JOURNAL-005)
 *
 * Creates a SHA256 hash of the JSON-serialized parameters with keys sorted
 * alphabetically. This ensures the same parameters always produce the same hash,
 * enabling reproducibility checks.
 *
 * @example
 * const params = { b: 2, a: 1 };
 * const hash = generateDataHash(params);
 * // Always produces same hash regardless of key order
 *
 * @param obj - Object to hash (typically strategy parameters)
 * @returns SHA256 hex digest (64 characters)
 */
export function generateDataHash(obj: any): string {
  const crypto = require("crypto");

  // Sort keys to ensure deterministic output
  const serialized = JSON.stringify(obj, Object.keys(obj).sort());

  // Generate SHA256 hash for integrity verification
  return crypto.createHash("sha256").update(serialized).digest("hex");
}
```

#### Test Case

```typescript
describe("generateDataHash", () => {
  test("Should generate consistent hash for same parameters", () => {
    const params1 = { a: 1, b: 2, c: 3 };
    const params2 = { c: 3, a: 1, b: 2 }; // Different key order

    const hash1 = generateDataHash(params1);
    const hash2 = generateDataHash(params2);

    expect(hash1).toBe(hash2);
    expect(hash1).toHaveLength(64); // SHA256 produces 64-char hex string
  });

  test("Should produce different hash for different parameters", () => {
    const hash1 = generateDataHash({ a: 1 });
    const hash2 = generateDataHash({ a: 2 });

    expect(hash1).not.toBe(hash2);
  });

  test("Should handle nested objects", () => {
    const params = {
      nested: { value: 123 },
      array: [1, 2, 3],
    };

    const hash = generateDataHash(params);
    expect(hash).toHaveLength(64);
  });
});
```

#### Effort Estimation

- **Implementation:** <1 hour (documentation update only)
- **Testing:** 1 hour (add test cases)
- **Code Review:** 15 minutes
- **Total:** 1.5 hours

#### Deadline

- **Target:** Week 1, Day 1 morning
- **Must Fix By:** Before code review

#### Checklist

- [ ] Update JSDoc comments
- [ ] Add example to comment
- [ ] Add/verify test cases
- [ ] Run tests
- [ ] Code review
- [ ] Merge

---

### [MEDIUM-3] Incomplete Rollback Edge Case Test

**Status:** 🟡 MEDIUM
**Priority:** TEST COVERAGE
**Component:** `state-machine.test.ts`
**File Location:** `/test/state-machine.test.ts:266-272`
**Lines:** 266-272

#### Issue Description

Test T-024 is supposed to test the edge case "no rollback target found," but the test setup code doesn't actually achieve that condition. The comment says "Manually set to ACTIVE" but the code doesn't do it.

#### Current Code

```typescript
test("T-024: Should throw error when no rollback target found", async () => {
  const sm = new StrategyStateMachine(testRunId);
  // Manually set to ACTIVE for this edge case test
  // (In practice, this shouldn't happen due to valid transitions)
  await expect(sm.rollback("No target")).rejects.toThrow();
});
```

#### Problem

- State machine starts in DRAFT (not ACTIVE)
- Rollback() throws "Cannot rollback from DRAFT" error (not "No valid target")
- Test passes but doesn't actually test the intended edge case
- The edge case (ACTIVE with no valid target) is never triggered

#### Recommended Fix

Properly set up the edge case:

```typescript
test("T-024: Should throw error when no rollback target found", async () => {
  const sm = new StrategyStateMachine("edge-case-test");

  // Manually set state machine to ACTIVE with corrupted audit trail
  // This simulates a corrupted database or recovery scenario
  (sm as any).currentState = StrategyState.ACTIVE;
  (sm as any).auditTrail = [
    {
      timestamp: new Date(),
      fromState: StrategyState.DRAFT,
      toState: StrategyState.DRAFT,
      trigger: "initialization",
      metadata: { runId: "edge-case-test" },
      auditTrailId: "init-123",
    },
    // No path to ACTIVE - corrupted trail!
  ];

  // Should throw "No valid rollback target" error
  await expect(sm.rollback("No target")).rejects.toThrow(
    /No valid rollback target/
  );
});

test("T-025: Should handle corrupted audit trail during rollback", async () => {
  const sm = new StrategyStateMachine("corrupted-test");

  // Simulate corrupted path: DRAFT directly to ACTIVE (invalid!)
  (sm as any).currentState = StrategyState.ACTIVE;
  (sm as any).auditTrail = [
    {
      timestamp: new Date(),
      fromState: StrategyState.DRAFT,
      toState: StrategyState.DRAFT,
      trigger: "initialization",
      auditTrailId: "init-123",
    },
    {
      timestamp: new Date(),
      fromState: StrategyState.DRAFT,
      toState: StrategyState.ACTIVE, // Invalid transition!
      trigger: "corrupted",
      auditTrailId: "corrupt-123",
    },
  ];

  // Should detect corruption and fail gracefully
  await expect(sm.rollback("Detect corruption")).rejects.toThrow();
});
```

#### Effort Estimation

- **Implementation:** 1 hour
- **Testing:** Included in implementation
- **Code Review:** 15 minutes
- **Total:** 1.5 hours

#### Deadline

- **Target:** Week 1, Day 1 afternoon
- **Must Fix By:** Before test suite finalization

#### Checklist

- [ ] Fix T-024 test setup
- [ ] Add T-025 corruption test
- [ ] Run tests and verify they fail/pass correctly
- [ ] Code review
- [ ] Merge

---

### [MEDIUM-4] Hash Collision Risk with Arbitrary Objects

**Status:** 🟡 MEDIUM
**Priority:** DATA INTEGRITY
**Component:** `validation.ts`
**File Location:** `/shared/validation.ts:427-433`
**Lines:** 427-433

#### Issue Description

The `generateDataHash()` function hashes entire parameter objects, but if those objects contain non-deterministic fields (like timestamps), the same logical parameters will produce different hashes each time, defeating reproducibility.

#### Problem Scenario

```typescript
// Run 1
const params1 = {
  strategy: "RSI",
  period: 14,
  generated_at: new Date("2026-02-27T10:00:00Z"), // Timestamp!
};
const hash1 = generateDataHash(params1); // hash1 = "abc123..."

// Run 2 - same parameters, different timestamp
const params2 = {
  strategy: "RSI",
  period: 14,
  generated_at: new Date("2026-02-27T10:00:01Z"), // 1 second later
};
const hash2 = generateDataHash(params2); // hash2 = "def456..."

// Problem: hash1 !== hash2, but parameters are logically identical!
// This breaks reproducibility verification
```

#### Risk Assessment

- **Likelihood:** MEDIUM (objects may contain metadata)
- **Impact:** MEDIUM (breaks reproducibility checks)
- **Severity:** MEDIUM

#### Recommended Fix

Only hash relevant algorithm parameters, exclude metadata:

```typescript
/**
 * Generate data hash for reproducibility (S-JOURNAL-005)
 *
 * Creates SHA256 hash of ONLY algorithm parameters (not metadata/timestamps).
 * This ensures the same strategy parameters always produce the same hash.
 *
 * Excluded fields (don't affect reproducibility):
 * - timestamp, createdAt, updatedAt (metadata)
 * - _id, uuid, hash (IDs)
 * - internal flags
 */
export function generateDataHash(obj: any): string {
  // Fields to exclude from hash calculation
  const EXCLUDED_FIELDS = [
    "timestamp",
    "createdAt",
    "updatedAt",
    "dataHash", // Don't hash the hash itself!
    "_id",
    "id",
    "uuid",
    "internal",
    "metadata",
  ];

  // Create a clean copy with only algorithm-relevant fields
  const hashableObj: Record<string, any> = {};
  for (const [key, value] of Object.entries(obj)) {
    if (!EXCLUDED_FIELDS.includes(key)) {
      hashableObj[key] = value;
    }
  }

  const crypto = require("crypto");
  const serialized = JSON.stringify(hashableObj, Object.keys(hashableObj).sort());

  return crypto.createHash("sha256").update(serialized).digest("hex");
}
```

#### Test Cases

```typescript
describe("generateDataHash - Reproducibility", () => {
  test("Should produce same hash for same parameters (different timestamps)", () => {
    const params1 = {
      strategy: "RSI",
      period: 14,
      threshold: 70,
      timestamp: new Date("2026-02-27T10:00:00Z"),
    };

    const params2 = {
      strategy: "RSI",
      period: 14,
      threshold: 70,
      timestamp: new Date("2026-02-27T10:00:01Z"), // Different!
    };

    const hash1 = generateDataHash(params1);
    const hash2 = generateDataHash(params2);

    // Should be same hash (timestamps excluded)
    expect(hash1).toBe(hash2);
  });

  test("Should produce different hash for different algorithms", () => {
    const params1 = { strategy: "RSI", period: 14 };
    const params2 = { strategy: "MACD", period: 14 };

    const hash1 = generateDataHash(params1);
    const hash2 = generateDataHash(params2);

    expect(hash1).not.toBe(hash2);
  });

  test("Should exclude metadata fields from hash", () => {
    const params1 = {
      period: 14,
      threshold: 70,
      _id: "id-123",
    };

    const params2 = {
      period: 14,
      threshold: 70,
      _id: "id-456", // Different ID
    };

    const hash1 = generateDataHash(params1);
    const hash2 = generateDataHash(params2);

    // Should be same (ID excluded)
    expect(hash1).toBe(hash2);
  });

  test("Should handle nested parameters", () => {
    const params1 = {
      indicators: { rsi: 14, bb: 20 },
      timestamp: new Date("2026-02-27T10:00:00Z"),
    };

    const params2 = {
      indicators: { rsi: 14, bb: 20 },
      timestamp: new Date("2026-02-27T10:00:05Z"), // Different time
    };

    const hash1 = generateDataHash(params1);
    const hash2 = generateDataHash(params2);

    expect(hash1).toBe(hash2);
  });
});
```

#### Effort Estimation

- **Implementation:** 1-2 hours
- **Testing:** 1-2 hours
- **Code Review:** 30 minutes
- **Total:** 3-4.5 hours

#### Deadline

- **Target:** Week 1-2 (not blocking launch)
- **Must Fix By:** Before Phase 1.0 finalization

#### Checklist

- [ ] Implement hash field exclusion
- [ ] Add test cases (4 tests)
- [ ] Verify reproducibility
- [ ] Document excluded fields
- [ ] Code review
- [ ] Merge

---

## LOW-PRIORITY ISSUES

### [LOW-1] Console.log Used for Logging (Not Production-Ready)

**Status:** 🔵 LOW
**Priority:** OBSERVABILITY
**Component:** `StrategyStateMachine` (state-machine.ts)
**File Location:** `/features/01-strategy-lifecycle/state-machine.ts:101-103, 166-168`

Use structured logging (Winston, Pino, or similar) for production readiness. Effort: 2-3 hours (next sprint).

---

### [LOW-2] Missing Recursive Secret Sanitization

**Status:** 🔵 LOW
**Priority:** SECURITY
**Component:** `validation.ts`
**File Location:** `/shared/validation.ts:438-455`

Add recursive traversal to `sanitizeForLogging()` for nested secrets. Effort: 1-2 hours (next sprint).

---

### [LOW-3] Test Helpers Missing UUID Validation

**Status:** 🔵 LOW
**Priority:** TEST QUALITY
**Component:** `test-helpers.ts`
**File Location:** `/shared/test-helpers.ts:78-93`

Add UUID format validation in `generateTestManifest()`. Effort: <1 hour (next sprint).

---

## Summary

| ID | Issue | Severity | Status | Effort | Week |
|----|-------|----------|--------|--------|------|
| HIGH-1 | Concurrent lock race condition | 🔴 HIGH | BLOCKING | 4-6h | 1 |
| HIGH-2 | Rollback target validation | 🔴 HIGH | BLOCKING | 3-4h | 1 |
| MEDIUM-1 | Input validation gap | 🟡 MEDIUM | NORMAL | 2-3h | 1 |
| MEDIUM-2 | Hash doc misleading | 🟡 MEDIUM | NORMAL | 1-2h | 1 |
| MEDIUM-3 | Test incomplete | 🟡 MEDIUM | NORMAL | 1-2h | 1 |
| MEDIUM-4 | Hash collision risk | 🟡 MEDIUM | NORMAL | 3-4h | 1-2 |
| LOW-1 | Logging strategy | 🔵 LOW | NICE-TO-HAVE | 2-3h | 2 |
| LOW-2 | Sanitization depth | 🔵 LOW | NICE-TO-HAVE | 1-2h | 2 |
| LOW-3 | UUID validation | 🔵 LOW | NICE-TO-HAVE | <1h | 2 |

**Total Effort:** 18-26 hours
**Week 1 Critical Path:** HIGH-1 + HIGH-2 = 7-10 hours
**Go-Live Readiness:** ✅ GREEN (after HIGH fixes)

---

**Document Generated:** 2026-02-27
**Status:** Ready for Development Tracking
