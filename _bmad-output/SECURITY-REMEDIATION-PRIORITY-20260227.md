# SECURITY REMEDIATION: Priority & Timeline
**Date:** 2026-02-27
**Critical Path:** 12 hours to Phase 2 launch
**Deadline:** Mar 1, 2026 (3 days)

---

## CRITICAL PATH ANALYSIS

```
Feb 27 EOD     Feb 28 (8h)      Feb 28 EOD     Mar 1 (4h)     Mar 1 EOD
   |               |                |             |              |
PLAN         DEVELOP & TEST    MERGE & VALIDATE   QA TEST    GATE DECISION
   |               |                |             |              |
   v               v                v             v              v
[CRITICAL]    [PICKLE FIX]     [AUDIT TEST]   [REGRESSION]   [✅ LAUNCH]
[3 TASKS]     [CAPITAL FIX]    [MERGE PR]     [SECURITY]
              [PARAM FIX]      [CODE REVIEW]  [FINAL REVIEW]
```

---

## TASK BREAKDOWN

### CRITICAL TASK #1: Fix Pickle Vulnerability (FR-MTF-025/030)

**Priority:** 🔴 CRITICAL
**Effort:** 4 hours
**Owner:** Backend Dev #1
**Deadline:** Feb 28, 12:00 PM UTC

#### Definition of Done
- [ ] All pickle.load() removed from codebase
- [ ] Replaced with JSON + NumPy serialization
- [ ] Signature validation added (optional but recommended)
- [ ] Unit tests passing (100% coverage)
- [ ] No pickle imports in code
- [ ] Integration test with real HNSW indices
- [ ] PR reviewed and merged

#### Files to Modify
```
/katana/analysis/hnsw_indexing.py
  - Line 297: Replace pickle.load() with json.load()
  - Line 269: Replace pickle.dump() with json.dump()
  - Add numpy array serialization handling
  - Add signature verification (optional)

/tests/test_hnsw_indexing.py
  - Add tests for JSON serialization
  - Add tests for integrity checks
  - Add tests for tampered file rejection
  - (Create if missing)
```

#### Validation Steps
```python
# Step 1: Create test indices
index = HNSWIndex("1m", vector_dim=115)
vectors = np.random.randn(1000, 115)
trial_ids = [f"trial_{i}" for i in range(1000)]
index.build(vectors, trial_ids)

# Step 2: Save with new method
path = Path("/tmp/test_hnsw_1m.json")
index.save(path)

# Step 3: Verify file is JSON (not pickle binary)
assert path.suffix == ".json"
with open(path) as f:
    data = json.load(f)  # Should work
assert isinstance(data, dict)
assert "trial_ids" in data
assert "vectors" in data

# Step 4: Load and verify
index2 = HNSWIndex("1m", vector_dim=115)
index2.load(path)
assert index2.built
assert len(index2.trial_ids) == 1000

# Step 5: Attempt attack (should fail)
with open(path, "w") as f:
    json.dump({"vectors": "MALICIOUS"}, f)
try:
    index3 = HNSWIndex("1m", vector_dim=115)
    index3.load(path)
    assert False, "Should have rejected corrupted file"
except ValueError:
    pass  # Expected
```

#### Patch Code
```python
# /katana/analysis/hnsw_indexing.py - Line 258-281

def save(self, path: Path) -> None:
    """Persist index to disk using JSON + NumPy binary format.

    Args:
        path: File path to save index (.json format).
    """
    if not self.built:
        logger.warning(f"Skipping save for {self.timeframe}: index not built")
        return

    try:
        data = {
            "timeframe": self.timeframe,
            "trial_ids": self.trial_ids,
            "vectors": self.vectors.tolist(),  # Convert to list for JSON
            "config": {
                "ef_construction": self.config.ef_construction,
                "max_m": self.config.max_m,
                "seed": self.config.seed,
                "ef": self.config.ef,
                "num_threads": self.config.num_threads,
            }
        }

        with open(path, "w") as f:
            json.dump(data, f, indent=2)

        logger.info(f"Saved HNSW index for {self.timeframe} to {path}")
    except Exception as e:
        logger.error(f"Failed to save index {path}: {e}")

def load(self, path: Path) -> None:
    """Load index from disk (JSON format).

    Args:
        path: File path to load index from.

    Raises:
        FileNotFoundError: If file not found.
        ValueError: If file format invalid or corrupted.
    """
    if not path.exists():
        raise FileNotFoundError(f"Index file not found: {path}")

    try:
        with open(path, "r") as f:
            data = json.load(f)

        # NEW: Strict validation
        if not isinstance(data, dict):
            raise ValueError(f"Index file must contain JSON object, got {type(data)}")

        required_fields = ["trial_ids", "vectors", "timeframe"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(data["trial_ids"], list):
            raise ValueError("trial_ids must be a list")

        if not isinstance(data["vectors"], list):
            raise ValueError("vectors must be a list")

        # NEW: Validate vector dimensions
        vectors = np.array(data["vectors"])
        if vectors.shape[1] != self.vector_dim:
            raise ValueError(
                f"Vector dimension {vectors.shape[1]} != expected {self.vector_dim}"
            )

        if len(vectors) != len(data["trial_ids"]):
            raise ValueError(
                f"Vector count {len(vectors)} != trial ID count {len(data['trial_ids'])}"
            )

        self.trial_ids = data["trial_ids"]
        self.vectors = vectors
        self.config = HNSWConfig(
            ef_construction=data["config"].get("ef_construction", 200),
            max_m=data["config"].get("max_m", 16),
            seed=data["config"].get("seed", 42),
            ef=data["config"].get("ef", 200),
            num_threads=data["config"].get("num_threads", 4),
        )
        self.built = True

        logger.info(f"Loaded HNSW index for {self.timeframe} from {path}")
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON index {path}: {e}")
        raise ValueError(f"Invalid JSON file: {path}") from e
    except Exception as e:
        logger.error(f"Failed to load index {path}: {e}")
        raise
```

#### Time Estimate
- Implementation: 1.5 hours
- Testing: 1.5 hours
- Code review & fixes: 1 hour
- **Total: 4 hours** (achievable in Feb 28 morning)

---

### CRITICAL TASK #2: Add Capital Overflow Guards (FR-RKT-CAPITAL-ALLOC)

**Priority:** 🔴 CRITICAL
**Effort:** 5 hours
**Owner:** Backend Dev #2
**Deadline:** Feb 28, 12:00 PM UTC

#### Definition of Done
- [ ] Capital bounds validation added
- [ ] All arithmetic validated (no inf/NaN)
- [ ] Immutable audit trail created
- [ ] Emergency derisking audited
- [ ] Unit tests passing (100% coverage)
- [ ] Integration test with edge cases
- [ ] PR reviewed and merged

#### Files to Modify
```
/katana/autonomy/optimization/capital_allocator.py
  - __init__: Add capital bounds (line 251-262)
  - _calculate_tier_metrics: Add validation (line 427-428)
  - _calculate_kelly_fraction: Add NaN/inf guards (line 467-493)
  - _emergency_derisking: Add audit trail (line 571-612)

/tests/test_capital_allocator.py
  - Create if missing
  - Add tests for overflow
  - Add tests for audit trail
  - Add tests for emergency derisking
```

#### Patch Code (Part 1: Bounds Checking)
```python
# /katana/autonomy/optimization/capital_allocator.py - Line 251-262

import math

def __init__(self, config, total_capital, history_df=None):
    """Initialize Capital Allocator with strict bounds checking.

    Args:
        config: CapitalAllocatorConfig instance
        total_capital: Total portfolio capital in dollars
        history_df: Historical allocation decisions (optional)

    Raises:
        ValueError: If configuration or capital is invalid
    """
    # NEW: Strict capital bounds validation
    if math.isnan(total_capital) or math.isinf(total_capital):
        raise ValueError(f"total_capital cannot be NaN or Inf: {total_capital}")

    if not (0 < total_capital < 1e9):  # 1 billion dollar max
        raise ValueError(
            f"total_capital must be in range (0, 1,000,000,000), "
            f"got {total_capital:,.2f}"
        )

    # ... rest of init
    self.total_capital = float(total_capital)
    self.history_df = history_df if history_df is not None else pd.DataFrame()
    self.last_rebalance: Optional[datetime] = None

    # NEW: Add audit trail
    self.audit_trail_path = Path(config.audit_log_path or "./.audit_trail.jsonl")
    self.audit_trail_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(
        f"CapitalAllocator initialized: capital=${total_capital:,.0f}, "
        f"base_tier_1={config.base_tier_1_allocation*100:.1f}%, "
        f"audit_trail={self.audit_trail_path}"
    )
```

#### Patch Code (Part 2: Arithmetic Safety)
```python
def _calculate_tier_metrics(self, tier_name, strategies, allocation_pct, total_capital):
    """Calculate metrics with strict validation."""

    # NEW: Validate allocation percentage
    if not (0 <= allocation_pct <= 1):
        raise ValueError(f"allocation_pct must be 0-1, got {allocation_pct}")

    if math.isnan(allocation_pct) or math.isinf(allocation_pct):
        raise ValueError(f"allocation_pct is NaN/Inf: {allocation_pct}")

    # NEW: Check for capital overflow
    capital_allocated = total_capital * allocation_pct

    if capital_allocated > total_capital:
        raise ValueError(
            f"Allocated capital {capital_allocated:,.2f} > "
            f"total {total_capital:,.2f}"
        )

    if math.isnan(capital_allocated) or math.isinf(capital_allocated):
        raise ValueError(f"capital_allocated is NaN/Inf: {capital_allocated}")

    # ... rest of method with similar validation
```

#### Patch Code (Part 3: Kelly Criterion Safety)
```python
def _calculate_kelly_fraction(self, win_rate, avg_win=1.0, avg_loss=1.0):
    """Calculate Kelly criterion with NaN/Inf protection."""

    # NEW: Validate all inputs
    for val, name in [
        (win_rate, "win_rate"),
        (avg_win, "avg_win"),
        (avg_loss, "avg_loss"),
    ]:
        if math.isnan(val) or math.isinf(val):
            logger.error(f"{name} is NaN/Inf: {val} - returning 0")
            return 0.0

    if win_rate <= 0 or win_rate >= 1:
        return 0.0

    b = avg_win / max(avg_loss, 0.0001)

    # NEW: Check for division results
    if math.isinf(b) or math.isnan(b):
        logger.error(f"Kelly divisor invalid: avg_win={avg_win}, avg_loss={avg_loss}")
        return 0.0

    p = win_rate
    q = 1.0 - win_rate

    full_kelly = (b * p - q) / b if b > 0 else 0.0

    # NEW: Validate result
    if math.isnan(full_kelly) or math.isinf(full_kelly):
        logger.error(f"Full Kelly is NaN/Inf: returning 0")
        return 0.0

    fractional_kelly = full_kelly * self.config.kelly_fraction
    kelly_capped = min(fractional_kelly, self.config.max_kelly_fraction)

    return max(0.0, kelly_capped)
```

#### Patch Code (Part 4: Immutable Audit Trail)
```python
import json
import hashlib

def _emergency_derisking(self, tier_1_strategies, tier_2_strategies):
    """Emergency derisking with immutable audit trail."""

    # NEW: Create immutable audit record
    timestamp = datetime.now(timezone.utc)
    audit_record = {
        "action": "EMERGENCY_DERISKING",
        "timestamp": timestamp.isoformat(),
        "trigger": "portfolio_drawdown_exceeded",
        "capital_before": self.total_capital,
        "decision": "liquidate_all_tier_1",
        "sequence": len(self.history_df),  # Sequence number
    }

    # NEW: Create cryptographic signature
    record_json = json.dumps(audit_record, sort_keys=True)
    record_hash = hashlib.sha256(record_json.encode()).hexdigest()
    audit_record["signature"] = record_hash

    # NEW: Append to immutable log (APPEND ONLY)
    self._write_audit_trail(audit_record)

    # Calculate allocations
    tier_1_pct = 0.0
    tier_2_pct = 1.0

    tier_1_metrics = self._calculate_tier_metrics(
        "Tier 1", tier_1_strategies, tier_1_pct, self.total_capital
    )
    tier_2_metrics = self._calculate_tier_metrics(
        "Tier 2", tier_2_strategies, tier_2_pct, self.total_capital
    )

    return AllocationResult(
        decision=AllocationDecision.EMERGENCY_DERISKING,
        trigger=RebalancingTrigger.PORTFOLIO_DRAWDOWN,
        tier_1_allocation_pct=tier_1_pct,
        tier_2_allocation_pct=tier_2_pct,
        tier_1_metrics=tier_1_metrics,
        tier_2_metrics=tier_2_metrics,
        rebalance_actions=[
            "EMERGENCY: Liquidate all Tier 1 (rocket) positions",
            "Transfer all capital to Tier 2 (conservative strategies)",
            "Engage circuit breaker protocols",
            "Alert portfolio manager and audit trail",
            f"AUDIT_SIGNATURE: {record_hash[:32]}...",  # NEW
        ],
        rationale="Portfolio drawdown exceeded safety threshold - full defensive mode activated.",
        metadata={
            "audit_hash": record_hash,  # NEW: Immutable reference
            "timestamp": timestamp.isoformat(),  # NEW
        }
    )

def _write_audit_trail(self, record):
    """Write to immutable append-only audit log."""
    try:
        with open(self.audit_trail_path, "a") as f:
            f.write(json.dumps(record) + "\n")

        logger.critical(
            f"EMERGENCY_DERISKING logged: signature={record['signature'][:16]}..."
        )
    except Exception as e:
        logger.error(f"Failed to write audit trail: {e}")
        raise  # Don't suppress audit failures
```

#### Validation Steps
```python
# Test overflow detection
allocator = CapitalAllocator(config, total_capital=1e10)  # Should fail

# Test NaN detection
result = allocator._calculate_kelly_fraction(
    win_rate=float('nan'),
    avg_win=1.0,
    avg_loss=1.0
)
assert result == 0.0  # Safe default

# Test emergency derisking audit
result = allocator._emergency_derisking([], [])
assert "audit_hash" in result.metadata
assert len(result.metadata["audit_hash"]) == 64  # SHA256

# Verify audit trail immutable
lines = self.audit_trail_path.read_text().split("\n")
assert len(lines) > 0
for line in lines[:-1]:  # Last line may be empty
    record = json.loads(line)
    assert "signature" in record
```

#### Time Estimate
- Implementation: 2 hours
- Testing & validation: 2 hours
- Code review & fixes: 1 hour
- **Total: 5 hours** (achievable in Feb 28)

---

### CRITICAL TASK #3: Add Parameter Validation Schema (FR-PARAM-CORE-015)

**Priority:** 🟡 HIGH
**Effort:** 3 hours
**Owner:** Backend Dev #3
**Deadline:** Mar 1, 8:00 AM UTC

#### Definition of Done
- [ ] Pydantic models created for all inputs
- [ ] Runtime type checking enabled
- [ ] Bounds checks on all numeric parameters
- [ ] String sanitization for taxonomy inputs
- [ ] Unit tests passing
- [ ] PR reviewed and merged

#### Implementation Plan
```python
# /katana/validation/strategy_validation.py - Add new section

from pydantic import BaseModel, Field, validator, root_validator
from typing import List, Optional, Dict, Any
import math

class TradeEntry(BaseModel):
    """Validated trade entry with strict bounds."""

    trade_id: str = Field(..., min_length=1, max_length=50)
    entry_time: datetime
    exit_time: datetime
    symbol: str = Field(..., min_length=1, max_length=20)
    entry_price: float = Field(..., gt=0, lt=1e6)
    exit_price: float = Field(..., gt=0, lt=1e6)
    quantity: float = Field(..., gt=0, lt=1e6)
    pnl: float = Field(..., ge=-1e8, le=1e8)

    @validator('trade_id')
    def validate_id(cls, v):
        if not v.replace('_', '').replace('-', '').isalnum():
            raise ValueError('trade_id must be alphanumeric')
        return v

    @validator('exit_time')
    def validate_times(cls, v, values):
        if 'entry_time' in values and v <= values['entry_time']:
            raise ValueError('exit_time must be after entry_time')
        return v

    @validator('pnl')
    def validate_pnl(cls, v, values):
        if math.isnan(v) or math.isinf(v):
            raise ValueError('pnl cannot be NaN or Inf')
        return v

class ValidationConfig(BaseModel):
    """Validated configuration with immutable defaults."""

    max_trades: int = Field(default=10000, ge=1, le=1000000)
    min_psr: float = Field(default=0.95, ge=0.0, le=1.0)
    min_trades: int = Field(default=30, ge=1, le=10000)
    max_drawdown_pct: float = Field(default=0.20, ge=0.0, le=1.0)
    commission_pct: float = Field(default=0.001, ge=0.0, le=0.1)
    slippage_pct: float = Field(default=0.0005, ge=0.0, le=0.1)

    class Config:
        frozen = True  # Immutable after creation

class SignalMetadata(BaseModel):
    """Validated signal metadata - no injection."""

    strategy_name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    sql_filter: Optional[str] = Field(None, max_length=0)  # ❌ BLOCK SQL

    @validator('strategy_name', 'description')
    def no_path_traversal(cls, v):
        if v is None:
            return v
        if '..' in v or '/' in v or '\\' in v:
            raise ValueError('Invalid characters in field')
        return v

    @validator('sql_filter')
    def no_sql_injection(cls, v):
        if v is not None:
            raise ValueError('SQL filters not allowed')
        return v

class StrategyValidator:
    def __init__(self, config: Optional[ValidationConfig] = None):
        self.config = config or ValidationConfig()

    def validate_trades(
        self,
        trades: List[Dict[str, Any]],
        data: pd.DataFrame,
        signals: Optional[Dict[str, Any]] = None,
    ) -> ValidationResult:
        """Validate trades with strict schema."""

        violations = []
        warnings = []
        metrics = {}

        # NEW: Convert dicts to validated models
        try:
            validated_trades = [TradeEntry(**trade) for trade in trades]
        except Exception as e:
            violations.append(f"Trade validation failed: {e}")
            return ValidationResult(
                passed=False,
                violations=violations,
                warnings=warnings,
                metrics=metrics
            )

        # NEW: Validate signal metadata if provided
        if signals:
            try:
                SignalMetadata(**signals)
            except Exception as e:
                violations.append(f"Signal metadata invalid: {e}")
                return ValidationResult(
                    passed=False,
                    violations=violations,
                    warnings=warnings,
                    metrics=metrics
                )

        # ... rest of validation with validated_trades
```

#### Validation Steps
```python
# Should pass
trade = TradeEntry(
    trade_id="trade_001",
    entry_time=datetime(2026, 1, 1, 10, 0),
    exit_time=datetime(2026, 1, 1, 11, 0),
    symbol="EUR/USD",
    entry_price=1.0850,
    exit_price=1.0900,
    quantity=1000,
    pnl=500
)
assert trade.trade_id == "trade_001"

# Should fail - path traversal
try:
    bad_trade = TradeEntry(
        trade_id="../../etc/passwd",  # ❌
        ...
    )
    assert False
except Exception:
    pass  # Expected

# Should fail - NaN
try:
    bad_trade = TradeEntry(
        ...
        pnl=float('nan'),  # ❌
    )
    assert False
except Exception:
    pass  # Expected

# Should fail - SQL injection
try:
    signals = SignalMetadata(
        strategy_name="test",
        sql_filter="'; DROP TABLE trades; --"  # ❌
    )
    assert False
except Exception:
    pass  # Expected
```

#### Time Estimate
- Create Pydantic models: 1.5 hours
- Add validators: 1 hour
- Testing: 0.5 hours
- **Total: 3 hours** (achievable Mar 1 morning)

---

## TESTING SCHEDULE

### Feb 28, 9:00 AM - START DEV

```
09:00 - 10:00: Dev #1 starts pickle replacement
10:00 - 10:30: Dev #2 starts capital guards planning
10:30 - 11:00: Dev #3 starts Pydantic model design

11:00 - 12:00: Dev #1 completes implementation
12:00 - 01:00: Dev #2 completes implementation
01:00 - 02:00: Dev #3 starts implementation (can overlap with testing)
```

### Feb 28, 2:00 PM - START TESTING

```
02:00 - 02:45: Dev #1 unit tests (pickle replacement)
02:45 - 03:30: Dev #1 integration tests

03:00 - 03:45: Dev #2 unit tests (capital guards)
03:45 - 04:30: Dev #2 integration tests

04:00 - 04:30: Dev #3 unit tests (parameter validation)
```

### Feb 28, 5:00 PM - CODE REVIEW

```
05:00 - 05:30: Security Lead reviews all 3 PRs
05:30 - 06:00: Dev team addresses feedback
06:00 - 06:30: Final approval & merge to main
```

### Mar 1, 8:00 AM - FINAL VALIDATION

```
08:00 - 09:00: QA runs full regression test suite
09:00 - 10:00: Security lead conducts final audit
10:00 - 11:00: Team lead prepares launch decision report
11:00 AM: GATE DECISION
```

---

## ROLLBACK PLAN (If Issues Found)

### If Pickle Fix Breaks HNSW
- Rollback to pickle with warning label
- Mark pickle usage as technical debt
- Plan full replacement for next sprint

### If Capital Guards Fail
- Rollback capital allocator to previous version
- Disable emergency derisking temporarily
- Keep manual derisking as fallback

### If Parameter Validation Too Strict
- Roll back to loose validation
- Gradually tighten in next sprint
- Document all rejected parameters

---

## SUCCESS METRICS

| Metric | Target | Status |
|--------|--------|--------|
| All 3 patches merged | Yes | ⏳ |
| Zero critical vulnerabilities | Yes | ⏳ |
| Security score 8.5+ / 10 | 8.5 | ⏳ |
| All unit tests passing | 100% | ⏳ |
| All integration tests passing | 100% | ⏳ |
| No new issues found in audit | 0 | ⏳ |
| Phase 2 launch approved | GO | ⏳ |

---

## CONCLUSION

**Critical Path:** 12 hours achievable over 3 days
**Timeline:** Feb 27 planning → Feb 28 dev → Mar 1 validation → Mar 1 launch
**Risk:** LOW if schedule maintained, HIGH if slipped

**Recommendation:** Start immediately. All patches are high-priority and achievable.

