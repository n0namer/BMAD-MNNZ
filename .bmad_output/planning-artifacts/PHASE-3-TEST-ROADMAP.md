# Phase 3 Test Deferral Roadmap

**Status:** Planning Document
**Date:** 2026-03-01
**Total Deferrable Tests:** 53 (32 FAILED + 21 ERROR)
**Estimated Fix Time:** 8-10 hours
**Recommended Phases:** 3 phases across 1-2 weeks

---

## Executive Summary

This document provides a comprehensive roadmap for fixing 53 failing tests deferred from Phase 2 deployment. Tests are organized by component, with priority assessment based on impact (trading execution, system integration) vs effort required.

**Quick Facts:**
- **32 FAILED** tests (known issues, can be debugged)
- **21 ERROR** tests (missing fixtures/setup, need investigation)
- **High Priority:** Dashboard & Callbacks (11 tests) - Direct user impact
- **Medium Priority:** Dashboard Panels (19 tests) - Feature completeness
- **Low Priority:** Setup/CI (21 tests) - Infrastructure/Polish

---

## Test Categorization & Priority Matrix

### Group 1: Callback Manager Tests (11 tests) - HIGH PRIORITY

**Impact:** Direct user interaction (position updates, risk alerts)
**Effort:** 2-3 hours
**Complexity:** Medium
**Skill Required:** bmad-tea-testarch-test-design

#### Tests (11 total):
1. `test_callback_with_async_handlers` - Missing `emit_async()` method
2. `test_callback_mixed_sync_async` - Missing `emit_async()` method
3. `test_callback_error_isolation` - Missing `emit_safe()` method
4. `test_callback_error_logging` - Missing `emit_safe()` method
5. `test_callback_context_preservation` - Event object mismatch (dict vs Event)
6. `test_callback_listener_state` - Event object mismatch (dict vs Event)
7. `test_callback_unsubscribe_from_callback` - Event object mismatch
8. `test_callback_latency_measurement` - Event object mismatch
9. `test_callback_throughput` - Event object mismatch
10. `test_callback_memory_efficiency` - Missing `listeners` attribute
11. Test file: `src/tests/test_dashboard_callbacks.py:TestDashboardCallbacks`

**Root Cause Analysis:**
- CallbackManager class missing methods: `emit_async()`, `emit_safe()`
- Event handling uses dict instead of Event namedtuple/dataclass
- Property access `.listeners` should use `.get_listeners()` method

**Fix Strategy:**
1. Add `emit_async()` method to AsyncCallbackManager
2. Add `emit_safe()` method to CallbackManager
3. Standardize event object as Event class or dict with `event_type` key
4. Replace `listeners` property with `get_listeners()` call

**Estimated Time:** 2-3 hours
**Dependencies:** None (standalone test group)
**Success Criteria:**
- All 11 tests pass ✓
- Callback events emit reliably ✓
- Error handling works correctly ✓

---

### Group 2: Dashboard Panel Tests (19 tests) - MEDIUM PRIORITY

**Impact:** Feature completeness (trading dashboard UI)
**Effort:** 3-4 hours
**Complexity:** Medium-High
**Skill Required:** bmad-tea-testarch-test-design

#### Subgroup 2A: DashboardPosition & PositionPanel (7 tests)
1. `test_position_panel_renders` - Missing `size` attribute on DashboardPosition
2. `test_position_panel_displays_symbols` - Missing `size` attribute
3. `test_position_panel_shows_size_and_pnl` - Missing `get_position_details()` method
4. `test_position_panel_color_coding` - Missing `get_position_colors()` method
5. `test_callbacks_on_position_update` - Unexpected kwarg `on_position_update`
6. `test_callbacks_data_consistency` - Unexpected kwarg `on_position_update`
7. `test_callbacks_error_handling` - Missing `register_callback()` method

**Root Cause:** PositionPanel/DashboardPosition interface mismatch

#### Subgroup 2B: DashboardMetrics & RiskPanel (7 tests)
1. `test_risk_panel_renders` - Missing `values` attribute on DashboardMetrics
2. `test_risk_panel_shows_metrics` - Missing `get_metric_values()` method
3. `test_risk_panel_updates_on_data_change` - Wrong method name (`update_metrics` vs `update_metric`)
4. `test_risk_panel_alerts_on_threshold` - Missing `get_alerts()` method
5. `test_callbacks_on_risk_alert` - Unexpected kwarg `on_risk_alert`
6. `test_callbacks_performance_monitoring` - Missing `register_callback()` method
7. Additional test relying on RiskPanel interface

**Root Cause:** RiskPanel/DashboardMetrics interface mismatch

#### Subgroup 2C: PerformancePanel (5 tests)
1. `test_performance_panel_renders` - Unexpected kwarg `equity_curve`
2. `test_performance_panel_equity_curve` - Unexpected kwarg `equity_curve`
3. `test_performance_panel_period_returns` - Unexpected kwarg `equity_curve`
4. `test_performance_panel_drawdown_chart` - Unexpected kwarg `equity_curve`
5. `test_callbacks_on_trade_executed` - Unexpected kwarg `equity_curve`

**Root Cause:** PerformancePanel constructor doesn't accept `equity_curve` kwarg

**Fix Strategy:**
1. Add missing attributes (`size`, `values`) to dashboard model classes
2. Add missing methods (`get_position_details()`, `get_metric_values()`, `get_alerts()`, `register_callback()`)
3. Update PerformancePanel.__init__() to accept `equity_curve` parameter
4. Update callback integration in all panel classes
5. Align method names with test expectations

**Estimated Time:** 3-4 hours
**Dependencies:** Group 1 (Callback Manager) should be done first
**Success Criteria:**
- All 19 tests pass ✓
- Panel rendering works ✓
- Callback integration complete ✓

---

### Group 3: Position Sizing & Risk Constraints (1 test) - MEDIUM PRIORITY

**Impact:** Trading risk management (allocation enforcement)
**Effort:** 1-2 hours
**Complexity:** Low-Medium
**Skill Required:** bmad-tea-testarch-test-design

#### Test (1 total):
1. `test_portfolio_constraint_max_allocation` - Constraint not enforced

**Location:** `src/tests/test_fr001_position_sizing_integration.py:TestFR001PositionSizingIntegration`

**Error Details:**
```
AssertionError: Position AAPL exceeds max allocation: 0.3
assert 0.3 <= 0.1
```

**Root Cause:** Portfolio constraint enforcement missing or broken in position sizing logic

**Fix Strategy:**
1. Debug position sizing algorithm for constraint application
2. Verify max_allocation constraint is checked before position acceptance
3. Add constraint validation in PortfolioManager or PositionSizer
4. Update test if constraint logic needs adjustment

**Estimated Time:** 1-2 hours
**Dependencies:** None
**Success Criteria:**
- Position allocation respects max_allocation limit ✓
- Test passes with correct constraint enforcement ✓

---

### Group 4: Imports & Dependencies (2 tests) - MEDIUM PRIORITY

**Impact:** Module loading and functionality
**Effort:** 1-2 hours
**Complexity:** Low
**Skill Required:** bmad-tea-testarch-test-design

#### Tests (2 total):
1. `test_kelly_criterion_with_plotly_available` - ValueError in KellyCriterion
   - Location: `src/tests/test_conditions_imports.py:TestKellyPositionSizingImports`
   - Error: `avg_loss must be negative`
   - Fix: Validate kelly criterion calculation logic, check sample data

2. `test_workflow_triggers_on_push_and_pr` - GitHub Actions workflow YAML issue
   - Location: `src/tests/test_github_actions.py:TestGitHubActionsWorkflow`
   - Error: `Workflow must define triggers - 'on' not in workflow dict`
   - Fix: Add `on:` key to GitHub Actions workflow YAML

**Root Cause:**
- KellyCriterion receives invalid input data (positive loss)
- GitHub Actions YAML has incorrect structure

**Fix Strategy:**
1. Fix kelly criterion test data (avg_loss must be negative)
2. Update .github/workflows/*.yml to include `on:` trigger key
3. Validate workflow YAML structure matches GitHub Actions spec

**Estimated Time:** 1-2 hours
**Dependencies:** None
**Success Criteria:**
- KellyCriterion calculation accepts valid data ✓
- GitHub Actions workflow validates correctly ✓

---

### Group 5: Build & Configuration (1 test) - LOW PRIORITY

**Impact:** Development setup (build system)
**Effort:** 0.5 hours
**Complexity:** Very Low
**Skill Required:** bmad-tea-testarch-test-design

#### Test (1 total):
1. `test_build_system_configured` - Poetry config issue
   - Location: `src/tests/test_poetry.py:TestPoetrySetup`
   - Error: `Must use poetry-core as build backend - found 'poetry.core.masonry.api'`
   - Fix: Update pyproject.toml build-backend field

**Root Cause:** pyproject.toml specifies full module path instead of poetry-core package name

**Fix Strategy:**
1. Edit pyproject.toml
2. Change build-backend from 'poetry.core.masonry.api' to 'poetry.core.masonry.api' (or verify current setting)
3. Ensure Poetry configuration is valid

**Estimated Time:** 0.5 hours
**Dependencies:** None
**Success Criteria:**
- Poetry recognizes correct build backend ✓

---

### Group 6: Story Acceptance Tests - Infrastructure (21 tests) - LOW PRIORITY

**Impact:** CI/CD pipeline and environment setup
**Effort:** 3-4 hours
**Complexity:** Medium
**Skill Required:** bmad-tea-testarch-test-design, bmad-bmm-qa-automate

#### Subgroup 6A: GitHub Setup (8 tests) - ERROR
1. `test_github_repo_exists` - Missing GitHub connection/fixture
2. `test_branch_protection_enabled` - Missing branch config
3. `test_project_structure` - Missing project fixture
4. `test_poetry_installs` - Missing poetry environment
5. `test_docker_builds` - Missing Docker setup
6. `test_precommit_installs` - Missing pre-commit setup
7. `test_setup_md_exists` - Missing SETUP.md file
8. `test_contributing_md_exists` - Missing CONTRIBUTING.md file

**Location:** `src/tests/test_story_0_1_acceptance.py:TestGitHubSetup`

**Root Cause:** Test fixtures/setup missing or GitHub API not configured

#### Subgroup 6B: Python Environment Setup (6 tests) - ERROR
1. `test_github_actions_workflow_valid` - Invalid GitHub Actions YAML
2. `test_pytest_runs` - pytest execution issue
3. `test_coverage_above_threshold` - Coverage calculation issue
4. `test_poetry_lock_exists` - Missing poetry.lock file
5. `test_all_quality_checks_pass` - Multiple quality check failures
6. `test_ci_blocks_failing_tests` - CI configuration issue

**Location:** `src/tests/test_story_0_2_acceptance.py:TestPythonEnvironmentSetup`

**Root Cause:** Missing fixtures, CI pipeline not fully configured

#### Subgroup 6C: Security Baseline (7 tests) - ERROR
1. `test_no_hardcoded_secrets` - Secret scanning fixture missing
2. `test_env_file_example_exists` - Missing .env.example file
3. `test_security_md_exists` - Missing SECURITY.md file
4. `test_bandit_scanning_passes` - Bandit not configured
5. `test_github_secrets_configured` - GitHub secrets not set
6. `test_dependency_audit_passes` - Dependency audit not configured
7. `test_precommit_blocks_secrets` - Pre-commit hook not configured

**Location:** `src/tests/test_story_0_sec_acceptance.py:TestSecurityBaseline`

**Root Cause:** Security infrastructure not fully implemented, missing documentation

**Fix Strategy:**
1. Create missing documentation (SETUP.md, CONTRIBUTING.md, SECURITY.md, .env.example)
2. Configure GitHub API access/fixtures for environment tests
3. Add pre-commit hooks configuration
4. Configure Bandit security scanning
5. Setup GitHub secrets for CI
6. Add missing Poetry lock file
7. Configure dependency audit tools

**Estimated Time:** 3-4 hours
**Dependencies:** Most of Group 1-5 should be working first
**Success Criteria:**
- All documentation files exist ✓
- GitHub setup validated ✓
- Security baseline established ✓
- CI/CD pipeline complete ✓

---

## Phase 3 Implementation Timeline

### Phase 3-A: Foundation (Days 1-2) - ~5 hours
**Focus:** Core callback and panel infrastructure

1. **Day 1 - Morning (2 hours)**
   - Group 1: Fix Callback Manager tests (11 tests)
     - Add `emit_async()` and `emit_safe()` methods
     - Standardize event objects
     - Fix listener attribute access
   - Skills needed: bmad-tea-testarch-test-design
   - Deliverable: 11/11 tests passing

2. **Day 1 - Afternoon (2 hours)**
   - Group 4: Fix imports & dependencies (2 tests)
     - Fix KellyCriterion test data
     - Update GitHub Actions workflow YAML
   - Group 5: Fix build config (1 test)
     - Update pyproject.toml
   - Skills needed: bmad-tea-testarch-test-design
   - Deliverable: 3/3 tests passing

3. **Day 1 - End: Checkpoint 1**
   - 15/53 tests fixed (28% complete)
   - Group 3 (Position Sizing) ready to start

### Phase 3-B: Features (Days 2-3) - ~4 hours
**Focus:** Dashboard panels and risk constraints

1. **Day 2 - Morning (2 hours)**
   - Group 3: Position Sizing Constraint (1 test)
     - Debug allocation enforcement
     - Fix constraint validation
   - Skills needed: bmad-tea-testarch-test-design
   - Deliverable: 1/1 tests passing

2. **Day 2-3 - Full (2 hours)**
   - Group 2: Dashboard Panel tests (19 tests)
     - Fix DashboardPosition/PositionPanel (7 tests)
     - Fix DashboardMetrics/RiskPanel (7 tests)
     - Fix PerformancePanel (5 tests)
   - Skills needed: bmad-tea-testarch-test-design
   - Deliverable: 19/19 tests passing

3. **Day 3 - End: Checkpoint 2**
   - 35/53 tests fixed (66% complete)
   - All core trading/dashboard functionality working

### Phase 3-C: Infrastructure (Days 4-7) - ~4 hours
**Focus:** CI/CD, setup, and documentation

1. **Day 4-5: Story Acceptance Tests**
   - Group 6: Infrastructure & security (21 tests)
     - Create missing documentation
     - Configure GitHub API fixtures
     - Setup pre-commit hooks
     - Configure security scanning
   - Skills needed: bmad-tea-testarch-test-design, bmad-bmm-qa-automate
   - Deliverable: 21/21 tests passing

2. **Day 6-7: Validation & Polish**
   - Full test suite run
   - Fix any integration issues
   - Performance validation
   - Memory cleanup

3. **End: Checkpoint 3**
   - **53/53 tests fixed (100% complete)**
   - All Phase 3 deferral tests resolved
   - Ready for production deployment

---

## Dependency Graph

```
Phase 3-A Foundation (15 tests)
├─ Group 1: Callback Manager (11) ──── prerequisite for Group 2
├─ Group 4: Imports & Deps (2) ──────── independent
└─ Group 5: Build Config (1) ───────── independent

Phase 3-B Features (20 tests)
├─ Group 3: Position Sizing (1) ──── independent
└─ Group 2: Dashboard Panels (19) ── depends on Group 1

Phase 3-C Infrastructure (21 tests)
└─ Group 6: Story Tests (21) ──── independent (can run parallel)

Critical Path: Group 1 → Group 2 → Full validation
Optional Path: Group 6 (CI/Infrastructure) can run in parallel with others
```

---

## Risk Assessment

### High Risk Items
1. **Group 2: Dashboard Panels** - Large test count, complex dependencies
   - Mitigation: Break into subgroups, test incrementally
   - Contingency: Extra 1-2 hours if interface refactoring needed

2. **Group 6: Story Acceptance** - Environment/fixture setup complexity
   - Mitigation: Use mock fixtures if GitHub API unavailable
   - Contingency: Document mock setup for CI

### Medium Risk Items
1. **Group 1: Callback Manager** - Event object standardization
   - Mitigation: Use namedtuple or dataclass for Event
   - Contingency: Update all consumers of event data

### Low Risk Items
1. Groups 3, 4, 5 - Single or simple tests
   - Should resolve quickly

---

## Success Criteria

### Per Group
- **Group 1:** All 11 callback tests passing, event emissions work reliably
- **Group 2:** All 19 panel tests passing, dashboard renders without errors
- **Group 3:** Position allocation constraints enforced correctly
- **Group 4:** KellyCriterion calculations valid, GitHub Actions validated
- **Group 5:** Poetry build backend recognized
- **Group 6:** All documentation exists, GitHub API fixtures working

### Overall
- ✓ 53/53 tests passing (100%)
- ✓ Test coverage > 90%
- ✓ No integration failures
- ✓ No performance regressions
- ✓ All documentation complete
- ✓ CI/CD pipeline green

---

## BMAD Skills Required

### Per Group
| Group | BMAD Workflow | Expected Duration |
|-------|---------------|-------------------|
| 1 | bmad-tea-testarch-test-design | 2-3 hours |
| 2 | bmad-tea-testarch-test-design | 3-4 hours |
| 3 | bmad-tea-testarch-test-design | 1-2 hours |
| 4 | bmad-tea-testarch-test-design | 1-2 hours |
| 5 | bmad-tea-testarch-test-design | 0.5 hours |
| 6 | bmad-tea-testarch-test-design + bmad-bmm-qa-automate | 3-4 hours |

### Recommended Approach
Use **bmad-tea-testarch-test-design** workflow for test-driven fixes:
1. Understand test requirements
2. Analyze failures systematically
3. Fix implementation to match test expectations
4. Validate with complete test suite

---

## Quick Reference: Test Locations

```
src/tests/
├── test_dashboard_callbacks.py ────── Group 1 (11 tests)
├── test_dashboard_panels.py ───────── Group 2 (19 tests)
├── test_fr001_position_sizing_integration.py - Group 3 (1 test)
├── test_conditions_imports.py ──────── Group 4 (1 test)
├── test_github_actions.py ─────────── Group 4 (1 test)
├── test_poetry.py ────────────────── Group 5 (1 test)
├── test_story_0_1_acceptance.py ────── Group 6A (8 tests)
├── test_story_0_2_acceptance.py ────── Group 6B (6 tests)
└── test_story_0_sec_acceptance.py ─── Group 6C (7 tests)
```

---

## Document History

| Date | Version | Status | Notes |
|------|---------|--------|-------|
| 2026-03-01 | 1.0 | Draft | Initial Phase 3 roadmap created |

---

## Next Steps

1. **Immediate (Today):**
   - Review this roadmap with team
   - Prioritize groups (recommended: 1→2→3→4→5→6)
   - Identify BMAD skill leads

2. **Start Phase 3-A (Day 1):**
   - Begin Group 1 (Callback Manager tests)
   - Use PHASE-3-QUICK-START.md for first 5 tests
   - Track progress in PHASE-3-IMPLEMENTATION-CHECKLIST.md

3. **Weekly Checkpoints:**
   - Day 2 Checkpoint: 15+ tests passing
   - Day 4 Checkpoint: 35+ tests passing
   - Day 7 Checkpoint: 53+ tests passing

---

**End of Phase 3 Test Roadmap**
