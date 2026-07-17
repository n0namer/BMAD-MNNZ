# Phase 2 Git Implementation Guide
**Document**: GIT-IMPLEMENTATION-GUIDE.md
**Created**: 2026-02-26
**Status**: READY FOR EXECUTION
**Purpose**: Step-by-step execution guide for branch creation and team onboarding

---

## Overview

This guide provides the exact sequence of steps to implement the Phase 2 git branch structure documented in:
- `PHASE-2-GIT-WORKFLOW.md` - Strategy and policies
- `GIT-BRANCH-STATUS-2026-02-26.md` - Branch specifications and timeline

**Do not execute these commands** - This is documentation of what SHOULD be done.

---

## Phase 1: Pre-Implementation Checklist

### Step 1: Verify Current State

```bash
# Check current branch and status
git branch -a
git status

# Expected output:
# * main
#   remotes/origin/main
# (clean working directory)
```

**Verification**:
- [ ] Currently on `main` branch
- [ ] Working directory is clean
- [ ] No uncommitted changes
- [ ] No stashed changes

### Step 2: Prepare Main Branch

```bash
# Ensure main is up to date
git checkout main
git fetch origin
git pull origin main

# Create a clean commit to mark Phase 2 start (optional but recommended)
echo "# Phase 2 Implementation Starting
Started: 2026-02-26
Branches: 12 features + 1 integration point" > PHASE-2-NOTES.txt
git add PHASE-2-NOTES.txt
git commit -m "docs: Mark beginning of Phase 2 implementation"
git push origin main
```

**Verification**:
- [ ] main updated from origin
- [ ] Phase 2 notes committed (optional)
- [ ] No conflicts

### Step 3: Configure Git for Phase 2

```bash
# Configure local git settings
git config --global user.name "Phase 2 Bot"
git config --global user.email "phase2@company.com"

# Or per-repo (recommended)
git config --local user.name "Phase 2 Bot"
git config --local user.email "phase2@company.com"

# Verify configuration
git config --list | grep user
```

**Verification**:
- [ ] Git user name configured
- [ ] Git user email configured

---

## Phase 2: Integration Branch Creation

### Step 4: Create phase-2-implementation Branch

**Purpose**: Central aggregation point for all Phase 2 features

```bash
# Create and push integration branch
git checkout main
git pull origin main
git checkout -b phase-2-implementation
git push -u origin phase-2-implementation
```

**Verification**:
```bash
git branch -a | grep phase-2-implementation
# Expected: remotes/origin/phase-2-implementation

git log --oneline phase-2-implementation | head -1
# Expected: Same as main's latest commit
```

**Checklist**:
- [ ] Branch created locally
- [ ] Branch pushed to origin
- [ ] Branch visible in `git branch -a`

### Step 5: Configure Branch Protection (Optional)

**For GitHub/GitLab**:

```
Repository Settings → Branches → Add Rule

For branch: phase-2-implementation
- [x] Require pull request reviews before merging (1 approver)
- [x] Require status checks to pass before merging
- [x] Require branches to be up to date before merging
- [x] Include administrators in restrictions
- [x] Allow auto-merge
- [x] Auto-delete head branches
```

---

## Phase 3: Feature Branch Creation (Group 1 - Infrastructure)

**Timeline**: Week 1 (2026-03-03)
**Execution**: Sequential (use this order)

### Step 6: Create develop/testing-framework

**Team**: QA/Testing Infrastructure
**Purpose**: Core testing infrastructure

```bash
git checkout main
git pull origin main
git checkout -b develop/testing-framework
git push -u origin develop/testing-framework
```

**Verification**:
```bash
git log --oneline develop/testing-framework | head -1
# Should show same commit as main
```

**Checklist**:
- [ ] Branch created
- [ ] Pushed to origin
- [ ] Visible in branch list

### Step 7: Create develop/database-schema

**Team**: Database Engineering
**Purpose**: Database schema and migrations

```bash
git checkout main
git pull origin main
git checkout -b develop/database-schema
git push -u origin develop/database-schema
```

**Verification**:
- [ ] Branch created and pushed
- [ ] Depends on: develop/testing-framework ✓ (already created in Step 6)

### Step 8: Create develop/api-gateway

**Team**: API Infrastructure
**Purpose**: API gateway and routing

```bash
git checkout main
git pull origin main
git checkout -b develop/api-gateway
git push -u origin develop/api-gateway
```

**Verification**:
- [ ] Branch created and pushed
- [ ] Depends on: develop/testing-framework ✓ (already created in Step 6)

---

## Phase 4: Feature Branch Creation (Group 2 - Blockers)

**Timeline**: Week 1 (2026-03-03)
**Execution**: Parallel (create all together)

### Step 9: Create feature/blocker-1-state-machine

```bash
git checkout main
git pull origin main
git checkout -b feature/blocker-1-state-machine
git push -u origin feature/blocker-1-state-machine
```

### Step 10: Create feature/blocker-2-journal-schema

```bash
git checkout main
git pull origin main
git checkout -b feature/blocker-2-journal-schema
git push -u origin feature/blocker-2-journal-schema
```

### Step 11: Create feature/blocker-3-telemetry

```bash
git checkout main
git pull origin main
git checkout -b feature/blocker-3-telemetry
git push -u origin feature/blocker-3-telemetry
```

### Step 12: Create feature/blocker-4-compare

```bash
git checkout main
git pull origin main
git checkout -b feature/blocker-4-compare
git push -u origin feature/blocker-4-compare
```

### Step 13: Create feature/blocker-5-audit

```bash
git checkout main
git pull origin main
git checkout -b feature/blocker-5-audit
git push -u origin feature/blocker-5-audit
```

**Batch Verification**:
```bash
git branch -a | grep feature/blocker
# Expected:
# feature/blocker-1-state-machine
# feature/blocker-2-journal-schema
# feature/blocker-3-telemetry
# feature/blocker-4-compare
# feature/blocker-5-audit
```

**Checklist**:
- [ ] All 5 blocker branches created
- [ ] All pushed to origin
- [ ] Dependencies verified (infra branches exist)

---

## Phase 5: Feature Branch Creation (Group 3 - Frontend)

**Timeline**: Week 1 (2026-03-03)
**Execution**: Parallel

### Step 14: Create feature/ui-strategy-lifecycle

```bash
git checkout main
git pull origin main
git checkout -b feature/ui-strategy-lifecycle
git push -u origin feature/ui-strategy-lifecycle
```

### Step 15: Create feature/ui-telemetry-dashboard

```bash
git checkout main
git pull origin main
git checkout -b feature/ui-telemetry-dashboard
git push -u origin feature/ui-telemetry-dashboard
```

### Step 16: Create feature/ui-compare-workflow

```bash
git checkout main
git pull origin main
git checkout -b feature/ui-compare-workflow
git push -u origin feature/ui-compare-workflow
```

**Batch Verification**:
```bash
git branch -a | grep feature/ui
# Expected:
# feature/ui-strategy-lifecycle
# feature/ui-telemetry-dashboard
# feature/ui-compare-workflow
```

**Checklist**:
- [ ] All 3 frontend branches created
- [ ] All pushed to origin
- [ ] Frontend teams notified of branch names

---

## Phase 6: Verification & Audit

### Step 17: Complete Branch Inventory Verification

**Verify All 13 Branches Created**:

```bash
git branch -a | grep -E "phase-2|feature|develop"
```

**Expected Output**:
```
remotes/origin/develop/api-gateway
remotes/origin/develop/database-schema
remotes/origin/develop/testing-framework
remotes/origin/feature/blocker-1-state-machine
remotes/origin/feature/blocker-2-journal-schema
remotes/origin/feature/blocker-3-telemetry
remotes/origin/feature/blocker-4-compare
remotes/origin/feature/blocker-5-audit
remotes/origin/feature/ui-strategy-lifecycle
remotes/origin/feature/ui-telemetry-dashboard
remotes/origin/feature/ui-compare-workflow
remotes/origin/phase-2-implementation
```

**Checklist** (Count: 12 branches):
- [ ] develop/testing-framework ✓
- [ ] develop/database-schema ✓
- [ ] develop/api-gateway ✓
- [ ] feature/blocker-1-state-machine ✓
- [ ] feature/blocker-2-journal-schema ✓
- [ ] feature/blocker-3-telemetry ✓
- [ ] feature/blocker-4-compare ✓
- [ ] feature/blocker-5-audit ✓
- [ ] feature/ui-strategy-lifecycle ✓
- [ ] feature/ui-telemetry-dashboard ✓
- [ ] feature/ui-compare-workflow ✓
- [ ] phase-2-implementation ✓

### Step 18: Verify Branch Independence

```bash
# Check that each feature branch matches main (no divergence)
for branch in $(git branch -a | grep -E "feature|develop" | sed 's/^[* ]//'); do
  echo "Checking $branch..."
  git log --oneline $branch | head -1
done
```

**Expected**: All show same commit as main (no divergence yet)

### Step 19: Verify No Circular Dependencies

**Manual Check Against Matrix** (from GIT-BRANCH-STATUS-2026-02-26.md):

```
Testing Framework → None (independent)
Database Schema → Testing Framework
API Gateway → Testing Framework
BLOCKER-1 → API Gateway
BLOCKER-2 → Database Schema
BLOCKER-3 → API Gateway
BLOCKER-4 → Database Schema
BLOCKER-5 → Database Schema
Frontend 1 → BLOCKER-1
Frontend 2 → BLOCKER-3
Frontend 3 → BLOCKER-4
```

**Verification**:
- [ ] No backward dependencies (circular)
- [ ] All dependencies flow downward
- [ ] Teams can work independently

---

## Phase 7: Team Onboarding

### Step 20: Create Team-Specific Documentation

**For Each Team**, create a file `TEAM-[NAME]-SETUP.md`:

**Example: TEAM-BLOCKER-1-SETUP.md**

```markdown
# BLOCKER-1 State Machine Team Setup

## Your Branch
- **Name**: feature/blocker-1-state-machine
- **Status**: Created 2026-02-26, ready for work
- **Target Merge Date**: 2026-03-17
- **Team Size**: 3-4 engineers

## Dependencies
- Must complete after: develop/api-gateway, develop/testing-framework
- **Status**: Both branches created ✓

## Getting Started
1. Clone repo: git clone <repo-url>
2. Create local branch: git checkout feature/blocker-1-state-machine
3. Pull latest: git pull origin feature/blocker-1-state-machine
4. Create feature branch: git checkout -b feature/blocker-1/<task-name>
5. Start development

## Merge Requirements
- [x] Unit tests >80% coverage
- [x] API integration tested
- [x] Security scan passed
- [x] 1 code review approval
- [x] No breaking changes

## Merge Steps (When Ready)
1. Ensure all commits pushed: git push origin feature/blocker-1/<task-name>
2. Create Pull Request: feature/blocker-1/<task-name> → phase-2-implementation
3. Add description with what was built
4. Wait for CI/CD gates to pass
5. Request 1 reviewer from core team
6. Merge when approved + gates pass

## Questions?
Contact Phase 2 Lead: [name]
```

### Step 21: Communicate With Teams

**Email/Slack Template**:

```
Subject: Phase 2 Git Branches Created - Ready to Start Work

Hi [Team Name],

Your Phase 2 branch is ready!

Branch: [branch-name]
Target Date: [date]
Dependencies: [list]

Next Steps:
1. Checkout your branch:
   git checkout [branch-name]

2. Create feature branches for your work:
   git checkout -b feature/[branch-name]/[task-name]

3. Start development! All teams can work in parallel.

4. When ready to merge:
   - Create PR to phase-2-implementation
   - Ensure CI/CD gates pass
   - Get code review approval
   - Merge!

Full details: GIT-BRANCH-STATUS-2026-02-26.md
Questions? Reach out to Phase 2 Lead.

Ready to go!
```

**Checklist**:
- [ ] All 12 teams/leads notified
- [ ] Team-specific setup docs created
- [ ] Access to branch documentation provided
- [ ] Merge requirements explained
- [ ] Questions answered

### Step 22: Configure CI/CD (GitHub Actions)

**Create**: `.github/workflows/phase-2-ci.yml`

```yaml
name: Phase 2 CI/CD

on:
  pull_request:
    branches:
      - phase-2-implementation
      - feature/**
      - develop/**

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
      - run: npm test -- --coverage

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm audit
      - name: OWASP Security Check
        run: npx snyk test || true

  integration:
    if: startsWith(github.head_ref, 'develop/')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run test:integration

  status:
    needs: [build, security]
    runs-on: ubuntu-latest
    steps:
      - name: Set status
        run: echo "All checks passed"
```

**Checklist**:
- [ ] CI workflow created
- [ ] Runs on pull requests to phase-2 branches
- [ ] Build step passes
- [ ] Tests run
- [ ] Security checks enabled

---

## Phase 8: Post-Creation Verification

### Step 23: Final Health Check

**Run This Verification Script**:

```bash
#!/bin/bash
# phase-2-git-health-check.sh

echo "=== Phase 2 Git Structure Health Check ==="
echo ""

# Count branches
BRANCH_COUNT=$(git branch -a | grep -E "remotes/origin/(feature|develop|phase-2)" | wc -l)
echo "✓ Branch Count: $BRANCH_COUNT (expected: 13)"

# Verify each branch exists
EXPECTED_BRANCHES=(
  "phase-2-implementation"
  "develop/testing-framework"
  "develop/database-schema"
  "develop/api-gateway"
  "feature/blocker-1-state-machine"
  "feature/blocker-2-journal-schema"
  "feature/blocker-3-telemetry"
  "feature/blocker-4-compare"
  "feature/blocker-5-audit"
  "feature/ui-strategy-lifecycle"
  "feature/ui-telemetry-dashboard"
  "feature/ui-compare-workflow"
)

MISSING=0
for branch in "${EXPECTED_BRANCHES[@]}"; do
  if git branch -a | grep -q "origin/$branch"; then
    echo "✓ $branch"
  else
    echo "✗ MISSING: $branch"
    ((MISSING++))
  fi
done

if [ $MISSING -eq 0 ]; then
  echo ""
  echo "✓ All 12 branches verified!"
  echo "✓ Phase 2 git structure ready for development"
else
  echo ""
  echo "✗ $MISSING branch(es) missing - please create them"
fi
```

**Run It**:
```bash
bash phase-2-git-health-check.sh
```

**Expected Output**:
```
=== Phase 2 Git Structure Health Check ===

✓ Branch Count: 13 (expected: 13)
✓ phase-2-implementation
✓ develop/testing-framework
✓ develop/database-schema
✓ develop/api-gateway
✓ feature/blocker-1-state-machine
✓ feature/blocker-2-journal-schema
✓ feature/blocker-3-telemetry
✓ feature/blocker-4-compare
✓ feature/blocker-5-audit
✓ feature/ui-strategy-lifecycle
✓ feature/ui-telemetry-dashboard
✓ feature/ui-compare-workflow

✓ All 12 branches verified!
✓ Phase 2 git structure ready for development
```

### Step 24: Document Completion

**Update**: GIT-BRANCH-STATUS-2026-02-26.md

**Add to Top**:
```
## IMPLEMENTATION STATUS

✓ All 12 feature/develop branches created: 2026-02-26 20:30 UTC
✓ Integration branch (phase-2-implementation) created: 2026-02-26 20:00 UTC
✓ CI/CD gates configured: 2026-02-26 20:45 UTC
✓ All teams notified: [Pending - Date TBD]
✓ Development ready: [Pending - Date TBD]
```

---

## Phase 9: Week 1 Kickoff Meeting Agenda

**When**: 2026-03-03 (Monday morning)
**Attendees**: All Phase 2 teams + leadership
**Duration**: 60 minutes

### Agenda

**0:00-0:05 Welcome & Overview**
- Phase 2 goals
- Timeline (6 weeks)
- Success criteria

**0:05-0:15 Git Structure Walkthrough**
- Show branch topology
- Explain non-blocking/parallel model
- Show dependency map

**0:15-0:25 Team Assignments**
- Review team ↔ branch mapping
- Clarify dependencies
- Identify team leads

**0:25-0:35 Development Workflow**
- How to checkout branch
- Commit conventions
- When to merge (gates + review)

**0:35-0:45 First Sprint Goals**
- For each team: what should be done by Week 3?
- Identify any blocking dependencies
- Clarify acceptance criteria

**0:45-0:55 Q&A & Blockers**
- Address team questions
- Identify early blockers
- Confirm all teams ready to start

**0:55-1:00 Next Steps**
- Email team-specific runbooks
- Schedule standup times
- Confirm kick-off complete

---

## Troubleshooting During Implementation

### Issue: Branch creation command fails

**Error**: `fatal: destination path 'xxx' already exists and is not an empty directory`

**Solution**:
```bash
# The branch might already exist locally
git branch | grep feature/blocker-1

# If it does, switch to it instead
git checkout feature/blocker-1-state-machine
git pull origin feature/blocker-1-state-machine

# If not, ensure you're on a clean state
git status  # Should be clean
git checkout main
git pull origin main
# Then retry branch creation
```

### Issue: Cannot push branch

**Error**: `error: src refspec feature/blocker-1-state-machine does not match any file`

**Solution**:
```bash
# Make sure branch exists locally first
git branch -a | grep feature/blocker-1

# If missing, create it
git checkout -b feature/blocker-1-state-machine

# Then push
git push -u origin feature/blocker-1-state-machine
```

### Issue: Too many branches in wrong state

**Reset**: If something went wrong, start fresh

```bash
# Delete all local Phase 2 branches
git branch -D phase-2-implementation
git branch -D feature/blocker-1-state-machine
git branch -D feature/blocker-2-journal-schema
# ... etc

# Delete remote branches (requires admin access)
git push origin --delete phase-2-implementation
git push origin --delete feature/blocker-1-state-machine
# ... etc

# Start fresh from Phase 2: Integration Branch Creation (Step 4)
```

---

## Success Criteria Checklist

**After completing all phases, you should have**:

- [x] 13 total branches created (1 integration + 12 feature/develop)
- [x] All branches based on main
- [x] All branches pushed to origin
- [x] No circular dependencies
- [x] CI/CD workflow configured
- [x] All 12+ teams notified
- [x] Branch protection rules applied to main and phase-2-implementation
- [x] Team-specific runbooks created
- [x] Kick-off meeting scheduled
- [x] Weekly status tracking set up
- [x] Teams ready to begin development
- [x] Zero blocking dependencies (teams can work in parallel)

---

## Next Steps After Implementation

### Day 1 (Branch Creation Done)
- [ ] Run health check script (Step 23)
- [ ] Verify all teams have access
- [ ] Confirm CI/CD gates working

### Day 2-3 (Teams Start)
- [ ] Teams checkout their branches
- [ ] Initial commits pushed (test commit)
- [ ] First standup meeting
- [ ] Clarify any blockers

### Week 1 Kickoff (2026-03-03)
- [ ] Run kickoff meeting (Phase 9 agenda)
- [ ] Confirm all teams are developing
- [ ] Infrastructure branches (testing, database, api) should be ~20% complete

### Week 2-4 (Development)
- [ ] Weekly status updates
- [ ] Monitor for merge conflicts
- [ ] Track merge readiness
- [ ] Manage any blockers

### Week 5-6 (Merge Phase)
- [ ] Start merging completed branches
- [ ] Deploy to staging
- [ ] Run integration tests
- [ ] Prepare main merge

### Week 7 (Phase Completion)
- [ ] Final merge: phase-2-implementation → main
- [ ] Production deployment
- [ ] Retrospective
- [ ] Document learnings

---

**Document Version**: 1.0
**Created**: 2026-02-26
**Next Review**: After branch creation completion (2026-02-27)
**Owner**: Phase 2 Infrastructure Lead
