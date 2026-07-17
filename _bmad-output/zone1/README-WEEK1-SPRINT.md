# Phase 1 - Week 1 Sprint Planning Package

**Project:** Katana Vectorbt Optimizer
**Phase:** Phase 1 - Core Foundation
**Sprint:** Week 1 (March 3-7, 2026)
**Target:** 21 story points
**Team:** Dev A, Dev B, QA Engineer, Tech Lead

---

## 📦 What's in This Package?

This folder contains everything needed to execute Phase 1, Week 1 sprint successfully. Five comprehensive documents provide detailed planning, daily tasks, quick references, and import files.

### Documents Overview

#### 1. **PHASE-1-WEEK1-SPRINT-TASKS.md** (PRIMARY - 5000+ words)
**The Master Plan** - Detailed daily breakdown with all tasks, subtasks, acceptance criteria, and verification steps.

**Who should read:** Everyone (especially Dev A and Dev B)
**When:** Before starting work each day
**Key sections:**
- Executive Summary
- Daily breakdown (Monday-Friday with hourly breakdown)
- Acceptance criteria checklist (AC1.1-AC1.6 for S-STRATEGY-001; AC2.1-AC2.5 for S-JOURNAL-001)
- Testing summary (24 unit tests, 3 integration tests)
- Code quality metrics
- Deliverable files list

**How to use:**
- Tech Lead: Share with team, reference for daily standups
- Dev A: Focus on Mon-Wed sections (state machine)
- Dev B: Focus on Tue-Wed sections (manifest schema)
- QA: Use acceptance criteria and verification steps

---

#### 2. **WEEK1-EXECUTION-SUMMARY.md** (1500+ words)
**The Overview** - High-level summary of what's being built, why, and how.

**Who should read:** Stakeholders, managers, team leads
**When:** Before planning discussion or status updates
**Key sections:**
- What's being delivered (2 stories, 21 pts)
- Daily breakdown (hours planned per day)
- Critical path & dependencies
- Team assignments
- Success metrics & risk management
- Milestones and next steps

**How to use:**
- Share with stakeholders before sprint kickoff
- Reference for sprint review/demo
- Use for velocity tracking and reporting

---

#### 3. **WEEK1-DAILY-REFERENCE.md** (1000+ words)
**The Quick Reference** - Printable card for desk/screen during daily work.

**Who should read:** Entire team
**When:** Every morning before work
**Key sections:**
- Status board for each day (tasks, durations, status checkboxes)
- Key outputs expected (what should be done by EOD)
- Standup questions (what to discuss at 5 PM)
- Daily critical success factors
- Final checklist and metrics table

**How to use:**
- Print and post near desk
- Update checkboxes as tasks complete
- Reference standup questions at 5 PM
- Track metrics collection Friday

---

#### 4. **WEEK1-QUICK-START.md** (1200+ words)
**The Team Onboarding Guide** - Get everyone ready Monday morning.

**Who should read:** Dev A, Dev B (especially on Monday)
**When:** Monday morning before 9 AM
**Key sections:**
- TL;DR summary (what are we building?)
- Getting started (environment setup, Git branches)
- Daily workflow (morning/dev/afternoon/standup)
- Code quality standards (TypeScript, testing, reviews)
- File structure (where files go)
- Testing commands (how to run tests)
- Common tasks (what to do when...)
- Quick reference (AC list)

**How to use:**
- Send to Dev A & Dev B Friday before sprint
- Review Monday morning before kickoff
- Keep open during development as reference
- Troubleshoot using "Common Tasks" section

---

#### 5. **WEEK1-TASKS-JIRA-IMPORT.csv** (CSV format)
**The Project Import File** - Import all tasks directly into Jira/GitHub Projects.

**Who should use:** Tech Lead or Project Manager
**When:** Monday morning, before sprint kickoff
**Includes:**
- 34 subtasks (M1.1 through F1.8)
- 2 main stories (S-STRATEGY-001, S-JOURNAL-001)
- All metadata: points, assignees, due dates, labels
- Acceptance criteria for each task

**How to use:**
```bash
# Import to Jira
jira import --format csv WEEK1-TASKS-JIRA-IMPORT.csv

# Or GitHub Projects
gh project view [project-id] --format csv < WEEK1-TASKS-JIRA-IMPORT.csv

# Or copy-paste into tool of choice
```

**Benefit:** Saves 1-2 hours of manual task creation

---

## 🎯 Quick Start (Monday 9 AM)

### For Tech Lead (30 min before kickoff)
1. [ ] Read WEEK1-EXECUTION-SUMMARY.md (10 min)
2. [ ] Print WEEK1-DAILY-REFERENCE.md (2 min)
3. [ ] Import WEEK1-TASKS-JIRA-IMPORT.csv (5 min)
4. [ ] Share all docs with team in Slack (3 min)
5. [ ] Open PHASE-1-WEEK1-SPRINT-TASKS.md on screen

### For Dev A & Dev B (Monday morning)
1. [ ] Read WEEK1-QUICK-START.md (15 min)
2. [ ] Clone repo and run `npm install` (10 min)
3. [ ] Create feature branches (5 min)
4. [ ] Join Slack #week1-sprint (2 min)
5. [ ] Ready for 9 AM kickoff

### For QA (Monday morning)
1. [ ] Read "Acceptance Criteria Checklist" section in PHASE-1-WEEK1-SPRINT-TASKS.md (10 min)
2. [ ] Bookmark the verification steps (W1.3 section) (2 min)
3. [ ] Prepare test environment (5 min)
4. [ ] Ready for Wednesday QA verification

---

## 📋 What We're Building

### Story 1: S-STRATEGY-001 (13 points) - State Machine
**Owner:** Dev A | **Duration:** Mon-Wed | **Blocking:** Everything else

```
Create a state machine that manages strategy lifecycle:
- 5 states: draft → approved → active → completed → archived
- Transition validation (prevent invalid transitions)
- Audit trail (log all state changes with timestamp)
- 10+ unit tests + integration tests
```

**Files Created:**
- `/src/core/strategy-lifecycle/state-machine.ts`
- `/src/core/strategy-lifecycle/audit-trail.ts`
- `/tests/unit/strategy-lifecycle/*.test.ts`
- `/docs/state-machine.md`
- `/docs/audit-trail.md`

**Success:** All acceptance criteria (AC1.1-AC1.6) met, 13 tests passing

---

### Story 2: S-JOURNAL-001 (8 points) - Manifest Schema
**Owner:** Dev B | **Duration:** Tue-Wed | **Blocking:** Journal epics

```
Create JSON schema and TypeScript types for strategy manifests:
- Schema structure: strategyId, version, status, metadata, parameters
- TypeScript interfaces for type safety
- Validation logic (accept valid, reject invalid)
- 8+ unit tests
```

**Files Created:**
- `/src/core/journal/manifest-types.ts`
- `/src/core/journal/manifest-validator.ts`
- `/src/core/journal/manifest-schema.json`
- `/tests/unit/journal/*.test.ts`
- `/docs/manifest-schema.md`
- `/docs/examples/manifest-example.json`

**Success:** All acceptance criteria (AC2.1-AC2.5) met, 8 tests passing

---

## 📊 Sprint Metrics

| Metric | Target | Expected |
|--------|--------|----------|
| Story Points | 21 | 21 ✓ |
| Unit Tests | 20+ | 24 ✓ |
| Integration Tests | 2+ | 3 ✓ |
| Test Coverage | >75% | 80%+ ✓ |
| Code Reviews | 2/2 | 2/2 ✓ |
| Bugs Found | 0 | 0 ✓ |
| Blocker Issues | 0 | 0 ✓ |
| Build Success | 100% | 100% ✓ |

**Sprint Definition of Done:** All metrics hit targets by Friday EOD

---

## 🔄 Daily Workflow

### Morning (Every Day)
1. Read relevant day section in PHASE-1-WEEK1-SPRINT-TASKS.md
2. Check WEEK1-DAILY-REFERENCE.md status board
3. Pull latest code: `git pull origin main`
4. Identify any blockers

### Development (All Day)
1. Follow daily task breakdown
2. Write code + tests (test-driven approach)
3. Commit progress: `git commit -m "WIP: [task]"`
4. Run tests: `npm test`

### Afternoon (Before Standup)
1. Ensure all tests passing
2. Verify code compiles: `npm run build`
3. Push to branch: `git push origin [your-branch]`
4. Update task board

### Standup (5:00-5:15 PM)
1. **Status:** What did I do today?
2. **Blockers:** What's stopping me?
3. **Next:** What's next?

---

## 🚀 Critical Path

### Blocking Chain
```
S-STRATEGY-001 (Dev A, 13 pts) → S-STRATEGY-002/003 (Week 2)
S-JOURNAL-001 (Dev B, 8 pts) → S-JOURNAL-002/003 (Week 2)
Both → E-COMPARE-WORKFLOW, E-AUDIT-TRAIL (Week 5+)
```

**Impact:** If either story slips by 1 day, Week 2 starts 1 day late.

### Risk Mitigation
- Start immediately Monday morning
- Code review same day (Tuesday)
- QA verification Wednesday morning
- Merge by Wednesday afternoon
- Friday = buffer for any issues

---

## 📞 Team Communication

### Daily Standup (5:00-5:15 PM)
- **Location:** [Slack, Zoom, or in-person]
- **Time:** 15 minutes sharp
- **Format:** Status, Blockers, Next

### Slack Channel
- **Channel:** #week1-sprint
- **Use for:** Quick questions, blocker escalation, progress updates
- **Avoid:** Long discussions (use sync meetings instead)

### Emergency Escalation
**If critical blocker:** Call Tech Lead immediately, don't wait for standup

---

## ✅ Success Checklist

### Monday EOD
- [ ] Environment setup complete (npm install works)
- [ ] State machine code started (M1.4 half-done)
- [ ] Team questions answered

### Tuesday EOD
- [ ] State machine code complete (M1.4 + M1.5)
- [ ] Code review started (T1.1)
- [ ] Manifest schema started (T1.6 half-done)

### Wednesday EOD
- [ ] Both stories complete
- [ ] Both stories code reviewed
- [ ] QA signed off on acceptance criteria
- [ ] Ready to merge

### Thursday EOD
- [ ] Sprint review demo completed
- [ ] Retrospective conducted
- [ ] Week 2 sprint plan complete

### Friday EOD
- [ ] Regression testing passed
- [ ] Metrics collected
- [ ] Sprint officially closed
- [ ] Week 2 ready to start Monday

---

## 📁 File Locations

All files located in: `_bmad-output/zone1/`

```
PHASE-1-WEEK1-SPRINT-TASKS.md ← START HERE (master plan)
WEEK1-EXECUTION-SUMMARY.md ← Share with stakeholders
WEEK1-DAILY-REFERENCE.md ← Print and keep visible
WEEK1-QUICK-START.md ← Share with Dev A/B Monday
WEEK1-TASKS-JIRA-IMPORT.csv ← Import to project tool
README-WEEK1-SPRINT.md ← This file
```

---

## 📖 Reading Guide

**For Different Audiences:**

| Role | Primary | Secondary | Reference |
|------|---------|-----------|-----------|
| **Tech Lead** | EXECUTION-SUMMARY | SPRINT-TASKS | JIRA-IMPORT |
| **Dev A** | QUICK-START | SPRINT-TASKS (Mon-Wed) | DAILY-REFERENCE |
| **Dev B** | QUICK-START | SPRINT-TASKS (Tue-Wed) | DAILY-REFERENCE |
| **QA** | SPRINT-TASKS (AC section) | EXECUTION-SUMMARY | DAILY-REFERENCE |
| **Stakeholder** | EXECUTION-SUMMARY | SPRINT-TASKS (summary) | - |

---

## 🎓 Learning & Knowledge Transfer

### Code Patterns Established in Week 1
1. **State Machine Pattern** - Used for strategy lifecycle
2. **Audit Trail Pattern** - Used for event logging
3. **Validation Pattern** - Used for schema/data validation
4. **Test-Driven Development** - Core approach for quality

### Reusable Artifacts
- State machine template → can be reused for other entities
- Audit trail class → can be reused for other workflows
- Manifest schema → can be extended for other resource types
- Test structure → can be copied for other modules

---

## 🔗 Related Documents

**Phase 1 Related:**
- `sprint-plan-phase1.md` (overall phase plan with 6 sprints)
- `sprint-status.yaml` (weekly status tracking)

**Architecture Related:**
- Phase 1 brief (from product/design phase)
- Architecture decision records (decisions made)

**Team Related:**
- Team availability calendar
- Skills matrix
- Code review guidelines

---

## ✨ Pro Tips

1. **Version Control:** Push to branch multiple times per day (not just EOD)
2. **Testing:** Run tests after every change, not just at task completion
3. **Code Review:** Request review same day you finish, not next day
4. **Documentation:** Add comments/docs alongside code, not after
5. **Standup:** Be specific ("finished M1.5: state machine unit tests") not vague ("working on tasks")
6. **Blockers:** Communicate immediately, not at standup
7. **Slack:** Use threads to keep discussions organized
8. **Commits:** Write good commit messages (helps with code review)

---

## 🚨 Known Constraints

- **Timeline:** 5 working days (no flexibility, deadline Friday)
- **Capacity:** 20 pts/week (21 pts committed is 1 pt over, acceptable as buffer)
- **People:** No additional resources (team of 4 fixed)
- **Scope:** Both stories must be 100% done (no partial completion)

---

## 🎯 Vision for Phase 1

Week 1 establishes the foundation for Phase 1 Core Foundation. Once both stories are done:

- **Week 2:** Approval workflows + kill-switch logic
- **Week 3:** State timeline + rejection logic
- **Week 4:** Database persistence (Postgres)
- **Week 5:** Telemetry instrumentation
- **Week 6-7:** Comparison & audit features

**By end of Phase 1 (7 weeks):** Fully functional strategy lifecycle, data persistence, metrics, comparison, and audit trail.

---

## ❓ FAQ

**Q: What if I get stuck?**
A: 1. Check this README, 2. Ask on Slack, 3. Call Tech Lead

**Q: Do I need to do all tasks exactly as written?**
A: No, use as guide. Tech Lead can adjust based on progress.

**Q: What if I finish early?**
A: Good! Help other dev, or start next task early (with TL approval)

**Q: Can I work remotely?**
A: Yes, all communication via Slack/Zoom. Just be available for standups.

**Q: What if something breaks?**
A: Tell Tech Lead immediately. We'll fix it together.

---

## 📝 Document Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-02-27 | Initial creation - 5 documents |
| - | - | - |

---

## 🏁 Ready to Start?

1. ✅ Download all 5 files from this folder
2. ✅ Tech Lead: Import CSV to Jira/GitHub Projects
3. ✅ Team: Read WEEK1-QUICK-START.md Monday morning
4. ✅ Everyone: Join Slack #week1-sprint
5. ✅ Tech Lead: Send this README to team Friday before

**Monday 9 AM: Sprint Kickoff - Let's build Phase 1! 🚀**

---

*For questions or issues, reach out to Tech Lead.*
*For updates, check Slack #week1-sprint.*
*Status updates posted daily at standup.*

**Good luck, team! Make Week 1 count!**
