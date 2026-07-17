# Phase 3 Quick Start: First 5 Tests + 3-Day Execution Plan

**Target:** Get first 5 tests passing in 2-3 hours
**Timeline:** Day 1 morning
**Success Metric:** 5/53 tests (9%) complete, foundation established

---

## Why These 5 Tests First?

These tests are quick wins that establish the foundation for all other fixes:

1. **Lowest complexity** - Single or simple fixes
2. **Fast feedback** - Can fix and verify in 30-45 min each
3. **Build momentum** - Creates 9% progress quickly
4. **Enable downstream** - Callback tests needed before panel fixes

---

## Test 1: Kelly Criterion Import Fix

**File:** `src/tests/test_conditions_imports.py`
**Test:** `TestKellyPositionSizingImports::test_kelly_criterion_with_plotly_available`
**Status:** FAILED
**Estimated Time:** 30 minutes

### Error
```
ValueError: avg_loss must be negative
```

### Root Cause
Test is passing positive avg_loss value to KellyCriterion calculator.
Kelly formula requires negative losses for calculation.

### Fix Steps

**Step 1: Examine test** (5 min)
```bash
cd "d:/Users/NIKITA/Documents/DEV/BMAD-MNNZ"
grep -A 20 "test_kelly_criterion_with_plotly_available" src/tests/test_conditions_imports.py
```

**Step 2: Find test data** (5 min)
Look for KellyCriterion instantiation with avg_loss parameter:
```python
# TEST EXPECTS: avg_loss to be NEGATIVE
# Change: avg_loss=0.02
# To: avg_loss=-0.02
```

**Step 3: Update test data** (10 min)
```python
# In test, ensure sample data has negative avg_loss
sample_data = {
    'avg_win': 0.03,
    'avg_loss': -0.02,  # ← MUST BE NEGATIVE
    'win_rate': 0.55
}
```

**Step 4: Run test to verify** (10 min)
```bash
python -m pytest src/tests/test_conditions_imports.py::TestKellyPositionSizingImports::test_kelly_criterion_with_plotly_available -v
```

### Success Criteria
✓ Test passes without ValueError
✓ KellyCriterion accepts negative avg_loss
✓ No other tests broken

---

## Test 2: GitHub Actions Workflow Triggers

**File:** `src/tests/test_github_actions.py`
**Test:** `TestGitHubActionsWorkflow::test_workflow_triggers_on_push_and_pr`
**Status:** FAILED
**Estimated Time:** 20 minutes

### Error
```
AssertionError: Workflow must define triggers
assert 'on' in workflow_dict
```

### Root Cause
GitHub Actions workflow YAML missing `on:` key that defines triggers.

### Fix Steps

**Step 1: Locate workflow file** (5 min)
```bash
find . -name "*.yml" -path ".github/workflows/*" -type f
```

**Step 2: Check workflow structure** (5 min)
Look for missing `on:` section:
```yaml
# INCORRECT:
name: CI/CD Pipeline
jobs:
  setup: ...

# CORRECT:
name: CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
jobs:
  setup: ...
```

**Step 3: Add triggers** (5 min)
Insert `on:` section after `name:`:
```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]
```

**Step 4: Validate YAML** (5 min)
```bash
# Use yamllint or pytest validation
python -m pytest src/tests/test_github_actions.py::TestGitHubActionsWorkflow::test_workflow_triggers_on_push_and_pr -v
```

### Success Criteria
✓ Test passes
✓ Workflow YAML is valid
✓ Triggers defined on push and PR

---

## Test 3: Poetry Build Backend Config

**File:** `src/tests/test_poetry.py`
**Test:** `TestPoetrySetup::test_build_system_configured`
**Status:** FAILED
**Estimated Time:** 15 minutes

### Error
```
AssertionError: Must use poetry-core as build backend
assert 'poetry-core' in 'poetry.core.masonry.api'
```

### Root Cause
pyproject.toml specifies full module path instead of simple poetry-core name.

### Fix Steps

**Step 1: Locate pyproject.toml** (2 min)
```bash
cat pyproject.toml | grep -A 5 "build-backend"
```

**Step 2: Check current config** (3 min)
Should look like:
```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

**Step 3: Update if needed** (5 min)
Ensure build-backend contains "poetry-core":
```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"  # ← This is correct!
```

If it says something else, update to `poetry.core.masonry.api`

**Step 4: Verify** (5 min)
```bash
python -m pytest src/tests/test_poetry.py::TestPoetrySetup::test_build_system_configured -v
```

### Success Criteria
✓ Test passes
✓ Build backend is poetry-core
✓ pyproject.toml valid TOML

---

## Test 4: Position Sizing Allocation Constraint

**File:** `src/tests/test_fr001_position_sizing_integration.py`
**Test:** `TestFR001PositionSizingIntegration::test_portfolio_constraint_max_allocation`
**Status:** FAILED
**Estimated Time:** 45 minutes

### Error
```
AssertionError: Position AAPL exceeds max allocation: 0.3
assert 0.3 <= 0.1
```

### Root Cause
PortfolioManager or PositionSizer not enforcing max_allocation constraint.
Position is 30% when limit is 10%.

### Fix Steps

**Step 1: Find constraint enforcement** (10 min)
```bash
grep -r "max_allocation" src/ --include="*.py" | grep -v test
```

**Step 2: Locate sizing logic** (15 min)
Find PositionSizer or PortfolioManager class:
- Should have method like `validate_constraints()` or `check_allocation()`
- Look for where position size is determined

**Step 3: Add/fix constraint check** (15 min)
```python
def validate_constraints(self, position):
    max_alloc = self.portfolio_constraints['max_allocation']
    if position.allocation_pct > max_alloc:
        raise PortfolioConstraintError(
            f"Position {position.symbol} exceeds max allocation: {position.allocation_pct}"
        )
    return True
```

**Step 4: Run test to verify** (5 min)
```bash
python -m pytest src/tests/test_fr001_position_sizing_integration.py::TestFR001PositionSizingIntegration::test_portfolio_constraint_max_allocation -v
```

### Success Criteria
✓ Allocation constraint enforced
✓ Position exceeding limit is rejected
✓ Test passes
✓ Other position sizing tests still pass

---

## Test 5: Callback Manager Async Support (Foundation)

**File:** `src/tests/test_dashboard_callbacks.py`
**Test:** `TestDashboardCallbacks::test_callback_with_async_handlers`
**Status:** FAILED
**Estimated Time:** 45 minutes

### Error
```
AttributeError: 'AsyncCallbackManager' object has no attribute 'emit_async'
```

### Root Cause
AsyncCallbackManager class missing `emit_async()` method needed for async event emission.

### Fix Steps

**Step 1: Examine AsyncCallbackManager** (10 min)
```bash
find . -name "*.py" -type f -exec grep -l "class AsyncCallbackManager" {} \;
cat <file_path>  # View the class
```

**Step 2: Check what methods exist** (5 min)
Look for: `emit()`, `emit_sync()`, `emit_safe()`
Identify: missing `emit_async()` and `emit_safe()` methods

**Step 3: Add emit_async() method** (20 min)
```python
class AsyncCallbackManager:
    # ... existing code ...

    async def emit_async(self, event_data):
        """Emit event to all async handlers"""
        for listener in self.listeners:
            if asyncio.iscoroutinefunction(listener.handler):
                await listener.handler(event_data)

    def emit_safe(self, event_data):
        """Emit event with error isolation"""
        for listener in self.listeners:
            try:
                if asyncio.iscoroutinefunction(listener.handler):
                    asyncio.run(listener.handler(event_data))
                else:
                    listener.handler(event_data)
            except Exception as e:
                logger.error(f"Error in callback: {e}")
```

**Step 4: Run test to verify** (10 min)
```bash
python -m pytest src/tests/test_dashboard_callbacks.py::TestDashboardCallbacks::test_callback_with_async_handlers -v
```

### Success Criteria
✓ emit_async() method exists
✓ emit_safe() method exists
✓ Test passes
✓ Async handlers work correctly

---

## 3-Day Execution Plan

### Day 1: Quick Wins (2.5 hours)

**Morning (0:00-0:30)** - Setup & Review
- Read this document
- Review test file locations
- Prepare IDE/editor

**Session 1 (0:30-1:00)** - Tests 1-2
- Test 1: Kelly Criterion (30 min) ✓
- Test 2: GitHub Actions (20 min) ✓

**Session 2 (1:00-1:45)** - Tests 3-4
- Test 3: Poetry Config (15 min) ✓
- Test 4: Position Sizing (45 min) ✓

**Session 3 (1:45-2:30)** - Test 5
- Test 5: Async Callbacks (45 min) ✓

**Checkpoint 1 (2:30-2:45)** - Validation
- Run all 5 tests together
- Verify no integration issues
- Document findings

**Result:** 5/53 tests passing (9% complete)

---

### Day 2: Callback Foundation (3 hours)

**Morning (0:00-3:00)** - Complete Group 1
- Tests 6-11 from Group 1 (Callback Manager)
- Fix remaining callback methods
- Standardize event objects

**Following the pattern from Test 5:**
1. Find CallbackManager class
2. Add missing methods (emit_safe, listener property fixes)
3. Standardize event handling
4. Test all 11 callback tests together

**Result:** 16/53 tests passing (30% complete)

---

### Day 3: Early Dashboard Tests (3 hours)

**Morning (0:00-3:00)** - Start Group 2
- Tests 12-14 from Group 2 (DashboardPosition/PositionPanel)
- Fix position panel attributes and methods
- Validate callback integration

**Following the pattern from previous days:**
1. Find DashboardPosition and PositionPanel classes
2. Add missing `size` attribute
3. Add missing methods (get_position_details, get_position_colors)
4. Test the 7 position panel tests

**Result:** 23/53 tests passing (43% complete)

---

## Key Success Metrics (First 3 Days)

| Checkpoint | Tests | Target | Success |
|-----------|-------|--------|---------|
| Day 1 EOD | 5 | 5/5 | ✓ All passing |
| Day 2 EOD | 16 | 16/16 | ✓ All passing |
| Day 3 EOD | 23 | 23/23 | ✓ All passing |

---

## Commands You'll Use Most

```bash
# Single test
python -m pytest src/tests/test_dashboard_callbacks.py::TestDashboardCallbacks::test_callback_with_async_handlers -v

# All tests in file
python -m pytest src/tests/test_dashboard_callbacks.py -v

# All tests (full suite)
python -m pytest src/tests/ -v

# With specific output
python -m pytest src/tests/ -v --tb=short

# Find files quickly
find . -name "test_*.py" -type f | grep dashboard
```

---

## Debugging Tips

### If a test still fails after your fix:

**Check 1: Wrong file location**
```bash
# Verify test file path
ls -la src/tests/test_dashboard_callbacks.py
```

**Check 2: Import issues**
```bash
# Run just the imports
python -c "from src.bmad.dashboard import CallbackManager; print('✓ Imports work')"
```

**Check 3: Method signature mismatch**
```bash
# Check method exists and signature
python -c "from src.bmad.dashboard import CallbackManager; c = CallbackManager(); print(dir(c))" | grep emit
```

**Check 4: Run with more verbose output**
```bash
python -m pytest src/tests/test_name.py::TestClass::test_method -vv --tb=long
```

---

## Getting Help

If a test fix seems stuck:

1. **Read the test** - Understand what it expects
2. **Read the error** - Exact error message is key
3. **Search the codebase** - Find similar patterns
4. **Check the IMPLEMENTATION-CHECKLIST** - Other developers may have solved this
5. **Ask:** Reference line numbers and exact error in question

---

## Track Your Progress

As you complete each test, mark it:

```markdown
## Day 1 Progress

- [x] Test 1: Kelly Criterion Import Fix (COMPLETED)
- [x] Test 2: GitHub Actions Workflow Triggers (COMPLETED)
- [x] Test 3: Poetry Build Backend Config (COMPLETED)
- [x] Test 4: Position Sizing Allocation Constraint (COMPLETED)
- [x] Test 5: Callback Manager Async Support (COMPLETED)

**Result: 5/53 tests passing (9% complete)**
```

---

## Next Document

After completing these 5 tests, see:
**PHASE-3-IMPLEMENTATION-CHECKLIST.md** - Full 53-test checklist with line numbers and fixes

---

**End of Quick Start Guide**

*Ready to start? Pick Test 1 and open the file location in your editor!*
