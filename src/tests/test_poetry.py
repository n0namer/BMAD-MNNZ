"""Tests for Poetry project setup."""

import subprocess
from pathlib import Path
from typing import Any, Dict

import pytest
import tomllib


class TestPoetrySetup:
    """Test suite for Poetry configuration and dependencies."""

    @pytest.fixture
    def project_root(self) -> Path:
        """Get the project root directory."""
        return Path(__file__).parent.parent.parent

    @pytest.fixture
    def pyproject_path(self, project_root: Path) -> Path:
        """Get the pyproject.toml file path."""
        return project_root / "pyproject.toml"

    @pytest.fixture
    def poetry_lock_path(self, project_root: Path) -> Path:
        """Get the poetry.lock file path."""
        return project_root / "poetry.lock"

    @pytest.fixture
    def pyproject_content(self, pyproject_path: Path) -> Dict[str, Any]:
        """Load and parse pyproject.toml."""
        with open(pyproject_path, "rb") as f:
            return tomllib.load(f)

    def test_pyproject_file_exists(self, pyproject_path: Path) -> None:
        """Test that pyproject.toml exists in project root."""
        assert pyproject_path.exists(), "pyproject.toml not found in project root"

    def test_poetry_lock_file_exists(self, poetry_lock_path: Path) -> None:
        """Test that poetry.lock exists in project root."""
        assert poetry_lock_path.exists(), (
            "poetry.lock not found in project root. "
            "Run 'poetry lock' to generate it."
        )

    def test_pyproject_has_required_sections(
        self, pyproject_content: Dict[str, Any]
    ) -> None:
        """Test that pyproject.toml has required sections."""
        required_sections = ["tool", "build-system"]
        for section in required_sections:
            assert section in pyproject_content, (
                f"pyproject.toml must have [{section}] section"
            )

    def test_poetry_section_exists(self, pyproject_content: Dict[str, Any]) -> None:
        """Test that [tool.poetry] section exists."""
        assert "tool" in pyproject_content, "pyproject.toml must have [tool] section"
        assert "poetry" in pyproject_content["tool"], (
            "pyproject.toml must have [tool.poetry] section"
        )

    def test_python_version_constraint(
        self, pyproject_content: Dict[str, Any]
    ) -> None:
        """Test that Python version is constrained to 3.11+."""
        poetry_config = pyproject_content["tool"]["poetry"]
        assert "dependencies" in poetry_config, "Poetry config must have dependencies"

        python_version = poetry_config["dependencies"].get("python")
        assert python_version is not None, "Python version must be specified"

        # Check that it requires Python 3.11 or higher
        assert (
            "^3.11" in python_version or "^3.12" in python_version
        ), f"Python version must be ^3.11 or higher, got: {python_version}"

    def test_all_dependencies_are_pinned(
        self, pyproject_content: Dict[str, Any]
    ) -> None:
        """Test that all dependencies have version constraints."""
        poetry_config = pyproject_content["tool"]["poetry"]
        dependencies = poetry_config.get("dependencies", {})

        # Filter out python itself
        dep_list = {k: v for k, v in dependencies.items() if k != "python"}

        for dep_name, version in dep_list.items():
            assert version is not None, f"Dependency {dep_name} must have a version"

            # Check for version constraint symbols
            version_str = str(version)
            valid_constraints = [
                "^",  # Caret: compatible versions
                "~",  # Tilde: approximately equal
                "==",  # Exact
                ">=",  # Greater than or equal
                "<=",  # Less than or equal
                "*",  # Any version
            ]
            assert any(
                constraint in version_str for constraint in valid_constraints
            ), f"Dependency {dep_name} version '{version}' lacks proper constraint"

    def test_pytest_dependency_present(self, pyproject_content: Dict[str, Any]) -> None:
        """Test that pytest is listed as a dependency."""
        poetry_config = pyproject_content["tool"]["poetry"]
        dependencies = poetry_config.get("dependencies", {})

        assert "pytest" in dependencies, "pytest must be listed in dependencies"

    def test_pytest_cov_dependency_present(
        self, pyproject_content: Dict[str, Any]
    ) -> None:
        """Test that pytest-cov is listed as a dependency."""
        poetry_config = pyproject_content["tool"]["poetry"]
        dependencies = poetry_config.get("dependencies", {})

        assert "pytest-cov" in dependencies, "pytest-cov must be listed in dependencies"

    def test_code_quality_tools_present(
        self, pyproject_content: Dict[str, Any]
    ) -> None:
        """Test that code quality tools are listed as dependencies."""
        poetry_config = pyproject_content["tool"]["poetry"]
        dependencies = poetry_config.get("dependencies", {})

        required_tools = ["black", "ruff", "mypy"]
        for tool in required_tools:
            assert tool in dependencies, f"{tool} must be listed in dependencies"

    def test_build_system_configured(self, pyproject_content: Dict[str, Any]) -> None:
        """Test that build system is properly configured for Poetry."""
        build_system = pyproject_content.get("build-system", {})
        assert "requires" in build_system, "build-system must have 'requires'"
        assert "build-backend" in build_system, "build-system must have 'build-backend'"

        assert (
            "poetry-core" in build_system["build-backend"]
        ), "Must use poetry-core as build backend"

    def test_poetry_config_file_is_valid_toml(self, pyproject_path: Path) -> None:
        """Test that pyproject.toml is valid TOML."""
        try:
            with open(pyproject_path, "rb") as f:
                tomllib.load(f)
        except Exception as e:
            pytest.fail(f"pyproject.toml is not valid TOML: {e}")

    def test_poetry_lock_file_format(self, poetry_lock_path: Path) -> None:
        """Test that poetry.lock has valid format."""
        with open(poetry_lock_path, "r", encoding="utf-8") as f:
            content = f.read()

        # poetry.lock should have metadata section
        assert "[metadata]" in content, "poetry.lock must have [metadata] section"

        # Should have at least some packages
        assert "[package" in content, "poetry.lock must have package sections"

        # Should have lock file version
        assert "lock-version" in content, "poetry.lock should have lock-version"
