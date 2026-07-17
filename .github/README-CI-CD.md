# Sprint 0 CI/CD Pipeline

**Status:** ✅ COMPLETE - Ready for Deployment
**Date:** 2026-02-28
**Project:** BMAD-MNNZ

---

## Quick Start

This directory contains the GitHub Actions CI/CD pipeline for Sprint 0.

### For First-Time Deployment

1. **Review:** Start with `IMPLEMENTATION-CHECKLIST.md`
2. **Configure:** Follow `BRANCH-PROTECTION-SETUP.md`
3. **Deploy:** Push all files to repository
4. **Test:** Run first workflow and verify

### For Team Members

1. **Understand:** Read `STORY-0-AUTOMATION-REPORT-2026-02-28.md` (main documentation)
2. **Before coding:** Check troubleshooting section if tests fail
3. **Before pushing:** Run local checks:
   ```bash
   poetry run pytest src/tests/ --cov=src
   poetry run ruff check src/
   poetry run mypy --strict src/
   ```

### For Troubleshooting

See the Troubleshooting Guide in `STORY-0-AUTOMATION-REPORT-2026-02-28.md`

---

## Files in This Setup

### Workflows (`.github/workflows/`)
- **test-automation.yml** - Main CI/CD: tests, linting, coverage, security
- **scheduled-checks.yml** - Weekly/daily: dependency audits, security scans

### Configuration
- **quality-gate-config.yaml** - Quality thresholds and branch protection rules

### Documentation
- **STORY-0-AUTOMATION-REPORT-2026-02-28.md** - Complete reference (START HERE)
- **IMPLEMENTATION-CHECKLIST.md** - Deployment steps
- **BRANCH-PROTECTION-SETUP.md** - Branch protection configuration
- **DEPLOYMENT-SUMMARY.txt** - Quick reference
- **README-CI-CD.md** - This file

---

## Pipeline Overview

**Trigger Events:**
- Push to main/develop/feature/* branches
- Pull requests to main/develop
- Manual workflow dispatch
- Scheduled: Weekly (Mon/Wed) + Daily

**Jobs:** 11 total (6 + 5 scheduled)
- Python 3.11, 3.12, 3.13 testing (parallel)
- Coverage enforcement (90% minimum)
- Linting + Type checking + Security scanning
- Weekly dependency audits
- Weekly security audits

**Duration:** ~10 minutes per push/PR

---

## Quality Gates

| Gate | Threshold | Action |
|------|-----------|--------|
| Coverage | 90% | Block merge if lower |
| Linting | 0 warnings | Reported but not blocking |
| Type checking | 0 errors | Reported but not blocking |
| Security | 0 critical | Block merge if violated |
| Dependencies | 0 high | Auto-creates issue if violated |

**Branch Protection:**
- Main: 2 approvals + all checks required
- Develop: 1 approval + key checks required

---

## Key Files to Read

### Complete Understanding
Read: **STORY-0-AUTOMATION-REPORT-2026-02-28.md**
- Full architecture and design
- All 11 jobs explained
- Quality metrics
- Troubleshooting guide (10+ scenarios)
- Future enhancements
- Compliance & standards

### Quick Deployment
Read: **.github/IMPLEMENTATION-CHECKLIST.md**
- Pre-deployment checklist
- Step-by-step deployment (6 steps)
- Customization guide
- Success indicators

### Configure Branch Protection
Read: **.github/BRANCH-PROTECTION-SETUP.md**
- CLI commands (recommended)
- Manual web UI instructions
- Verification procedures
- Testing & troubleshooting

### Fast Reference
Read: **.github/DEPLOYMENT-SUMMARY.txt** or **SPRINT-0-CI-CD-COMPLETE.txt**
- File overview
- Next steps
- Quick setup summary

---

## Workflow Descriptions

### test-automation.yml (Main Pipeline)

**Triggers:** Push (main/develop/feature/*), PR, manual

**Jobs:**
1. **test-matrix** (Python 3.11/3.12/3.13 parallel)
   - Linting (Ruff)
   - Formatting check (Black)
   - Type checking (mypy strict)
   - Unit tests with coverage (pytest)
   - Security scan (Bandit)
   - Dependency audit (Poetry)

2. **quality-gates**
   - Enforces coverage >= 90%
   - Publishes test results

3. **security-checks**
   - Bandit SAST scanning
   - Safety dependency check
   - Semgrep pattern matching
   - Uploads SARIF reports

4. **integration-test**
   - Runs integration test suite

5. **build-check**
   - Validates package build

6. **report-summary**
   - Creates GitHub step summary

**Duration:** ~10 minutes (all parallel)

### scheduled-checks.yml (Automated Checks)

**Jobs:**
1. **dependency-check** - Weekly (Monday 02:00 UTC)
2. **security-audit** - Weekly (Wednesday 03:00 UTC)
3. **performance-baseline** - Daily (01:00 UTC)
4. **license-check** - On-demand
5. **health-check-summary** - Always

---

## Local Development

Before pushing code, run these locally:

```bash
# Install dependencies
poetry install --with dev --with test

# Run tests with coverage
poetry run pytest src/tests/ --cov=src

# Check code quality
poetry run ruff check src/

# Check formatting
poetry run black --check src/

# Check types
poetry run mypy --strict src/

# Security scan
poetry run bandit -r src/
```

If any check fails locally, fix before pushing.

---

## Troubleshooting

### Common Issues

**Coverage below 90%**
- Write more unit tests
- Focus on untested code paths
- Run locally: `poetry run pytest src/tests/ --cov=src`

**Lint/type failures**
- Run locally: `poetry run ruff check src/`
- Run locally: `poetry run mypy --strict src/`
- Fix issues before pushing

**Security vulnerabilities**
- Review Bandit output
- Fix code issues or update dependencies
- Run locally: `poetry run bandit -r src/`

**Build failures**
- Check pyproject.toml syntax
- Ensure all dependencies are declared
- Run locally: `poetry build`

For more details, see Troubleshooting Guide in **STORY-0-AUTOMATION-REPORT-2026-02-28.md**

---

## Next Steps

### For Deployment
1. Read `IMPLEMENTATION-CHECKLIST.md`
2. Stage all files in Git
3. Commit and push to main
4. Configure branch protection
5. Test with first workflow run

### For Team
1. Read `STORY-0-AUTOMATION-REPORT-2026-02-28.md`
2. Understand quality gates
3. Learn troubleshooting procedures
4. Update development workflow

---

## Support

- **Questions?** See `STORY-0-AUTOMATION-REPORT-2026-02-28.md`
- **Setup issues?** See `.github/IMPLEMENTATION-CHECKLIST.md`
- **Branch protection?** See `.github/BRANCH-PROTECTION-SETUP.md`
- **Workflow fails?** See Troubleshooting section in main documentation

---

## Document Index

| Document | Purpose | Size |
|----------|---------|------|
| STORY-0-AUTOMATION-REPORT-2026-02-28.md | Complete documentation | 20 KB |
| IMPLEMENTATION-CHECKLIST.md | Deployment guide | 14 KB |
| BRANCH-PROTECTION-SETUP.md | Branch config guide | 7.7 KB |
| DEPLOYMENT-SUMMARY.txt | Quick reference | 5.5 KB |
| SPRINT-0-CI-CD-COMPLETE.txt | Status summary | 6 KB |
| README-CI-CD.md | This file | - |

---

**Last Updated:** 2026-02-28
**Version:** 1.0
**Status:** Ready for Deployment
