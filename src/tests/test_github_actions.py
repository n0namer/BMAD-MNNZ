"""Tests for GitHub Actions CI/CD configuration."""

import json
import re
from pathlib import Path
from typing import Any, Dict

import pytest
import yaml


class TestGitHubActionsWorkflow:
    """Test suite for GitHub Actions workflow configuration."""

    @pytest.fixture
    def workflow_path(self) -> Path:
        """Get the GitHub Actions workflow file path."""
        return Path(__file__).parent.parent.parent / ".github" / "workflows" / "ci.yml"

    @pytest.fixture
    def workflow_content(self, workflow_path: Path) -> Dict[str, Any]:
        """Load and parse the GitHub Actions workflow YAML."""
        with open(workflow_path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def test_workflow_file_exists(self, workflow_path: Path) -> None:
        """Test that GitHub Actions workflow file exists."""
        assert workflow_path.exists(), f"Workflow file not found at {workflow_path}"
        assert workflow_path.suffix == ".yml", "Workflow file should be YAML"

    def test_workflow_yaml_is_valid(self, workflow_content: Dict[str, Any]) -> None:
        """Test that workflow YAML is syntactically valid."""
        assert isinstance(workflow_content, dict), "Workflow must be valid YAML"
        assert "jobs" in workflow_content, "Workflow must define jobs"

    def test_workflow_has_required_jobs(self, workflow_content: Dict[str, Any]) -> None:
        """Test that all required jobs are present in the workflow."""
        required_jobs = {"setup", "lint", "format", "type-check", "test", "coverage"}
        actual_jobs = set(workflow_content["jobs"].keys())

        missing_jobs = required_jobs - actual_jobs
        assert (
            not missing_jobs
        ), f"Workflow is missing required jobs: {missing_jobs}"

        for job_name in required_jobs:
            assert (
                job_name in workflow_content["jobs"]
            ), f"Job '{job_name}' not found in workflow"

    def test_setup_job_configuration(self, workflow_content: Dict[str, Any]) -> None:
        """Test that setup job is properly configured."""
        setup_job = workflow_content["jobs"]["setup"]

        assert "runs-on" in setup_job, "Setup job must specify runner"
        assert setup_job["runs-on"] == "ubuntu-latest"

        assert "steps" in setup_job, "Setup job must have steps"
        step_names = [step.get("name") for step in setup_job["steps"]]

        assert any(
            "checkout" in name.lower() for name in step_names
        ), "Setup job must checkout code"
        assert any(
            "python" in name.lower() for name in step_names
        ), "Setup job must set up Python"
        assert any(
            "poetry" in name.lower() for name in step_names
        ), "Setup job must install Poetry"
        assert any(
            "dependencies" in name.lower() for name in step_names
        ), "Setup job must install dependencies"

    def test_lint_job_uses_ruff(self, workflow_content: Dict[str, Any]) -> None:
        """Test that lint job uses ruff without auto-fix."""
        lint_job = workflow_content["jobs"]["lint"]
        steps_str = json.dumps(lint_job["steps"])

        assert "ruff" in steps_str.lower(), "Lint job must use ruff"
        assert "ruff check" in steps_str, "Ruff should use 'check' (no auto-fix)"

    def test_format_job_uses_black(self, workflow_content: Dict[str, Any]) -> None:
        """Test that format job checks with black."""
        format_job = workflow_content["jobs"]["format"]
        steps_str = json.dumps(format_job["steps"])

        assert "black" in steps_str.lower(), "Format job must use black"
        assert "--check" in steps_str, "Black must use --check flag"

    def test_type_check_job_uses_mypy(self, workflow_content: Dict[str, Any]) -> None:
        """Test that type check job uses mypy with strict mode."""
        type_check_job = workflow_content["jobs"]["type-check"]
        steps_str = json.dumps(type_check_job["steps"])

        assert "mypy" in steps_str.lower(), "Type check job must use mypy"

    def test_test_job_matrix_includes_python_versions(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that test job runs on multiple Python versions."""
        test_job = workflow_content["jobs"]["test"]
        assert "strategy" in test_job, "Test job must have strategy"
        assert "matrix" in test_job["strategy"], "Test job must use matrix"

        matrix = test_job["strategy"]["matrix"]
        assert (
            "python-version" in matrix
        ), "Matrix must include python-version"

        python_versions = matrix["python-version"]
        assert "3.11" in python_versions, "Must test on Python 3.11"
        assert "3.12" in python_versions, "Must test on Python 3.12"

    def test_test_job_runs_pytest_with_coverage(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that test job runs pytest with coverage."""
        test_job = workflow_content["jobs"]["test"]
        steps_str = json.dumps(test_job["steps"])

        assert "pytest" in steps_str.lower(), "Test job must use pytest"
        assert "--cov" in steps_str, "Pytest must include coverage"
        assert "--cov-report=xml" in steps_str, "Coverage report must be XML"

    def test_coverage_job_enforces_threshold(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that coverage job enforces 90% threshold."""
        coverage_job = workflow_content["jobs"]["coverage"]
        steps_str = json.dumps(coverage_job["steps"])

        assert "pytest" in steps_str.lower(), "Coverage job must run pytest"
        assert (
            "cov-fail-under=90" in steps_str or "--cov-fail-under 90" in steps_str
        ), "Coverage threshold must be 90%"

    def test_workflow_triggers_on_push_and_pr(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that workflow triggers on push and pull request."""
        assert "on" in workflow_content, "Workflow must define triggers"
        triggers = workflow_content["on"]

        assert "push" in triggers, "Workflow must trigger on push"
        assert "pull_request" in triggers, "Workflow must trigger on pull_request"

        push_trigger = triggers["push"]
        assert "branches" in push_trigger, "Push trigger must specify branches"
        branches = push_trigger["branches"]
        assert "main" in branches, "Must trigger on main branch"
        assert "develop" in branches or "development" in branches, (
            "Must trigger on develop/development branch"
        )

    def test_workflow_enforces_python_311_minimum(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that workflow enforces Python 3.11+ requirement."""
        test_job = workflow_content["jobs"]["test"]
        matrix = test_job["strategy"]["matrix"]
        python_versions = matrix["python-version"]

        for version in python_versions:
            version_float = float(version)
            assert version_float >= 3.11, f"Python {version} is below 3.11 requirement"

    def test_workflow_uploads_coverage_artifacts(
        self, workflow_content: Dict[str, Any]
    ) -> None:
        """Test that workflow uploads coverage artifacts."""
        test_job = workflow_content["jobs"]["test"]
        steps_str = json.dumps(test_job["steps"])

        assert (
            "codecov" in steps_str.lower() or "upload" in steps_str.lower()
        ), "Workflow should upload coverage artifacts"
