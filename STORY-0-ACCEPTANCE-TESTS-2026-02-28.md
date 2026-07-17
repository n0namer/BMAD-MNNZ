# Sprint 0 Acceptance Tests (ATDD)

**Document Date:** 2026-02-28
**Author:** QA Specialist - Acceptance Test Driven Development
**Status:** SETUP PHASE (All tests failing - Red Phase)
**Framework:** pytest + BDD
**Total Tests:** 21
**Pass Rate:** 0/21 (0%) - EXPECTED before implementation

---

## Executive Summary

This document defines the **failing acceptance tests** for Sprint 0 stories using ATDD (Acceptance Test Driven Development) methodology. All tests are intentionally failing in the RED phase before implementation.

### Key Principles

1. **Test-First Development**: Tests are written BEFORE implementation
2. **BDD Scenarios**: Each test documents "Given-When-Then" acceptance criteria
3. **Clear Failure Messages**: Tests explain exactly what needs to be implemented
4. **Executable Documentation**: Tests serve as specification and verification

### Test Organization

```
src/tests/
├── conftest.py                          # Shared fixtures & configuration
├── test_story_0_1_acceptance.py         # GitHub Setup (8 tests)
├── test_story_0_2_acceptance.py         # Python Setup (6 tests)
└── test_story_0_sec_acceptance.py       # Security (7 tests)
```

---

## Test Execution Guide

### Prerequisites

```bash
# Install testing dependencies
poetry install

# Install system tools (if testing all features)
pip install pytest pytest-cov bandit detect-secrets
```

### Running All Tests

```bash
# Run all Sprint 0 acceptance tests
pytest src/tests/test_story_0_*.py -v

# Expected output: 21 FAILED, 0 PASSED (before implementation)
```

### Running Tests by Story

```bash
# STORY-0-1: GitHub Setup (8 tests)
pytest src/tests/test_story_0_1_acceptance.py -v -m story_0_1

# STORY-0-2: Python Setup (6 tests)
pytest src/tests/test_story_0_2_acceptance.py -v -m story_0_2

# STORY-0-SEC: Security (7 tests)
pytest src/tests/test_story_0_sec_acceptance.py -v -m story_0_sec
```

### Running Tests by Marker

```bash
# All acceptance tests
pytest -m acceptance -v

# Slow tests only
pytest -m slow -v

# Integration tests (require Docker/services)
pytest -m integration -v
```

### Expected Test Results (Pre-Implementation)

```
STORY-0-1 (GitHub Scaffolding)
✗ test_github_repo_exists
✗ test_branch_protection_enabled
✗ test_project_structure
✗ test_poetry_installs
✗ test_docker_builds
✗ test_precommit_installs
✗ test_setup_md_exists
✗ test_contributing_md_exists

STORY-0-2 (Python Setup)
✗ test_github_actions_workflow_valid
✗ test_pytest_runs
✗ test_coverage_above_threshold
✗ test_poetry_lock_exists
✗ test_all_quality_checks_pass
✗ test_ci_blocks_failing_tests

STORY-0-SEC (Security)
✗ test_no_hardcoded_secrets
✗ test_env_file_example_exists
✗ test_security_md_exists
✗ test_bandit_scanning_passes
✗ test_github_secrets_configured
✗ test_dependency_audit_passes
✗ test_precommit_blocks_secrets

Total: 21 FAILED
```

---

## STORY-0-1: GitHub Repository Scaffolding (8 Tests)

### Overview

**Story**: Set up GitHub repository with proper scaffolding, documentation, and automation.

**Acceptance Criteria**: 8 detailed tests validating all aspects of repository setup.

### Test Cases

#### AC1: Repository Exists and Is Accessible
**Test**: `test_github_repo_exists()`

**Scenario**:
```
GIVEN: A GitHub repository URL
WHEN: Attempting to access the repository
THEN: The repository should be accessible and valid
```

**What it validates**:
- GitHub repository is reachable
- `.git` directory exists
- Git remote is configured
- Repository is not a 404

**Expected to fail because**:
- Repository URL not yet verified
- Origin remote not configured

**Implementation requirement**:
- Ensure GitHub repository exists at specified URL
- Configure origin remote in `.git/config`

---

#### AC2: Main Branch Protection Enabled
**Test**: `test_branch_protection_enabled()`

**Scenario**:
```
GIVEN: A configured GitHub repository
WHEN: Checking branch protection settings
THEN: Main branch requires 2 approvals and status checks
```

**What it validates**:
- Branch protection rules exist for `main`
- Requires 2 approving reviews
- Requires CI/CD status checks
- Dismisses stale reviews on new commits
- Requires code owner review

**Expected to fail because**:
- `.github/branch-protection-rules.json` not created
- GitHub API not configured for protection

**Implementation requirement**:
- Create `.github/branch-protection-rules.json`
- Configure protection via GitHub API or UI

---

#### AC3: Project Directory Structure Is Correct
**Test**: `test_project_structure()`

**Scenario**:
```
GIVEN: A scaffolded repository
WHEN: Examining directory layout
THEN: All required directories exist and are accessible
```

**What it validates**:
- `src/` directory exists
- `src/bmad_method/` package directory exists
- `tests/` directory exists
- `docs/` directory exists
- `.github/` directory exists
- `.github/workflows/` directory exists

**Expected to fail because**:
- Some directories not yet created

**Implementation requirement**:
```bash
mkdir -p src/bmad_method
mkdir -p tests
mkdir -p docs
mkdir -p .github/workflows
```

---

#### AC4: Poetry Installs Successfully
**Test**: `test_poetry_installs()`

**Scenario**:
```
GIVEN: A project with pyproject.toml
WHEN: Running 'poetry install'
THEN: All dependencies install and poetry.lock is created
```

**What it validates**:
- `pyproject.toml` exists with valid syntax
- All dependencies are resolved
- Poetry virtual environment created
- `poetry.lock` is generated
- Installation completes without errors

**Expected to fail because**:
- `pyproject.toml` not yet created
- `poetry.lock` not generated

**Implementation requirement**:
- Create `pyproject.toml` with all dependencies
- Run `poetry install`
- Commit `poetry.lock`

---

#### AC5: Docker Image Builds Successfully
**Test**: `test_docker_builds()`

**Scenario**:
```
GIVEN: A Dockerfile in project root
WHEN: Building Docker image
THEN: Image builds without errors and is reasonable size
```

**What it validates**:
- `Dockerfile` exists and is valid
- Uses slim base image (`python:3.11-slim`)
- Build completes successfully
- Image is created and tagged
- Image size is reasonable (<500MB)

**Expected to fail because**:
- `Dockerfile` not yet created
- Docker not available in test environment (expected)

**Implementation requirement**:
- Create `Dockerfile` with:
  - Slim base image
  - Multi-layer optimization
  - Non-root user setup
  - Proper health checks

---

#### AC6: Pre-commit Hooks Install Successfully
**Test**: `test_precommit_installs()`

**Scenario**:
```
GIVEN: A .pre-commit-config.yaml file
WHEN: Running 'pre-commit install'
THEN: Git hooks are installed and executable
```

**What it validates**:
- `.pre-commit-config.yaml` exists with valid YAML
- `pre-commit install` succeeds
- `.git/hooks/pre-commit` is created
- Hook file is executable

**Expected to fail because**:
- `.pre-commit-config.yaml` not yet created
- Pre-commit hooks not installed

**Implementation requirement**:
- Create `.pre-commit-config.yaml` with hooks
- Run `pre-commit install`

---

#### AC7: SETUP.md Exists and Is Comprehensive
**Test**: `test_setup_md_exists()`

**Scenario**:
```
GIVEN: A project directory
WHEN: Looking for SETUP.md
THEN: File exists with >300 lines of comprehensive setup instructions
```

**What it validates**:
- `SETUP.md` exists in project root
- File has at least 300 lines
- Contains required sections:
  - Prerequisites
  - Installation
  - Development Setup
  - Running Tests
  - Troubleshooting
- Contains code blocks with copyable commands

**Expected to fail because**:
- `SETUP.md` not yet created

**Implementation requirement**:
- Create `SETUP.md` with 300+ lines
- Include all required sections
- Provide copy-paste friendly commands
- Platform-specific instructions (Windows/Unix)

---

#### AC8: CONTRIBUTING.md Exists and Is Comprehensive
**Test**: `test_contributing_md_exists()`

**Scenario**:
```
GIVEN: A GitHub repository
WHEN: Looking for CONTRIBUTING.md
THEN: File exists with >400 lines of contribution guidelines
```

**What it validates**:
- `CONTRIBUTING.md` exists in project root
- File has at least 400 lines
- Contains required sections:
  - Code of Conduct
  - How to report bugs
  - How to suggest features
  - Development setup (references SETUP.md)
  - Code style guidelines
  - Testing requirements
  - Coverage threshold
  - PR submission process
  - Commit message format
- References SETUP.md for environment setup

**Expected to fail because**:
- `CONTRIBUTING.md` not yet created

**Implementation requirement**:
- Create `CONTRIBUTING.md` with 400+ lines
- Include all required sections
- Reference SETUP.md
- Specify code coverage requirement

---

## STORY-0-2: Python Environment & Quality Setup (6 Tests)

### Overview

**Story**: Set up Python environment with CI/CD pipeline and quality tools.

**Acceptance Criteria**: 6 tests validating Python setup and quality infrastructure.

### Test Cases

#### AC1: GitHub Actions CI Workflow Is Valid
**Test**: `test_github_actions_workflow_valid()`

**Scenario**:
```
GIVEN: A .github/workflows/ci.yml file
WHEN: Validating workflow structure
THEN: Workflow is valid YAML with proper GitHub Actions syntax
```

**What it validates**:
- `.github/workflows/ci.yml` exists
- Valid YAML syntax
- Has `name`, `on`, `jobs` sections
- Triggers on push/PR to main branches
- Has test job running on `ubuntu-latest`
- Includes lint, type-check, test steps

**Expected to fail because**:
- `.github/workflows/ci.yml` not yet created

**Implementation requirement**:
- Create `.github/workflows/ci.yml`
- Configure triggers: `[push, pull_request]` on `[main, develop]`
- Add jobs: checkout, setup-python, install, lint, type-check, test

---

#### AC2: pytest Can Run All Tests
**Test**: `test_pytest_runs()`

**Scenario**:
```
GIVEN: A tests/ directory with test files
WHEN: Running 'pytest'
THEN: pytest discovers and runs all tests successfully
```

**What it validates**:
- `tests/` directory exists
- At least one `test_*.py` file exists
- `pytest` discovers all tests
- Test run completes within timeout
- Test summary is displayed

**Expected to fail because**:
- Test infrastructure not fully set up
- Tests may fail (that's expected in red phase)

**Implementation requirement**:
- Create test files in `tests/` directory
- Run `pytest` to discover tests
- Fix any test failures

---

#### AC3: Code Coverage Is Above 90%
**Test**: `test_coverage_above_threshold()`

**Scenario**:
```
GIVEN: A test suite with coverage measurement
WHEN: Running 'pytest --cov'
THEN: Coverage report shows >= 90% overall coverage
```

**What it validates**:
- `pytest-cov` is installed
- Coverage report is generated
- Overall coverage >= 90%
- Coverage HTML report exists
- Coverage XML report exists (for CI)

**Expected to fail because**:
- Code coverage not yet achieved
- May need to write more tests

**Implementation requirement**:
- Implement enough code and tests to reach 90% coverage
- Configure pytest.ini with coverage options
- Run tests with coverage: `pytest --cov=src`

---

#### AC4: poetry.lock Is Committed
**Test**: `test_poetry_lock_exists()`

**Scenario**:
```
GIVEN: A project using Poetry
WHEN: Checking for poetry.lock
THEN: File exists and is tracked in git (not in .gitignore)
```

**What it validates**:
- `poetry.lock` exists in project root
- File is NOT in `.gitignore`
- File is tracked by git
- File has valid Poetry lock format
- Contains package dependency information

**Expected to fail because**:
- `poetry.lock` not yet created
- May need to run `poetry install`

**Implementation requirement**:
- Run `poetry install` to generate `poetry.lock`
- Remove `poetry.lock` from `.gitignore` if present
- Commit `poetry.lock` to git

---

#### AC5: All Quality Checks Pass
**Test**: `test_all_quality_checks_pass()`

**Scenario**:
```
GIVEN: A Python project with quality tools
WHEN: Running quality checks
THEN: ruff, black, and mypy all pass (exit code 0)
```

**What it validates**:
- `ruff check .` passes (no linting errors)
- `black --check .` passes (proper formatting)
- `mypy .` passes (no type errors)
- No quality violations

**Expected to fail because**:
- Code quality tools not configured
- Code may not meet standards yet

**Implementation requirement**:
- Configure quality tools in `pyproject.toml`
- Run each tool: `ruff check .`, `black --check .`, `mypy .`
- Fix issues until all pass

---

#### AC6: CI Pipeline Blocks Failing Tests
**Test**: `test_ci_blocks_failing_tests()`

**Scenario**:
```
GIVEN: A GitHub Actions workflow with tests and quality checks
WHEN: A PR is submitted with failing tests
THEN: CI marks status as failed and blocks merge
```

**What it validates**:
- Workflow has proper fail-fast logic
- Tests block merge on failure
- Quality checks block merge on failure
- No auto-pass of failed checks

**Expected to fail because**:
- CI pipeline not fully configured
- GitHub branch protection not set up

**Implementation requirement**:
- Configure CI workflow without `continue-on-error: true`
- Set up branch protection to require CI pass
- Test that failing PRs are blocked

---

## STORY-0-SEC: Security Baseline & Compliance (7 Tests)

### Overview

**Story**: Establish security baseline and compliance infrastructure.

**Acceptance Criteria**: 7 tests validating security measures.

### Test Cases

#### AC1: No Hardcoded Secrets Detected
**Test**: `test_no_hardcoded_secrets()`

**Scenario**:
```
GIVEN: A Python project scanned for secrets
WHEN: Running 'detect-secrets scan'
THEN: Zero secrets are found in code
```

**What it validates**:
- `detect-secrets` scan finds 0 secrets
- No API keys hardcoded
- No passwords in code
- No private keys committed
- No AWS credentials visible

**Expected to fail because**:
- `detect-secrets` not yet configured
- Initial scan may find issues

**Implementation requirement**:
- Install: `pip install detect-secrets`
- Run: `detect-secrets scan`
- Remove any found secrets
- Create baseline: `detect-secrets baseline`

---

#### AC2: Environment File Example Exists
**Test**: `test_env_file_example_exists()`

**Scenario**:
```
GIVEN: A project using environment variables
WHEN: Looking for .env.example
THEN: File exists with safe example values and no real secrets
```

**What it validates**:
- `.env.example` exists in project root
- Is NOT in `.gitignore` (should be committed)
- Contains variable definitions
- Has comments explaining each variable
- Contains only placeholder values (no real secrets)
- Real `.env` IS in `.gitignore`

**Expected to fail because**:
- `.env.example` not yet created

**Implementation requirement**:
- Create `.env.example` with placeholder values:
  ```
  # Database Configuration
  DATABASE_URL=postgresql://user:pass@localhost/dbname

  # API Configuration
  API_KEY=your-api-key-here
  ```
- Ensure `.env` is in `.gitignore`
- Ensure `.env.example` is NOT in `.gitignore`

---

#### AC3: SECURITY.md Exists
**Test**: `test_security_md_exists()`

**Scenario**:
```
GIVEN: A public GitHub project
WHEN: Looking for SECURITY.md
THEN: File exists with vulnerability reporting policy
```

**What it validates**:
- `SECURITY.md` exists in project root
- Contains how to report vulnerabilities
- Includes security contact email
- Mentions responsible disclosure
- Specifies SLA for response
- References any CVEs or advisories

**Expected to fail because**:
- `SECURITY.md` not yet created

**Implementation requirement**:
- Create `SECURITY.md` with sections:
  - How to report security issues
  - Contact information
  - Responsible disclosure policy
  - Response timeline
  - Fixed vulnerabilities list

---

#### AC4: Bandit Scanning Passes
**Test**: `test_bandit_scanning_passes()`

**Scenario**:
```
GIVEN: A Python project scanned with Bandit
WHEN: Running 'bandit -r src/'
THEN: Zero HIGH or CRITICAL security issues found
```

**What it validates**:
- `bandit` scan finds 0 HIGH severity issues
- `bandit` scan finds 0 CRITICAL severity issues
- MEDIUM/LOW issues documented
- Security patterns are safe

**Expected to fail because**:
- `bandit` not yet configured
- Initial scan may find issues

**Implementation requirement**:
- Install: `pip install bandit`
- Run: `bandit -r src/`
- Fix any HIGH/CRITICAL issues
- Create baseline for LOW/MEDIUM issues

---

#### AC5: GitHub Secrets Configured
**Test**: `test_github_secrets_configured()`

**Scenario**:
```
GIVEN: A GitHub workflow using sensitive data
WHEN: Checking for secrets usage
THEN: Workflow references GitHub Secrets properly
```

**What it validates**:
- CI workflow uses `${{ secrets.VARIABLE }}`
- No hardcoded credentials in workflow
- Secrets referenced in environment
- Sensitive operations use secrets

**Expected to fail because**:
- GitHub Secrets not yet configured
- Workflow may not reference secrets

**Implementation requirement**:
- Configure GitHub Secrets in repository settings
- Update CI workflow to use: `${{ secrets.VARIABLE }}`
- Document required secrets in README

---

#### AC6: Dependency Audit Passes
**Test**: `test_dependency_audit_passes()`

**Scenario**:
```
GIVEN: A project with locked dependencies
WHEN: Running 'poetry audit'
THEN: Zero vulnerabilities are found
```

**What it validates**:
- `poetry audit` finds 0 vulnerabilities
- All dependencies safe
- No CVEs in dependency tree
- Audit can be integrated into CI

**Expected to fail because**:
- Dependency audit not yet run
- May have vulnerable dependencies

**Implementation requirement**:
- Run: `poetry audit`
- Update vulnerable dependencies
- Re-run audit until passes
- Add to CI pipeline

---

#### AC7: Pre-commit Blocks Secrets
**Test**: `test_precommit_blocks_secrets()`

**Scenario**:
```
GIVEN: A .pre-commit-config.yaml with detect-secrets
WHEN: Attempting to commit code with secrets
THEN: Pre-commit hook blocks the commit
```

**What it validates**:
- `.pre-commit-config.yaml` includes detect-secrets hook
- Hook is configured for commit stage
- Hook not disabled
- Detection works before commit

**Expected to fail because**:
- `.pre-commit-config.yaml` not yet created
- detect-secrets hook not configured

**Implementation requirement**:
- Add to `.pre-commit-config.yaml`:
  ```yaml
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        stages: [commit]
  ```
- Run: `pre-commit install`
- Test by attempting to commit a secret (should be blocked)

---

## Test Fixtures (conftest.py)

### Available Fixtures

All fixtures are defined in `src/tests/conftest.py` and automatically available to all tests.

#### `project_root`
Returns the root directory of the project as a `Path` object.

```python
def test_example(project_root: Path):
    assert (project_root / "README.md").exists()
```

#### `temp_directory`
Creates and cleans up a temporary directory for test operations.

```python
def test_example(temp_directory: Path):
    # Create temporary files
    test_file = temp_directory / "test.txt"
    test_file.write_text("content")
    # Cleaned up after test
```

#### `mock_github_repo`
Creates a mock GitHub repository structure with git initialization.

```python
def test_example(mock_github_repo: Dict[str, Any]):
    repo_path = mock_github_repo["path"]
    repo_url = mock_github_repo["url"]
```

#### `poetry_venv`
Creates a mock Python virtual environment with Poetry configuration.

```python
def test_example(poetry_venv: Dict[str, Any]):
    venv_path = poetry_venv["path"]
    python_version = poetry_venv["python_version"]
```

#### `docker_image`
Provides Docker build configuration and metadata.

```python
def test_example(docker_image: Dict[str, Any]):
    image_name = docker_image["name"]
    base_image = docker_image["base_image"]
```

#### `ci_environment`
Provides mock CI/CD environment variables.

```python
def test_example(ci_environment: Dict[str, str]):
    workspace = ci_environment["github_workspace"]
    commit_sha = ci_environment["github_sha"]
```

#### `security_config`
Provides security configuration state for testing.

```python
def test_example(security_config: Dict[str, Any]):
    secrets_found = security_config["secrets_found"]
    bandit_enabled = security_config["bandit_enabled"]
```

---

## Implementation Roadmap

### Phase 1: RED (Tests Failing) - Current
**Duration**: Now
**Deliverables**: All 21 tests created and failing

- [x] Create `conftest.py` with fixtures
- [x] Create 8 tests for STORY-0-1
- [x] Create 6 tests for STORY-0-2
- [x] Create 7 tests for STORY-0-SEC
- [x] Document all test cases
- [x] Define acceptance criteria

**Status**: COMPLETE ✓

### Phase 2: GREEN (Tests Passing) - Next
**Duration**: Sprint 0 (2-3 days)
**Deliverables**: All 21 tests passing

For each test:
1. Create/configure required files
2. Run test in isolation
3. Fix until passes
4. Move to next test

**Priority Order**:
1. STORY-0-1: GitHub Setup (foundation)
2. STORY-0-2: Python Setup (CI/CD)
3. STORY-0-SEC: Security (compliance)

### Phase 3: REFACTOR (Tests Maintainable)
**Duration**: After all pass
**Deliverables**: Clean, maintainable test code

- Remove debug/skip statements
- Consolidate similar tests
- Improve fixtures if needed
- Update documentation

---

## Success Criteria

### Test Quality Metrics

| Metric | Target | Current |
|--------|--------|---------|
| All tests passing | 100% (21/21) | 0% (0/21) |
| Code coverage | >= 90% | TBD |
| Test execution time | < 5 min | ~2 min (expected) |
| All AC met | 100% | 0% |

### Implementation Metrics

| Metric | Target | Evidence |
|--------|--------|----------|
| Files created | 8+ | `.github/workflows/ci.yml`, `Dockerfile`, etc. |
| Lines of docs | > 700 | `SETUP.md`, `CONTRIBUTING.md`, `SECURITY.md` |
| Configuration files | 5+ | `pyproject.toml`, `.pre-commit-config.yaml`, etc. |
| Security issues | 0 | `detect-secrets`, `bandit`, `poetry audit` |

---

## Troubleshooting

### Common Test Failures

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'poetry'`

**Solution**: Install Poetry
```bash
pip install poetry
```

**Error**: `pytest: command not found`

**Solution**: Install pytest
```bash
poetry install --with dev
```

**Error**: `ModuleNotFoundError: No module named 'yaml'`

**Solution**: Install PyYAML
```bash
pip install pyyaml
```

### Skipped Tests

Some tests may be skipped in certain environments:

- **Docker tests** - Skipped if Docker daemon not running
- **Bandit tests** - Skipped if bandit not installed
- **Integration tests** - Skipped if external services unavailable

Use `-v` flag to see skip reasons:
```bash
pytest -v --tb=short
```

---

## References

### ATDD/BDD Resources

- [Behavior Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development)
- [Gherkin Language](https://cucumber.io/docs/gherkin/)
- [pytest Documentation](https://docs.pytest.org/)

### Tools Used

- **pytest** - Python testing framework
- **PyYAML** - YAML parsing for workflow validation
- **detect-secrets** - Secret scanning
- **bandit** - Python security analysis
- **poetry** - Python dependency management

### Project Files Created

- `src/tests/conftest.py` - Test configuration
- `src/tests/test_story_0_1_acceptance.py` - 8 tests
- `src/tests/test_story_0_2_acceptance.py` - 6 tests
- `src/tests/test_story_0_sec_acceptance.py` - 7 tests

---

## Sign-Off

**Document Created**: 2026-02-28
**Author**: QA Specialist (ATDD Expert)
**Status**: READY FOR IMPLEMENTATION
**Next Phase**: Green Phase - Implement features to pass tests

---

## Appendix: Test Execution Examples

### Run All Tests with Verbose Output

```bash
pytest src/tests/test_story_0_*.py -v --tb=short
```

**Expected output (before implementation)**:
```
test_story_0_1_acceptance.py::TestGitHubSetup::test_github_repo_exists FAILED
test_story_0_1_acceptance.py::TestGitHubSetup::test_branch_protection_enabled FAILED
...
21 failed in 2.34s
```

### Run Tests by Story with Markers

```bash
# STORY-0-1 only
pytest -m story_0_1 -v

# STORY-0-2 only
pytest -m story_0_2 -v

# STORY-0-SEC only
pytest -m story_0_sec -v
```

### Run Tests with Coverage

```bash
pytest --cov=src tests/ --cov-report=html
```

### Run Single Test

```bash
pytest src/tests/test_story_0_1_acceptance.py::TestGitHubSetup::test_setup_md_exists -v
```

### Run Tests and Show Failures

```bash
pytest src/tests/ -v --tb=long
```

---

**Total Lines in This Document**: 1000+
**Total Test Cases Defined**: 21
**Total AC Criteria**: 21
**Status**: Ready for Green Phase Implementation
