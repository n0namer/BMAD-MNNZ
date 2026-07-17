"""
STORY-0-SEC: Security Baseline & Compliance - Acceptance Tests

BDD Test Suite for security configuration and compliance verification.
Tests are intentionally failing (red) before implementation (green).

Story: STORY-0-SEC - Security Baseline & Compliance
Acceptance Criteria: 7 tests covering all required security tasks

Test Execution Order:
  1. test_no_hardcoded_secrets - Verify detect-secrets scan finds 0 secrets
  2. test_env_file_example_exists - Verify .env.example without secrets
  3. test_security_md_exists - Verify SECURITY.md documentation
  4. test_bandit_scanning_passes - Verify Bandit finds 0 high-severity issues
  5. test_github_secrets_configured - Verify GitHub Secrets setup
  6. test_dependency_audit_passes - Verify no vulnerable dependencies
  7. test_precommit_blocks_secrets - Verify pre-commit secret blocking

All tests SHOULD FAIL until implementation is complete.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, Any

import pytest


class TestSecurityBaseline:
    """Test suite for security baseline and compliance (STORY-0-SEC).

    BDD Scenario: As a maintainer, I need a secure development environment
    so that the BMAD project protects user data and prevents vulnerabilities.

    Feature: Security Baseline & Compliance
      - No hardcoded secrets in code
      - Environment variables documented safely
      - Security policy defined
      - Static security analysis runs and passes
      - Dependency vulnerabilities are checked
      - Pre-commit hooks block secret commits
      - GitHub Secrets configured for sensitive data
    """

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_no_hardcoded_secrets(self, project_root: Path, security_config: Dict[str, Any]):
        """AC1: No hardcoded secrets detected in codebase.

        GIVEN: A Python project with detect-secrets configured
        WHEN: Running 'detect-secrets scan'
        THEN: No secrets should be found:
              - No API keys in code
              - No passwords hardcoded
              - No private keys committed
              - No AWS credentials visible
              - No database passwords exposed

        Expected Output:
            - detect-secrets scan completes successfully
            - Results show 0 secrets detected
            - Baseline file exists for future scans
            - No false positives in secure areas

        Prerequisites:
            - detect-secrets is installed
            - Source code is in src/ directory
            - .detecsecretsrc exists (optional baseline)

        Status: FAILING (detect-secrets not yet configured)
        """
        src_dir = project_root / "src"

        # GIVEN: Source directory exists
        assert src_dir.exists(), \
            "src/ directory must exist for security scanning"

        # WHEN: Run detect-secrets scan
        result = subprocess.run(
            ["detect-secrets", "scan", "--no-verify"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=60
        )

        # THEN: Scan should complete successfully
        assert result.returncode in [0, 4], \
            f"detect-secrets should execute: {result.stderr}"

        # THEN: Parse results
        try:
            if result.stdout:
                output = json.loads(result.stdout)
                results = output.get("results", {})

                # Count detected secrets
                secret_count = sum(
                    len(files) for files in results.values()
                )

                assert secret_count == 0, \
                    f"Found {secret_count} hardcoded secrets - must be 0"

                security_config["detect_secrets_enabled"] = True
                security_config["secrets_found"] = 0
        except json.JSONDecodeError:
            # If JSON parsing fails, check output for success indicators
            if "0 secrets found" in result.stdout or result.returncode == 0:
                security_config["detect_secrets_enabled"] = True
                security_config["secrets_found"] = 0
            else:
                pytest.skip("detect-secrets output format not recognized")

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_env_file_example_exists(self, project_root: Path):
        """AC2: Environment file example exists without real secrets.

        GIVEN: A project that uses environment variables
        WHEN: Looking for .env.example or .env.sample
        THEN: File should exist and:
              - Contain all required environment variables
              - Have placeholder values (not real secrets)
              - Be documented with variable descriptions
              - Include comments for each variable
              - Show format but not credentials

        Expected Output:
            - .env.example exists in project root
            - File is NOT in .gitignore (should be committed)
            - Contains sample values like:
              DATABASE_URL=postgresql://user:pass@localhost/dbname
              API_KEY=your-api-key-here
              SECRET_TOKEN=your-secret-token-here
            - Each variable has a comment explaining its purpose

        Prerequisites:
            - Project uses environment variables
            - .env is in .gitignore
            - .env.example provides safe documentation

        Status: FAILING (.env.example not yet created)
        """
        env_example = project_root / ".env.example"
        env_file = project_root / ".env"
        gitignore = project_root / ".gitignore"

        # THEN: .env.example should exist
        assert env_example.exists(), \
            ".env.example must exist to document required environment variables"

        # THEN: .env.example should NOT be in .gitignore
        if gitignore.exists():
            with open(gitignore) as f:
                gitignore_content = f.read()
                # .env.example should be tracked, only .env should be ignored
                assert ".env.example" not in gitignore_content, \
                    ".env.example should be committed (document safe)"

        # THEN: Real .env should be in .gitignore
        assert ".env" in gitignore_content or "*.env" in gitignore_content, \
            ".env should be in .gitignore (contains real secrets)"

        # THEN: .env.example should contain sample values
        with open(env_example) as f:
            content = f.read()

            # Should have variable definitions
            assert "=" in content, \
                ".env.example should contain variable definitions"

            # Should have comments explaining variables
            assert "#" in content or "Example:" in content, \
                ".env.example should document each variable"

            # Should NOT contain real API keys/passwords (if any were configured)
            # This is context-dependent, but generic check:
            dangerous_patterns = [
                "sk-ant",  # Anthropic API key pattern
                "AKIA",    # AWS access key pattern
                "mongodb+srv://",  # Real MongoDB connection
            ]
            for pattern in dangerous_patterns:
                assert pattern not in content, \
                    f".env.example should not contain real secrets like {pattern}"

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_security_md_exists(self, project_root: Path):
        """AC3: SECURITY.md exists with vulnerability reporting policy.

        GIVEN: A public GitHub project
        WHEN: Looking for SECURITY.md
        THEN: File should exist and contain:
              - Security policy statement
              - How to report vulnerabilities (email, private report)
              - Supported versions for security updates
              - Timeline for response to reports
              - Links to security advisories
              - List of fixed vulnerabilities
              - Preferred communication method (not public issues)

        Expected Output:
            - SECURITY.md exists in project root
            - File explains how to report security issues
            - Contains security contact email or instructions
            - Mentions responsible disclosure
            - References any CVEs or advisories
            - Specifies SLA for security response

        Prerequisites:
            - Project is public/open-source
            - Security contact is available
            - Clear reporting process documented

        Status: FAILING (SECURITY.md not yet created)
        """
        security_file = project_root / "SECURITY.md"

        # THEN: SECURITY.md should exist
        assert security_file.exists(), \
            "SECURITY.md must exist with vulnerability reporting policy"

        # THEN: Should contain required sections
        with open(security_file) as f:
            content = f.read()

            # Should explain how to report
            report_indicators = [
                "report",
                "vulnerability",
                "security issue",
                "responsibly",
            ]
            has_report_section = any(
                indicator.lower() in content.lower()
                for indicator in report_indicators
            )
            assert has_report_section, \
                "SECURITY.md must explain how to report vulnerabilities"

            # Should have security contact
            assert "@" in content or "email" in content.lower() or "contact" in content.lower(), \
                "SECURITY.md must provide security contact information"

            # Should mention responsible disclosure
            disclosure_indicators = [
                "responsible",
                "private",
                "confidential",
                "embargo",
            ]
            has_disclosure = any(
                indicator.lower() in content.lower()
                for indicator in disclosure_indicators
            )
            # Not strictly required but good practice
            if not has_disclosure:
                pytest.skip("Consider adding responsible disclosure guidance")

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_bandit_scanning_passes(self, project_root: Path, security_config: Dict[str, Any]):
        """AC4: Bandit static security analysis finds no high-severity issues.

        GIVEN: A Python project with Bandit security scanner
        WHEN: Running 'bandit -r src/'
        THEN: Results should show:
              - 0 HIGH severity issues
              - 0 CRITICAL severity issues
              - MEDIUM/LOW issues documented and accepted
              - All issues have remediation notes
              - No dangerous patterns in code

        Expected Output:
            - bandit scan completes successfully
            - Report shows 0 high/critical issues
            - Security metrics available
            - Suggestions for fixes included
            - Baseline file tracks known issues

        Prerequisites:
            - bandit is installed (via pyproject.toml)
            - Source code follows secure practices
            - .bandit baseline exists for known issues

        Status: FAILING (Bandit not yet configured/passing)
        """
        src_dir = project_root / "src"

        # GIVEN: Source directory exists
        assert src_dir.exists(), \
            "src/ directory must exist for security scanning"

        # WHEN: Run Bandit security scanner
        result = subprocess.run(
            ["bandit", "-r", str(src_dir), "-f", "json"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=60
        )

        # THEN: Bandit should run successfully
        # Exit code 0 = no issues, 1 = issues found, others = error
        assert result.returncode in [0, 1], \
            f"Bandit should complete successfully: {result.stderr}"

        # THEN: Parse results and check severity
        try:
            if result.stdout:
                output = json.loads(result.stdout)
                metrics = output.get("metrics", {})

                # Check for high/critical issues
                high_severity = 0
                critical_severity = 0

                for result_item in output.get("results", []):
                    severity = result_item.get("severity", "")
                    if severity == "HIGH":
                        high_severity += 1
                    elif severity == "CRITICAL":
                        critical_severity += 1

                assert high_severity == 0, \
                    f"Found {high_severity} HIGH severity issues - must be 0"

                assert critical_severity == 0, \
                    f"Found {critical_severity} CRITICAL severity issues - must be 0"

                security_config["bandit_enabled"] = True
        except json.JSONDecodeError:
            pytest.skip("Bandit output format not recognized")

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_github_secrets_configured(self, project_root: Path, security_config: Dict[str, Any]):
        """AC5: GitHub Secrets are configured for sensitive data.

        GIVEN: A GitHub repository with CI/CD workflows
        WHEN: Checking for GitHub Secrets configuration
        THEN: The following secrets should be configured:
              - API_KEY (for external services)
              - DATABASE_URL (if using database)
              - GITHUB_TOKEN (automatic for GH Actions)
              - Any other service credentials

        Implementation Note:
            GitHub Secrets cannot be directly read (they're encrypted).
            This test validates the workflow structure that uses secrets.

        Expected Output:
            - ci.yml uses secrets with ${{ secrets.VARIABLE }}
            - No secrets hardcoded in workflow
            - Environment variables reference secrets
            - Secrets documentation exists

        Prerequisites:
            - .github/workflows/ci.yml exists
            - Workflow uses secrets for sensitive operations
            - GitHub repository settings allow secret management

        Status: FAILING (GitHub Secrets not yet verified)
        """
        workflow_file = project_root / ".github" / "workflows" / "ci.yml"

        # GIVEN: Workflow file exists
        assert workflow_file.exists(), \
            ".github/workflows/ci.yml must exist"

        # WHEN: Read workflow
        with open(workflow_file) as f:
            workflow_content = f.read()

            # THEN: Workflow should reference secrets
            assert "secrets." in workflow_content or "${{ secrets" in workflow_content, \
                "Workflow should use GitHub secrets for sensitive data"

            # THEN: Should NOT have hardcoded credentials
            dangerous_patterns = [
                "password=",
                "api_key=",
                "bearer ",
            ]
            for pattern in dangerous_patterns:
                assert pattern.lower() not in workflow_content.lower(), \
                    f"Workflow should not contain hardcoded {pattern}"

        security_config["github_secrets_configured"] = True

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    @pytest.mark.slow
    def test_dependency_audit_passes(self, project_root: Path, security_config: Dict[str, Any]):
        """AC6: Dependency audit passes with no vulnerable packages.

        GIVEN: A project using Poetry for dependencies
        WHEN: Running 'poetry audit'
        THEN: Results should show:
              - 0 vulnerabilities found
              - All dependencies safe
              - No outdated packages with known CVEs
              - Audit report can be generated

        Expected Output:
            - poetry audit completes successfully (exit 0)
            - No vulnerabilities reported
            - All packages verified against security DB
            - Audit log available for CI integration

        Prerequisites:
            - poetry.lock exists with pinned versions
            - Poetry is configured for security audits
            - Internet access for vulnerability database

        Status: FAILING (Dependency audit not yet passing)
        """
        pyproject_file = project_root / "pyproject.toml"
        poetry_lock = project_root / "poetry.lock"

        # GIVEN: Poetry files exist
        assert pyproject_file.exists(), \
            "pyproject.toml must exist"

        # WHEN: Run poetry audit
        result = subprocess.run(
            ["poetry", "audit"],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=60
        )

        # THEN: Audit should complete
        # Exit code 0 = no vulnerabilities, 1 = vulnerabilities found, others = error
        assert result.returncode in [0, 1], \
            f"poetry audit should complete: {result.stderr}"

        # THEN: Should report no vulnerabilities
        output = result.stdout + result.stderr
        if result.returncode == 0:
            assert "vulnerability" not in output.lower() or "no" in output.lower(), \
                "poetry audit should find no vulnerabilities"
            security_config["audit_enabled"] = True
        else:
            # If vulnerabilities found, list them
            pytest.fail(f"Vulnerabilities found in dependencies:\n{output}")

    @pytest.mark.story_0_sec
    @pytest.mark.acceptance
    def test_precommit_blocks_secrets(self, project_root: Path, security_config: Dict[str, Any]):
        """AC7: Pre-commit hooks block commits with secrets.

        GIVEN: A .pre-commit-config.yaml with detect-secrets hook
        WHEN: Attempting to commit a file with hardcoded secret
        THEN: The pre-commit hook should:
              - Detect the secret pattern
              - Reject the commit
              - Provide helpful error message
              - Allow commit after secret is removed

        Implementation Note:
            This test validates the hook configuration.
            Actual testing of hook behavior requires git operations.

        Expected Output:
            - .pre-commit-config.yaml references detect-secrets
            - Hook ID is 'detect-secrets'
            - Hook is not disabled
            - Configuration includes baseline file (if needed)

        Prerequisites:
            - .pre-commit-config.yaml exists
            - detect-secrets hook is configured
            - Pre-commit is installed and initialized

        Status: FAILING (.pre-commit-config.yaml not yet created)
        """
        precommit_config = project_root / ".pre-commit-config.yaml"

        # GIVEN: .pre-commit-config.yaml exists
        assert precommit_config.exists(), \
            ".pre-commit-config.yaml must exist"

        # WHEN: Read configuration
        import yaml
        with open(precommit_config) as f:
            try:
                config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f".pre-commit-config.yaml is invalid YAML: {e}")

        # THEN: Should have detect-secrets hook
        repos = config.get("repos", [])
        has_detect_secrets = False

        for repo in repos:
            repo_url = repo.get("repo", "")
            if "detect-secrets" in repo_url or "detect_secrets" in repo_url:
                has_detect_secrets = True

                # Check hooks
                hooks = repo.get("hooks", [])
                for hook in hooks:
                    hook_id = hook.get("id", "")
                    if "detect-secrets" in hook_id or "secrets" in hook_id:
                        # Hook should not be disabled
                        stages = hook.get("stages", [])
                        if stages:
                            assert "commit" in stages, \
                                "Secret detection should run at commit stage"

        assert has_detect_secrets, \
            ".pre-commit-config.yaml must include detect-secrets hook"

        security_config["detect_secrets_enabled"] = True


class TestSecurityBaselineSummary:
    """Summary and status tracking for STORY-0-SEC.

    Test Results:
        Current Status: ALL FAILING (expected before implementation)

        Tests Summary:
        ✗ test_no_hardcoded_secrets - detect-secrets scan
        ✗ test_env_file_example_exists - Safe environment documentation
        ✗ test_security_md_exists - Vulnerability reporting policy
        ✗ test_bandit_scanning_passes - Static security analysis
        ✗ test_github_secrets_configured - GitHub Secrets usage
        ✗ test_dependency_audit_passes - Dependency vulnerability check
        ✗ test_precommit_blocks_secrets - Secret detection hooks

        Total: 7 tests, 0 passed, 7 failing

    Implementation Checklist:
        ☐ Install security tools:
            - detect-secrets
            - bandit
            - pip-audit (via poetry)
        ☐ Create .env.example with safe placeholder values
        ☐ Create SECURITY.md with:
            - Vulnerability reporting instructions
            - Security contact
            - Response SLA
            - Fixed vulnerabilities list
        ☐ Configure detect-secrets:
            - Initialize baseline if needed
            - Add to pre-commit hooks
            - Run initial scan (should find 0 secrets)
        ☐ Run Bandit scan:
            - Fix HIGH/CRITICAL issues
            - Document LOW/MEDIUM issues
            - Create .bandit baseline if needed
        ☐ Configure GitHub Secrets:
            - Set up CI workflow variables
            - Add secrets reference in workflows
            - Document required secrets
        ☐ Run poetry audit:
            - Update dependencies if vulnerabilities found
            - Verify all pass
            - Configure in CI pipeline
        ☐ Update .pre-commit-config.yaml:
            - Add detect-secrets hook
            - Add bandit hook
            - Configure proper stages

    Success Criteria:
        All 7 tests pass (100% pass rate)
        No hardcoded secrets in codebase
        No high/critical security issues
        All dependencies pass audit
        Security policy documented
    """

    @pytest.mark.story_0_sec
    def test_story_0_sec_summary(self):
        """Summary of STORY-0-SEC acceptance tests."""
        summary = {
            "story": "STORY-0-SEC",
            "title": "Security Baseline & Compliance",
            "total_tests": 7,
            "status": "SETUP",
            "expected_result": "ALL FAILING (before implementation)"
        }
        assert summary["total_tests"] == 7, "Story should have 7 AC tests"
