# Technical Debt Registry - Phase 1 Implementation
## Quick Reference for Phase 2 Planning

**Date:** 2026-02-27
**Status:** 13.5 hours identified, 10 hours blocking Phase 2

---

## 🔴 BLOCKING ITEMS (Must Fix Before Phase 2)

### 1. Test Coverage Below Threshold
**Priority:** CRITICAL
**Location:** All modules
**Current:** 38.6% | **Target:** 85% | **Phase 2 GO Gate:** 70%
**Effort:** 6-8 hours
**Status:** UNSTARTED

**Details:**
- Jest configured with 85% threshold for CI/CD
- Current coverage fails build pipeline
- Need 40+ new tests to reach 70%
- Missing: 180 lines in StateTimeline, 200 lines in validation

**Fix:** Write unit + integration tests
```bash
npm test -- --coverage
# Shows 62% uncovered lines that need tests
```

**Blocking:** Phase 2 CI/CD won't merge any code until coverage ≥ 70%

---

### 2. StateTimeline Class Untested
**Priority:** HIGH
**Location:** `features/01-strategy-lifecycle/state-machine.ts:323-472`
**Lines of Code:** ~150 (18 total after EOF)
**Coverage:** 0%
**Effort:** 2 hours

**Details:**
- Class has 8 public methods:
  - `addEntry()` - basic test exists indirectly (T-030)
  - `getTimeline()` - 0% coverage
  - `getRange()` - 0% coverage
  - `getStateAt()` - 0% coverage
  - `getDurationInState()` - 0% coverage
  - `getStateDurations()` - 0% coverage
  - `validateChronology()` - 0% coverage
  - `toCsv()` - 0% coverage
  - `toJSON()` - 0% coverage

**Methods Used by:** S-STRATEGY-004 FR (State Timeline feature)

**Test Matrix Needed:**
| Method | Tests | Risk |
|--------|-------|------|
| addEntry() | 3 | LOW |
| getTimeline() | 2 | LOW |
| getRange() | 4 | MEDIUM |
| getStateAt() | 3 | MEDIUM |
| getDurationInState() | 4 | HIGH |
| getStateDurations() | 2 | HIGH |
| validateChronology() | 3 | MEDIUM |
| toCsv() | 2 | LOW |
| toJSON() | 2 | LOW |
| **Total** | **25+ tests** | |

**Blocking:** S-STRATEGY-004 cannot be marked complete without these tests

---

### 3. ManifestValidator Untested
**Priority:** HIGH
**Location:** `features/02-journal-schema/manifest.ts:206-302`
**Lines of Code:** ~96
**Coverage:** 0% (direct unit tests)
**Effort:** 1-1.5 hours

**Details:**
- 3 main methods tested only indirectly:
  - `validateNumericRanges()` - tested via validateAll()
  - `validateEnumParameters()` - tested via validateAll()
  - `validateAll()` - tested in T-054 to T-055

**Test Matrix Needed:**
| Method | Tests | Coverage | Risk |
|--------|-------|----------|------|
| validateNumericRanges() | 4 | 0% | MEDIUM |
| validateEnumParameters() | 3 | 0% | LOW |
| validateAll() | 3 | 40% | HIGH |
| Edge cases | 5 | 0% | MEDIUM |
| **Total** | **15+ tests** | |

**Blocking:** Phase 2 profile validation depends on this

---

### 4. Validation Utilities Untested
**Priority:** HIGH
**Location:** `shared/validation.ts`
**Lines of Code:** ~200+ (of 481 total)
**Coverage:** ~30%
**Effort:** 3 hours

**Details:**
- Functions written but untested:
  - `validateRunSummary()` - 0% (Phase 2 blocker)
  - `validatePerformanceMetrics()` - 0%
  - `validateProfileConfig()` - 0%
  - `validateDFFConfig()` - 0%
  - `validateDFFMutualExclusion()` - 0%
  - `sanitizeForLogging()` - 0%
  - `validateSchema()` - 0%

**Test Matrix:**
| Function | Tests | Phase | Risk |
|----------|-------|-------|------|
| validateRunSummary() | 6 | 2 | HIGH |
| validatePerformanceMetrics() | 5 | 2 | MEDIUM |
| validateProfileConfig() | 7 | 2 | HIGH |
| validateDFFConfig() | 4 | 2 | MEDIUM |
| validateDFFMutualExclusion() | 3 | 2 | MEDIUM |
| sanitizeForLogging() | 3 | 2 | LOW |
| validateSchema() | 4 | 2 | HIGH |
| **Total** | **32+ tests** | |

**Blocking:** All Phase 2 features that use these validators (S-JOURNAL-002, S-JOURNAL-004, S-PROFILE-*)

---

### 5. No Integration Tests
**Priority:** HIGH
**Location:** `test/` directory
**Tests:** 0/5 needed
**Coverage Impact:** Critical (no cross-module validation)
**Effort:** 4 hours

**Details:**
- No tests verify:
  - Manifest creation → State machine transition flow
  - Error handling across module boundaries
  - Data consistency between manifest and audit trail
  - Phase 2 workflows that span multiple modules

**Integration Test Scenarios Needed:**
1. Create manifest (S-JOURNAL-001) → Transition state (S-STRATEGY-001) → Verify audit consistency
2. Invalid manifest rejection → No state transition
3. Concurrent manifest creation + transitions
4. Rollback from ACTIVE → Manifest still valid
5. Error recovery: failed validation → state lock released

**Blocking:** Phase 2 will add features across multiple modules; need integration tests to prevent breakage

---

## 🟡 SHOULD FIX ITEMS (Non-Blocking, Improves Maintainability)

### 6. Production console.log() Calls
**Priority:** MEDIUM
**Location:** `state-machine.ts:101-103, 166-168`
**Impact:** DEBUG logs visible in production
**Effort:** 10 minutes
**Blocker for:** Production deployment

**Code:**
```typescript
// Line 101-103
console.log(
  `[StateMachine:${this.runId}] Transitioned: ${previousState} → ${nextState} (trigger: ${trigger})`
);

// Line 166-168
console.log(
  `[StateMachine:${this.runId}] Rolled back: ${previousState} → ${rollbackTarget} (reason: ${reason})`
);
```

**Fix:** Create logging service abstraction
```typescript
// New file: shared/logger.ts
export interface Logger {
  debug(msg: string): void;
  info(msg: string): void;
  warn(msg: string): void;
  error(msg: string, err?: Error): void;
}

// In production: connect to Winston, Pino, or Datadog
```

**Risk if not fixed:** Production logs polluted with debug info; no way to centralize/aggregate

---

### 7. Duplicated Lock Acquisition Logic
**Priority:** MEDIUM
**Location:** `state-machine.ts:64-72, 139-146`
**Impact:** DRY violation, maintenance risk
**Effort:** 20 minutes

**Code:**
```typescript
// Appears twice - in transitionState() and rollback()
if (this.stateLock) {
  throw new Error(`Cannot transition from ${this.currentState}: state machine is locked...`);
}
this.stateLock = true;
await Promise.resolve();
```

**Fix:** Extract helper method
```typescript
private async acquireLock(operation: string): Promise<void> {
  if (this.stateLock) {
    throw new Error(`Cannot ${operation}: state machine is locked (concurrent attempt detected)`);
  }
  this.stateLock = true;
  await Promise.resolve();
}

// Usage
await this.acquireLock('transition');
```

**Risk:** Changes to lock logic must be replicated in 2 places

---

### 8. Fallback Hash Algorithm (base64 instead of SHA256)
**Priority:** MEDIUM
**Location:** `manifest.ts:148-156`
**Impact:** Hash portability concern
**Effort:** 15 minutes

**Code:**
```typescript
try {
  // ... crypto.createHash('sha256')
} catch (error) {
  // Fallback: Base64 substring (NOT SHA256)
  return Buffer.from(serialized).toString("base64").substring(0, 64);
}
```

**Issues:**
1. Non-crypto environments get different hash algorithm
2. 64-char base64 ≠ 64-char SHA256 hex
3. Data reproducibility breaks across environments

**Fix:** Detect environment, throw clear error
```typescript
public static calculateDataHash(parameters: Record<string, any>): string {
  let crypto: any;
  try {
    crypto = require("crypto");
  } catch {
    throw new Error(
      'Crypto module not available. DataHash requires Node.js crypto. ' +
      'For browser environments, use a different hashing mechanism or calculate offline.'
    );
  }
  // ... rest of implementation
}
```

**Risk:** Manifests created in different environments may have incompatible hashes

---

### 9. validateAll() Duplicates Logic
**Priority:** LOW
**Location:** `manifest.ts:257-301`
**Impact:** Maintenance burden
**Effort:** 10 minutes

**Code:**
```typescript
public static validateAll(...) {
  // Duplicates: validateNumericRanges() + validateEnumParameters()
  const numericValidation = this.validateNumericRanges(...);
  const enumValidation = this.validateEnumParameters(...);
  // Then duplicates the error building logic
  for (const [key, valid] of Object.entries(numericValidation)) {
    if (!valid) {
      errors.push(`Parameter ${key} out of range...`);  // Duplicated message
    }
  }
}
```

**Fix:** Consolidate
```typescript
public static validateAll(...) {
  const numericValidation = this.validateNumericRanges(...);
  const enumValidation = this.validateEnumParameters(...);
  const errors = this.buildErrors(numericValidation, enumValidation);
  return {
    valid: errors.length === 0,
    numericValidation,
    enumValidation,
    errors,
  };
}
```

**Risk:** Adding new constraint types requires changes in 2 places

---

### 10. Dynamic require("crypto") Placement
**Priority:** LOW
**Location:** `validation.ts:430, manifest.ts:137`
**Impact:** Code style, module resolution
**Effort:** 5 minutes

**Code:**
```typescript
// Inside function
export function generateDataHash(obj: any): string {
  const crypto = require("crypto");  // Dynamic require inside function
  // ...
}

// Alternative: top of file (better for bundlers)
import crypto from "crypto";
```

**Fix:** Import at top of file
```typescript
import crypto from "crypto";

export function generateDataHash(obj: any): string {
  const serialized = JSON.stringify(obj, Object.keys(obj).sort());
  return crypto.createHash("sha256").update(serialized).digest("hex");
}
```

**Risk:** Dynamic require confuses bundlers; tree-shaking may fail

---

### 11. Hardcoded Configuration Values
**Priority:** MEDIUM
**Location:** Multiple files
**Impact:** Constraints not easily modifiable
**Effort:** 45 minutes

**Hardcoded Values:**
| Value | Location | Type | Phase 2 Impact |
|-------|----------|------|----------------|
| Max active params = 70 | types.ts:98, validation.ts:119, manifest.ts:46 | REPEATED 3x | Profile constraints |
| Max resubmits = 3 | state-machine.ts:40 | HARDCODED | S-STRATEGY-005 |
| Sharpe range -5 to 5 | validation.ts:236 | HARDCODED | Telemetry validation |
| Calmar >= 0 | validation.ts:241 | HARDCODED | Telemetry validation |
| Max drawdown 0-1 | validation.ts:245 | HARDCODED | Risk validation |

**Fix:** Create config object
```typescript
// shared/config.ts
export const StrategyConfig = {
  constraints: {
    maxActiveParams: 70,
    maxResubmits: 3,
  },
  validation: {
    sharpeRange: { min: -5, max: 5 },
    calmarMinimum: 0,
    maxDrawdownRange: { min: 0, max: 1 },
  },
};

// Usage
if (activeParamCount > StrategyConfig.constraints.maxActiveParams) {
  throw new ValidationError(...);
}
```

**Risk:** Constraints become difficult to modify for Phase 2 profiles or experimentation

---

### 12. Unused sanitizeForLogging() Function
**Priority:** LOW
**Location:** `validation.ts:438-454`
**Impact:** Dead code, potential security hole
**Effort:** 15 minutes (test or remove)

**Code:**
```typescript
export function sanitizeForLogging(obj: any, sensitiveKeys: string[] = []): any {
  // Implemented but NEVER CALLED
  const defaultSensitiveKeys = ["password", "apiKey", "secret", "token"];
  // ... redaction logic
}
```

**Decision:** Test OR remove
- **Option A:** Write tests + document usage (2 tests, add to logging strategy)
- **Option B:** Remove with TODO comment for Phase 2 (5 min)

**Recommendation:** Test it (good security practice)

**Risk:** If kept untested, may have bugs when actually needed for PII redaction

---

## 📊 EFFORT SUMMARY

### By Priority

| Priority | Items | Hours | Category |
|----------|-------|-------|----------|
| 🔴 BLOCKING | 5 | ~10 | Must fix for Phase 2 |
| 🟡 SHOULD FIX | 7 | ~1.5 | Improves maintainability |
| 🔵 NICE-TO-HAVE | 3+ | 4+ | Can defer to Phase 2 |

**Total Identified Debt:** 13.5 hours

### By Type

| Type | Count | Hours |
|------|-------|-------|
| Testing Gaps | 5 | 10 |
| Code Smells | 3 | 0.5 |
| DRY Violations | 2 | 0.3 |
| Configuration | 1 | 0.75 |
| Crypto/Security | 1 | 0.25 |
| Dead Code | 1 | 0.2 |

---

## ✅ RESOLUTION CHECKLIST

### Week 1 Action Plan

- [ ] **Day 1-2: Add 40+ Unit Tests (6 hrs)**
  - [ ] StateTimeline: 8 tests
  - [ ] ManifestValidator: 6 tests
  - [ ] Validation utilities: 15 tests
  - [ ] Edge cases: 11 tests
  - [ ] Target: Coverage 38.6% → 65%

- [ ] **Day 2-3: Integration Tests (4 hrs)**
  - [ ] Manifest → State flow
  - [ ] Error recovery scenarios
  - [ ] Rollback sequences
  - [ ] Cross-module consistency

- [ ] **Day 3: Code Quality (1 hr)**
  - [ ] Remove 2 console.log() calls
  - [ ] Fix crypto require placement
  - [ ] Update fallback hash algorithm

- [ ] **Day 4: Configuration (0.75 hrs)**
  - [ ] Extract hardcoded values
  - [ ] Create config object
  - [ ] Add env var support

- [ ] **Day 4-5: Refactoring (0.5 hrs)**
  - [ ] Extract lock acquisition
  - [ ] Remove validateAll() duplication
  - [ ] Test/document sanitizeForLogging()

### Phase 2 Gate Checklist

- [ ] Coverage ≥ 70% (current: 38.6%)
- [ ] All Jest thresholds passing
- [ ] No console.log() in production
- [ ] StateTimeline tested
- [ ] Integration tests passing
- [ ] Configuration extracted
- [ ] No outstanding blocking TODOs

---

## PHASE 2 IMPACT MATRIX

### Which Blockers Affect Which Phase 2 Stories?

| Blocker | S-STRATEGY-* | S-JOURNAL-* | S-TELEMETRY-* | S-PROFILE-* |
|---------|------------|-----------|-------------|-----------|
| Test Coverage | ✓ ALL | ✓ ALL | ✓ ALL | ✓ ALL |
| StateTimeline | ✓ S-004 | | | |
| ManifestValidator | | ✓ S-001 | | |
| RunSummary Validation | | ✓ S-002 | ✓ ALL | |
| ProfileConfig Validation | | | | ✓ ALL |
| Integration Tests | ✓ ALL | ✓ ALL | ✓ ALL | ✓ ALL |

**Conclusion:** All 287 Phase 2 FRs are blocked until test coverage ≥ 70% and integration tests pass

---

## ESCALATION POINTS

### If Delays Occur

**If cleanup extends beyond 1 week:**
- Reduce scope: Keep P0 + P1 items, defer P2 to Phase 2
- Parallel execution: Use additional agents to accelerate testing
- Risk acceptance: Proceed with Phase 2 but increase testing overhead

**If testing uncovers major issues:**
- Potential architectural rework of StateTimeline or ManifestValidator
- May require backporting Phase 2 validation patterns
- Communication: Update product roadmap timeline

---

**Prepared By:** Code Quality Analyzer
**Date:** 2026-02-27
**Next Review:** After 1-week cleanup cycle
