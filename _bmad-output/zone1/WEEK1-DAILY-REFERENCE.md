# Week 1 Daily Reference Card

**Sprint:** Phase 1 - Week 1 (Mar 3-7, 2026)
**Target:** 21 story points (13 + 8)
**Team:** Dev A, Dev B, QA, Tech Lead

---

## Monday, March 3 - "Foundation & Architecture"

### Status Board
| Task | Owner | Duration | Status | Done? |
|------|-------|----------|--------|-------|
| M1.1: Kickoff | Tech Lead | 0.5h | Scheduled | [ ] |
| M1.2: Setup | Dev A+B | 1.5h | Scheduled | [ ] |
| M1.3: Design | Tech Lead+A | 1h | Scheduled | [ ] |
| M1.4: Code State Machine | Dev A | 2.5h | Scheduled | [ ] |
| M1.5: Unit Tests | Dev A | 1.5h | Scheduled | [ ] |
| **Daily Total** | | **6.5h** | | |

### Key Outputs
- [ ] State machine specification.md complete
- [ ] state-machine.ts created (150-200 LOC)
- [ ] 8+ unit tests written
- **Target End-of-Day:** Dev A has code + tests ready for review

### Standup Questions
**Dev A:** What state machine patterns did you implement? Any edge cases found?
**Dev B:** How's manifest schema planning going? Any unknowns?
**Tech Lead:** Architecture decisions locked in? Ready for code review tomorrow?

---

## Tuesday, March 4 - "Core Development & Parallel Progress"

### Status Board
| Task | Owner | Duration | Status | Done? |
|------|-------|----------|--------|-------|
| T1.1: Code Review | Tech Lead | 1h | Scheduled | [ ] |
| T1.2: Audit Trail | Dev A | 1.5h | Scheduled | [ ] |
| T1.3: Audit Tests | Dev A | 1h | Scheduled | [ ] |
| T1.4: Integration Test | Dev A | 1h | Scheduled | [ ] |
| T1.5: Design | Dev B+TL | 1h | Scheduled | [ ] |
| T1.6: Types | Dev B | 1.5h | Scheduled | [ ] |
| T1.7: Validator | Dev B | 1h | Scheduled | [ ] |
| T1.8: Tests | Dev B | 1h | Scheduled | [ ] |
| **Daily Total** | | **9h** | | |

### Key Outputs
- [ ] State machine code approved and merged
- [ ] audit-trail.ts complete (200 LOC)
- [ ] manifest-types.ts complete (150 LOC)
- [ ] manifest-validator.ts complete (200 LOC)
- [ ] 5 audit tests passing
- [ ] 8 manifest tests passing
- **Target End-of-Day:** Both stories 80% complete, tests passing

### Standup Questions
**Dev A:** Code review feedback addressed? Audit trail integrated cleanly?
**Dev B:** Types and validator working together? Any schema issues discovered?
**Tech Lead:** Anything blocking either dev? Ready to finalize Wednesday?

---

## Wednesday, March 5 - "Finalization & Acceptance"

### Status Board
| Task | Owner | Duration | Status | Done? |
|------|-------|----------|--------|-------|
| W1.1: Final Integration | Dev A | 1h | Scheduled | [ ] |
| W1.2: Final Integration | Dev B | 1h | Scheduled | [ ] |
| W1.3: QA Verification | QA | 1.5h | Scheduled | [ ] |
| W1.4: Code Review Final | Tech Lead | 1h | Scheduled | [ ] |
| W1.5: Code Review Final | Tech Lead | 1h | Scheduled | [ ] |
| W1.6: Completion Report | Tech Lead | 1h | Scheduled | [ ] |
| W1.7: Deployment Check | Dev A+B | 0.5h | Scheduled | [ ] |
| **Daily Total** | | **7.5h** | | |

### Key Outputs - AC Verification
**S-STRATEGY-001:**
- [ ] AC1.1: 5 states + transitions verified ✓
- [ ] AC1.2: Invalid transitions rejected ✓
- [ ] AC1.3: Transition rules match spec ✓
- [ ] AC1.4: Audit trail logs all changes ✓
- [ ] AC1.5: 10+ unit tests passing ✓
- [ ] AC1.6: TypeScript strict types ✓

**S-JOURNAL-001:**
- [ ] AC2.1: Schema structure complete ✓
- [ ] AC2.2: TypeScript types exported ✓
- [ ] AC2.3: Validation logic works ✓
- [ ] AC2.4: JSON schema file created ✓
- [ ] AC2.5: 8+ unit tests passing ✓

**Target End-of-Day:** Both stories 100% complete, QA signed off, ready to merge

### Standup Questions
**QA:** Any acceptance criteria failures? Edge cases found?
**Dev A & B:** All tests passing locally? Ready to merge?
**Tech Lead:** Code quality acceptable? Any tech debt to capture?

---

## Thursday, March 6 - "Sprint Review & Planning"

### Status Board
| Task | Owner | Duration | Status | Done? |
|------|-------|----------|--------|-------|
| Th1.1: Sprint Review | Team | 1.5h | Scheduled | [ ] |
| Th1.2: Retrospective | Team | 1h | Scheduled | [ ] |
| Th1.3: Status Update | Tech Lead | 0.5h | Scheduled | [ ] |
| Th1.4: Week 2 Planning | Team | 1.5h | Scheduled | [ ] |
| Th1.5: Week 2 Breakdown | Tech Lead | 1h | Scheduled | [ ] |
| Th1.6: Week 2 Prep | Dev B | 0.5h | Scheduled | [ ] |
| Th1.7: Archive | Tech Lead | 0.5h | Scheduled | [ ] |
| **Daily Total** | | **6.5h** | | |

### Key Outputs
- [ ] Sprint Review demo complete
- [ ] Retrospective notes captured (3-5 items)
- [ ] Project status updated
- [ ] Week 2 sprint plan created
- [ ] PHASE-1-WEEK2-SPRINT-TASKS.md created
- [ ] Week 1 artifacts archived
- [ ] Week 2 blockers identified
- **Target End-of-Day:** Week 2 ready to go, all stakeholders updated

### Sprint Review Demo Talking Points
1. **State Machine:** Show 5 states, valid/invalid transitions, audit trail in action
2. **Manifest Schema:** Show JSON validation, TypeScript types, examples
3. **Metrics:** 21 pts committed, 21 pts delivered = 100%. 24 tests passing. 80%+ coverage.
4. **Team:** Excellent collaboration, no blockers, on track for Phase 1.

### Retrospective Topics
- What went well? (architecture clarity, parallel work, TDD)
- What to improve? (any surprises? any process gaps?)
- Actions for next sprint? (training? tooling? process changes?)

### Standup Questions
**Entire Team:** How did this week feel? Any surprises or blockers?
**Dev A & B:** Ready for Week 2 stories? Anything you need?
**Tech Lead:** Velocity on target? Any quality concerns?

---

## Friday, March 7 - "Final Verification & Closure"

### Status Board
| Task | Owner | Duration | Status | Done? |
|------|-------|----------|--------|-------|
| F1.1: Regression Testing | QA | 1.5h | Scheduled | [ ] |
| F1.2: Doc Review | Tech Lead | 1h | Scheduled | [ ] |
| F1.3: Performance Test | Dev A | 0.5h | Scheduled | [ ] |
| F1.4: Metrics | Tech Lead | 1h | Scheduled | [ ] |
| F1.5: Closure Checklist | Tech Lead | 0.5h | Scheduled | [ ] |
| F1.6: Summary Report | Tech Lead | 1h | Scheduled | [ ] |
| F1.7: Stakeholder Comm | Tech Lead | 0.5h | Scheduled | [ ] |
| F1.8: Git Tagging | Dev A | 0.25h | Scheduled | [ ] |
| **Daily Total** | | **6.25h** | | |

### Final Checklist
- [ ] All regression tests passing
- [ ] All docs reviewed and complete
- [ ] Performance baseline established
- [ ] Metrics collected (LOC, coverage, velocity)
- [ ] Sprint closure checklist 100% complete
- [ ] Summary report written
- [ ] Stakeholders notified
- [ ] Git tagged with `week1-complete`
- [ ] Week 2 ready to begin Monday

### Metrics to Collect
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Story Points Delivered | 21 | 21 | ✓ |
| Test Pass Rate | 100% | ? | |
| Test Coverage | >80% | ? | |
| Code Review Approvals | 2/2 | ? | |
| Bugs Found | 0 | ? | |
| Build Success | 5/5 | ? | |

### Standup Questions (Final)
**QA:** All regression tests passing? Any issues discovered in final testing?
**Dev A & B:** Anything to note for Week 2? Any patterns to reuse?
**Tech Lead:** Velocity sustained? Quality maintained? Recommendations for Phase 1?

---

## Critical Success Factors (CSF)

### Monday
- [ ] Team clarity on S-STRATEGY-001 and S-JOURNAL-001 requirements
- [ ] Dev A has state machine code + tests by EOD (not perfect, ready for review)
- [ ] Dev B understands manifest schema design

### Tuesday
- [ ] Dev A: Audit trail integrated, all code ready for Wed review
- [ ] Dev B: Types + validator complete, all tests passing
- [ ] Zero blockers identified

### Wednesday
- [ ] Both stories pass all acceptance criteria
- [ ] QA sign-off obtained
- [ ] Code review approved and merged
- [ ] No new bugs found in regression testing

### Thursday
- [ ] Sprint review demo successful (stakeholder engagement)
- [ ] Retrospective conducted (team morale + learnings captured)
- [ ] Week 2 sprint plan finalized (no delays to Week 2 kickoff)
- [ ] Week 1 artifacts archived (clean project state)

### Friday
- [ ] All metrics collected and documented
- [ ] Stakeholders notified of completion
- [ ] Team ready for Week 2 Monday kickoff
- [ ] No outstanding issues or blockers

---

## Team Contact Info

| Role | Name | Contact | Phone |
|------|------|---------|-------|
| Tech Lead | [Name] | [Email] | [Phone] |
| Dev A (Backend) | [Name] | [Email] | [Phone] |
| Dev B (Schema) | [Name] | [Email] | [Phone] |
| QA Engineer | [Name] | [Email] | [Phone] |

## Daily Standup Times

- **Monday-Friday:** 17:00-17:15 (5 min standup)
- **Location:** [Slack, Zoom, or in-person]
- **Format:** Status, Blockers, Next steps

## Emergency Contact

**If critical blocker discovered:**
1. Notify Tech Lead immediately
2. Document issue in Slack #week1-sprint channel
3. Call emergency 30-min sync if needed

---

## Helpful Links

- Jira Board: [link]
- GitHub Project: [link]
- Documentation: [link to /docs folder]
- Slack Channel: #week1-sprint
- Drive Folder: [shared drive link]

---

**Print this card and keep it visible throughout Week 1.**
**Update status at end of each day (mark [x] for completed tasks).**
