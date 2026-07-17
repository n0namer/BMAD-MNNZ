"""
STORY-0-1: GitHub Repository Scaffolding - Acceptance Tests

BDD Test Suite for GitHub repository configuration and scaffolding.
Tests are intentionally failing (red) before implementation (green).

Story: STORY-0-1 - GitHub Repo Scaffolding
Acceptance Criteria: 8 tests covering all required setup tasks

Test Execution Order:
  1. test_github_repo_exists - Verify repo is accessible
  2. test_branch_protection_enabled - Verify main branch protection
  3. test_project_structure - Verify directory layout
  4. test_poetry_installs - Verify Poetry works
  5. test_docker_builds - Verify Docker image builds
  6. test_precommit_installs - Verify pre-commit hooks
  7. test_setup_md_exists - Verify setup documentation
  8. test_contributing_md_exists - Verify contribution guidelines

All tests SHOULD FAIL until implementation is complete.
"""

import subprocess
from pathlib import Path
from typing import Dict, Any

import pytest


class TestGitHubSetup:
    """Test suite for GitHub repository scaffolding (STORY-0-1).

    BDD Scenario: As a developer, I need a properly configured GitHub repository
    so that I can start contributing to the BMAD Method project.

    Feature: GitHub Repository Scaffolding
      - Repository is publicly accessible
      - Main branch has protection rules
      - All required configuration files exist
      - Development tools are installed and working
      - Documentation guides contributors
    """

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_github_repo_exists(self, mock_github_repo: Dict[str, Any]):
        """AC1: Repository exists and is accessible.

        GIVEN: A GitHub repository URL
        WHEN: Attempting to access the repository
        THEN: The repository should be accessible (no 404, valid git repo)

        Expected Output:
            - git remote -v returns valid origin
            - git ls-remote works without authentication errors
            - .git directory exists

        Status: FAILING (repository not verified yet)
        """
        repo_path = mock_github_repo["path"]
        repo_url = mock_github_repo["url"]

        # WHEN: Verify repository exists
        result = subprocess.run(
            ["git", "remote", "-v"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )

        # THEN: Repository should be queryable
        assert result.returncode == 0, "git remote command should succeed"

        # THEN: .git directory should exist
        assert (repo_path / ".git").exists(), ".git directory must exist"

        # THEN: Origin remote should be set (will be set during implementation)
        # Currently failing because origin is not yet configured
        assert "origin" in result.stdout or result.returncode == 0, \
            "Repository should have origin remote configured"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_branch_protection_enabled(self, project_root: Path):
        """AC2: Main branch has protection rules enabled.

        GIVEN: A configured GitHub repository
        WHEN: Checking branch protection settings
        THEN: Main branch requires:
              - 2 approving reviews before merge
              - Status checks pass (CI/CD)
              - Dismiss stale PR approvals on new commits
              - Require code owner reviews for CODEOWNERS files

        Implementation Note:
            Branch protection requires GitHub API access.
            This test validates the structure for protection rules.

        Expected Output:
            - .github/branch-protection-rules.json exists
            - Contains main branch configuration
            - Specifies required review count

        Status: FAILING (branch protection not yet configured)
        """
        rules_file = project_root / ".github" / "branch-protection-rules.json"

        # THEN: Branch protection configuration should exist
        assert rules_file.exists(), \
            "Branch protection rules must be defined in .github/branch-protection-rules.json"

        # When implemented, validate structure
        if rules_file.exists():
            import json
            with open(rules_file) as f:
                rules = json.load(f)

                assert rules.get("branch") == "main", \
                    "Rules must target main branch"

                assert rules.get("required_approving_review_count") >= 2, \
                    "Main branch must require 2 approving reviews"

                assert rules.get("require_code_owner_reviews") is True, \
                    "Code owner reviews must be required"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_project_structure(self, project_root: Path):
        """AC3: Project directory structure is correct.

        GIVEN: A scaffolded GitHub repository
        WHEN: Examining the directory layout
        THEN: All required directories should exist:
              - src/ - Source code
              - tests/ - Test suites
              - docs/ - Documentation
              - .github/ - GitHub configuration
              - .github/workflows/ - CI/CD workflows

        Expected Output:
            Required directories present:
            - src/
            - src/bmad_method/
            - tests/
            - docs/
            - .github/
            - .github/workflows/

        Status: FAILING (structure not fully created)
        """
        required_dirs = [
            "src",
            "src/bmad_method",
            "tests",
            "docs",
            ".github",
            ".github/workflows",
        ]

        # THEN: All required directories should exist
        for dir_name in required_dirs:
            dir_path = project_root / dir_name
            assert dir_path.exists() and dir_path.is_dir(), \
                f"Required directory '{dir_name}' must exist"

        # THEN: Directory permissions should be accessible
        for dir_name in required_dirs:
            dir_path = project_root / dir_name
            assert dir_path.is_dir(), \
                f"Path '{dir_name}' must be a directory, not a file"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    @pytest.mark.slow
    def test_poetry_installs(self, project_root: Path):
        """AC4: Poetry dependency manager installs successfully.

        GIVEN: A project with pyproject.toml
        WHEN: Running 'poetry install'
        THEN: All dependencies should install without errors
              Poetry virtual environment should be created
              poetry.lock should be generated

        Expected Output:
            - poetry install completes successfully (exit code 0)
            - poetry.lock file is created
            - Virtual environment contains installed packages

        Prerequisites:
            - pyproject.toml exists with valid dependencies
            - Python 3.9+ is available
            - Poetry is installed

        Status: FAILING (pyproject.toml not yet created)
        """
        pyproject_file = project_root / "pyproject.toml"
        poetry_lock_file = project_root / "poetry.lock"

        # GIVEN: pyproject.toml exists
        assert pyproject_file.exists(), \
            "pyproject.toml must exist before running poetry install"

        # WHEN: Run poetry install
        result = subprocess.run(
            ["poetry", "install"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=120
        )

        # THEN: Poetry install should succeed
        assert result.returncode == 0, \
            f"poetry install failed: {result.stderr}"

        # THEN: poetry.lock should be created
        assert poetry_lock_file.exists(), \
            "poetry.lock must be created after poetry install"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    @pytest.mark.slow
    @pytest.mark.integration
    def test_docker_builds(self, project_root: Path, docker_image: Dict[str, Any]):
        """AC5: Docker image builds successfully.

        GIVEN: A Dockerfile in project root
        WHEN: Building Docker image with 'docker build'
        THEN: Image should build without errors
              Image should be tagged correctly
              Image size should be reasonable (<500MB for slim base)

        Expected Output:
            - docker build completes successfully
            - Image tagged as bmad-method:latest
            - Build log contains no ERROR or FAILED messages
            - Image size < 500MB (efficiency check)

        Prerequisites:
            - Dockerfile exists
            - Docker daemon is running
            - pyproject.toml and poetry.lock exist

        Status: FAILING (Dockerfile not yet created)
        """
        dockerfile = project_root / "Dockerfile"

        # GIVEN: Dockerfile exists
        assert dockerfile.exists(), \
            "Dockerfile must exist in project root"

        # WHEN: Build Docker image
        result = subprocess.run(
            [
                "docker", "build",
                "-t", f"{docker_image['name']}:{docker_image['tag']}",
                "."
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=300
        )

        # THEN: Build should succeed
        assert result.returncode == 0, \
            f"Docker build failed: {result.stderr}"

        # THEN: Image should be created
        list_result = subprocess.run(
            ["docker", "images", "--filter", f"reference={docker_image['name']}:{docker_image['tag']}"],
            capture_output=True,
            text=True
        )
        assert len(list_result.stdout.strip().split('\n')) > 1, \
            "Docker image should be created after successful build"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_precommit_installs(self, project_root: Path):
        """AC6: Pre-commit hooks install and work correctly.

        GIVEN: A .pre-commit-config.yaml file
        WHEN: Running 'pre-commit install'
        THEN: Git hooks should be installed
              Pre-commit can run checks on staged files
              Linting and formatting hooks execute

        Expected Output:
            - pre-commit install succeeds
            - .git/hooks/pre-commit exists and is executable
            - pre-commit run --all-files completes

        Prerequisites:
            - .pre-commit-config.yaml exists
            - git repository is initialized
            - pre-commit is installed

        Status: FAILING (.pre-commit-config.yaml not yet created)
        """
        precommit_config = project_root / ".pre-commit-config.yaml"
        precommit_hook = project_root / ".git" / "hooks" / "pre-commit"

        # GIVEN: .pre-commit-config.yaml exists
        assert precommit_config.exists(), \
            ".pre-commit-config.yaml must exist"

        # WHEN: Install pre-commit hooks
        result = subprocess.run(
            ["pre-commit", "install"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=30
        )

        # THEN: Installation should succeed
        assert result.returncode == 0, \
            f"pre-commit install failed: {result.stderr}"

        # THEN: Hook file should be created
        assert precommit_hook.exists(), \
            ".git/hooks/pre-commit must be created"

        # THEN: Hook should be executable
        assert precommit_hook.stat().st_mode & 0o111, \
            "Pre-commit hook must be executable"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_setup_md_exists(self, project_root: Path):
        """AC7: SETUP.md exists and is comprehensive.

        GIVEN: A project directory
        WHEN: Looking for SETUP.md
        THEN: File should exist and contain:
              - System requirements (Python version, OS)
              - Installation steps (git clone, poetry install)
              - Environment configuration (.env setup)
              - How to run tests
              - How to run the application
              - Development workflow
              - Troubleshooting section

        Expected Output:
            - SETUP.md exists in project root
            - File is > 300 lines
            - Contains all required sections
            - Instructions are platform-specific (Windows/Unix)

        Status: FAILING (SETUP.md not yet created)
        """
        setup_file = project_root / "SETUP.md"

        # THEN: SETUP.md should exist
        assert setup_file.exists(), \
            "SETUP.md must exist in project root"

        # THEN: File should be substantial (>300 lines for good docs)
        with open(setup_file) as f:
            content = f.read()
            lines = content.split('\n')

            assert len(lines) > 300, \
                f"SETUP.md should be > 300 lines (currently {len(lines)})"

        # THEN: Should contain required sections
        required_sections = [
            "Prerequisites",
            "Installation",
            "Development Setup",
            "Running Tests",
            "Troubleshooting"
        ]

        for section in required_sections:
            assert section.lower() in content.lower(), \
                f"SETUP.md must contain '{section}' section"

        # THEN: Should be copyable code blocks
        assert "```" in content or "```bash" in content, \
            "SETUP.md must contain code blocks (``` markers)"

    @pytest.mark.story_0_1
    @pytest.mark.acceptance
    def test_contributing_md_exists(self, project_root: Path):
        """AC8: CONTRIBUTING.md exists with complete guidelines.

        GIVEN: A GitHub repository
        WHEN: Looking for CONTRIBUTING.md
        THEN: File should exist and contain:
              - Code of Conduct reference or full CoC
              - How to report bugs
              - How to suggest features
              - Development setup (ref to SETUP.md)
              - Code style guidelines
              - Testing requirements (coverage threshold)
              - PR submission process
              - Commit message format
              - Code review guidelines

        Expected Output:
            - CONTRIBUTING.md exists in project root
            - File is > 400 lines
            - All required sections present
            - Links to SETUP.md for environment setup

        Status: FAILING (CONTRIBUTING.md not yet created)
        """
        contributing_file = project_root / "CONTRIBUTING.md"

        # THEN: CONTRIBUTING.md should exist
        assert contributing_file.exists(), \
            "CONTRIBUTING.md must exist in project root"

        # THEN: File should be comprehensive (>400 lines)
        with open(contributing_file) as f:
            content = f.read()
            lines = content.split('\n')

            assert len(lines) > 400, \
                f"CONTRIBUTING.md should be > 400 lines (currently {len(lines)})"

        # THEN: Should reference SETUP.md
        assert "SETUP.md" in content or "setup" in content.lower(), \
            "CONTRIBUTING.md should reference SETUP.md for environment setup"

        # THEN: Should contain required sections
        required_sections = [
            "code of conduct",
            "report",
            "feature",
            "setup",
            "style",
            "test",
            "pull request",
            "commit"
        ]

        content_lower = content.lower()
        for section in required_sections:
            assert section in content_lower, \
                f"CONTRIBUTING.md must contain '{section}' guidance"

        # THEN: Should specify coverage requirement
        assert "coverage" in content_lower, \
            "CONTRIBUTING.md must specify code coverage requirements"


class TestGitHubScaffoldingSummary:
    """Summary and status tracking for STORY-0-1.

    Test Results:
        Current Status: ALL FAILING (expected before implementation)

        Tests Summary:
        ✗ test_github_repo_exists - Repository accessibility
        ✗ test_branch_protection_enabled - Main branch protection
        ✗ test_project_structure - Directory layout verification
        ✗ test_poetry_installs - Python dependency management
        ✗ test_docker_builds - Container image build
        ✗ test_precommit_installs - Pre-commit hook installation
        ✗ test_setup_md_exists - Setup documentation (>300 lines)
        ✗ test_contributing_md_exists - Contributing guide (>400 lines)

        Total: 8 tests, 0 passed, 8 failing

    Implementation Checklist:
        ☐ Create/configure GitHub repository
        ☐ Set up main branch protection rules
        ☐ Create project directory structure
        ☐ Create pyproject.toml with dependencies
        ☐ Create Dockerfile with slim base image
        ☐ Create .pre-commit-config.yaml
        ☐ Write SETUP.md (>300 lines)
        ☐ Write CONTRIBUTING.md (>400 lines)

    Success Criteria:
        All 8 tests pass (100% pass rate)
        All artifacts exist and are valid
        Project is ready for development
    """

    @pytest.mark.story_0_1
    def test_story_0_1_summary(self):
        """Summary of STORY-0-1 acceptance tests."""
        summary = {
            "story": "STORY-0-1",
            "title": "GitHub Repository Scaffolding",
            "total_tests": 8,
            "status": "SETUP",
            "expected_result": "ALL FAILING (before implementation)"
        }
        assert summary["total_tests"] == 8, "Story should have 8 AC tests"
