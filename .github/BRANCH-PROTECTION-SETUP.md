# Branch Protection Rules Setup Guide

This guide explains how to configure branch protection rules for Sprint 0 CI/CD pipeline.

**Location:** GitHub Repository Settings → Branches → Branch protection rules

---

## Automated Setup (Recommended)

Use the GitHub CLI to apply branch protection:

```bash
# Login to GitHub
gh auth login

# Set up main branch protection
gh api \
  --method PUT \
  repos/:owner/:repo/branches/main/protection \
  -f required_status_checks='{"strict":true,"contexts":["test-matrix (3.11)","test-matrix (3.12)","test-matrix (3.13)","quality-gates","security-checks","build-check"]}' \
  -f enforce_admins=true \
  -f required_pull_request_reviews='{"dismiss_stale_reviews":true,"require_code_owner_reviews":false,"required_approving_review_count":2}' \
  -f allow_force_pushes=false \
  -f allow_deletions=false

# Set up develop branch protection
gh api \
  --method PUT \
  repos/:owner/:repo/branches/develop/protection \
  -f required_status_checks='{"strict":true,"contexts":["test-matrix (3.12)","quality-gates","security-checks"]}' \
  -f enforce_admins=false \
  -f required_pull_request_reviews='{"dismiss_stale_reviews":true,"require_code_owner_reviews":false,"required_approving_review_count":1}' \
  -f allow_force_pushes=false \
  -f allow_deletions=false
```

Replace `:owner` and `:repo` with your GitHub organization and repository name.

---

## Manual Setup (GitHub Web UI)

### Step 1: Navigate to Settings

1. Go to your GitHub repository
2. Click "Settings" tab
3. Click "Branches" in left sidebar
4. Click "Add rule"

### Step 2: Protect Main Branch

**Branch name pattern:** `main`

#### Required Status Checks
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- Select these status checks:
  - `test-matrix (3.11)`
  - `test-matrix (3.12)`
  - `test-matrix (3.13)`
  - `quality-gates`
  - `security-checks`
  - `build-check`

#### Require Reviews
- ✅ Require pull request reviews before merging
- Required approving reviews: **2**
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ❌ Require review from Code Owners

#### Require Admin Approval (Optional)
- ✅ Enforce all the above rules even for admins

#### Additional Rules
- ❌ Allow force pushes (Disabled)
- ❌ Allow deletions (Disabled)

### Step 3: Protect Develop Branch

**Branch name pattern:** `develop`

Follow same steps as Main branch, but:
- Required approving reviews: **1** (instead of 2)
- Allow admin approval: **Leave to your preference**

---

## Verifying Setup

### Check Main Branch Protection
```bash
gh api repos/:owner/:repo/branches/main/protection
```

Expected response includes:
```json
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "test-matrix (3.11)",
      "test-matrix (3.12)",
      "test-matrix (3.13)",
      "quality-gates",
      "security-checks",
      "build-check"
    ]
  },
  "required_pull_request_reviews": {
    "required_approving_review_count": 2,
    "dismiss_stale_reviews": true
  },
  "enforce_admins": true,
  "allow_force_pushes": false,
  "allow_deletions": false
}
```

### Check Develop Branch Protection
```bash
gh api repos/:owner/:repo/branches/develop/protection
```

---

## Testing Branch Protection

### Test 1: PR Cannot Merge Without Passing Checks

1. Create a feature branch: `git checkout -b feature/test`
2. Make a change that breaks tests (e.g., reduce coverage)
3. Push and create PR: `git push -u origin feature/test`
4. GitHub should show: **"Some checks are pending" or "Some checks failed"**
5. Merge button should be **disabled** (greyed out)
6. Fix the issue to enable merge

### Test 2: PR Cannot Merge Without Reviews

1. From the failing PR above, fix the code
2. All checks pass, but merge button still **disabled** (on main)
3. Need 2 reviewers to approve
4. Request 2 reviews from team members
5. Merge button enables after 2 approvals

### Test 3: Stale Reviews Dismissed

1. Get 2 approvals on a PR
2. Push a new commit
3. Reviews should become **stale** (grayed out)
4. New reviews required (or requesters must re-approve)

---

## Troubleshooting

### "Merge Blocked: Required Status Check Failed"

**Cause:** One or more CI jobs failed

**Solution:**
1. Click "Details" next to failed check
2. Review workflow logs
3. Fix issue locally: `poetry run pytest --cov=src`
4. Push fix: `git push`
5. GitHub automatically reruns checks
6. Wait for all checks to pass (green)

### "Merge Blocked: Required Reviews"

**Cause:** Not enough approvals

**Solution:**
1. Click "Request review" (right sidebar)
2. Select required number of reviewers
3. Reviewers should see PR notification
4. After review and approval, merge button unlocks

### "Merge Blocked: Stale Reviews"

**Cause:** PR was approved, but new commits pushed

**Solution:**
1. Reviewers need to re-review with latest changes
2. Click "Request review" again
3. Reviewers can click "Re-approve" after reviewing new changes
4. Merge once you have enough current approvals

### "Can't Find Status Check"

**Cause:** Check name mismatch or check hasn't run yet

**Solution:**
1. Open PR
2. Scroll to "Checks" section
3. Look for exact check names from workflow file
4. Check must run at least once before it appears in dropdown
5. If missing, push dummy commit to trigger workflow

---

## Maintenance

### Updating Required Status Checks

If you add new workflow jobs:

```bash
gh api \
  --method PATCH \
  repos/:owner/:repo/branches/main/protection \
  -f required_status_checks.contexts='["job1","job2","job3","newjob"]'
```

### Temporarily Bypass Protection (Emergency)

If admin needs to merge during incident:

```bash
# Remove protection temporarily
gh api \
  --method DELETE \
  repos/:owner/:repo/branches/main/protection

# ... merge emergency fix ...

# Re-apply protection
# Use the setup commands above
```

⚠️ **Warning:** Use sparingly for true emergencies only.

---

## Best Practices

✅ **DO:**
- Require at least 2 reviews for main branch
- Keep status checks up to date
- Dismiss stale reviews
- Enforce for admins too
- Document exceptions in PR comments

❌ **DON'T:**
- Bypass checks without audit trail
- Require excessive reviews (slows development)
- Allow force pushes (loses history)
- Allow branch deletions without backup
- Change rules without team discussion

---

## Team Communication

Inform your team about rules:

```
Subject: Branch Protection Rules Enabled

Hi team,

As of [DATE], we've enabled branch protection rules for Sprint 0:

**Main Branch:**
- All 3 Python version tests must pass
- All quality/security checks must pass
- 2 approvals required
- Status checks must be current

**Develop Branch:**
- Python 3.12 tests must pass
- Quality/security checks must pass
- 1 approval required

See `.github/BRANCH-PROTECTION-SETUP.md` for detailed rules and how to fix failures.

Questions? Check troubleshooting section.
```

---

## Quick Reference

| Rule | Main | Develop | Purpose |
|------|------|---------|---------|
| Status checks | 6 jobs | 3 jobs | Ensure quality |
| Approvals | 2 | 1 | Code review |
| Up-to-date | Yes | Yes | Prevent conflicts |
| Dismiss stale | Yes | Yes | Re-review changes |
| Admin override | No | Optional | Enforce rules |
| Force push | No | No | Preserve history |
| Deletion | No | No | Prevent accidents |

---

## File Location
- **File:** `.github/BRANCH-PROTECTION-SETUP.md`
- **Last Updated:** 2026-02-28
- **Version:** 1.0

See `STORY-0-AUTOMATION-REPORT-2026-02-28.md` for complete pipeline documentation.
