# Phase 1 Week 1 - Quick Start Guide

**Date:** March 3-7, 2026
**Target:** 21 story points (S-STRATEGY-001: 13 pts + S-JOURNAL-001: 8 pts)
**Team:** Dev A, Dev B, QA, Tech Lead

---

## TL;DR - What We're Building

### S-STRATEGY-001 (13 pts) - State Machine
**What:** A state machine that manages strategy lifecycle transitions
- 5 states: draft → approved → active → completed → archived
- Validation logic to prevent invalid transitions
- Audit trail to log all state changes with timestamp and actor

**Why:** Foundation for entire Phase 1. All other epics depend on it.

**Files to create:**
- `/src/core/strategy-lifecycle/state-machine.ts` (state transitions + validation)
- `/src/core/strategy-lifecycle/audit-trail.ts` (event logging)
- Tests in `/tests/unit/strategy-lifecycle/`

**Success Criteria:**
- 5 states work correctly ✓
- Invalid transitions rejected ✓
- Audit trail captures all changes ✓
- 10+ unit tests passing ✓
- Full TypeScript type coverage ✓

---

### S-JOURNAL-001 (8 pts) - Manifest Schema
**What:** A JSON schema and TypeScript types for strategy manifest files
- Define structure: strategyId, version, status, metadata, parameters
- Create JSON schema for validation
- Implement validator class

**Why:** Foundation for journal data layer. Other epics depend on it.

**Files to create:**
- `/src/core/journal/manifest-types.ts` (TypeScript interfaces)
- `/src/core/journal/manifest-validator.ts` (validation logic)
- `/src/core/journal/manifest-schema.json` (JSON schema)
- Tests in `/tests/unit/journal/`

**Success Criteria:**
- Schema structure complete ✓
- TypeScript types exported ✓
- Validation logic works ✓
- JSON schema file created ✓
- 8+ unit tests passing ✓

---

## Getting Started (Monday Morning)

### Step 1: Environment Setup (15 min)

```bash
# Clone the repo (if not already done)
git clone [repo-url]
cd katana-vectorbt-optimizer

# Install dependencies
npm install

# Verify setup
npm run build           # Should succeed
npm test               # Should show existing tests pass
npm run type-check     # Should have zero errors
```

### Step 2: Create Feature Branches

**Dev A (State Machine):**
```bash
git checkout -b feature/S-STRATEGY-001-state-machine
# or: git checkout -b feat/state-machine
```

**Dev B (Manifest Schema):**
```bash
git checkout -b feature/S-JOURNAL-001-manifest-schema
# or: git checkout -b feat/manifest-schema
```

### Step 3: Review Sprint Plan

**Everyone:** Read `PHASE-1-WEEK1-SPRINT-TASKS.md`
- Understand acceptance criteria
- Note daily breakdown
- Identify dependencies

**Dev A:** Focus on Monday M1.1-M1.5 (state machine code + tests)
**Dev B:** Focus on Monday M1.3 design planning, Tuesday T1.5-T1.8 (manifest schema)

---

## Daily Workflow

### Morning (Before Standup)

1. **Update task board** - Mark yesterday's tasks as complete
2. **Review today's tasks** - Read the specific day section in PHASE-1-WEEK1-SPRINT-TASKS.md
3. **Identify blockers** - Any issues preventing progress?
4. **Pull latest code** - `git pull origin main` (in case Tech Lead merged anything)

### Development

**Keep focus on 1-2 tasks per day.** Reference the daily breakdown:

**Monday:**
- M1.4 (Dev A): Create state-machine.ts
- M1.5 (Dev A): Create unit tests
- T1.5-T1.8 (Dev B): Plan manifest schema

**Tuesday:**
- T1.1-T1.4 (Dev A): Code review, audit trail, integration tests
- T1.6-T1.8 (Dev B): Create types, validator, tests

**Wednesday:**
- W1.1-W1.7: Finalization and QA verification

**Thursday:**
- Th1.1-Th1.7: Review, retrospective, planning

**Friday:**
- F1.1-F1.8: Final testing, metrics, closure

### Afternoon (Before Standup)

1. **Test your code** - `npm test -- [your-module]`
2. **Commit progress** - `git commit -m "WIP: [task description]"`
3. **Push to branch** - `git push origin [your-branch]`
4. **Update task board** - Mark tasks as "In Progress" or "Done"

### Standup (5:00-5:15 PM)

Say briefly:
1. **Status:** What did I do today?
2. **Blockers:** What's stopping me?
3. **Next:** What's next?

**Example:**
> "Dev A here. Finished M1.5 - wrote 8 unit tests for state machine transitions. All passing. Pushing code now. No blockers. Tomorrow I'll do code review and start audit trail work."

---

## Code Quality Standards

### TypeScript
- ✓ All functions have explicit parameter and return types
- ✓ No `any` or `implicit any`
- ✓ Run `npm run type-check` before committing

### Testing
- ✓ Write tests ALONGSIDE code (TDD style)
- ✓ Aim for 80%+ coverage
- ✓ Test both happy path AND error cases

**Example test structure:**
```typescript
describe('StateTransitionValidator', () => {
  it('should allow draft -> approved transition', () => {
    const validator = new StateTransitionValidator();
    expect(validator.isValidTransition('draft', 'approved')).toBe(true);
  });

  it('should reject draft -> completed transition', () => {
    const validator = new StateTransitionValidator();
    expect(() => validator.isValidTransition('draft', 'completed'))
      .toThrow('Invalid transition');
  });
});
```

### Code Review Checklist

Before pushing for review, verify:
- [ ] Code compiles without errors
- [ ] All tests passing (`npm test`)
- [ ] No TypeScript warnings
- [ ] Comments added for complex logic
- [ ] File structure matches design
- [ ] Acceptance criteria met

---

## File Structure

```
katana-vectorbt-optimizer/
├── src/
│   ├── core/
│   │   ├── strategy-lifecycle/
│   │   │   ├── state-machine.ts (dev A)
│   │   │   └── audit-trail.ts (dev A)
│   │   └── journal/
│   │       ├── manifest-types.ts (dev B)
│   │       ├── manifest-validator.ts (dev B)
│   │       └── manifest-schema.json (dev B)
│   └── ...
├── tests/
│   ├── unit/
│   │   ├── strategy-lifecycle/
│   │   │   ├── state-machine.test.ts
│   │   │   └── audit-trail.test.ts
│   │   └── journal/
│   │       └── manifest-types.test.ts
│   └── integration/
│       └── strategy-lifecycle-flow.test.ts
├── docs/
│   ├── state-machine.md (dev A)
│   ├── audit-trail.md (dev A)
│   ├── manifest-schema.md (dev B)
│   └── examples/
│       └── manifest-example.json (dev B)
├── package.json
├── tsconfig.json
└── README.md
```

---

## Testing Commands

```bash
# Run all tests
npm test

# Run specific test file
npm test -- state-machine.test.ts
npm test -- manifest-types.test.ts

# Run with coverage report
npm run coverage

# Run with watch mode (auto-rerun on file changes)
npm test -- --watch

# Type checking
npm run type-check

# Lint and format
npm run lint
npm run format
```

---

## Common Tasks

### I finished a task, what's next?

1. **Verify acceptance criteria** - Check that all AC are met
2. **Run tests** - `npm test -- [your-module]` should show all passing
3. **Commit** - `git commit -m "feat: [task description]"`
4. **Push** - `git push origin [your-branch]`
5. **Update task board** - Mark task as "Done" or "Ready for Review"
6. **Notify Tech Lead** - "Ready for code review"

### My code doesn't compile, what do I do?

1. **Check error message** - `npm run build` shows what's wrong
2. **Common issues:**
   - Missing type definition → add explicit type
   - Unused variable → remove or use it
   - Import error → check file path
3. **Ask for help** - If stuck >10 min, ask Tech Lead in Slack

### I need to merge my code, what's the process?

1. **Local verification:**
   ```bash
   npm test                 # All tests passing?
   npm run type-check      # Zero errors?
   npm run lint            # Lint clean?
   ```
2. **Create Pull Request** - GitHub PRs with description
3. **Code Review** - Wait for Tech Lead approval
4. **Merge** - Tech Lead merges to main
5. **Pull latest** - `git checkout main && git pull origin main`

---

## Quick Reference: Acceptance Criteria

### S-STRATEGY-001 Must Have:

- [ ] **AC1.1** State machine with 5 states: draft, approved, active, completed, archived
- [ ] **AC1.2** Invalid transitions are rejected with clear error message
- [ ] **AC1.3** Transition rules match specification (see `/docs/state-machine.md`)
- [ ] **AC1.4** Audit trail logs state changes with timestamp and actor ID
- [ ] **AC1.5** 10+ unit tests, all passing
- [ ] **AC1.6** Full TypeScript type coverage, zero implicit any

### S-JOURNAL-001 Must Have:

- [ ] **AC2.1** manifest.json schema with: strategyId, version, status, metadata, parameters
- [ ] **AC2.2** TypeScript interfaces exported: ManifestMetadata, ManifestParameters, StrategyManifest
- [ ] **AC2.3** Validation logic that accepts valid manifests, rejects invalid ones
- [ ] **AC2.4** JSON Schema file at `/src/core/journal/manifest-schema.json`
- [ ] **AC2.5** 8+ unit tests, all passing

---

## Help & Support

**Questions?** Ask in Slack #week1-sprint or mention @tech-lead

**Stuck?** Follow this escalation:
1. Check the documentation (PHASE-1-WEEK1-SPRINT-TASKS.md)
2. Ask team member on Slack
3. Call Tech Lead for sync discussion

**Want to pair program?** Say in standup: "I'd like to pair on [task]"

---

## Success Metrics

By Friday EOD, we should have:

| Metric | Target |
|--------|--------|
| S-STRATEGY-001 complete | 13 pts |
| S-JOURNAL-001 complete | 8 pts |
| Total delivered | 21 pts |
| Unit tests passing | 24 tests |
| Test coverage | >80% |
| Code reviews approved | 2/2 stories |
| Bugs found | 0 |
| Blockers | 0 |

---

## Key Files to Keep Open

1. **PHASE-1-WEEK1-SPRINT-TASKS.md** - Daily task breakdown
2. **WEEK1-DAILY-REFERENCE.md** - Quick checklist
3. Your IDE with TypeScript/Node.js support
4. Terminal for `npm test` commands
5. Slack for team communication

---

## Monday 9 AM Checklist

Before the 9 AM kickoff meeting:

- [ ] Clone/pull repo
- [ ] Install dependencies (`npm install`)
- [ ] Verify build works (`npm run build`)
- [ ] Create feature branch
- [ ] Open PHASE-1-WEEK1-SPRINT-TASKS.md
- [ ] Join Slack #week1-sprint
- [ ] Have IDE open and ready

**You're ready to go!**

---

*Questions before we start?* Ask in Slack now.
*Let's build Week 1!*
