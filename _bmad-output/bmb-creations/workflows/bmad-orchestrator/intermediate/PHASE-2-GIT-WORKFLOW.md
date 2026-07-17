# Phase 2 Git Workflow & Branch Structure
**Document**: PHASE-2-GIT-WORKFLOW.md
**Created**: 2026-02-26
**Status**: IMPLEMENTATION PLAN (Ready for Execution)
**Purpose**: Define branch structure, merge strategy, and CI/CD gating for Phase 2

---

## Executive Summary

This document defines the complete git branch structure for Phase 2 implementation using an **atomic, non-blocking approach**. All feature branches are **independent** (no circular dependencies) and can proceed in parallel without blocking each other.

**Key Statistics**:
- **12 feature/development branches** created from main
- **1 integration branch** (phase-2-implementation) for staged merging
- **Zero circular dependencies** - all branches are orthogonal
- **Parallel execution capable** - teams work independently
- **Atomic merge units** - each branch is self-contained

---

## Branch Naming Conventions

### Pattern: `{branch-type}/{blocker-or-feature}-{short-description}`

### Branch Type Categories

| Type | Purpose | Merge Strategy | CI/CD Gate |
|------|---------|---|---|
| `feature/*` | Feature development for blockers | Squash | Build + Unit Tests + Security Scan |
| `develop/*` | Infrastructure/schema development | Merge Commit | Build + Integration Tests + Contracts |
| `phase-*` | Integration branches for phases | Merge Commit | Full Pipeline (Build + Test + Deploy to Staging) |

### Naming Examples

**Feature Branches (Blocker-specific)**:
- `feature/blocker-1-state-machine` → BLOCKER-1: Implement state machine
- `feature/blocker-2-journal-schema` → BLOCKER-2: Design journal schema
- `feature/blocker-3-telemetry` → BLOCKER-3: Implement telemetry system
- `feature/blocker-4-compare` → BLOCKER-4: Build comparison engine
- `feature/blocker-5-audit` → BLOCKER-5: Create audit trail system

**Feature Branches (UI-specific)**:
- `feature/ui-strategy-lifecycle` → Frontend Team 1: Strategy lifecycle UI
- `feature/ui-telemetry-dashboard` → Frontend Team 2: Telemetry dashboard
- `feature/ui-compare-workflow` → Frontend Team 3: Comparison workflow UI

**Development Branches (Infrastructure)**:
- `develop/database-schema` → Database schema and migrations
- `develop/api-gateway` → API infrastructure and routing
- `develop/testing-framework` → Test infrastructure and utilities

---

## Branch Hierarchy & Parent Chain

```
main (PRIMARY TRUNK)
│
├─── phase-2-implementation (INTEGRATION POINT)
│    │
│    ├─── feature/blocker-1-state-machine
│    ├─── feature/blocker-2-journal-schema
│    ├─── feature/blocker-3-telemetry
│    ├─── feature/blocker-4-compare
│    ├─── feature/blocker-5-audit
│    ├─── feature/ui-strategy-lifecycle
│    ├─── feature/ui-telemetry-dashboard
│    ├─── feature/ui-compare-workflow
│    ├─── develop/database-schema
│    ├─── develop/api-gateway
│    └─── develop/testing-framework
```

**Key Points**:
- All 12 feature/develop branches branch FROM main (or phase-2-implementation)
- NO inter-branch dependencies
- Teams can merge independently WITHOUT waiting for other teams
- phase-2-implementation serves as **optional integration point** (not required for individual team progress)

---

## Merge Strategy

### Per-Branch Type

#### Feature Branches (feature/*)
```
Merge Strategy: SQUASH
Rationale: Keep main/phase-2-implementation clean with logical commits per feature
Command: git merge --squash <branch-name>
Result: One commit per feature on main (reduces noise)
```

**Process**:
1. Developer completes feature on `feature/*`
2. Create Pull Request → main or phase-2-implementation
3. Code review + CI/CD gate pass
4. Merge with `--squash`
5. Delete branch

#### Development Branches (develop/*)
```
Merge Strategy: MERGE COMMIT (--no-ff)
Rationale: Preserve full history of infrastructure changes for audit
Command: git merge --no-ff <branch-name>
Result: Merge commit visible in log (maintain context)
```

**Process**:
1. Infrastructure team completes work on `develop/*`
2. Create Pull Request with detailed description
3. Integration tests + contract tests + security scan pass
4. Merge with `--no-ff` to preserve commit history
5. Delete branch

#### Phase Integration Branch (phase-*)
```
Merge Strategy: MERGE COMMIT (--no-ff)
Rationale: Preserve when each team integrated with phase-2
Command: git merge --no-ff <branch-name>
Result: Clear phase history and team contributions
```

**Process**:
1. Teams complete feature/develop branches
2. Create PRs from feature/* and develop/* to phase-2-implementation
3. All CI/CD gates pass
4. Merge with `--no-ff`
5. Eventually merge phase-2-implementation → main with single commit

---

## CI/CD Gating Rules

### Universal Gates (All Branches)
- [x] Build succeeds (`npm run build`)
- [x] No TypeScript errors
- [x] Linting passes (`npm run lint`)
- [x] Unit tests pass with >80% coverage

### Feature Branch Gates (feature/*)
- [x] Build + Linting + Unit Tests (above)
- [x] Security scan (OWASP/npm audit)
- [x] No new critical vulnerabilities
- [x] Code review approval (1 reviewer minimum)
- [x] Status checks on PR: `status/all-checks-passed`

### Development Branch Gates (develop/*)
- [x] Build + Linting + Unit Tests (above)
- [x] Integration tests pass
- [x] Contract tests pass (API/Database)
- [x] Security scan (infrastructure-specific)
- [x] Code review approval (2 reviewers minimum)
- [x] Database migration validation (if schema changes)
- [x] Status checks: `status/integration-complete`

### Phase Integration Gates (phase-*)
- [x] All dependent branches have passed their gates
- [x] Full end-to-end test suite passes
- [x] No conflicts (auto-resolved or manual approval)
- [x] Code review approval (2+ senior reviewers)
- [x] Staging deployment succeeds
- [x] Status checks: `status/phase-ready`

---

## Code Review Requirements

### Feature Branches (feature/*)
- **Minimum reviewers**: 1
- **Review focuses**:
  - Code quality and readability
  - Alignment with BLOCKER requirements
  - No breaking changes to APIs
  - Test coverage adequate for feature
- **Timeline**: 24 hours turnaround SLA
- **Approval required**: Any one reviewer from core team

### Development Branches (develop/*)
- **Minimum reviewers**: 2
- **Required reviewer roles**:
  - [x] At least one infrastructure specialist
  - [x] At least one security engineer (for API/database changes)
- **Review focuses**:
  - Backward compatibility
  - Database migration reversibility
  - API contract stability
  - Security implications
  - Documentation completeness
- **Timeline**: 48 hours turnaround SLA
- **Approval required**: BOTH reviewers from specialist pool

### Phase Integration (phase-*)
- **Minimum reviewers**: 2+
- **Required approvers**: At least one tech lead
- **Sign-off required**: Phase owner or project lead
- **Final checks**:
  - All dependent work verified
  - No regressions in staging
  - Performance baseline met
  - Documentation complete
- **Timeline**: 3 day SLA (includes testing)

---

## Independence Verification Matrix

### Blocker Teams (Cross-Check Dependencies)

| Team | Branch | Depends On | Blocks | Status |
|------|--------|-----------|--------|--------|
| BLOCKER-1 | `feature/blocker-1-state-machine` | `develop/api-gateway` | None | ✓ Independent |
| BLOCKER-2 | `feature/blocker-2-journal-schema` | `develop/database-schema` | None | ✓ Independent |
| BLOCKER-3 | `feature/blocker-3-telemetry` | `develop/api-gateway` | None | ✓ Independent |
| BLOCKER-4 | `feature/blocker-4-compare` | `develop/database-schema` | None | ✓ Independent |
| BLOCKER-5 | `feature/blocker-5-audit` | `develop/database-schema` | None | ✓ Independent |

### Frontend Teams (Cross-Check Dependencies)

| Team | Branch | Depends On | Blocks | Status |
|------|--------|-----------|--------|--------|
| Frontend-1 | `feature/ui-strategy-lifecycle` | `feature/blocker-1-state-machine` | None | ✓ Independent |
| Frontend-2 | `feature/ui-telemetry-dashboard` | `feature/blocker-3-telemetry` | None | ✓ Independent |
| Frontend-3 | `feature/ui-compare-workflow` | `feature/blocker-4-compare` | None | ✓ Independent |

### Infrastructure Teams

| Team | Branch | Depends On | Blocks | Status |
|------|--------|-----------|--------|--------|
| Database | `develop/database-schema` | None | BLOCKER-2, BLOCKER-4, BLOCKER-5 | ✓ Independent |
| API | `develop/api-gateway` | `develop/testing-framework` | BLOCKER-1, BLOCKER-3 | ✓ Independent |
| Testing | `develop/testing-framework` | None | All feature branches | ✓ Independent |

### Dependency Flow (Acyclic Graph - No Circular Dependencies)

```
develop/testing-framework
├─→ develop/api-gateway
│   ├─→ feature/blocker-1-state-machine
│   └─→ feature/blocker-3-telemetry
│
develop/database-schema
├─→ feature/blocker-2-journal-schema
├─→ feature/blocker-4-compare
└─→ feature/blocker-5-audit

feature/blocker-1-state-machine
└─→ feature/ui-strategy-lifecycle

feature/blocker-3-telemetry
└─→ feature/ui-telemetry-dashboard

feature/blocker-4-compare
└─→ feature/ui-compare-workflow
```

**Verification**: All dependencies flow downward. No circular references detected.

---

## How to Handle Circular Dependencies (Mitigation Strategy)

### Prevention

**Rule 1**: If Team A depends on Team B and Team B depends on Team A → **IMMEDIATE ESCALATION**

**Rule 2**: Always verify dependency directionality before creating feature branch

**Rule 3**: Use dependency matrix (section above) as source of truth

### Detection

```bash
# Check for circular deps in your branch plan
# (Manual process - review dependency matrix above)
# If any branch appears both as "depends on" and "blocks", escalate
```

### Resolution (If Circular Dependency Detected)

**Option A: Refactor Interface** (Preferred)
- Break dependency into two independent pieces
- Create shared utility/contract layer
- Both teams consume shared component

**Option B: Sequential Phases**
- Team A completes first (Phase 2A)
- Team B depends on Team A completion (Phase 2B)
- Document clearly in PHASE-2-GIT-BRANCH-STATUS.md

**Option C: Parallel with Mocking**
- Team B mocks Team A's interface
- Team A implements behind mock
- Swap implementation when Team A completes
- Requires careful contract testing

**Escalation Path**:
1. Identify circular dependency (engineering team)
2. Document in issue/ticket with teams involved
3. Escalate to phase owner/tech lead
4. Choose resolution option above
5. Update branch plan and rebase if needed

**Current Status**: No circular dependencies detected in Phase 2 plan ✓

---

## Branch Lifecycle Management

### Creation Phase
```bash
# (DO NOT EXECUTE - This is documentation)
# From main, create branches:
git checkout main
git pull origin main
git checkout -b phase-2-implementation
git checkout -b feature/blocker-1-state-machine
git checkout -b feature/blocker-2-journal-schema
# ... (see GIT-BRANCH-STATUS-2026-02-26.md for full list)

# Push to remote
git push -u origin phase-2-implementation
git push -u origin feature/blocker-1-state-machine
# ... (push all branches)
```

### Development Phase
```
1. Engineer checks out their branch
2. Works independently on feature/blocker
3. Creates Pull Request when ready
4. CI/CD gates run automatically
5. Code review happens
6. Merge when approved + gates pass
7. Delete branch after merge
```

### Cleanup Phase
```bash
# (DO NOT EXECUTE - This is documentation)
# After team completes work:
git branch -d feature/blocker-1-state-machine  # Local
git push origin --delete feature/blocker-1-state-machine  # Remote

# Or use GitHub UI to delete branches after merge
# Setting: "Delete branch on merge" (enable for all repos)
```

---

## Integration Points

### Single-Merge vs Multi-Merge Strategy

**RECOMMENDED: Two-Stage Merge**

**Stage 1 - Feature Merge** (to phase-2-implementation)
```
feature/blocker-* → phase-2-implementation (individual PRs)
develop/*         → phase-2-implementation (individual PRs)
```
- Teams merge as soon as ready
- No waiting for other teams
- phase-2-implementation accumulates completed work

**Stage 2 - Phase Merge** (to main)
```
phase-2-implementation → main (single PR)
```
- Merge complete phase when all blockers done
- OR merge incrementally as phases complete
- Final verification before production merge

**Benefits**:
- Individual teams unblocked immediately
- Controlled phase integration
- Easy rollback (rollback phase-2-implementation PR)
- Clear phase boundary in git history

---

## CI/CD Pipeline Status Files

### Required Status Checks

**For feature/* branches**:
- `status/build-passed` ✓
- `status/tests-passed` ✓
- `status/linting-passed` ✓
- `status/security-scan-passed` ✓

**For develop/* branches**:
- `status/build-passed` ✓
- `status/integration-tests-passed` ✓
- `status/contract-tests-passed` ✓
- `status/security-scan-passed` ✓

**For phase-* branches**:
- `status/all-checks-passed` ✓
- `status/staging-deployment-passed` ✓
- `status/e2e-tests-passed` ✓

### Example GitHub Actions Workflow

```yaml
name: Phase 2 CI/CD Gate

on:
  pull_request:
    branches:
      - phase-2-implementation
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - run: npm run lint
      - run: npm test -- --coverage --coverage-threshold=80
      - run: npm audit --audit-level=moderate

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - name: Security scan
        run: npm audit
      - name: OWASP scan
        run: npx snyk test || true

  integration:
    if: contains(github.head_ref, 'develop/')
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run test:integration
      - run: npm run test:contract

  staging-deploy:
    if: github.base_ref == 'main'
    runs-on: ubuntu-latest
    needs: [build, security, integration]
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to staging
        run: npm run deploy:staging
      - name: Run E2E tests
        run: npm run test:e2e
```

---

## Best Practices & Guidelines

### DO's

- [x] Keep feature branches short-lived (1-2 weeks maximum)
- [x] Commit frequently with atomic, logical commits
- [x] Write clear commit messages (conventional commits)
- [x] Create PRs early (draft if needed)
- [x] Review code thoroughly before approving
- [x] Run tests locally before pushing
- [x] Update dependencies on your branch (don't let debt accumulate)
- [x] Document migration strategies for schema changes
- [x] Communicate blockers/dependencies early

### DON'Ts

- [x] Don't commit to main directly (always use feature branches)
- [x] Don't force-push to shared branches (feature/* after PR created)
- [x] Don't merge without CI/CD gates passing
- [x] Don't skip code review even for small changes
- [x] Don't leave stale branches (delete after merge)
- [x] Don't commit secrets/API keys (use environment variables)
- [x] Don't merge feature branches without author review
- [x] Don't rebase phase-2-implementation (use merge commits for stability)

---

## Troubleshooting Guide

### Scenario: Two teams' branches have conflicts

**Resolution**:
1. Identify conflicting files
2. Coordinate between teams
3. Decide who should update their branch
4. Team updates branch, resolves conflicts
5. Re-run CI/CD gates
6. Merge when gates pass

### Scenario: Feature branch becomes stale

**Resolution**:
```bash
# Update feature branch with latest main
git checkout feature/blocker-1-state-machine
git fetch origin
git rebase origin/main  # or merge if prefer merge commits
git push origin feature/blocker-1-state-machine --force-with-lease
```

### Scenario: Need to cherry-pick commit from other branch

**Resolution**:
```bash
# Only do this for hotfixes/critical changes
git cherry-pick <commit-hash>
# Requires: source branch commit is in a merged or staging branch
```

### Scenario: Accidental commit to main

**Resolution**:
```bash
# Create new branch with your commits
git branch feature/fix-name
# Reset main to last good state
git reset --hard origin/main
git push origin main --force-with-lease  # Use with extreme caution
```

---

## Metrics & Monitoring

### Track These Metrics Per Branch

| Metric | Target | Tool |
|--------|--------|------|
| Time-to-Merge | <2 days for feature/* | GitHub insights |
| Code Review Turnaround | <24 hours | GitHub automated checks |
| Test Coverage | >80% | Code coverage reports |
| Build Pass Rate | >95% | CI/CD logs |
| Security Issues | 0 critical | Security scan reports |

### Review Monthly
- Branches merged per month
- Average merge time by branch type
- Most common merge conflicts
- Security vulnerabilities found/fixed
- Test failure root causes

---

## Phase 2 Git Structure Summary

**Total Branches**: 12 feature/development + 1 integration
**Creation Timeline**: Week 1 of Phase 2
**Expected Merge Timeline**: 4-6 weeks (parallel execution)
**Integration Point**: phase-2-implementation (optional staging branch)
**Final Merge**: phase-2-implementation → main (single PR)

**Key Success Factors**:
1. ✓ No circular dependencies
2. ✓ Independent parallel execution
3. ✓ Clear merge strategy per branch type
4. ✓ Automated CI/CD gates
5. ✓ Structured code review process

---

## Next Steps

1. **Execute Branch Creation**: Follow GIT-BRANCH-STATUS-2026-02-26.md to create all 12 branches
2. **Enable Branch Protection**: Add protection rules to main and phase-2-implementation
3. **Configure CI/CD**: Set up GitHub Actions or equivalent for gating
4. **Communicate to Teams**: Share this document with all development teams
5. **Start Feature Work**: Teams begin work on assigned branches
6. **Monitor Progress**: Track via branch status document (updated weekly)

---

**Document Version**: 1.0
**Last Updated**: 2026-02-26 19:45 UTC
**Owner**: Phase 2 Infrastructure Lead
**Distribution**: All Phase 2 development teams
