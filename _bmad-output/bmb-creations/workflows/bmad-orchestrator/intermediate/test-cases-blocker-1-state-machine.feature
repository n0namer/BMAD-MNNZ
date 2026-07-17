# Feature: BLOCKER-1 - State Machine & Workflow Control
# Author: QA Agent
# Created: 2026-02-26
# Description: Comprehensive test cases for state transitions, rejection logic, timeouts, and kill-switch mechanisms

Feature: State Machine & Workflow Control (BLOCKER-1)
  Background:
    Given a Journal Keeper System is initialized
    And the state machine is in IDLE state
    And the database is empty

  # ========================================
  # STATE TRANSITIONS (10 tests)
  # ========================================

  Scenario: ST-001 - Transition IDLE to CANDIDATE
    Given the system is in IDLE state
    When a new idea is submitted
    Then the state should transition to CANDIDATE
    And the idea should be stored with timestamp
    And the submission log should record the state change
    And Pass Criteria: State is CANDIDATE, timestamp exists, log entry exists

  Scenario: ST-002 - Transition CANDIDATE to PAPER
    Given an idea in CANDIDATE state
    And the idea has been reviewed and approved
    When the idea is marked for paper submission
    Then the state should transition to PAPER
    And the paper reference should be linked
    And the timestamp should be recorded
    And Pass Criteria: State is PAPER, paper_ref exists, timestamp recorded

  Scenario: ST-003 - Transition PAPER to MICRO_LIVE
    Given an idea in PAPER state
    And the paper has been published/accepted
    When the micro-project is launched
    Then the state should transition to MICRO_LIVE
    And project metadata should be initialized
    And the launch timestamp should be recorded
    And Pass Criteria: State is MICRO_LIVE, metadata exists, launch_ts recorded

  Scenario: ST-004 - Transition MICRO_LIVE to COMPLETED
    Given a micro-project in MICRO_LIVE state
    And all project milestones are achieved
    When completion is confirmed
    Then the state should transition to COMPLETED
    And the completion timestamp should be recorded
    And metrics should be finalized
    And Pass Criteria: State is COMPLETED, completion_ts recorded, metrics finalized

  Scenario: ST-005 - Invalid state transition detection
    Given an idea in CANDIDATE state
    When an invalid transition request is made (e.g., CANDIDATE → COMPLETED)
    Then the state should remain unchanged
    And an error should be logged
    And a validation failure should be recorded
    And Pass Criteria: State unchanged, error logged, validation recorded

  Scenario: ST-006 - State rollback on error
    Given a transition from CANDIDATE to PAPER is in progress
    When a critical error occurs during transition
    Then the system should rollback to CANDIDATE state
    And the error should be logged with details
    And the transaction should be marked as failed
    And Pass Criteria: State is CANDIDATE, error logged, txn marked failed

  Scenario: ST-007 - Concurrent state transition handling
    Given two ideas are in CANDIDATE state
    And both are being transitioned to PAPER simultaneously
    When both transitions are triggered
    Then both ideas should transition to PAPER independently
    And no state corruption should occur
    And both transitions should be logged separately
    And Pass Criteria: Both in PAPER, no corruption, logs separate

  Scenario: ST-008 - State audit trail
    Given an idea progressing through states: IDLE → CANDIDATE → PAPER → MICRO_LIVE → COMPLETED
    When the audit trail is queried
    Then all state transitions should be visible
    And timestamps should be in chronological order
    And state-changer metadata should be recorded (user/system)
    And Pass Criteria: All states visible, timestamps ordered, metadata recorded

  Scenario: ST-009 - State transition with dependencies
    Given an idea in CANDIDATE state with blockers
    When attempting transition to PAPER without resolving blockers
    Then the transition should fail
    And a dependency error should be returned
    And the state should remain CANDIDATE
    And Pass Criteria: Transition failed, dependency error returned, state unchanged

  Scenario: ST-010 - Idempotent state transitions
    Given an idea in PAPER state
    When the same transition request is sent twice (PAPER → MICRO_LIVE)
    Then the first transition should succeed
    And the second transition should be idempotent (no-op or return success)
    And no duplicate records should be created
    And Pass Criteria: First succeeds, second is idempotent, no duplicates

  # ========================================
  # REJECTION LOGIC (8 tests)
  # ========================================

  Scenario: RJ-001 - Reject idea in CANDIDATE state
    Given an idea in CANDIDATE state
    And the idea has quality issues
    When a reviewer rejects the idea
    Then the state should transition to REJECTED_CANDIDATE
    And rejection reason should be stored
    And the rejection timestamp should be recorded
    And Pass Criteria: State is REJECTED_CANDIDATE, reason stored, timestamp recorded

  Scenario: RJ-002 - Resubmit rejected idea
    Given a rejected idea in REJECTED_CANDIDATE state
    And the rejection reasons have been addressed
    When the idea is resubmitted
    Then the state should transition back to CANDIDATE
    And the resubmission should be logged
    And the previous rejection record should be preserved
    And Pass Criteria: State is CANDIDATE, resubmission logged, history preserved

  Scenario: RJ-003 - Reject paper in submission
    Given an idea in PAPER state (paper submitted but not accepted)
    When the paper is rejected by publisher
    Then the state should transition to REJECTED_PAPER
    And rejection details should be stored
    And resubmission window should be calculated
    And Pass Criteria: State is REJECTED_PAPER, details stored, resubmission window calculated

  Scenario: RJ-004 - Authorization check on rejection
    Given an idea in CANDIDATE state
    And a user with insufficient permissions
    When the user attempts to reject the idea
    Then the rejection should be denied
    And an authorization error should be logged
    And the state should remain unchanged
    And Pass Criteria: Rejection denied, auth error logged, state unchanged

  Scenario: RJ-005 - Cascade rejection effect
    Given a paper (in PAPER state) with 3 dependent micro-projects (MICRO_LIVE)
    When the paper is rejected (back to REJECTED_PAPER)
    Then dependent micro-projects should be marked as at-risk
    And notifications should be sent to affected project leads
    And a cascade effect log should be recorded
    And Pass Criteria: Projects marked at-risk, notifications sent, log recorded

  Scenario: RJ-006 - Rejection with mandatory feedback
    Given an idea in CANDIDATE state
    When a reviewer rejects the idea without providing feedback
    Then the rejection should fail
    And an error requesting feedback should be returned
    And the state should remain CANDIDATE
    And Pass Criteria: Rejection failed, feedback error returned, state unchanged

  Scenario: RJ-007 - Maximum rejection threshold
    Given an idea that has been rejected 3 times already
    And all rejection reasons have been addressed in resubmissions
    When another rejection is attempted
    Then the system should warn about exceeding rejection threshold
    And the rejection should be logged with escalation flag
    And escalation notification should be sent to leadership
    And Pass Criteria: Warning issued, escalation flag set, notification sent

  Scenario: RJ-008 - Appeal rejected decision
    Given an idea in REJECTED_CANDIDATE state
    And the decision has been appealed by the submitter
    When an appeal review is conducted
    Then the appeal should be either accepted (revert to CANDIDATE) or denied (stay REJECTED)
    And appeal decision should be logged
    And appeal reviewer should be recorded
    And Pass Criteria: Appeal processed, decision logged, reviewer recorded

  # ========================================
  # TIMEOUTS (7 tests)
  # ========================================

  Scenario: TO-001 - CANDIDATE state timeout
    Given an idea in CANDIDATE state for 30 days (default timeout)
    When the timeout threshold is reached
    Then the state should transition to EXPIRED_CANDIDATE
    And an expiration notification should be sent to the submitter
    And the expiration timestamp should be recorded
    And Pass Criteria: State is EXPIRED_CANDIDATE, notification sent, timestamp recorded

  Scenario: TO-002 - Extend timeout with resubmission
    Given an idea in EXPIRED_CANDIDATE state
    When the submitter provides additional context/updates and resubmits
    Then the state should transition back to CANDIDATE
    And the timeout counter should be reset
    And the resubmission timestamp should be recorded
    And Pass Criteria: State is CANDIDATE, timeout reset, resubmission recorded

  Scenario: TO-003 - PAPER submission timeout
    Given an idea in PAPER state awaiting publisher response for 90 days
    When the timeout threshold is reached without publisher decision
    Then the state should transition to PAPER_STALLED
    And a follow-up action should be triggered (remind publisher, consider alternatives)
    And a stall notification should be sent
    And Pass Criteria: State is PAPER_STALLED, action triggered, notification sent

  Scenario: TO-004 - MICRO_LIVE project timeout
    Given a micro-project in MICRO_LIVE state for 180 days
    And no significant progress has been made (defined by metrics)
    When the timeout threshold is reached
    Then the state should transition to STALLED_LIVE
    And a stall analysis should be triggered
    And project stakeholders should be notified
    And Pass Criteria: State is STALLED_LIVE, analysis triggered, stakeholders notified

  Scenario: TO-005 - Timeout escalation
    Given a stalled project in STALLED_LIVE state for additional 30 days
    When escalation timeout threshold is reached
    Then the state should escalate to ESCALATED_STALLED
    And leadership notification should be sent
    And intervention recommendations should be generated
    And Pass Criteria: State is ESCALATED_STALLED, leadership notified, recommendations generated

  Scenario: TO-006 - Timeout cancellation
    Given a PAPER_STALLED idea with timeout pending
    When explicit cancellation is requested by authorized user
    Then the timeout should be cancelled
    And the state should revert to appropriate state (PAPER)
    And cancellation reason should be logged
    And Pass Criteria: Timeout cancelled, state reverted, reason logged

  Scenario: TO-007 - Multiple timeout triggers simultaneously
    Given 100 ideas with different timeout thresholds all reaching expiration at same time
    When the batch timeout processor runs
    Then all 100 ideas should be processed
    And each should transition appropriately
    And no race conditions should occur
    And batch processing log should record all transitions
    And Pass Criteria: All 100 processed, no race conditions, batch log complete

  # ========================================
  # KILL-SWITCH (5 tests)
  # ========================================

  Scenario: KS-001 - Threshold breach triggers kill-switch
    Given metrics are being tracked for a micro-project
    And a critical metric (e.g., bug count, error rate) exceeds threshold
    When the metric breach is detected
    Then the kill-switch should be activated automatically
    And the project state should transition to KILLED_BY_THRESHOLD
    And incident notifications should be sent to stakeholders
    And Post-mortem trigger should be initiated
    And Pass Criteria: Kill-switch active, state is KILLED_BY_THRESHOLD, notifications sent

  Scenario: KS-002 - Manual kill-switch activation
    Given a micro-project in MICRO_LIVE state
    And an authorized user decides to terminate the project
    When the manual kill-switch is activated
    Then the project state should transition to KILLED_MANUAL
    And termination reason should be recorded
    And all affected parties should be notified
    And project cleanup should be scheduled
    And Pass Criteria: State is KILLED_MANUAL, reason recorded, notifications sent

  Scenario: KS-003 - Kill-switch prevention (non-escalation)
    Given a project showing early warning signs
    When corrective actions are taken before threshold breach
    Then the kill-switch should not be activated
    And project should transition to RECOVERING state (if needed)
    And prevention actions should be logged
    And And notification should confirm success
    And Pass Criteria: Kill-switch not activated, actions logged, notification sent

  Scenario: KS-004 - Kill-switch audit trail
    Given a project that was killed (either manually or by threshold)
    When the audit trail is queried
    Then all events leading to kill-switch should be visible
    And decision maker/system should be identifiable
    And timeline should be accurate
    And justification should be documented
    And Pass Criteria: Full audit trail visible, decision identifiable, timeline accurate

  Scenario: KS-005 - Kill-switch with dependent cleanup
    Given a killed project with 5 downstream dependencies (linked papers, ideas, etc.)
    When kill-switch is activated
    Then the project should be marked as KILLED
    And dependent items should be notified and marked as at-risk
    And cascade cleanup logic should execute
    And cleanup completion should be logged
    And Pass Criteria: Project killed, dependencies notified, cleanup complete, log recorded

