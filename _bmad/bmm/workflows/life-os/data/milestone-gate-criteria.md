# Milestone Gate Criteria

## Purpose
Gate criteria define "done" for each milestone. Prevents scope creep and ensures quality before proceeding to next milestone.

## Quality Standards by Milestone Type

### Foundation Milestones (M1 typically)
**Definition:** Initial setup, architecture, infrastructure
**Quality Gates:**
- Architecture documented and approved
- Development environment set up
- Key technical decisions recorded
- Risks identified and mitigated
- Team aligned on approach

**Example Criteria:**
```yaml
success_criteria:
  - "System architecture diagram completed and reviewed"
  - "Database schema designed and validated"
  - "Development environment set up for all team members"
  - "Technical stack decisions documented with rationale"
  - "Integration points with external systems identified"
```

### Development Milestones (M2-M3 typically)
**Definition:** Core feature implementation, iterative building
**Quality Gates:**
- Features implemented per requirements
- Unit tests written and passing (80%+ coverage)
- Code reviewed and merged
- Technical debt documented
- Performance benchmarks met

**Example Criteria:**
```yaml
success_criteria:
  - "All user stories in milestone completed"
  - "Unit test coverage ≥ 80%"
  - "Code review completed for all PRs"
  - "No P0/P1 bugs remaining"
  - "API documentation updated"
  - "Performance: API response time < 200ms"
```

### Integration Milestones (M4-M5 typically)
**Definition:** Combining components, end-to-end testing
**Quality Gates:**
- Integration tests passing
- End-to-end scenarios validated
- User acceptance criteria met
- Security audit passed
- Deployment runbook ready

**Example Criteria:**
```yaml
success_criteria:
  - "All integration tests passing"
  - "User acceptance testing completed (5+ users)"
  - "Security scan shows no critical vulnerabilities"
  - "Load testing: handles 1000 concurrent users"
  - "Deployment automation tested in staging"
  - "Rollback procedure validated"
```

### Launch Milestones (Final M)
**Definition:** Production deployment, go-live
**Quality Gates:**
- Production deployment successful
- Monitoring and alerting active
- Documentation complete
- Support team trained
- Success metrics defined and tracked

**Example Criteria:**
```yaml
success_criteria:
  - "Production deployment completed with zero downtime"
  - "All monitoring dashboards operational"
  - "User documentation published"
  - "Support team trained (100% completion rate)"
  - "Success metrics: 90% user satisfaction in first week"
  - "Post-launch retrospective completed"
```

## Validation Checklist

### Before Moving to Next Milestone
```
VALIDATION CHECKLIST - Milestone {N}

✅ All success criteria met (list from above)
✅ Acceptance criteria verified by stakeholder
✅ Technical debt documented and prioritized
✅ Known issues logged (and assessed as non-blocking)
✅ Dependencies for next milestone ready
✅ Team capacity confirmed for next milestone
✅ Go/No-Go decision made by project lead

DECISION:
[ ] PROCEED to next milestone
[ ] HOLD - address issues (list issues):
    - Issue 1: ___
    - Issue 2: ___
[ ] ROLLBACK - revert and fix (critical issues found)
```

## Criteria by Risk Level

### Low Risk Projects
**Minimum viable criteria:**
- Core functionality works
- Basic testing completed
- No critical bugs

### Medium Risk Projects
**Standard criteria:**
- All planned features implemented
- Test coverage ≥ 70%
- Security review passed
- Performance acceptable

### High Risk Projects
**Strict criteria:**
- 100% requirements met
- Test coverage ≥ 90%
- Independent security audit passed
- Performance SLA validated
- Disaster recovery tested
- Compliance verified

## Common Anti-Patterns

### ❌ "90% Done" Syndrome
**Problem:** Claiming milestone complete when small tasks remain
**Fix:** Define clear binary criteria (done = ALL criteria met)

### ❌ Moving Goalposts
**Problem:** Adding criteria mid-milestone
**Fix:** Lock criteria at milestone start, track changes as scope creep

### ❌ "Good Enough" Syndrome
**Problem:** Lowering standards to meet deadline
**Fix:** Extend deadline or descope features, don't compromise quality gates

### ❌ No Stakeholder Sign-Off
**Problem:** Team declares done without user/client validation
**Fix:** Include stakeholder acceptance as mandatory criterion

## Gate Criteria Template

```yaml
milestone_id: M{N}
name: "{milestone_name}"
gate_criteria:
  functional:
    - criterion: "{What must work}"
      validation: "{How to verify}"
      owner: "{Who validates}"
      status: PENDING|PASS|FAIL

  quality:
    - criterion: "Test coverage ≥ {X}%"
      validation: "Run coverage report"
      owner: "QA Lead"
      status: PENDING

  performance:
    - criterion: "{Performance requirement}"
      validation: "{Benchmark test}"
      owner: "Performance Engineer"
      status: PENDING

  security:
    - criterion: "{Security requirement}"
      validation: "{Security scan/audit}"
      owner: "Security Team"
      status: PENDING

  documentation:
    - criterion: "{Documentation complete}"
      validation: "{Review checklist}"
      owner: "Tech Writer"
      status: PENDING

gate_status: OPEN|READY_FOR_REVIEW|PASSED|FAILED
reviewed_by: "{Name}"
reviewed_date: "{YYYY-MM-DD}"
next_milestone: M{N+1}
```

## Decision Matrix

| Criteria Met | Gate Status | Action |
|--------------|-------------|--------|
| 100% | PASSED | Proceed to next milestone |
| 90-99% (non-critical gaps) | CONDITIONAL PASS | Proceed with risk log, address gaps in parallel |
| 80-89% | HOLD | Fix gaps before proceeding |
| < 80% | FAILED | Reassess plan, extend milestone, or descope |

## Examples by Domain

### Software Development
```yaml
milestone: "Backend API Development"
success_criteria:
  - "All 15 API endpoints implemented and deployed to staging"
  - "OpenAPI specification published"
  - "Unit test coverage: 85%"
  - "Integration tests: 100% passing"
  - "API response time < 200ms (p95)"
  - "Security scan: 0 critical/high vulnerabilities"
  - "Code review: 100% of PRs approved"
  - "Load test: handles 500 req/sec"
```

### Content Creation
```yaml
milestone: "Draft Chapters 1-5"
success_criteria:
  - "5 chapters written (min 2000 words each)"
  - "Peer review completed (2+ reviewers)"
  - "Fact-checking: 100% claims verified"
  - "Style guide compliance: 95%+"
  - "Readability score: Grade 8-10 (Flesch-Kincaid)"
  - "SEO: 5+ target keywords per chapter"
  - "Images/diagrams: Min 2 per chapter"
```

### Product Launch
```yaml
milestone: "Beta Testing"
success_criteria:
  - "100+ beta users recruited and onboarded"
  - "Beta period: 2 weeks completed"
  - "User feedback collected (80%+ response rate)"
  - "Critical bugs identified and fixed (0 remaining P0)"
  - "User satisfaction score ≥ 4.0/5.0"
  - "Feature adoption: 60%+ users tried core features"
  - "Performance metrics within targets (uptime 99%+)"
  - "Support documentation validated by beta users"
```

## Gate Review Process

### Step 1: Self-Assessment
Team reviews all criteria, marks status (PASS/FAIL)

### Step 2: Evidence Collection
Gather proof for each criterion:
- Test reports
- Coverage reports
- Stakeholder sign-offs
- Performance benchmarks
- Security scan results

### Step 3: Gate Review Meeting
- Present evidence
- Discuss gaps
- Make Go/No-Go decision
- Document decision rationale

### Step 4: Decision Communication
- Notify stakeholders of decision
- Update project plan if delayed
- Log decision in project journal

### Step 5: Proceed or Remediate
- If PASS: Start next milestone
- If CONDITIONAL: Start next + fix gaps in parallel
- If HOLD/FAIL: Fix gaps, re-review
