# Sprint 0 ATDD - Complete Index & Quick Reference

**Date**: 2026-02-28
**Status**: SETUP COMPLETE
**Total Tests**: 24 (21 AC tests + 3 summary tests)
**Pass Rate**: 0/21 (100% failing, as expected in RED phase)

---

## Quick Navigation

### Documentation Files (Where to Start)

| File | Purpose | Lines | Read Time |
|------|---------|-------|-----------|
| **STORY-0-ACCEPTANCE-TESTS-2026-02-28.md** | Main ATDD documentation with all test specs | 1,022 | 30 min |
| **ATDD-SETUP-SUMMARY.md** | Executive summary of setup | 400 | 10 min |
| **ATDD-INDEX.md** | This file - quick reference | 200 | 5 min |

### Test Files (In src/tests/)

| File | Purpose | Tests | Lines | Type |
|------|---------|-------|-------|------|
| **conftest.py** | Pytest fixtures & configuration | 7 fixtures | 200+ | Support |
| **test_story_0_1_acceptance.py** | GitHub scaffolding tests | 8 AC + 1 summary | 500+ | Acceptance |
| **test_story_0_2_acceptance.py** | Python setup tests | 6 AC + 1 summary | 600+ | Acceptance |
| **test_story_0_sec_acceptance.py** | Security baseline tests | 7 AC + 1 summary | 700+ | Acceptance |

---

## Test Structure at a Glance

### STORY-0-1: GitHub Repository Scaffolding (8 tests)

```
TestGitHubSetup
├── test_github_repo_exists
│   └── Validates repository accessibility
├── test_branch_protection_enabled
│   └── Validates main branch protection rules
├── test_project_structure
│   └── Validates directory layout (src/, tests/, docs/, .github/)
├── test_poetry_installs
│   └── Validates Poetry installation and poetry.lock creation
├── test_docker_builds
│   └── Validates Docker image building
├── test_precommit_installs
│   └── Validates pre-commit hook installation
├── test_setup_md_exists
│   └── Validates SETUP.md (>300 lines)
└── test_contributing_md_exists
    └── Validates CONTRIBUTING.md (>400 lines)
```

**Focus**: Foundation (repository, tools, documentation)
**Estimated Implementation Time**: 4-6 hours
**Priority**: P0 (must complete first)

---

### STORY-0-2: Python Environment & Quality Setup (6 tests)

```
TestPythonEnvironmentSetup
├── test_github_actions_workflow_valid
│   └── Validates .github/workflows/ci.yml structure
├── test_pytest_runs
│   └── Validates pytest can discover and run tests
├── test_coverage_above_threshold
│   └── Validates coverage >= 90%
├── test_poetry_lock_exists
│   └── Validates poetry.lock is committed
├── test_all_quality_checks_pass
│   └── Validates ruff, black, mypy all pass
└── test_ci_blocks_failing_tests
    └── Validates CI pipeline blocks failures
```

**Focus**: Quality assurance (CI/CD, testing, code quality)
**Estimated Implementation Time**: 6-8 hours
**Priority**: P0 (must complete after P0-1)
**Dependencies**: STORY-0-1

---

### STORY-0-SEC: Security Baseline & Compliance (7 tests)

```
TestSecurityBaseline
├── test_no_hardcoded_secrets
│   └── Validates detect-secrets finds 0 secrets
├── test_env_file_example_exists
│   └── Validates .env.example with safe values
├── test_security_md_exists
│   └── Validates SECURITY.md documentation
├── test_bandit_scanning_passes
│   └── Validates Bandit finds 0 HIGH/CRITICAL issues
├── test_github_secrets_configured
│   └── Validates GitHub Secrets usage in workflows
├── test_dependency_audit_passes
│   └── Validates poetry audit finds 0 vulnerabilities
└── test_precommit_blocks_secrets
    └── Validates detect-secrets hook blocks commits
```

**Focus**: Security and compliance
**Estimated Implementation Time**: 3-4 hours
**Priority**: P1 (can be done in parallel with P0-2)
**Dependencies**: STORY-0-1

---

## Fixtures Reference

### Available Fixtures (from conftest.py)

```python
@pytest.fixture(scope="session")
def project_root() -> Path:
    """Get project root directory"""

@pytest.fixture
def temp_directory() -> Path:
    """Create temporary directory with auto-cleanup"""

@pytest.fixture
def mock_github_repo() -> Dict[str, Any]:
    """Create mock GitHub repo structure"""

@pytest.fixture
def poetry_venv() -> Dict[str, Any]:
    """Create mock Python virtual environment"""

@pytest.fixture
def docker_image() -> Dict[str, Any]:
    """Provide Docker configuration"""

@pytest.fixture
def ci_environment() -> Dict[str, str]:
    """Provide CI environment variables"""

@pytest.fixture
def security_config() -> Dict[str, Any]:
    """Provide security configuration state"""

@pytest.fixture(autouse=True)
def cleanup_test_files(project_root: Path):
    """Auto-cleanup test artifacts"""
```

### Using Fixtures in Tests

```python
def test_example(project_root: Path, temp_directory: Path):
    """Fixtures are automatically injected by pytest"""
    assert (project_root / "README.md").exists()
    test_file = temp_directory / "test.txt"
```

---

## Running Tests

### All Tests
```bash
pytest src/tests/test_story_0_*.py -v
```

**Expected**: 21 FAILED, 0 PASSED (RED phase)

### By Story
```bash
pytest src/tests/test_story_0_1_acceptance.py -v    # 8 tests
pytest src/tests/test_story_0_2_acceptance.py -v    # 6 tests
pytest src/tests/test_story_0_sec_acceptance.py -v  # 7 tests
```

### By Marker
```bash
pytest -m story_0_1 -v          # STORY-0-1 only
pytest -m story_0_2 -v          # STORY-0-2 only
pytest -m story_0_sec -v        # STORY-0-SEC only
pytest -m acceptance -v         # All acceptance tests
pytest -m integration -v        # Integration tests only
pytest -m slow -v               # Slow tests only
```

### Single Test
```bash
pytest src/tests/test_story_0_1_acceptance.py::TestGitHubSetup::test_setup_md_exists -v
```

### With Verbose Output
```bash
pytest src/tests/test_story_0_*.py -v --tb=short
```

### With Coverage
```bash
pytest src/tests/ --cov=src --cov-report=html --cov-report=term
```

---

## Test Execution Markers

### Available Markers

```python
@pytest.mark.story_0_1      # STORY-0-1 tests (8)
@pytest.mark.story_0_2      # STORY-0-2 tests (6)
@pytest.mark.story_0_sec    # STORY-0-SEC tests (7)
@pytest.mark.acceptance     # All acceptance tests (21)
@pytest.mark.integration    # Integration tests (4)
@pytest.mark.slow           # Slow tests (5)
```

### Marker Statistics

| Marker | Count | Examples |
|--------|-------|----------|
| story_0_1 | 8 | GitHub setup tests |
| story_0_2 | 6 | Python setup tests |
| story_0_sec | 7 | Security tests |
| acceptance | 21 | All AC tests |
| integration | 4 | Docker, bandit, poetry audit |
| slow | 5 | Docker build, poetry install, etc. |

---

## Test Execution Flow

### Pre-Implementation (RED Phase)
```
Run Tests → All Fail → Read Error Messages → Understand Requirements
```

### During Implementation (GREEN Phase)
```
Implement Feature → Run Test → Pass? → Yes → Next Feature / No → Debug & Fix
```

### Post-Implementation (REFACTOR Phase)
```
All Tests Pass → Clean Up Code → Remove Debug Statements → Optimize
```

### Continuous Integration
```
Commit Code → CI Runs Tests → All Pass? → Merge / No → Review & Fix
```

---

## Test Statistics

### Test Count Breakdown

| Category | Count |
|----------|-------|
| Story 0-1 Tests | 8 |
| Story 0-2 Tests | 6 |
| Story 0-SEC Tests | 7 |
| Summary Tests | 3 |
| **Total** | **24** |

### Test Type Breakdown

| Type | Count |
|------|-------|
| Acceptance Tests (AC) | 21 |
| Summary Tests | 3 |
| Integration Tests | 4 |
| Unit Tests | 0 (by design - ATDD focuses on acceptance) |

### Estimated Execution Time

| Test Type | Time |
|-----------|------|
| Fast tests (< 1s) | 12 tests |
| Medium tests (1-5s) | 6 tests |
| Slow tests (> 5s) | 6 tests |
| **Total** | ~2-3 minutes |

---

## Implementation Priority Matrix

### Critical Path (Must Do)

```
STORY-0-1 ─────────────────────┐
                                ├─→ STORY-0-2 ──────────┐
                                                          ├─→ Sprint 0 Complete
STORY-0-SEC ─────────────────────────────────────────────┘
```

### Priority Levels

| Priority | Story | Reason |
|----------|-------|--------|
| P0 | STORY-0-1 | Foundation - all others depend on it |
| P0 | STORY-0-2 | CI/CD infrastructure - needed before merge |
| P1 | STORY-0-SEC | Security - important but can be in parallel |

---

## Success Criteria

### Test Phase Criteria

| Criterion | Target | Current | Status |
|-----------|--------|---------|--------|
| Tests Written | 21 | 21 | ✓ Complete |
| Tests Failing | 21 | 21 | ✓ Expected |
| Documentation | Complete | Complete | ✓ Complete |
| Fixtures | Working | Working | ✓ Complete |
| Markers | Configured | Configured | ✓ Complete |

### Implementation Phase Criteria (GREEN)

| Criterion | Target | Current |
|-----------|--------|---------|
| All tests passing | 21/21 | 0/21 |
| Code coverage | >= 90% | TBD |
| Quality checks | Pass | TBD |
| Security scan | 0 issues | TBD |
| Documentation | Complete | TBD |

---

## Quick Command Reference

```bash
# Initialize pytest environment
cd /d/Users/NIKITA/Documents/DEV/BMAD-MNNZ

# Run all tests
pytest src/tests/test_story_0_*.py -v

# Run STORY-0-1 only
pytest src/tests/test_story_0_1_acceptance.py -v

# Run STORY-0-2 only
pytest src/tests/test_story_0_2_acceptance.py -v

# Run STORY-0-SEC only
pytest src/tests/test_story_0_sec_acceptance.py -v

# Run with coverage
pytest src/tests/ --cov=src --cov-report=html

# Run single test
pytest src/tests/test_story_0_1_acceptance.py::TestGitHubSetup::test_setup_md_exists -v

# Collect tests without running
pytest src/tests/test_story_0_*.py --collect-only -q

# Show test markers
pytest src/tests/ --markers | grep story

# Run with verbose output
pytest src/tests/ -vv --tb=long

# Run only fast tests
pytest src/tests/ -m "not slow" -v

# Run only integration tests
pytest src/tests/ -m integration -v
```

---

## File Locations Reference

```
D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\
│
├── Documentation (Top Level)
│   ├── STORY-0-ACCEPTANCE-TESTS-2026-02-28.md    (Main docs - 1,022 lines)
│   ├── ATDD-SETUP-SUMMARY.md                      (Executive summary - 400 lines)
│   └── ATDD-INDEX.md                              (This file - 200 lines)
│
└── src/tests/
    ├── conftest.py                                (Fixtures - 200+ lines)
    ├── test_story_0_1_acceptance.py               (8 AC tests - 500+ lines)
    ├── test_story_0_2_acceptance.py               (6 AC tests - 600+ lines)
    └── test_story_0_sec_acceptance.py             (7 AC tests - 700+ lines)
```

---

## Common Issues & Solutions

### Issue: Tests Not Found
```bash
# Solution: Ensure pytest can find tests
pytest src/tests/ --collect-only
```

### Issue: Fixture Not Found
```bash
# Solution: Ensure conftest.py is in tests directory
ls src/tests/conftest.py
```

### Issue: Unknown Marker Warning
```bash
# Solution: Markers are auto-registered by pytest_configure in conftest.py
# No action needed - warning is harmless
```

### Issue: Import Errors
```bash
# Solution: Add src to Python path
export PYTHONPATH=$PYTHONPATH:src
pytest
```

---

## Key Takeaways

1. **21 Acceptance Tests** - All failing (RED phase)
2. **3 Stories** - GitHub Setup, Python Setup, Security
3. **Comprehensive Docs** - 1,000+ lines of specification
4. **Reusable Fixtures** - 7 fixtures for test support
5. **Ready for Implementation** - Tests document exactly what needs to be built

---

## Next Steps

1. Review `STORY-0-ACCEPTANCE-TESTS-2026-02-28.md` for detailed specs
2. Run tests: `pytest src/tests/test_story_0_*.py -v`
3. Start with STORY-0-1 (foundational)
4. Implement features to make tests pass
5. Move to STORY-0-2 when 0-1 is complete
6. Run STORY-0-SEC in parallel with other work

---

**ATDD Setup Status**: ✓ COMPLETE

All tests ready for implementation.
RED phase in progress.
GREEN phase to begin on 2026-02-28 or later.

---

**Quick Links**
- [Full Test Documentation](./STORY-0-ACCEPTANCE-TESTS-2026-02-28.md)
- [Setup Summary](./ATDD-SETUP-SUMMARY.md)
- [Test Code](./src/tests/test_story_0_*.py)
