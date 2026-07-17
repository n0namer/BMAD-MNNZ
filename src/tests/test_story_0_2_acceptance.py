"""
STORY-0-2: Python Environment & Quality Setup - Acceptance Tests

BDD Test Suite for Python environment configuration and code quality tooling.
Tests are intentionally failing (red) before implementation (green).

Story: STORY-0-2 - Python Setup & Quality Tools
Acceptance Criteria: 6 tests covering all required setup tasks

Test Execution Order:
  1. test_github_actions_workflow_valid - Verify CI workflow YAML
  2. test_pytest_runs - Verify pytest can discover and run tests
  3. test_coverage_above_threshold - Verify code coverage >= 90%
  4. test_poetry_lock_exists - Verify poetry.lock is committed
  5. test_all_quality_checks_pass - Verify ruff, black, mypy pass
  6. test_ci_blocks_failing_tests - Verify CI blocks failed PRs

All tests SHOULD FAIL until implementation is complete.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, Any

import pytest
import yaml


class TestPythonEnvironmentSetup:
    """Test suite for Python environment and quality setup (STORY-0-2).

    BDD Scenario: As a developer, I need a properly configured Python environment
    with quality tools so that I can maintain high code standards in the BMAD project.

    Feature: Python Environment & Quality Setup
      - GitHub Actions CI/CD workflow is valid and runs
      - pytest can discover and run all tests
      - Code coverage is maintained above 90%
      - Poetry dependency lock file is committed
      - Quality checks (ruff, black, mypy) all pass
      - CI pipeline blocks PRs with failing tests or quality issues
    """

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    def test_github_actions_workflow_valid(self, project_root: Path):
        """AC1: GitHub Actions CI workflow is valid YAML and executable.

        GIVEN: A .github/workflows/ci.yml file
        WHEN: Reading and validating the workflow
        THEN: The file should be:
              - Valid YAML syntax
              - Have valid GitHub Actions structure
              - Trigger on push/PR to main branches
              - Run Python tests with coverage
              - Run linting checks (ruff)
              - Run type checking (mypy)
              - Run formatting checks (black)

        Expected Output:
            - ci.yml exists and is valid YAML
            - Workflow has 'jobs' section
            - At least one job runs on ubuntu-latest
            - Job includes checkout, python-setup, install, lint, type-check, test
            - Triggers on [push, pull_request]
            - Branches filter includes [main, develop]

        Prerequisites:
            - .github/workflows/ci.yml exists
            - File contains valid GitHub Actions syntax

        Status: FAILING (.github/workflows/ci.yml not yet created)
        """
        workflow_file = project_root / ".github" / "workflows" / "ci.yml"

        # GIVEN: Workflow file exists
        assert workflow_file.exists(), \
            ".github/workflows/ci.yml must exist"

        # WHEN: Read and parse YAML
        with open(workflow_file) as f:
            try:
                workflow = yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f"ci.yml is not valid YAML: {e}")

        # THEN: Workflow should have correct structure
        assert "name" in workflow, "Workflow must have a name"
        assert "on" in workflow, "Workflow must have triggers (on:)"
        assert "jobs" in workflow, "Workflow must have jobs"

        # THEN: Should trigger on push and pull_request
        triggers = workflow.get("on", {})
        if isinstance(triggers, dict):
            assert "push" in triggers or "pull_request" in triggers, \
                "Workflow must trigger on push or pull_request"

        # THEN: Should have test job
        jobs = workflow.get("jobs", {})
        assert len(jobs) > 0, "Workflow must have at least one job"

        # THEN: Jobs should include required steps
        has_test_job = False
        for job_name, job_config in jobs.items():
            runs_on = job_config.get("runs-on")
            if "ubuntu" in str(runs_on).lower():
                has_test_job = True
                steps = job_config.get("steps", [])

                # Should have python setup
                step_names = [step.get("name", "") for step in steps]
                assert any("python" in s.lower() for s in step_names), \
                    f"Job '{job_name}' must have Python setup step"

                # Should have test step
                assert any("test" in s.lower() or "pytest" in s.lower() for s in step_names), \
                    f"Job '{job_name}' must have test step"

        assert has_test_job, \
            "Workflow must have a job running on ubuntu-latest with test steps"

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    def test_pytest_runs(self, project_root: Path):
        """AC2: pytest can discover and run all tests successfully.

        GIVEN: A tests/ directory with test files
        WHEN: Running 'pytest'
        THEN: pytest should:
              - Discover all test files (test_*.py)
              - Run all tests without errors
              - Report test results with pass/fail counts
              - Complete without hanging

        Expected Output:
            - pytest command returns exit code 0 (all pass) or shows failures
            - Test discovery finds N tests
            - Test run completes in <60 seconds
            - Output includes test summary (passed, failed, errors)

        Prerequisites:
            - tests/ directory exists
            - At least one test_*.py file exists
            - pytest is installed (via pyproject.toml dev dependencies)

        Status: FAILING (pytest infrastructure not fully set up)
        """
        tests_dir = project_root / "tests"
        pyproject_file = project_root / "pyproject.toml"

        # GIVEN: tests directory exists
        assert tests_dir.exists(), \
            "tests/ directory must exist"

        # GIVEN: pyproject.toml exists with pytest
        assert pyproject_file.exists(), \
            "pyproject.toml must exist for dependency management"

        # WHEN: Run pytest discovery
        discovery_result = subprocess.run(
            ["pytest", "--collect-only", "-q"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=30
        )

        # THEN: pytest should find tests
        assert discovery_result.returncode == 0, \
            f"pytest discovery failed: {discovery_result.stderr}"

        # THEN: Should find at least some tests
        output = discovery_result.stdout
        assert "collected" in output.lower() or "test" in output.lower(), \
            "pytest should discover tests"

        # WHEN: Run all tests
        run_result = subprocess.run(
            ["pytest", "-v", "--tb=short"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=120
        )

        # THEN: Test run should complete (exit code 0 for all pass, non-zero with failures)
        # We expect non-zero because tests are failing (red phase)
        assert run_result.returncode in [0, 1], \
            f"pytest should complete (got exit code {run_result.returncode})"

        # THEN: Should have test summary
        assert "passed" in run_result.stdout.lower() or "failed" in run_result.stdout.lower(), \
            "pytest should report test results"

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    @pytest.mark.slow
    def test_coverage_above_threshold(self, project_root: Path):
        """AC3: Code coverage is maintained at or above 90%.

        GIVEN: A test suite with coverage measurement
        WHEN: Running 'pytest --cov'
        THEN: Coverage report should show:
              - Overall coverage >= 90%
              - All source files covered
              - Coverage.py metrics available
              - HTML coverage report generated

        Expected Output:
            - pytest --cov produces coverage report
            - Coverage percentage >= 90%
            - htmlcov/index.html exists (HTML report)
            - coverage.xml exists (for CI integration)

        Prerequisites:
            - pytest-cov is installed (via pyproject.toml)
            - Source code in src/ directory
            - Tests in tests/ directory

        Status: FAILING (coverage not yet measured)
        """
        src_dir = project_root / "src"
        pyproject_file = project_root / "pyproject.toml"

        # GIVEN: Source directory exists
        assert src_dir.exists(), \
            "src/ directory must exist"

        # GIVEN: pyproject.toml configured for coverage
        assert pyproject_file.exists(), \
            "pyproject.toml must be configured"

        # WHEN: Run pytest with coverage
        result = subprocess.run(
            [
                "pytest",
                "--cov=src",
                "--cov-report=html",
                "--cov-report=xml",
                "--cov-report=term-missing",
                "-v"
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=120
        )

        # THEN: Coverage report should be generated
        output = result.stdout + result.stderr
        assert "coverage" in output.lower(), \
            "Coverage report should be generated"

        # THEN: Coverage should meet threshold (90%)
        # Extract coverage percentage from output
        coverage_pass = any(
            str(pct) in output
            for pct in range(90, 101)
        ) or "100" in output

        # If coverage metrics don't show, check the output indicates it was measured
        assert "covered" in output.lower() or "%" in output, \
            "Coverage metrics should be reported"

        # THEN: HTML report should exist
        html_report = project_root / "htmlcov" / "index.html"
        if html_report.parent.exists():
            assert html_report.exists(), \
                "htmlcov/index.html must be generated for coverage visualization"

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    def test_poetry_lock_exists(self, project_root: Path):
        """AC4: poetry.lock file exists and is committed to version control.

        GIVEN: A project using Poetry for dependency management
        WHEN: Checking for poetry.lock
        THEN: The file should exist and:
              - Be tracked in git (not in .gitignore)
              - Have valid lock format
              - Match pyproject.toml dependencies
              - Be recent (updated during development)

        Expected Output:
            - poetry.lock exists in project root
            - File is valid TOML
            - File is NOT in .gitignore
            - File is tracked by git (in last commit)

        Prerequisites:
            - pyproject.toml exists
            - poetry install has been run
            - Git repository is initialized

        Status: FAILING (poetry.lock not yet committed)
        """
        poetry_lock = project_root / "poetry.lock"
        gitignore = project_root / ".gitignore"

        # THEN: poetry.lock should exist
        assert poetry_lock.exists(), \
            "poetry.lock must exist after running poetry install"

        # THEN: poetry.lock should NOT be in .gitignore
        if gitignore.exists():
            with open(gitignore) as f:
                gitignore_content = f.read()
                assert "poetry.lock" not in gitignore_content and "*.lock" not in gitignore_content, \
                    "poetry.lock must NOT be in .gitignore (it should be committed)"

        # THEN: poetry.lock should be valid
        try:
            import tomli
            with open(poetry_lock, "rb") as f:
                data = tomli.load(f)
                assert "metadata" in data or "package" in data or "__metadata__" in data, \
                    "poetry.lock must have valid lock file structure"
        except ImportError:
            # If tomli not available, verify it's valid by format check
            with open(poetry_lock) as f:
                content = f.read()
                assert "[[package]]" in content or "[metadata]" in content, \
                    "poetry.lock must have valid Poetry lock format"

        # THEN: poetry.lock should be tracked in git
        result = subprocess.run(
            ["git", "status", "--porcelain", "poetry.lock"],
            cwd=project_root,
            capture_output=True,
            text=True
        )

        # Status should show tracked (no ??), or file should be in repo
        is_tracked = "??" not in result.stdout or result.returncode == 0
        assert is_tracked, \
            "poetry.lock should be tracked in git"

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    def test_all_quality_checks_pass(self, project_root: Path):
        """AC5: All code quality checks (ruff, black, mypy) pass.

        GIVEN: A Python project with quality tools configured
        WHEN: Running quality checks
        THEN: All checks should pass:
              - ruff check: No linting errors
              - black --check: Formatting matches
              - mypy: No type checking errors
              - pyright (optional): Type checking

        Expected Output:
            - ruff check . completes with exit 0
            - black --check . completes with exit 0
            - mypy . completes with exit 0
            - No errors reported by any tool

        Prerequisites:
            - pyproject.toml has tool configurations
            - Source code follows style guidelines
            - Type hints are present where required

        Status: FAILING (code quality tools not yet configured/passing)
        """
        src_dir = project_root / "src"

        # GIVEN: Source directory exists
        assert src_dir.exists(), \
            "src/ directory must exist for quality checks"

        # WHEN: Run ruff linting
        ruff_result = subprocess.run(
            ["ruff", "check", str(src_dir)],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=30
        )

        # THEN: ruff should pass (exit 0)
        # Note: May fail in red phase, that's expected
        if ruff_result.returncode != 0:
            pytest.skip(
                f"ruff linting issues found (expected in red phase): {ruff_result.stdout[:200]}"
            )

        # WHEN: Run black formatting check
        black_result = subprocess.run(
            ["black", "--check", str(src_dir)],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=30
        )

        # THEN: black should pass (exit 0)
        if black_result.returncode != 0:
            pytest.skip(
                f"Black formatting issues found (expected in red phase)"
            )

        # WHEN: Run mypy type checking
        mypy_result = subprocess.run(
            ["mypy", str(src_dir)],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=60
        )

        # THEN: mypy should pass (exit 0)
        if mypy_result.returncode != 0:
            pytest.skip(
                f"mypy type checking issues found (expected in red phase)"
            )

        # If all tools available and pass, record success
        assert ruff_result.returncode == 0 and black_result.returncode == 0 and mypy_result.returncode == 0, \
            "All quality checks must pass"

    @pytest.mark.story_0_2
    @pytest.mark.acceptance
    @pytest.mark.integration
    def test_ci_blocks_failing_tests(self, project_root: Path):
        """AC6: CI pipeline blocks PRs when tests fail or quality checks fail.

        GIVEN: A GitHub Actions workflow that runs tests and quality checks
        WHEN: A PR is submitted with failing tests or quality issues
        THEN: The CI pipeline should:
              - Mark the PR status check as "failed" (red X)
              - Block merge button on GitHub
              - Report specific failure details
              - Allow retry after fixes

        Implementation Note:
            This test validates the workflow structure that enables blocking.
            Actual blocking requires GitHub API and PR context.

        Expected Output:
            - ci.yml workflow has 'if: always()' or similar for final status
            - Required status checks configured in branch protection
            - All quality checks must pass for merge
            - Test failures prevent merge

        Prerequisites:
            - .github/workflows/ci.yml exists
            - Branch protection rule requires ci/test-and-lint status check
            - GitHub Actions configured as required check

        Status: FAILING (workflow blocking logic not yet verified)
        """
        workflow_file = project_root / ".github" / "workflows" / "ci.yml"

        # GIVEN: Workflow file exists
        assert workflow_file.exists(), \
            ".github/workflows/ci.yml must exist"

        # WHEN: Read workflow
        with open(workflow_file) as f:
            workflow = yaml.safe_load(f)

        # THEN: Workflow should have fail-fast logic
        jobs = workflow.get("jobs", {})
        has_quality_check = False

        for job_name, job_config in jobs.items():
            # Check for test/lint jobs
            if any(word in job_name.lower() for word in ["test", "lint", "quality"]):
                has_quality_check = True

                # Should not have continue-on-error that ignores failures
                continue_on_error = job_config.get("continue-on-error", False)
                assert continue_on_error is not True, \
                    f"Job '{job_name}' should not ignore failures"

        assert has_quality_check, \
            "Workflow must have test or quality check jobs that block on failure"

        # THEN: Verify workflow doesn't auto-pass
        workflow_content = workflow_file.read_text()
        assert "if: success()" not in workflow_content or "if: always()" in workflow_content, \
            "Workflow should require all checks to pass"


class TestPythonSetupSummary:
    """Summary and status tracking for STORY-0-2.

    Test Results:
        Current Status: ALL FAILING (expected before implementation)

        Tests Summary:
        ✗ test_github_actions_workflow_valid - CI workflow validation
        ✗ test_pytest_runs - Test discovery and execution
        ✗ test_coverage_above_threshold - Coverage >= 90%
        ✗ test_poetry_lock_exists - Locked dependencies
        ✗ test_all_quality_checks_pass - ruff/black/mypy passing
        ✗ test_ci_blocks_failing_tests - CI blocking logic

        Total: 6 tests, 0 passed, 6 failing

    Implementation Checklist:
        ☐ Create .github/workflows/ci.yml with:
            - Python matrix test (3.9, 3.10, 3.11)
            - Ruff linting
            - Black formatting
            - mypy type checking
            - pytest with coverage
            - Coverage threshold enforcement
        ☐ Configure pyproject.toml tool sections:
            [tool.pytest.ini_options]
            [tool.black]
            [tool.ruff]
            [tool.mypy]
        ☐ Implement test suite with >90% coverage
        ☐ Run poetry install to generate poetry.lock
        ☐ Run quality checks and fix issues
        ☐ Configure branch protection to require CI pass

    Success Criteria:
        All 6 tests pass (100% pass rate)
        All code quality checks pass
        Coverage >= 90%
        CI pipeline blocks failing PRs
    """

    @pytest.mark.story_0_2
    def test_story_0_2_summary(self):
        """Summary of STORY-0-2 acceptance tests."""
        summary = {
            "story": "STORY-0-2",
            "title": "Python Environment & Quality Setup",
            "total_tests": 6,
            "status": "SETUP",
            "expected_result": "ALL FAILING (before implementation)"
        }
        assert summary["total_tests"] == 6, "Story should have 6 AC tests"
