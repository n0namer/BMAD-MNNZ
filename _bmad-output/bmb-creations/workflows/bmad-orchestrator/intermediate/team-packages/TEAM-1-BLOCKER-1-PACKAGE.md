# TEAM 1: BLOCKER-1 PACKAGE - State Machine & Workflow Control

**Project:** Katana Vectorbt Optimizer - Phase 2 Implementation
**Team:** Backend Team 1 (State Management)
**Blocker:** BLOCKER-1
**Package Created:** 2026-02-26
**Duration:** 8 weeks (Weeks 1-8)

---

## EXECUTIVE SUMMARY

Team 1 is responsible for implementing the foundational state machine architecture that controls the entire Journal Keeper System lifecycle. This work is **CRITICAL** and **BLOCKING** all other backend teams. The state machine manages the complete lifecycle of ideas: from initial submission (IDLE → CANDIDATE) through paper publication (PAPER) to active project execution (MICRO_LIVE) and completion/termination.

### Key Deliverables
- State machine engine with 10+ defined state transitions
- Rejection workflow with resubmission logic
- Timeout handling for 4 different timeout scenarios
- Kill-switch mechanism with automatic and manual triggers
- Comprehensive audit trail (30+ unit tests minimum)

### Business Impact
- Enables reproducibility via state tracking
- Controls resource allocation through state gating
- Provides compliance audit trail for all state changes
- Foundation for all downstream epics (Teams 2-5 depend on this)

---

## EPIC ASSIGNMENT

**Epic ID:** E-STRATEGY-LIFECYCLE
**Priority:** CRITICAL
**Complexity:** HIGH
**Total Story Points:** 34
**Minimum Tests:** 30 unit tests

### Epic Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Minimum 30 unit tests covering all state transitions
- State machine diagram documented and validated
- Approval workflow tested with 5+ scenarios
- Kill-switch functionality verified for all states

---

## STORY BREAKDOWN

### Story 1: S-STRATEGY-001 - Implement State Machine Transitions
**Points:** 13 | **Dependencies:** None | **Tests Required:** 10+

#### Description
Build state machine for strategy lifecycle with support for these transitions:
- IDLE → CANDIDATE (idea submission)
- CANDIDATE → PAPER (submit for publication)
- PAPER → MICRO_LIVE (launch project)
- MICRO_LIVE → COMPLETED (project completion)
- Any state → REJECTED_* (rejection paths)
- Any state → KILLED_* (termination)

#### Acceptance Criteria
1. State transitions defined and validated in code
2. Invalid transitions rejected with clear error messages
3. Audit trail tracks all transitions with timestamps
4. Idempotent transitions supported (same request twice = success on both)
5. Concurrent transitions handled safely (no race conditions)
6. State rollback on error (transaction-like behavior)
7. 10+ unit tests covering primary and edge cases

#### Implementation Checklist
- [ ] Define state enum (IDLE, CANDIDATE, PAPER, MICRO_LIVE, COMPLETED, REJECTED_CANDIDATE, REJECTED_PAPER, KILLED_BY_THRESHOLD, KILLED_MANUAL, etc.)
- [ ] Create state transition table/validation matrix
- [ ] Implement transition engine with validation
- [ ] Add audit trail logging to each transition
- [ ] Handle concurrent access (locking/versioning)
- [ ] Add rollback mechanism for failed transitions
- [ ] Write 10+ unit tests (ST-001 through ST-010 from test spec)
- [ ] Document state diagram (Mermaid or similar)

#### Test Scenarios Covered
- ST-001: IDLE → CANDIDATE transition with logging
- ST-002: CANDIDATE → PAPER with paper reference linking
- ST-003: PAPER → MICRO_LIVE with metadata initialization
- ST-004: MICRO_LIVE → COMPLETED with metrics finalization
- ST-005: Invalid transition rejection
- ST-006: State rollback on error
- ST-007: Concurrent transition handling
- ST-008: State audit trail chronological ordering
- ST-009: Transition with blockers (dependencies)
- ST-010: Idempotent transition handling

#### Files to Create/Modify
- `lib/state-machine.ts` - Core state machine implementation
- `lib/state-machine.spec.ts` - Unit tests (10+ tests)
- `docs/state-machine-diagram.md` - State diagram and documentation

---

### Story 2: S-STRATEGY-002 - Build Approval Workflow
**Points:** 8 | **Dependencies:** S-STRATEGY-001 | **Tests Required:** 8+

#### Description
Implement approval workflow enabling reviewers to approve/reject strategies with comments and audit trails. Integrates with state machine for CANDIDATE → PAPER transition.

#### Acceptance Criteria
1. Reviewers can be assigned to pending strategies (CANDIDATE state)
2. Approval and rejection decisions recorded with rationale
3. Comments captured with approval decisions
4. Notification system alerts reviewers when assigned
5. Approver authorization verified (permission checks)
6. 8+ unit tests for approval scenarios

#### Implementation Checklist
- [ ] Create reviewer assignment service
- [ ] Implement approval/rejection decision endpoints
- [ ] Add comment capture and storage
- [ ] Build notification system (email/webhook)
- [ ] Add authorization checks for approver roles
- [ ] Create audit trail for approval events
- [ ] Write 8+ unit tests for approval workflows
- [ ] Integrate with state machine (trigger CANDIDATE → PAPER)

#### Test Scenarios Covered
- Assign reviewer to strategy
- Approve strategy with comment
- Reject strategy with feedback (mandatory)
- Multiple reviewers approval sequence
- Authorization check on rejection (RJ-004)
- Resubmission after rejection

#### Files to Create/Modify
- `lib/approval-service.ts` - Approval workflow logic
- `lib/approval-service.spec.ts` - Unit tests (8+ tests)
- `lib/notification-service.ts` - Reviewer notifications

---

### Story 3: S-STRATEGY-003 - Add Kill-Switch Mechanism
**Points:** 5 | **Dependencies:** S-STRATEGY-001 | **Tests Required:** 5+

#### Description
Implement kill-switch to immediately stop strategy execution from any state. Supports both automatic (threshold breach) and manual triggers with full audit trail.

#### Acceptance Criteria
1. Kill-switch callable from ACTIVE state (MICRO_LIVE)
2. Graceful shutdown of running strategy (cleanup operations)
3. Final state recorded as KILLED (KILLED_BY_THRESHOLD or KILLED_MANUAL)
4. Cleanup operations executed (stop running tasks, release resources)
5. Dependent items notified of termination
6. 5+ unit tests for all kill-switch scenarios

#### Implementation Checklist
- [ ] Create kill-switch handler service
- [ ] Implement automatic threshold breach detection
- [ ] Add manual kill-switch activation endpoint
- [ ] Implement graceful shutdown sequence
- [ ] Create dependent notification logic
- [ ] Add cleanup operations (stop tasks, release resources)
- [ ] Write 5+ unit tests for kill-switch scenarios
- [ ] Document kill-switch state transitions

#### Test Scenarios Covered
- KS-001: Threshold breach triggers automatic kill-switch
- KS-002: Manual kill-switch activation by authorized user
- KS-003: Prevention by corrective actions before threshold
- KS-004: Kill-switch audit trail verification
- KS-005: Kill-switch with dependent cleanup (cascade)

#### Files to Create/Modify
- `lib/kill-switch.ts` - Kill-switch implementation
- `lib/kill-switch.spec.ts` - Unit tests (5+ tests)
- `lib/threshold-detector.ts` - Metric threshold monitoring

---

### Story 4: S-STRATEGY-004 - Create State Timeline
**Points:** 5 | **Dependencies:** S-STRATEGY-001 | **Tests Required:** 4+

#### Description
Build visual timeline showing all state transitions with timestamps and responsible actors. Enables users to understand project history and identify bottlenecks.

#### Acceptance Criteria
1. Timeline displays all transitions chronologically
2. Actors and timestamps shown for each transition
3. Zoom and filter capabilities (by state, date range, actor)
4. Export timeline as JSON/CSV
5. Performance: load timeline for 1000+ transitions in <1 second
6. 4+ unit tests for timeline functionality

#### Implementation Checklist
- [ ] Design timeline data structure
- [ ] Implement timeline query API
- [ ] Add filtering by state, date range, actor
- [ ] Add zoom/pan capabilities
- [ ] Implement JSON/CSV export
- [ ] Optimize for large datasets (pagination/indexing)
- [ ] Write 4+ unit tests for timeline queries
- [ ] Create UI component specification

#### Test Scenarios Covered
- ST-004: Timeline chronological ordering
- ST-008: State audit trail with actor metadata
- Filtering by date range
- Export to JSON/CSV formats

#### Files to Create/Modify
- `lib/timeline.ts` - Timeline query logic
- `lib/timeline.spec.ts` - Unit tests (4+ tests)
- `ui/timeline.tsx` - Timeline visualization component (React)

---

### Story 5: S-STRATEGY-005 - Build Rejection/Resubmit Logic
**Points:** 3 | **Dependencies:** S-STRATEGY-002 | **Tests Required:** 3+

#### Description
Implement workflow for rejected strategies to be resubmitted with updated parameters. Rejected strategies return to CANDIDATE state for re-review, with full history preserved.

#### Acceptance Criteria
1. Rejected strategy can be edited by submitter
2. Resubmit creates new approval request
3. Previous rejection reason visible to submitter
4. Audit trail shows complete resubmission chain
5. Maximum rejection threshold enforced (escalation at 3+ rejections)
6. 3+ unit tests for resubmission workflows

#### Implementation Checklist
- [ ] Create resubmission handler
- [ ] Store rejection history with reasons
- [ ] Add edit capability for rejected strategies
- [ ] Implement max rejection threshold check
- [ ] Add escalation notifications at threshold
- [ ] Maintain complete audit chain
- [ ] Write 3+ unit tests for resubmission
- [ ] Document resubmission workflow

#### Test Scenarios Covered
- RJ-002: Resubmit rejected idea
- RJ-007: Maximum rejection threshold enforcement
- RJ-008: Appeal rejected decision
- Rejection history preservation

#### Files to Create/Modify
- `lib/resubmit.ts` - Resubmission logic
- `lib/resubmit.spec.ts` - Unit tests (3+ tests)

---

## TIMEOUT IMPLEMENTATION

### Timeout Scenarios (Not in individual stories, but integrated)

**Scenario 1: CANDIDATE Timeout (30 days)**
- When idea not progresses in CANDIDATE for 30 days
- Transition to: EXPIRED_CANDIDATE
- Action: Send notification to submitter
- Window to recover: Resubmit to reset timeout

**Scenario 2: PAPER Timeout (90 days)**
- When paper awaits publisher response for 90 days
- Transition to: PAPER_STALLED
- Action: Auto-trigger follow-up or alternative submission
- Window to recover: Publish decision or manual cancellation

**Scenario 3: MICRO_LIVE Timeout (180 days)**
- When project shows no progress for 180 days (metric-based)
- Transition to: STALLED_LIVE
- Action: Trigger stall analysis, notify stakeholders
- Window to recover: Progress metrics or manual cancellation

**Scenario 4: Escalation Timeout (30 days from stall)**
- When stalled project remains stalled for additional 30 days
- Transition to: ESCALATED_STALLED
- Action: Leadership notification, intervention recommendations
- Window to recover: Corrective actions or kill-switch

#### Timeout Implementation Checklist
- [ ] Design timeout configuration (durations, thresholds)
- [ ] Implement batch timeout processor (runs periodically)
- [ ] Create timeout state transitions
- [ ] Add notification triggers
- [ ] Implement timeout cancellation (manual override)
- [ ] Write 7+ timeout unit tests (TO-001 through TO-007)

#### Files to Create/Modify
- `lib/timeout-engine.ts` - Timeout processing logic
- `lib/timeout-engine.spec.ts` - Unit tests (7+ tests)

---

## TESTING REQUIREMENTS

### Unit Tests (30+ total required)

**State Transitions (10 tests):** ST-001 through ST-010
- Test all valid transitions
- Test invalid transitions
- Test rollback on error
- Test concurrent handling
- Test idempotence

**Rejection Logic (8 tests):** RJ-001 through RJ-008
- Test rejection at each state
- Test resubmission
- Test authorization checks
- Test rejection threshold
- Test appeal workflow

**Timeouts (7 tests):** TO-001 through TO-007
- Test 4 timeout scenarios
- Test timeout escalation
- Test timeout cancellation
- Test batch processing

**Kill-Switch (5 tests):** KS-001 through KS-005
- Test automatic trigger
- Test manual activation
- Test prevention
- Test audit trail
- Test cascade cleanup

### Test Coverage Requirements
- Minimum 80% code coverage
- All critical paths tested
- Edge cases covered (empty states, null values, race conditions)
- Performance tests (transition latency <100ms)

---

## DELIVERABLES CHECKLIST

### Code Deliverables
- [ ] `lib/state-machine.ts` - Core state machine (estimated 500-800 lines)
- [ ] `lib/approval-service.ts` - Approval workflow (estimated 300-400 lines)
- [ ] `lib/kill-switch.ts` - Kill-switch handler (estimated 200-300 lines)
- [ ] `lib/timeline.ts` - Timeline logic (estimated 200-300 lines)
- [ ] `lib/resubmit.ts` - Resubmission logic (estimated 150-200 lines)
- [ ] `lib/timeout-engine.ts` - Timeout processing (estimated 250-350 lines)
- [ ] `lib/notification-service.ts` - Notifications (estimated 200-300 lines)

### Test Deliverables
- [ ] Unit test files with 30+ passing tests
- [ ] Test coverage report (80%+ coverage)
- [ ] Integration tests for state machine (5+ scenarios)
- [ ] Performance benchmarks (transition latency)

### Documentation Deliverables
- [ ] State machine diagram (Mermaid or SVG)
- [ ] Timeout configuration guide
- [ ] Kill-switch operational procedures
- [ ] API documentation for state transitions
- [ ] Approval workflow diagram

### Configuration Deliverables
- [ ] Timeout duration configuration (config.yaml)
- [ ] Threshold configuration for kill-switch
- [ ] Role-based access control for approval
- [ ] Notification channel configuration

---

## DEPENDENCIES & BLOCKING RELATIONSHIPS

### Blocks
- **Blocks TEAM 2** (E-JOURNAL-SCHEMA): Requires state definitions from state machine
- **Blocks TEAM 3** (E-TELEMETRY-METRICS): Requires state transitions for metric collection
- **Blocks TEAM 4** (E-COMPARE-WORKFLOW): Requires state data in journal schema
- **Blocks TEAM 5** (E-AUDIT-TRAIL): Requires audit trail data from state machine

### Dependencies
- **Depends on:** Database schema (assume ready)
- **Depends on:** Notification infrastructure (can mock initially)
- **Depends on:** Authorization/permissions system (can use stubs)

---

## TEAM COMPOSITION

**Team Lead:** Backend Architect (1)
**Senior Backend Developers:** 2
**Junior Backend Developers:** 1
**QA Engineer:** 1
**DevOps Engineer:** 0.5 (shared with other teams)

**Total: 4.5 FTE over 8 weeks**

---

## TIMELINE & MILESTONES

### Week 1: State Machine Core (S-STRATEGY-001)
- Design state machine architecture
- Implement transition engine
- Add audit trail logging
- Write 10 unit tests
- **Exit Criteria:** All state transitions working, 100% of tests passing

### Week 2: Approval Workflow (S-STRATEGY-002)
- Implement reviewer assignment
- Build approval/rejection endpoints
- Add notifications
- Write 8 unit tests
- **Exit Criteria:** Approval workflow integrated with state machine

### Week 3: Kill-Switch & Timeout Foundation
- Implement kill-switch handler (S-STRATEGY-003 partial)
- Design timeout architecture
- Write 5+ kill-switch tests
- **Exit Criteria:** Kill-switch mechanism working

### Week 4: Timeout Engine Completion
- Complete timeout engine implementation
- Add all 4 timeout scenarios
- Write 7+ timeout tests
- **Exit Criteria:** All timeout scenarios tested and working

### Week 5: Resubmission Logic (S-STRATEGY-005)
- Implement resubmission workflow
- Add rejection history tracking
- Add threshold enforcement
- Write 3 unit tests
- **Exit Criteria:** Full rejection/resubmit cycle working

### Week 6: Timeline Component (S-STRATEGY-004)
- Implement timeline query API
- Add filtering and export
- Write 4+ unit tests
- Design UI component spec
- **Exit Criteria:** Timeline queries working, UI spec complete

### Week 7: Integration & Testing
- Integration tests between all components
- Performance optimization
- Stress testing (concurrent operations)
- Documentation completion
- **Exit Criteria:** 80%+ code coverage, all integration tests passing

### Week 8: Hardening & Handoff
- Fix any remaining issues
- Performance tuning
- Documentation review
- Handoff to TEAM 2
- **Exit Criteria:** All acceptance criteria met, ready for other teams

---

## QUALITY GATES

### Definition of Done
1. All acceptance criteria met
2. 30+ unit tests passing (100% pass rate)
3. 80%+ code coverage
4. Code review approved by lead architect
5. Zero critical bugs
6. Documentation complete and reviewed

### Code Quality Standards
- ESLint rules enforced (TypeScript strict mode)
- No console.log in production code
- All errors explicitly handled
- Type safety: 100% TypeScript coverage
- Comments for complex logic

### Performance Requirements
- State transition latency: <100ms
- Timeline query for 1000+ transitions: <1s
- Approval assignment: <500ms
- Kill-switch activation: <500ms (graceful shutdown allows more time)

---

## RISK MITIGATION

### Risk 1: State Machine Complexity
**Risk:** Complex state transitions with many edge cases
**Mitigation:**
- Start with basic transitions, add complexity incrementally
- Extensive unit tests for edge cases
- Code review focus on transition logic
- Visual state diagrams to catch errors early

### Risk 2: Concurrent State Access
**Risk:** Race conditions with simultaneous transitions
**Mitigation:**
- Use database-level locking (pessimistic) or versioning (optimistic)
- ST-007 test specifically for concurrent handling
- Load testing with concurrent requests
- Monitor in staging before production

### Risk 3: Approval Workflow Scope Creep
**Risk:** Additional approval layers requested mid-sprint
**Mitigation:**
- Lock approval workflow spec early
- Document "out of scope" enhancements
- Create separate stories for future enhancements
- Regular stakeholder sync-ups

### Risk 4: Timeout Scheduler Reliability
**Risk:** Missed timeouts or duplicate processing
**Mitigation:**
- Idempotent timeout processing (safe to re-run)
- TO-007 test for batch processing reliability
- Monitoring and alerting on timeout processor health
- Database-backed job queue with deduplication

---

## SUCCESS CRITERIA

### Functional Success
- All 30+ unit tests passing
- All acceptance criteria met for all 5 stories
- State machine correctly handles 15+ state transitions
- Approval workflow fully operational
- Kill-switch terminating projects correctly
- Timeout engine processing on schedule
- Resubmission workflow enabling rejected ideas to re-enter cycle

### Technical Success
- 80%+ code coverage
- Zero critical bugs in testing
- Transition latency <100ms
- State machine documented with diagrams
- All code reviewed and approved
- Performance benchmarks showing no regressions

### Team Success
- No scope creep (exactly 5 stories, 34 points)
- On-time delivery (8 weeks)
- Knowledge transfer complete to TEAM 2
- Handoff documentation ready

---

## COMMUNICATION PLAN

### Daily Standup: 15 minutes (same time as other teams)
- What was accomplished yesterday
- What's planned for today
- Any blockers
- No deep technical dives (save for offline)

### Weekly Sync: 1 hour (Thursday)
- Status update to program manager
- Blockers escalation
- Next week planning
- Coordination with other teams

### Bi-weekly Architecture Review: 1 hour
- Design review for upcoming work
- Integration points with other teams
- Performance review
- Risk assessment

---

## APPENDIX: REFERENCE LINKS

- **Architecture Document:** katana-v-04-architecture.md (section 4.3)
- **Epic Definition:** katana-v-05-epics.md (E-STRATEGY-LIFECYCLE)
- **Test Specification:** test-cases-blocker-1-state-machine.feature
- **Related Blockers:**
  - BLOCKER-2 (TEAM 2): E-JOURNAL-SCHEMA
  - BLOCKER-3 (TEAM 3): E-TELEMETRY-METRICS
  - BLOCKER-4 (TEAM 4): E-COMPARE-WORKFLOW
  - BLOCKER-5 (TEAM 5): E-AUDIT-TRAIL

---

**Package Status:** READY FOR TEAM 1 KICKOFF
**Last Updated:** 2026-02-26
**Package Version:** 1.0
