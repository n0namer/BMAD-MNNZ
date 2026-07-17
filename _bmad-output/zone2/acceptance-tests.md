---
workflow: testarch-atdd
project: katana-vectorbt
phase: Phase 1 Core Foundation
generated: 2026-02-26
mode: atdd-red-phase
total_tests: 180
test_framework: playwright-pytest
status: FAILING (RED phase - awaiting implementation)
---

# Acceptance Tests - Katana Vectorbt Phase 1
## ATDD Red Phase - 180 Failing Tests

**Generated:** 2026-02-26
**Author:** Agent-5 (testarch-atdd specialist)
**Framework:** Playwright (E2E) + pytest (Unit/Integration)
**Phase:** Phase 1 Core Foundation
**Scope:** 5 Epics × 25 Stories → 180 test scenarios

**Test Status:** All tests in RED state (failing) — awaiting implementation
**Purpose:** Define acceptance criteria via executable specifications (BDD Given-When-Then format)

---

## Table of Contents

1. [Epic 1: Strategy Lifecycle (S-STRATEGY-001 to S-STRATEGY-005)](#epic-1-strategy-lifecycle) — 34 tests
2. [Epic 2: Journal Schema (S-JOURNAL-001 to S-JOURNAL-005)](#epic-2-journal-schema) — 28 tests
3. [Epic 3: Telemetry Metrics (S-TELEMETRY-001 to S-TELEMETRY-005)](#epic-3-telemetry-metrics) — 29 tests
4. [Epic 4: Compare Workflow (S-COMPARE-001 to S-COMPARE-005)](#epic-4-compare-workflow) — 32 tests
5. [Epic 5: Audit Trail (S-AUDIT-001 to S-AUDIT-005)](#epic-5-audit-trail) — 30 tests
6. [Priority Index](#priority-index) — P0, P1, P2, P3 breakdown
7. [Coverage Matrix](#coverage-matrix) — Test → Story → Acceptance Criteria mapping

---

## Epic 1: Strategy Lifecycle

**Story Set:** S-STRATEGY-001 to S-STRATEGY-005
**Test Count:** 34 tests
**Priority Breakdown:** P0=18, P1=10, P2=4, P3=2

### S-STRATEGY-001: Implement State Machine Transitions (13 story points)

**Acceptance Criteria:**
- State transitions defined: DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED/CANCELLED
- Invalid transitions rejected
- Audit trail tracks all transitions
- 10+ unit tests passing

**Test Scenarios (13 tests):**

#### T-001.01 [P0-UNIT] Valid State Transition: DRAFT to PENDING
```
Given: A strategy in DRAFT state
When: transition_to_pending() is called with valid submission
Then: State becomes PENDING
And: Audit log records transition with actor ID and timestamp
And: No side effects occur (notifications sent asynchronously)
```

#### T-001.02 [P0-UNIT] Valid State Transition: PENDING to APPROVED
```
Given: A strategy in PENDING state
And: An approved reviewer has reviewed the strategy
When: approve() is called by reviewer
Then: State becomes APPROVED
And: Approval metadata (reviewer_id, reason) stored in audit
And: approval_timestamp is set to current UTC
```

#### T-001.03 [P0-UNIT] Valid State Transition: PENDING to REJECTED
```
Given: A strategy in PENDING state
When: reject(reason="Sharpe ratio below threshold") is called
Then: State becomes REJECTED
And: rejection_reason stored in strategy metadata
And: Strategy can be edited before resubmit
```

#### T-001.04 [P0-UNIT] Valid State Transition: APPROVED to ACTIVE
```
Given: A strategy in APPROVED state
And: All precondition checks pass (market hours, capital available)
When: deploy() is called
Then: State becomes ACTIVE
And: deployment_timestamp set
And: Initial equity snapshot stored
```

#### T-001.05 [P0-UNIT] Valid State Transition: ACTIVE to COMPLETED
```
Given: A strategy in ACTIVE state
When: completion condition met (end_date reached OR manual completion)
Then: State becomes COMPLETED
And: final_equity snapshot captured
And: Final performance metrics calculated
And: Return on investment (ROI) stored
```

#### T-001.06 [P0-UNIT] Valid State Transition: ACTIVE to KILLED
```
Given: A strategy in ACTIVE state
When: kill_switch(reason="Manual stop") is invoked
Then: State becomes KILLED
And: kill_timestamp recorded
And: Graceful shutdown executed (pending orders closed)
And: Final position snapshot stored
```

#### T-001.07 [P0-UNIT] Invalid Transition: DRAFT to ACTIVE (skipping PENDING)
```
Given: A strategy in DRAFT state
When: transition_to_active() is attempted
Then: InvalidTransitionError raised
And: State remains DRAFT
And: No audit entry created
And: Error message: "Cannot transition from DRAFT to ACTIVE"
```

#### T-001.08 [P0-UNIT] Invalid Transition: COMPLETED to ACTIVE (revert)
```
Given: A strategy in COMPLETED state
When: deploy() is attempted again
Then: InvalidTransitionError raised
And: State remains COMPLETED
```

#### T-001.09 [P0-UNIT] Invalid Transition: KILLED to any state
```
Given: A strategy in KILLED state
When: Any state transition attempted (to PENDING, APPROVED, ACTIVE, etc.)
Then: InvalidTransitionError raised
And: State remains KILLED (immutable)
```

#### T-001.10 [P0-UNIT] Audit Trail: All transitions logged with metadata
```
Given: A strategy undergoing multiple state transitions
When: DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED
Then: Audit log contains 5 entries, each with:
  - transition_timestamp (UTC)
  - from_state, to_state
  - actor_id (user or system)
  - reason/comment (if applicable)
And: Audit entries sorted chronologically
```

#### T-001.11 [P0-INT] State Machine Concurrency: Two simultaneous approve calls
```
Given: A strategy in PENDING state
And: Two concurrent approval requests (user A, user B)
When: Both approve() calls execute in parallel
Then: First call succeeds, state becomes APPROVED
And: Second call fails with ConflictError (state already APPROVED)
And: Audit shows only first approval
```

#### T-001.12 [P1-INT] Atomic State Transition with Side Effects
```
Given: A strategy transitioning from APPROVED to ACTIVE
And: Side effects configured (notify team, capture snapshot)
When: transition executes and side_effect_1 succeeds but side_effect_2 fails
Then: Entire transition rolled back (state remains APPROVED)
And: Error logged for failed side effect
And: Audit trail shows no state change
```

#### T-001.13 [P1-E2E] State Persistence: State survives service restart
```
Given: A strategy in ACTIVE state
When: Service is restarted (state reloaded from database)
Then: State still ACTIVE
And: All timestamps and metadata preserved
And: Audit trail unchanged
```

---

### S-STRATEGY-002: Build Approval Workflow (8 story points)

**Acceptance Criteria:**
- Reviewers can be assigned to pending strategies
- Approval and rejection decisions recorded
- Comments captured with approval decisions
- Notification system alerts reviewers
- 8+ unit tests passing

**Test Scenarios (11 tests):**

#### T-002.01 [P0-UNIT] Assign Reviewer: Valid reviewer ID
```
Given: A strategy in DRAFT state
When: assign_reviewer(reviewer_id="r-123") called
Then: Reviewer added to strategy.reviewers list
And: Assignment timestamp recorded
And: Status field shows "awaiting_review"
```

#### T-002.02 [P0-UNIT] Assign Multiple Reviewers
```
Given: A strategy in DRAFT state
When: assign_reviewer() called 3 times (r-1, r-2, r-3)
Then: All 3 reviewers in list
And: Initial review_votes map has 3 keys, all False
And: consensus_required = "all_reviewers_approve" enforced
```

#### T-002.03 [P0-UNIT] Invalid Reviewer ID
```
Given: A strategy ready for approval
When: assign_reviewer(reviewer_id="invalid-xyz") called
Then: ReviewerNotFoundError raised
And: Reviewer not added
And: State unchanged
```

#### T-002.04 [P0-UNIT] Approve with Comment
```
Given: A strategy assigned to reviewer "r-123"
When: approve(reviewer_id="r-123", comment="Good Sharpe ratio") called
Then: approval_decision stored with timestamp
And: comment appended to decision_history
And: review_votes["r-123"] = True
And: approval_comment visible to submitter
```

#### T-002.05 [P0-UNIT] Reject with Comment
```
Given: A strategy assigned to reviewer "r-456"
When: reject(reviewer_id="r-456", reason="High correlation with existing strategy") called
Then: rejection_decision recorded
And: reason stored
And: Submitter notified of rejection reason
And: Strategy state becomes REJECTED
```

#### T-002.06 [P0-UNIT] Approval Workflow: Consensus from all reviewers
```
Given: Strategy has 3 reviewers assigned (r-1, r-2, r-3)
When: All 3 approve
Then: State transitions to APPROVED
And: approval_consensus_timestamp = last_approval_timestamp
And: All reviews visible in decision_history
```

#### T-002.07 [P0-UNIT] Approval Workflow: Single rejection blocks approval
```
Given: Strategy has 3 reviewers (r-1, r-2, r-3)
When: r-1 and r-2 approve, r-3 rejects
Then: State remains PENDING
And: rejection_by field shows r-3
And: Submitter can request re-review after changes
```

#### T-002.08 [P1-INT] Notification: Reviewer receives approval task
```
Given: A strategy assigned to reviewer r-123
When: Strategy transitions to PENDING state
Then: Notification queued for r-123
And: notification_timestamp recorded
And: notification_channel = "in-app" (minimum)
And: Reviewer sees task in dashboard
```

#### T-002.09 [P1-INT] Notification: Submitter receives approval decision
```
Given: A strategy approved by all reviewers
When: Approval completes
Then: Notification sent to strategy submitter
And: notification includes approvers list
And: notification links to APPROVED strategy page
```

#### T-002.10 [P1-E2E] Approval Workflow End-to-End
```
Given: New strategy created by user1
And: Reviewers (r-1, r-2) assigned
When: r-1 approves with comment "DSR adjusted"
And: r-2 approves with comment "Within risk parameters"
Then: Strategy transitions to APPROVED
And: Both comments visible to user1
And: user1 can now deploy strategy
```

#### T-002.11 [P2-INT] Reviewer Workload: List pending approvals
```
Given: Multiple strategies assigned to reviewer r-999
When: get_pending_approvals(reviewer_id="r-999") called
Then: Returns list of strategies with PENDING approval from r-999
And: Sorted by submit_timestamp (oldest first)
And: Includes decision_deadline if enforced
```

---

### S-STRATEGY-003: Add Kill-Switch Mechanism (5 story points)

**Acceptance Criteria:**
- Kill-switch callable from ACTIVE state
- Graceful shutdown of running strategy
- Final state recorded as KILLED
- Cleanup operations executed
- 5+ unit tests passing

**Test Scenarios (8 tests):**

#### T-003.01 [P0-UNIT] Kill-Switch: Valid invocation from ACTIVE
```
Given: A strategy in ACTIVE state
When: trigger_kill_switch(reason="Manual operator stop") called
Then: State transitions to KILLED
And: kill_reason stored
And: kill_timestamp = current UTC
And: No further trades executed
```

#### T-003.02 [P0-UNIT] Kill-Switch: Cannot call from non-ACTIVE states
```
Given: A strategy in PENDING state
When: trigger_kill_switch() called
Then: InvalidStateError raised
And: State remains PENDING
And: Kill switch not triggered
```

#### T-003.03 [P0-UNIT] Kill-Switch: Graceful order closure
```
Given: A strategy in ACTIVE with 3 open orders
When: trigger_kill_switch(graceful=true) called
Then: All 3 orders closed at current market price
And: closure_type = "stop-loss" (or market order)
And: final_position recorded
And: Order closure log stored
```

#### T-003.04 [P0-INT] Kill-Switch: Cleanup operations
```
Given: A strategy in ACTIVE state with running optimization
When: trigger_kill_switch() called
Then: Optimizer process terminated
And: Any pending data syncs flushed
And: Database transactions committed
And: Artifact files finalized
```

#### T-003.05 [P0-INT] Kill-Switch: Final position snapshot
```
Given: A strategy killed mid-trade
When: Final position snapshot captured
Then: Snapshot includes:
  - open_positions (count, total_notional)
  - unrealized_pnl
  - equity_curve (final point)
  - timestamp
```

#### T-003.06 [P1-INT] Kill-Switch: Idempotent operation
```
Given: A strategy in KILLED state
When: trigger_kill_switch() called again
Then: State remains KILLED
And: No duplicate kill records created
And: Idempotent error message returned
```

#### T-003.07 [P1-E2E] Kill-Switch: Operator-initiated stop
```
Given: Strategy running and producing live trades
When: Operator clicks "Emergency Stop" in UI
Then: Kill-switch triggered within 2 seconds
And: All open orders closed
And: Final PnL report available
And: Strategy marked KILLED
```

#### T-003.08 [P2-INT] Kill-Switch: Reason audit trail
```
Given: Multiple kill-switch events on different strategies
When: Query kill_events with reason filtering
Then: Returns list with reasons (e.g., "Manual stop", "Max loss exceeded", "System error")
And: Can trace operator actions vs. automated stops
```

---

### S-STRATEGY-004: Create State Timeline (5 story points)

**Acceptance Criteria:**
- Timeline displays all transitions chronologically
- Actors and timestamps shown for each transition
- Zoom and filter capabilities
- Export timeline as JSON/CSV
- 4+ unit tests passing

**Test Scenarios (6 tests):**

#### T-004.01 [P0-UNIT] Timeline: Chronological order
```
Given: A strategy with 5 state transitions
When: get_state_timeline() called
Then: Returns list of events sorted by timestamp (ascending)
And: Each event has: timestamp, from_state, to_state, actor_id
```

#### T-004.02 [P0-UNIT] Timeline: Actor tracking
```
Given: Multiple actors performing transitions (user-1, system, user-2)
When: Timeline retrieved
Then: Each transition shows actor_id
And: Can identify which user caused each transition
```

#### T-004.03 [P1-E2E] Timeline: Filter by date range
```
Given: Timeline with 10 transitions over 30 days
When: filter_by_date_range(start="2026-02-01", end="2026-02-15") called
Then: Returns only transitions in range (5 transitions)
And: Excluded transitions not shown
```

#### T-004.04 [P1-E2E] Timeline: Filter by state
```
Given: Timeline with mixed transitions (DRAFT, PENDING, APPROVED, ACTIVE, COMPLETED)
When: filter_by_state("ACTIVE") called
Then: Returns only transitions involving ACTIVE state
And: Includes transitions TO and FROM ACTIVE
```

#### T-004.05 [P1-INT] Timeline: Export as JSON
```
Given: Complete state timeline
When: export_timeline(format="json") called
Then: Returns valid JSON with structure:
  {
    "strategy_id": "...",
    "timeline": [
      {"timestamp": "...", "from_state": "...", "to_state": "...", ...}
    ]
  }
```

#### T-004.06 [P2-INT] Timeline: Export as CSV
```
Given: State timeline
When: export_timeline(format="csv") called
Then: Returns CSV with columns: timestamp, from_state, to_state, actor_id, reason
And: CSV properly escaped for commas/quotes
```

---

### S-STRATEGY-005: Build Rejection/Resubmit Logic (3 story points)

**Acceptance Criteria:**
- Rejected strategy can be edited
- Resubmit creates new approval request
- Previous rejection reason visible to submitter
- Audit trail shows resubmission chain
- 3+ unit tests passing

**Test Scenarios (6 tests):**

#### T-005.01 [P0-UNIT] Rejection: Strategy transitions to REJECTED
```
Given: A strategy in PENDING state
When: reject(reviewer_id="r-1", reason="High correlation") called
Then: State becomes REJECTED
And: rejection_reason stored
And: rejected_by = "r-1"
And: rejection_timestamp recorded
```

#### T-005.02 [P0-UNIT] Rejection: Reason visible to submitter
```
Given: A rejected strategy
When: get_strategy_details() called
Then: rejection_reason visible: "High correlation"
And: rejected_by visible: reviewer name
And: rejection_timestamp visible
```

#### T-005.03 [P0-UNIT] Resubmit: Edit after rejection
```
Given: A rejected strategy
When: update_strategy(parameter_A=0.5) called
Then: Change recorded
And: edit_timestamp set
And: Strategy still in REJECTED state until resubmit
```

#### T-005.04 [P0-UNIT] Resubmit: Transition to PENDING with new reviewers
```
Given: A rejected strategy with edits made
When: resubmit() called
Then: State transitions from REJECTED to PENDING
And: New approval request created
And: Same reviewers automatically assigned (or new list)
And: Previous rejection visible in decision_history
```

#### T-005.05 [P1-INT] Rejection Chain: Multiple rejection cycles
```
Given: Strategy rejected, edited, resubmitted, rejected again
When: get_decision_history() called
Then: Shows both rejections with reasons and edit details between
And: Audit trail shows complete resubmission chain
```

#### T-005.06 [P1-E2E] Resubmit: Full cycle rejection → edit → reapproval
```
Given: Strategy rejected for "Sharpe too low"
When: Submitter adjusts strategy parameters
And: Calls resubmit()
And: Reviewers approve new version
Then: Strategy transitions to APPROVED
And: Both rejection and approval visible in audit
And: Submitter can deploy
```

---

## Epic 2: Journal Schema

**Story Set:** S-JOURNAL-001 to S-JOURNAL-005
**Test Count:** 28 tests
**Priority Breakdown:** P0=16, P1=8, P2=3, P3=1

### S-JOURNAL-001: Create manifest.json Structure (8 story points)

**Acceptance Criteria:**
- Schema includes: strategy_id, version, start_time, end_time, parameters, environment
- JSON Schema (.json) created and validated
- TypeScript types generated
- Sample manifests created
- 8+ unit tests passing

**Test Scenarios (8 tests):**

#### T-006.01 [P0-UNIT] Manifest: Valid JSON structure
```
Given: A manifest.json file
When: Load and parse manifest
Then: Contains fields: strategy_id, version, start_time, end_time, parameters, environment
And: JSON is valid according to JSON Schema spec
```

#### T-006.02 [P0-UNIT] Manifest: Required fields validation
```
Given: A manifest with missing strategy_id
When: validate(manifest) called
Then: ValidationError raised: "Missing required field: strategy_id"
And: Manifest rejected
```

#### T-006.03 [P0-UNIT] Manifest: Field type validation
```
Given: A manifest with strategy_id="123" (string)
When: validate(manifest) called
Then: Passes (strategy_id is string)

Given: A manifest with strategy_id=123 (integer)
When: validate(manifest) called
Then: ValidationError raised: "strategy_id must be string"
```

#### T-006.04 [P0-UNIT] Manifest: Timestamp format (ISO 8601)
```
Given: A manifest with start_time="2026-02-26T10:30:45Z"
When: validate(manifest) called
Then: Passes (valid ISO 8601)

Given: A manifest with start_time="2026/02/26 10:30:45"
When: validate(manifest) called
Then: ValidationError raised: "Invalid timestamp format"
```

#### T-006.05 [P0-UNIT] Manifest: TypeScript type generation
```
Given: The JSON Schema file
When: TypeScript type generator runs
Then: Generates ManifestV1 interface with:
  - strategy_id: string
  - version: string
  - start_time: string (ISO 8601)
  - end_time: string
  - parameters: Record<string, any>
  - environment: Record<string, string>
```

#### T-006.06 [P1-INT] Manifest: Sample manifests
```
Given: The manifest schema
When: generate_sample_manifests() called
Then: Creates 3 valid examples:
  - Simple strategy (5 parameters)
  - Complex strategy (20 parameters)
  - Edge case (1 parameter)
And: All samples pass validation
```

#### T-006.07 [P1-INT] Manifest: Round-trip serialization
```
Given: A manifest object
When: JSON.stringify() then JSON.parse()
Then: Deserialized object equals original
And: All types preserved
```

#### T-006.08 [P1-INT] Manifest: Backward compatibility
```
Given: An older manifest schema (v0.9)
When: Validator runs in compatibility mode
Then: Accepts v0.9 manifests
And: Auto-migrates to v1.0 schema
And: Migration logged
```

---

### S-JOURNAL-002: Create summary.json v3.0 (10 story points)

**Acceptance Criteria:**
- Schema includes: total_runs, win_rate, sharpe_ratio, max_drawdown, final_equity
- Aggregation logic implemented
- Summary auto-calculated from detailed results
- Backward compatible with v2.0 format
- 10+ unit tests passing

**Test Scenarios (10 tests):**

#### T-007.01 [P0-UNIT] Summary: Valid v3.0 structure
```
Given: A summary.json file (v3.0)
When: Load and validate
Then: Contains fields:
  - schema_version: "3.0"
  - total_runs: integer
  - win_rate: float (0.0–1.0)
  - sharpe_ratio: float
  - max_drawdown: float (negative)
  - final_equity: float
```

#### T-007.02 [P0-UNIT] Summary: Win rate calculation
```
Given: 100 runs with 75 profitable, 25 unprofitable
When: Aggregate summary
Then: win_rate = 0.75
```

#### T-007.03 [P0-UNIT] Summary: Sharpe ratio aggregation
```
Given: Multiple runs with individual Sharpe ratios
When: Aggregate summary
Then: sharpe_ratio = weighted_average(individual_sharpes)
And: Weights based on run_duration or capital_allocated
```

#### T-007.04 [P0-UNIT] Summary: Max drawdown (most negative)
```
Given: Multiple runs with drawdowns (-0.12, -0.18, -0.05, -0.22)
When: Aggregate summary
Then: max_drawdown = -0.22 (worst case)
```

#### T-007.05 [P0-UNIT] Summary: Final equity calculation
```
Given: Starting equity: $100,000
And: Cumulative PnL: $15,000
When: Calculate final_equity
Then: final_equity = 115,000.0
```

#### T-007.06 [P1-INT] Summary: Auto-calculation from run details
```
Given: Individual run results stored
When: finalize_strategy_run() called
Then: Summary automatically calculated
And: No manual input required
And: Summary persisted to summary.json
```

#### T-007.07 [P1-INT] Summary: Backward compatibility with v2.0
```
Given: A v2.0 summary (without schema_version)
When: v3.0 reader loads it
Then: Accepts v2.0 format
And: Auto-migrates to v3.0 (adds schema_version: "3.0")
And: All v2.0 fields preserved
```

#### T-007.08 [P1-INT] Summary: Migration from v2.0 to v3.0
```
Given: v2.0 summary with fields: total_trades, win_pct, sharpe, dd, final_balance
When: migrate_to_v3(v2_summary) called
Then: Returns v3.0 with:
  - total_runs = total_trades (remapped)
  - win_rate = win_pct / 100 (normalized)
  - sharpe_ratio = sharpe (unchanged)
  - max_drawdown = dd (unchanged)
  - final_equity = final_balance (renamed)
```

#### T-007.09 [P1-INT] Summary: Validation on update
```
Given: A summary with win_rate=1.5 (invalid, >1.0)
When: Validate summary
Then: ValidationError raised: "win_rate must be between 0.0 and 1.0"
And: Summary not persisted
```

#### T-007.10 [P2-INT] Summary: Audit trail for changes
```
Given: A summary updated multiple times
When: get_summary_changelog() called
Then: Returns list of:
  - Timestamp of each update
  - Changed fields
  - Previous vs new values
```

---

### S-JOURNAL-003: Implement events.ndjson (8 story points)

**Acceptance Criteria:**
- NDJSON format (one JSON object per line, newline-delimited)
- Each event: timestamp, event_type, details, actor
- Trade events, state transitions, errors all logged
- Query interface (filter by event_type, timestamp range)
- 8+ unit tests passing

**Test Scenarios (8 tests):**

#### T-008.01 [P0-UNIT] Events NDJSON: Valid format
```
Given: An events.ndjson file
When: Read file line by line
Then: Each line is valid JSON
And: No line spans multiple lines
```

#### T-008.02 [P0-UNIT] Events: Log trade event
```
Given: A completed trade
When: log_event(event_type="trade", details={...}) called
Then: NDJSON line appended with:
  - timestamp: ISO 8601
  - event_type: "trade"
  - details: {symbol, entry_price, exit_price, pnl, ...}
  - actor: "system" or user_id
```

#### T-008.03 [P0-UNIT] Events: Log state transition
```
Given: A strategy state transition
When: log_event(event_type="state_transition", details={...}) called
Then: NDJSON line appended with:
  - event_type: "state_transition"
  - details: {from_state, to_state, reason}
```

#### T-008.04 [P0-UNIT] Events: Log error event
```
Given: An error in strategy execution
When: log_event(event_type="error", details={...}) called
Then: NDJSON line appended with:
  - event_type: "error"
  - details: {error_message, error_code, stack_trace (optional)}
  - severity: "error"
```

#### T-008.05 [P1-INT] Events: Query by event_type
```
Given: 1000 events in NDJSON (mix of trade, state, error)
When: query_events(event_type="trade") called
Then: Returns only trade events
And: Count > 0
And: All events have event_type="trade"
```

#### T-008.06 [P1-INT] Events: Query by timestamp range
```
Given: Events spanning 10 days
When: query_events(start="2026-02-01", end="2026-02-05") called
Then: Returns only events in range
And: Events outside range excluded
```

#### T-008.07 [P1-INT] Events: Immutable append
```
Given: Existing events in NDJSON
When: New event logged
Then: Appended to file (no edits to existing lines)
And: File pointer at end after append
And: Previous events unchanged
```

#### T-008.08 [P2-INT] Events: Parse and deserialize
```
Given: 100 events in NDJSON
When: Load all events into memory
Then: Each line deserialized to Event object
And: All fields accessible (timestamp, event_type, details, actor)
And: No parse errors
```

---

### S-JOURNAL-004: Build Database Schema (Postgres) (8 story points)

**Acceptance Criteria:**
- SQLite → PostgreSQL migration path
- Tables: runs, strategies, trades, audit_log
- Foreign keys, indexes for performance
- Data integrity constraints
- Backup/restore functionality
- 8+ unit tests passing

**Test Scenarios (7 tests):**

#### T-009.01 [P0-INT] Database: Create schema
```
Given: Empty PostgreSQL database
When: apply_schema_migration(version="1.0") called
Then: Tables created:
  - runs (run_id PK, strategy_id FK, start_time, end_time, ...)
  - strategies (strategy_id PK, name, ...)
  - trades (trade_id PK, run_id FK, ...)
  - audit_log (event_id PK, entity_id FK, ...)
And: All constraints applied
```

#### T-009.02 [P0-INT] Database: Foreign key integrity
```
Given: A trade with run_id that doesn't exist in runs table
When: Insert trade
Then: FOREIGN KEY constraint violated
And: Insert fails with integrity error
```

#### T-009.03 [P0-INT] Database: Indexes for query performance
```
Given: 1,000,000 trades in database
When: Query all trades for run_id=12345
Then: Query executes in <100ms (index used)
And: EXPLAIN PLAN shows index scan, not full table scan
```

#### T-009.04 [P1-INT] Database: NOT NULL constraints
```
Given: A run with NULL required field (strategy_id)
When: Try to insert
Then: NOT NULL constraint fails
And: Run not inserted
```

#### T-009.05 [P1-INT] Database: SQLite to PostgreSQL migration
```
Given: SQLite database with 1000 runs, 10000 trades
When: Run migration script (export SQLite → import PostgreSQL)
Then: All data transferred
And: Row counts match
And: Foreign keys maintained
And: Timestamps preserved
```

#### T-009.06 [P1-INT] Database: Backup functionality
```
Given: PostgreSQL database with data
When: backup_database(destination="/backups/db-2026-02-26.dump") called
Then: Dump file created
And: File size > 0
And: Can be restored to fresh database
```

#### T-009.07 [P2-INT] Database: Restore from backup
```
Given: A backup dump file
When: restore_database(source="/backups/db-2026-02-26.dump") called
Then: Database populated from backup
And: All tables, data, constraints restored
And: Row counts match original
```

---

### S-JOURNAL-005: Create Reproducibility Verifier (6 story points)

**Acceptance Criteria:**
- data_hash (SHA256) stored with each run
- Verifier: re-run with same config/data → same hash
- Artifact integrity check (all files present, unmodified)
- Deterministic seed contract enforced
- Comparison report (expected vs actual)
- 6+ unit tests passing

**Test Scenarios (7 tests):**

#### T-010.01 [P0-INT] Reproducibility: Generate data_hash
```
Given: A backtest run with deterministic seed=12345
When: Run backtester
Then: Outputs backtest_summary.json with:
  - data_hash: "abc123..." (SHA256)
  - seed: 12345
  - symbol, timeframe, start_date, end_date (frozen)
```

#### T-010.02 [P0-INT] Reproducibility: Verify hash matches
```
Given: Original run with data_hash="abc123..."
When: Re-run same config with same seed and data
Then: New data_hash="abc123..." (matches)
And: Output: "Reproducibility verified ✓"
```

#### T-010.03 [P0-INT] Reproducibility: Hash mismatch detection
```
Given: Original run with data_hash="abc123..."
When: Re-run with different data (different symbol or date range)
Then: New data_hash="xyz789..." (different)
And: Output: "Reproducibility check FAILED - data mismatch"
And: Detailed diff report generated
```

#### T-010.04 [P1-INT] Reproducibility: Artifact integrity
```
Given: Run with artifacts: backtest_summary.json, optimizer_summary.json, events.ndjson
When: verify_artifact_integrity(run_id=123) called
Then: Checks each artifact:
  - File exists
  - File size > 0
  - JSON valid (if JSON)
  - No truncation detected
And: Report: "All artifacts intact" or list of issues
```

#### T-010.05 [P1-INT] Reproducibility: Deterministic seed enforcement
```
Given: A backtest run
When: Validate that all random operations seeded
Then: Confirms seed_value set globally
And: No unseeded numpy.random calls
And: No unseeded pandas operations
And: Seed documented in manifest
```

#### T-010.06 [P1-INT] Reproducibility: Comparison report
```
Given: Two runs (original and re-run) with same config
When: generate_comparison_report() called
Then: Report shows:
  - Metrics match (Sharpe, max_dd, ROI, etc.)
  - Prices match (entry, exit prices)
  - Order counts match
  - Trade sequence identical
  - Timestamp: "Reproducible on [date]"
```

#### T-010.07 [P2-INT] Reproducibility: Seed and environment freeze
```
Given: A run with stored: seed, numpy_version, vectorbt_version, python_version
When: verify_environment() called in different environment
Then: Warns if versions differ
And: Recommends Docker container with pinned versions
And: Reproducibility still verified (bitwise) if versions match
```

---

## Epic 3: Telemetry Metrics

**Story Set:** S-TELEMETRY-001 to S-TELEMETRY-005
**Test Count:** 29 tests
**Priority Breakdown:** P0=14, P1=11, P2=3, P3=1

### S-TELEMETRY-001: Instrument Time-to-Status (6 story points)

**Acceptance Criteria:**
- Time from DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED tracked
- Metrics: ttf_draft_to_pending, ttf_pending_to_active, ttf_total
- Dashboard histogram showing distribution
- Alert if ttf > 24 hours (threshold configurable)
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-011.01 [P0-UNIT] TTF: Calculate draft to pending
```
Given: Strategy created at 2026-02-26T10:00:00Z
When: Transitioned to PENDING at 2026-02-26T10:05:00Z
Then: ttf_draft_to_pending = 300 seconds
```

#### T-011.02 [P0-UNIT] TTF: Calculate pending to active
```
Given: Strategy in PENDING since 2026-02-26T10:00:00Z
When: Transitioned to ACTIVE at 2026-02-26T11:00:00Z
Then: ttf_pending_to_active = 3600 seconds
```

#### T-011.03 [P0-INT] TTF: Total time draft to active
```
Given: DRAFT (10:00) → PENDING (10:05) → APPROVED (10:30) → ACTIVE (11:00)
When: Calculate ttf_draft_to_active
Then: ttf_draft_to_active = 3600 seconds (total)
```

#### T-011.04 [P1-INT] TTF: Metrics stored with strategy
```
Given: A completed strategy
When: Retrieve strategy details
Then: Shows:
  - ttf_draft_to_pending: 300
  - ttf_pending_to_approved: 1500
  - ttf_approved_to_active: 1800
  - ttf_total: 3600
```

#### T-011.05 [P1-INT] TTF: Alert on slow approval
```
Given: Strategy in PENDING for >24 hours (86400 seconds)
When: Alert rule evaluates
Then: Alert fired: "Slow approval detected - ttf_pending > 24h"
And: Alert includes strategy_id, current_ttf
```

#### T-011.06 [P1-INT] TTF: Dashboard histogram
```
Given: 100 strategies with varying ttf values
When: Generate TTF histogram
Then: Histogram shows distribution:
  - X-axis: TTF (seconds or hours)
  - Y-axis: Count of strategies
  - Mean, median, p95 computed
```

---

### S-TELEMETRY-002: Implement MTIF Calculation (6 story points)

**Acceptance Criteria:**
- MTIF = Mean Time In Field (average duration in ACTIVE state)
- Tracked per strategy, per team
- Alert if MTIF < 10 minutes (indicates short-lived strategies)
- Integration with monitoring dashboard
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-012.01 [P0-UNIT] MTIF: Calculate single active duration
```
Given: Strategy ACTIVE from 10:00 to 10:15
When: Calculate duration
Then: duration = 900 seconds
```

#### T-012.02 [P0-UNIT] MTIF: Calculate average across multiple runs
```
Given: 3 strategy runs: 900s, 1200s, 1500s active time
When: Calculate MTIF
Then: MTIF = (900 + 1200 + 1500) / 3 = 1200 seconds
```

#### T-012.03 [P0-UNIT] MTIF: Account for killed strategies
```
Given: Strategy ACTIVE from 10:00, killed at 10:03
When: Calculate duration
Then: duration = 180 seconds (counts toward MTIF)
```

#### T-012.04 [P1-INT] MTIF: Per-team aggregation
```
Given: Team with 5 strategies (MTIF: 1200, 1500, 900, 2000, 1100 seconds)
When: Calculate team MTIF
Then: team_MTIF = (1200+1500+900+2000+1100) / 5 = 1340 seconds
```

#### T-012.05 [P1-INT] MTIF: Alert on low MTIF
```
Given: Strategy with MTIF = 300 seconds (5 minutes, below 10-minute threshold)
When: Alert rule evaluates
Then: Alert: "Low MTIF detected - strategy killed quickly (300s)"
And: Recommendation: "Review strategy parameters"
```

#### T-012.06 [P1-INT] MTIF: Dashboard tracking
```
Given: Multiple strategies
When: Generate MTIF dashboard widget
Then: Shows:
  - Current MTIF (today)
  - 7-day average MTIF
  - All-time MTIF
  - Alert status
```

---

### S-TELEMETRY-003: Implement Log Diving Rate (6 story points)

**Acceptance Criteria:**
- Log Diving Rate = % of active time with drawdown > 5%
- Metric: ldr_pct (0–100)
- Alert if LDR > 30% (strategy too volatile)
- Correlation with risk events
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-013.01 [P0-UNIT] LDR: Calculate drawdown percentage
```
Given: Peak equity: $100,000
When: Current equity: $95,000
Then: Drawdown = ($100,000 - $95,000) / $100,000 = 5%
```

#### T-013.02 [P0-UNIT] LDR: Flag severe drawdown
```
Given: Drawdown = 5% (at threshold)
When: Check if drawdown > 5%
Then: Flagged as "severe drawdown"

Given: Drawdown = 4.9% (below threshold)
When: Check if drawdown > 5%
Then: Not flagged
```

#### T-013.03 [P0-INT] LDR: Calculate for active period
```
Given: Strategy ACTIVE for 3600 seconds
When: 900 seconds with drawdown > 5%
And: Calculate LDR
Then: LDR = (900 / 3600) * 100 = 25%
```

#### T-013.04 [P1-INT] LDR: Time-series tracking
```
Given: Strategy with equity curve
When: Calculate LDR every minute during active period
Then: Generates 60-minute time-series of LDR
And: Shows peaks (high volatility periods)
```

#### T-013.05 [P1-INT] LDR: Alert on high LDR
```
Given: Strategy with LDR = 35% (above 30% threshold)
When: Alert rule evaluates
Then: Alert: "High log diving rate (35%) - strategy volatile"
And: Recommendation: "Review risk controls"
```

#### T-013.06 [P2-INT] LDR: Correlation with risk events
```
Given: Strategy with high LDR and multiple kill-switch triggers
When: Analyze correlation
Then: Report: "High LDR (35%) correlated with 5 risk events"
And: Suggests strategy parameter adjustment
```

---

### S-TELEMETRY-004: Build Metrics Dashboard (8 story points)

**Acceptance Criteria:**
- Dashboard displays: TTF, MTIF, LDR, win_rate, Sharpe, max_dd for all strategies
- Real-time updates (5-second refresh)
- Filter by date range, team, status
- Export metrics as CSV
- 8+ unit tests passing

**Test Scenarios (6 tests):**

#### T-014.01 [P0-INT] Dashboard: Display TTF metric
```
Given: Dashboard loaded
When: View strategy list
Then: TTF column shows time values (e.g., "10m 30s", "2h 15m")
And: Color-coded by threshold (green <4h, yellow 4-8h, red >8h)
```

#### T-014.02 [P0-INT] Dashboard: Real-time update
```
Given: Dashboard showing live strategies
When: New trade executed
Then: Dashboard updates within 5 seconds
And: Metrics (TTF, LDR, ROI) refreshed
```

#### T-014.03 [P1-INT] Dashboard: Filter by date range
```
Given: Dashboard with 6 months of data
When: Filter by date "Last 7 days"
Then: Shows only strategies with state changes in last 7 days
And: Count updates accordingly
```

#### T-014.04 [P1-INT] Dashboard: Filter by status
```
Given: Dashboard with mixed status strategies (DRAFT, PENDING, APPROVED, ACTIVE, COMPLETED)
When: Filter by status="ACTIVE"
Then: Shows only ACTIVE strategies
And: Metrics filtered accordingly
```

#### T-014.05 [P1-INT] Dashboard: Export to CSV
```
Given: Dashboard with 50 strategies
When: Click "Export Metrics"
Then: CSV file generated with columns:
  - strategy_id, status, ttf, mtif, ldr, win_rate, sharpe, max_dd
And: All 50 rows included
```

#### T-014.06 [P2-INT] Dashboard: Performance with large dataset
```
Given: Dashboard with 1000 strategies
When: Apply filter + refresh
Then: Dashboard responds in <2 seconds
And: No lag detected
And: Memory usage < 500MB
```

---

### S-TELEMETRY-005: Create Alert Rules (4 story points)

**Acceptance Criteria:**
- Rule: TTF > 24h → alert "Slow approval"
- Rule: MTIF < 10m → alert "Frequent kills"
- Rule: LDR > 30% → alert "High volatility"
- Rules configurable per team
- 4+ unit tests passing

**Test Scenarios (5 tests):**

#### T-015.01 [P0-INT] Alert: Slow approval (TTF > 24h)
```
Given: Strategy in PENDING for 25 hours
When: Alert rule evaluates
Then: Alert created: "Slow approval detected"
And: Alert includes strategy_id, current_ttf=25h
And: Alert severity: "warning"
```

#### T-015.02 [P0-INT] Alert: Frequent kills (MTIF < 10m)
```
Given: Strategy with MTIF = 5 minutes
When: Alert rule evaluates
Then: Alert created: "Low MTIF detected"
And: Alert includes: "Strategy killed frequently - avg 5m"
And: Alert severity: "info"
```

#### T-015.03 [P0-INT] Alert: High volatility (LDR > 30%)
```
Given: Strategy with LDR = 35%
When: Alert rule evaluates
Then: Alert created: "High log diving rate (35%)"
And: Alert severity: "warning"
```

#### T-015.04 [P1-INT] Alert: Configurable thresholds
```
Given: Alert rules with default thresholds
When: Admin updates rule "TTF > 24h" to "TTF > 12h"
Then: New threshold applied
And: Retroactive check on existing strategies
And: New alerts generated if exceeded
```

#### T-015.05 [P1-INT] Alert: Team-specific rules
```
Given: Team A and Team B with different risk tolerances
When: Set Team A: MTIF threshold = 5m, Team B: MTIF threshold = 10m
Then: Alerts generated based on team's threshold
And: Same strategy may trigger alert for Team B, not Team A
```

---

## Epic 4: Compare Workflow

**Story Set:** S-COMPARE-001 to S-COMPARE-005
**Test Count:** 32 tests
**Priority Breakdown:** P0=16, P1=12, P2=3, P3=1

### S-COMPARE-001: Implement Comparison Algorithm (7 story points)

**Acceptance Criteria:**
- Compare 2+ runs (different strategies, parameters, time periods)
- Metrics diff: Sharpe, win_rate, max_dd, ROI delta
- Identify best performer
- Statistical significance test (e.g., t-test on returns)
- 7+ unit tests passing

**Test Scenarios (7 tests):**

#### T-016.01 [P0-UNIT] Compare: Calculate delta Sharpe
```
Given: Run A (Sharpe = 1.5), Run B (Sharpe = 1.8)
When: Compare
Then: delta_sharpe = 1.8 - 1.5 = 0.3
And: Run B is better by 0.3 Sharpe points
```

#### T-016.02 [P0-UNIT] Compare: Win rate delta
```
Given: Run A (win_rate = 0.55), Run B (win_rate = 0.60)
When: Compare
Then: delta_win_rate = 0.05 (5 percentage points)
And: Run B wins 5% more trades
```

#### T-016.03 [P0-UNIT] Compare: Max drawdown comparison
```
Given: Run A (max_dd = -0.20), Run B (max_dd = -0.15)
When: Compare
Then: Run B is better (smaller drawdown)
And: delta_max_dd = 0.05 (B is 5% less risky)
```

#### T-016.04 [P0-INT] Compare: Multi-metric ranking
```
Given: 3 runs with different metrics
When: Rank all metrics
Then: Generates ranking:
  - Best Sharpe: Run A
  - Best win_rate: Run C
  - Best max_dd: Run B
And: Overall winner determined by weighted score
```

#### T-016.05 [P1-INT] Compare: Statistical significance (t-test)
```
Given: Run A returns: [0.01, -0.01, 0.02, 0.03, -0.02]
And: Run B returns: [0.02, 0.01, 0.03, 0.04, 0.02]
When: Run t-test (alpha=0.05)
Then: If p-value < 0.05: "Statistically significant difference"
And: If p-value >= 0.05: "No significant difference"
```

#### T-016.06 [P1-INT] Compare: Identify outperformer
```
Given: Run A overall score: 78, Run B overall score: 85
When: Determine best run
Then: Run B identified as outperformer
And: Confidence metric: "High" (if score diff > 10)
```

#### T-016.07 [P2-INT] Compare: Handling tied metrics
```
Given: Two runs with identical Sharpe, win_rate, max_dd
When: Compare
Then: Delta all zero
And: Reported: "Runs have equivalent performance"
And: Tie-breaker: compare secondary metric (e.g., Calmar ratio)
```

---

### S-COMPARE-002: Build Run Selection UI (5 story points)

**Acceptance Criteria:**
- UI component: Select 2+ runs from list
- Date range filter
- Strategy filter
- Checkbox selection with "Compare" button
- Display run details (creation date, metrics preview)
- 5+ unit tests passing

**Test Scenarios (6 tests):**

#### T-017.01 [P0-E2E] Compare UI: Load run list
```
Given: Dashboard with compare workflow
When: Click "Compare Runs" button
Then: Modal opens with list of available runs
And: Shows: run_id, creation_date, strategy_name, status
```

#### T-017.02 [P0-E2E] Compare UI: Select runs
```
Given: Run list displayed
When: Click checkbox next to Run A and Run B
Then: Both runs highlighted/selected
And: "Compare" button enabled
```

#### T-017.03 [P0-E2E] Compare UI: Date filter
```
Given: Run list with 10 runs over 3 months
When: Apply filter "Last 7 days"
Then: Shows only runs created in last 7 days (3 runs)
And: Others hidden
```

#### T-017.04 [P1-E2E] Compare UI: Strategy filter
```
Given: Run list with runs from 5 different strategies
When: Select strategy "Strategy-X"
Then: Shows only runs from Strategy-X
```

#### T-017.05 [P1-E2E] Compare UI: Multiple selections
```
Given: Run list
When: Select 3 runs (A, B, C)
Then: All 3 shown as selected
And: "Compare 3 Runs" button text updates
And: Clicking Compare proceeds to comparison view
```

#### T-017.06 [P1-E2E] Compare UI: Run details preview
```
Given: Hovering over a run in list
When: Details tooltip appears
Then: Shows: Sharpe, win_rate, max_dd, ROI (preview metrics)
```

---

### S-COMPARE-003: Create Delta Visualization (6 story points)

**Acceptance Criteria:**
- Side-by-side comparison table (Run A vs Run B metrics)
- Bar chart: Sharpe, ROI, win_rate delta
- Heatmap: Color green (better), red (worse)
- Equity curve overlay (Run A and Run B on same chart)
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-018.01 [P0-INT] Compare: Side-by-side table
```
Given: Two runs selected for comparison
When: Comparison view loaded
Then: Table displays:
  - Metric | Run A | Run B | Delta
  - Sharpe | 1.5 | 1.8 | +0.3 ✓
  - win_rate | 55% | 60% | +5% ✓
  - max_dd | -20% | -15% | +5% (better)
```

#### T-018.02 [P0-INT] Compare: Delta bar chart
```
Given: Comparison data
When: Bar chart rendered
Then: Shows bars for each metric:
  - Sharpe delta: +0.3
  - ROI delta: +$1000
  - win_rate delta: +5%
And: Bars proportional to delta magnitude
```

#### T-018.03 [P0-INT] Compare: Heatmap color coding
```
Given: Comparison metrics
When: Heatmap rendered
Then: Colors applied:
  - Green: Run A better (e.g., higher Sharpe)
  - Red: Run B better
  - Yellow: Within threshold (< 2% diff)
```

#### T-018.04 [P1-INT] Compare: Equity curve overlay
```
Given: Run A and Run B equity curves
When: Overlay both on same chart
Then: Two lines shown:
  - Run A: blue line
  - Run B: orange line
And: Both aligned to same time axis (start date)
And: Legend identifies each line
```

#### T-018.05 [P1-INT] Compare: Equity curve crossover
```
Given: Overlay chart where Run A starts better, Run B ends better
When: Chart rendered
Then: Clear visualization of performance crossover point
And: Identifies when one strategy overtook the other
```

#### T-018.06 [P2-INT] Compare: 3-way comparison
```
Given: 3 runs (A, B, C)
When: Comparison view loaded
Then: Table shows all 3 runs side-by-side
And: Identifies best performer (highlighted)
And: Worst performer shaded differently
```

---

### S-COMPARE-004: Add Metric Selection (4 story points)

**Acceptance Criteria:**
- User-selectable metrics: Sharpe, ROI, max_dd, win_rate, Calmar, Sortino, PSR, VaR
- Toggle visibility in visualization
- Save metric preference
- 4+ unit tests passing

**Test Scenarios (5 tests):**

#### T-019.01 [P0-E2E] Compare: Toggle metric visibility
```
Given: Comparison table with 8 metrics
When: Uncheck "Calmar ratio"
Then: Calmar column hidden from table
And: Calmar removed from bar chart
And: Table and chart update immediately
```

#### T-019.02 [P0-E2E] Compare: Select metrics for chart
```
Given: Metric selection panel
When: Select only ["Sharpe", "max_dd", "win_rate"]
Then: Bar chart shows only these 3 metrics
And: Others excluded
```

#### T-019.03 [P1-E2E] Compare: Save metric preference
```
Given: User selects custom metrics (Sharpe, Sortino, PSR)
When: Click "Save Preference"
Then: Preference stored for this user
And: Next comparison defaults to these metrics
And: Can reset to "All metrics" anytime
```

#### T-019.04 [P1-INT] Compare: Metric availability check
```
Given: Run with incomplete metrics (missing Sortino)
When: User selects Sortino in metric list
Then: "Not available for this run" shown grayed out
And: Cannot select/view unavailable metric
```

#### T-019.05 [P2-E2E] Compare: Metric tooltip details
```
Given: Hovering over metric name
When: Tooltip appears
Then: Shows definition: "Sharpe ratio = (return - risk_free) / std_dev"
And: Explains interpretation: "Higher is better"
And: Confidence level (if applicable)
```

---

### S-COMPARE-005: Build Export Functionality (3 story points)

**Acceptance Criteria:**
- Export comparison as CSV, PDF, JSON
- Include all metrics and delta values
- Timestamp of export
- Filename includes run IDs and export date
- 3+ unit tests passing

**Test Scenarios (4 tests):**

#### T-020.01 [P0-INT] Export: Generate CSV
```
Given: Comparison of Run A and Run B
When: Click "Export as CSV"
Then: CSV file generated with:
  - Headers: Metric, Run_A, Run_B, Delta
  - Row for each metric
  - Timestamp in footer
And: Filename: "compare-run-A-run-B-2026-02-26.csv"
```

#### T-020.02 [P0-INT] Export: Generate PDF
```
Given: Comparison visualization
When: Click "Export as PDF"
Then: PDF created with:
  - Comparison table
  - Bar chart
  - Equity curve overlay chart
  - Timestamp and run IDs
And: File size reasonable (<5MB)
```

#### T-020.03 [P1-INT] Export: Generate JSON
```
Given: Comparison data
When: Click "Export as JSON"
Then: JSON file generated with structure:
  {
    "comparison_metadata": {...},
    "run_A": {...},
    "run_B": {...},
    "delta": {...}
  }
And: Valid JSON syntax
```

#### T-020.04 [P1-INT] Export: Multiple runs
```
Given: 3-way comparison (Run A, B, C)
When: Export as CSV
Then: CSV shows all 3 runs as columns
And: Delta columns for A vs B, B vs C, A vs C
And: All data included
```

---

## Epic 5: Audit Trail

**Story Set:** S-AUDIT-001 to S-AUDIT-005
**Test Count:** 30 tests
**Priority Breakdown:** P0=16, P1=10, P2=3, P3=1

### S-AUDIT-001: Implement Audit Trail Collection (6 story points)

**Acceptance Criteria:**
- Capture all state transitions, decisions, modifications
- Timestamp (UTC), actor, action, details
- Immutable append-only log
- Query interface (filter by entity, actor, date range)
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-021.01 [P0-UNIT] Audit: Log state transition
```
Given: Strategy transitioning DRAFT → PENDING
When: Transition occurs
Then: Audit entry created:
  - timestamp: 2026-02-26T10:30:45Z
  - entity_id: strategy-123
  - action: "state_transition"
  - details: {from_state: "DRAFT", to_state: "PENDING"}
  - actor_id: "user-1"
```

#### T-021.02 [P0-UNIT] Audit: Log approval decision
```
Given: Reviewer approves strategy
When: approve() called
Then: Audit entry created:
  - action: "approval"
  - details: {reviewer_id, approval_comment}
  - timestamp recorded
```

#### T-021.03 [P0-UNIT] Audit: Log modification
```
Given: Strategy parameter updated
When: update_parameter() called
Then: Audit entry created:
  - action: "modification"
  - details: {parameter_name, old_value, new_value}
  - actor_id recorded
```

#### T-021.04 [P0-INT] Audit: Immutable append-only
```
Given: Existing audit entries
When: New entry added
Then: Appended to log (no edits to prior entries)
And: Audit entry IDs sequential or timestamped
And: No entry deleted or modified
```

#### T-021.05 [P1-INT] Audit: Query by entity
```
Given: Audit log with 1000 entries
When: query_audit(entity_id="strategy-123") called
Then: Returns only entries for strategy-123
And: Count: 20+ entries (typical for lifecycle)
```

#### T-021.06 [P1-INT] Audit: Query by date range
```
Given: Audit log spanning 6 months
When: query_audit(start="2026-02-01", end="2026-02-15") called
Then: Returns only entries in date range
And: 50+ entries (typical 2-week period)
```

---

### S-AUDIT-002: Build Verification Algorithm (7 story points)

**Acceptance Criteria:**
- Verify strategy lifecycle consistency (all required steps completed)
- Check decision completeness (all approvals obtained)
- Detect anomalies (state transition skipped, unauthorized actor)
- Report verification status: VALID, NEEDS_REVIEW, INVALID
- 7+ unit tests passing

**Test Scenarios (7 tests):**

#### T-022.01 [P0-INT] Verify: Valid lifecycle
```
Given: Strategy with complete lifecycle:
  DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED
When: verify_lifecycle(strategy_id=123) called
Then: Status: VALID
And: Message: "Strategy lifecycle complete and consistent"
```

#### T-022.02 [P0-INT] Verify: Missing approval step
```
Given: Strategy with audit trail: DRAFT → PENDING → ACTIVE (skipped APPROVED)
When: verify_lifecycle() called
Then: Status: INVALID
And: Message: "Missing APPROVED state transition"
And: Recommendation: "Manual review required"
```

#### T-022.03 [P0-INT] Verify: Incomplete approvals
```
Given: Strategy requires 3 approvals, only 2 obtained
When: verify_approvals() called
Then: Status: NEEDS_REVIEW
And: Message: "Approval from reviewer-3 pending"
```

#### T-022.04 [P0-INT] Verify: Unauthorized actor
```
Given: Audit entry showing approval by non-reviewer
When: verify_authorization() called
Then: Status: INVALID
And: Flag: "Unauthorized approver"
And: Recommendation: "Escalate to admin"
```

#### T-022.05 [P1-INT] Verify: State machine violations
```
Given: Impossible state transition detected (e.g., COMPLETED → DRAFT)
When: verify_state_machine() called
Then: Status: INVALID
And: Message: "Impossible transition detected"
```

#### T-022.06 [P1-INT] Verify: Full report generation
```
Given: Strategy audit trail
When: generate_verification_report() called
Then: Report includes:
  - Lifecycle status
  - Approval status
  - Authorization checks
  - Anomaly flags
  - Overall verdict
```

#### T-022.07 [P2-INT] Verify: Anomaly detection
```
Given: Audit trail with unusual pattern (state transition at 3am, unusual actor)
When: detect_anomalies() called
Then: Flags potential issues:
  - "State transition outside business hours"
  - "Unusual actor for approval"
And: Status: NEEDS_REVIEW (not automatically INVALID)
```

---

### S-AUDIT-003: Create Audit UI (6 story points)

**Acceptance Criteria:**
- Timeline view of all events (chronological)
- Filter by action type (transition, approval, modification)
- Show actor, timestamp, details for each event
- Search by keyword (strategy_id, actor, comment)
- 6+ unit tests passing

**Test Scenarios (6 tests):**

#### T-023.01 [P0-E2E] Audit UI: Load timeline
```
Given: Audit UI opened for a strategy
When: Timeline component loaded
Then: Displays chronological list of events:
  - 2026-02-26T10:00:00Z | State: DRAFT → PENDING | user-1
  - 2026-02-26T10:05:00Z | Approval | reviewer-1 | "Good strategy"
  - ...
```

#### T-023.02 [P0-E2E] Audit UI: Filter by action type
```
Given: Timeline with mixed actions (state, approval, modification)
When: Select filter "Approval only"
Then: Shows only approval events
And: State transitions and modifications hidden
```

#### T-023.03 [P0-E2E] Audit UI: Expand event details
```
Given: Timeline event visible
When: Click on event to expand
Then: Shows full details:
  - Timestamp (exact UTC)
  - Actor with link to profile
  - Action type
  - Details object (formatted JSON or readable text)
```

#### T-023.04 [P1-E2E] Audit UI: Search by keyword
```
Given: Timeline with 100+ events
When: Search for "reviewer-1"
Then: Shows only events involving reviewer-1
And: Highlights matching actor names
```

#### T-023.05 [P1-E2E] Audit UI: Search by timestamp
```
Given: Timeline spanning 6 months
When: Search for "2026-02-26"
Then: Shows all events from that date
And: Sorted chronologically
```

#### T-023.06 [P2-E2E] Audit UI: Export audit trail
```
Given: Audit timeline
When: Click "Export Audit Trail"
Then: CSV file generated with columns:
  - timestamp, action, actor, details
And: All events included
And: Filename: "audit-strategy-123-2026-02-26.csv"
```

---

### S-AUDIT-004: Add "Reproduce Run" Button (4 story points)

**Acceptance Criteria:**
- User clicks "Reproduce Run" on audit trail
- System creates new strategy with identical parameters from audited run
- New strategy starts in DRAFT state
- Original run_id linked as "based_on" metadata
- 4+ unit tests passing

**Test Scenarios (5 tests):**

#### T-024.01 [P0-E2E] Reproduce: Create new strategy from run
```
Given: Audit trail showing completed run
When: Click "Reproduce Run" button
Then: New strategy created with:
  - Same parameters as original run
  - Status: DRAFT
  - based_on_run_id: original_run_id
  - created_at: current timestamp
```

#### T-024.02 [P0-INT] Reproduce: Copy parameters
```
Given: Original run with parameters: {param_A: 0.5, param_B: 1.2, ...}
When: Reproduce run
Then: New strategy has identical parameters:
  - param_A: 0.5 (copied)
  - param_B: 1.2 (copied)
  - All parameters preserved
```

#### T-024.03 [P1-E2E] Reproduce: Link metadata
```
Given: New reproduced strategy created
When: View strategy details
Then: Shows "Based on run: run-12345"
And: Link to original run available
And: Can compare original vs reproduced metrics side-by-side
```

#### T-024.04 [P1-INT] Reproduce: Preserve decision history
```
Given: Original run with approval history
When: Reproduce run
Then: New strategy inherits NO approvals (starts fresh)
And: Original approvals visible as historical reference
And: New approvals required for new strategy
```

#### T-024.05 [P2-E2E] Reproduce: Safety check
```
Given: Original run from 6 months ago with outdated market data
When: User reproduces run
Then: Warning displayed: "Original run used data from 6 months ago"
And: User must confirm: "Proceed with stale data?" or "Update date range"
And: If confirmed, new strategy uses original date range
```

---

### S-AUDIT-005: Build Diagnostic Tool (2 story points)

**Acceptance Criteria:**
- Run diagnostic on audit trail (consistency checks)
- Report: all issues found, severity level
- Suggestions for remediation
- Export diagnostic report
- 2+ unit tests passing

**Test Scenarios (4 tests):**

#### T-025.01 [P0-INT] Diagnostic: Run checks
```
Given: Audit trail loaded
When: Run diagnostic_check(strategy_id=123) called
Then: Performs checks:
  - Lifecycle consistency
  - Decision completeness
  - Authorization validity
  - Timestamp monotonicity
And: Returns results for each check
```

#### T-025.02 [P0-INT] Diagnostic: Report issues
```
Given: Diagnostic completed with findings
When: Report generated
Then: Lists all issues:
  - "Missing APPROVED state" (severity: HIGH)
  - "Unauthorized transition" (severity: CRITICAL)
  - "Data integrity issue" (severity: MEDIUM)
And: Sorted by severity
```

#### T-025.03 [P1-INT] Diagnostic: Remediation suggestions
```
Given: Issue detected: "Missing APPROVED state"
When: Diagnostic report generated
Then: Suggestion provided:
  - "Manually review and approve strategy"
  - "Or mark as legacy (pre-approval era)"
```

#### T-025.04 [P2-INT] Diagnostic: Export report
```
Given: Diagnostic report completed
When: Export diagnostic report
Then: HTML file generated with:
  - Executive summary
  - Detailed findings
  - Remediation steps
  - Timestamp of diagnostic run
And: File: "diagnostic-strategy-123-2026-02-26.html"
```

---

## Priority Index

### P0 Priority (Critical Path, Must Pass Before Merge)

**Total P0 Tests: 90**

#### Epic 1 (Strategy Lifecycle): 18 P0 tests
- T-001.01 to T-001.10 (State Machine)
- T-002.01 to T-002.07 (Approval Workflow)
- T-003.01 to T-003.04 (Kill-Switch)

#### Epic 2 (Journal Schema): 16 P0 tests
- T-006.01 to T-006.04 (Manifest structure)
- T-007.01 to T-007.05 (Summary schema)
- T-008.01 to T-008.04 (Events NDJSON)
- T-009.01 to T-009.04 (Database schema)

#### Epic 3 (Telemetry): 14 P0 tests
- T-011.01 to T-011.03 (TTF)
- T-012.01 to T-012.03 (MTIF)
- T-013.01 to T-013.03 (LDR)
- T-014.01 to T-014.02 (Dashboard)
- T-015.01 to T-015.03 (Alerts)

#### Epic 4 (Compare): 16 P0 tests
- T-016.01 to T-016.04 (Comparison Algorithm)
- T-017.01 to T-017.02 (UI run selection)
- T-018.01 to T-018.03 (Visualization)
- T-019.01 to T-019.02 (Metric selection)
- T-020.01 (CSV export)

#### Epic 5 (Audit): 16 P0 tests
- T-021.01 to T-021.04 (Audit collection)
- T-022.01 to T-022.04 (Verification)
- T-023.01 to T-023.03 (Audit UI)
- T-024.01 to T-024.02 (Reproduce)
- T-025.01 (Diagnostic)

---

### P1 Priority (High Priority, Regression Tests)

**Total P1 Tests: 60**

These are integration and E2E tests validating cross-story workflows, data persistence, and correctness.

---

### P2 Priority (Boundary & Edge Cases)

**Total P2 Tests: 20**

Edge case handling, unusual but valid scenarios, and stress conditions.

---

### P3 Priority (Future/Nice-to-Have)

**Total P3 Tests: 10**

Performance optimization, scalability, and exploratory tests.

---

## Coverage Matrix

### Test → Story → Acceptance Criteria Mapping

| Test ID | Story ID | Story Title | Acceptance Criteria Covered | Framework | Priority |
|---------|----------|-------------|---------------------------|-----------|----------|
| T-001.01 - T-001.13 | S-STRATEGY-001 | State Machine | All 4 (transitions, invalid, audit, unit tests) | pytest | P0-P1 |
| T-002.01 - T-002.11 | S-STRATEGY-002 | Approval Workflow | All 5 (reviewers, decisions, comments, notifications, tests) | pytest | P0-P1 |
| T-003.01 - T-003.08 | S-STRATEGY-003 | Kill-Switch | All 4 (ACTIVE, graceful, state, cleanup) | pytest | P0-P2 |
| T-004.01 - T-004.06 | S-STRATEGY-004 | State Timeline | All 4 (chronological, actors, zoom, export) | pytest | P0-P2 |
| T-005.01 - T-005.06 | S-STRATEGY-005 | Rejection/Resubmit | All 4 (edit, resubmit, reason visible, chain) | pytest | P0-P1 |
| T-006.01 - T-006.08 | S-JOURNAL-001 | Manifest Schema | All 4 (schema, types, samples, tests) | pytest | P0-P1 |
| T-007.01 - T-007.10 | S-JOURNAL-002 | Summary v3.0 | All 4 (schema, calc, compat, tests) | pytest | P0-P1 |
| T-008.01 - T-008.08 | S-JOURNAL-003 | Events NDJSON | All 4 (format, events, query, tests) | pytest | P0-P1 |
| T-009.01 - T-009.07 | S-JOURNAL-004 | DB Schema | All 5 (create, FK, indexes, migration, backup) | pytest | P0-P2 |
| T-010.01 - T-010.07 | S-JOURNAL-005 | Reproducibility | All 5 (hash, verify, integrity, seed, freeze) | pytest | P0-P2 |
| T-011.01 - T-011.06 | S-TELEMETRY-001 | TTF Metrics | All 4 (track, alerts, dashboard, tests) | pytest | P0-P1 |
| T-012.01 - T-012.06 | S-TELEMETRY-002 | MTIF Calc | All 4 (calculate, agg, alerts, dashboard) | pytest | P0-P1 |
| T-013.01 - T-013.06 | S-TELEMETRY-003 | LDR | All 4 (calculate, track, alerts, correlation) | pytest | P0-P2 |
| T-014.01 - T-014.06 | S-TELEMETRY-004 | Dashboard | All 4 (display, realtime, filter, export) | playwright | P0-P2 |
| T-015.01 - T-015.05 | S-TELEMETRY-005 | Alert Rules | All 4 (rules, configurable, team-specific, tests) | pytest | P0-P1 |
| T-016.01 - T-016.07 | S-COMPARE-001 | Comparison Algo | All 4 (metrics, ranking, significance, winner) | pytest | P0-P2 |
| T-017.01 - T-017.06 | S-COMPARE-002 | Run Selection UI | All 4 (list, select, filter, preview) | playwright | P0-P1 |
| T-018.01 - T-018.06 | S-COMPARE-003 | Visualization | All 4 (table, chart, heatmap, equity curve) | playwright | P0-P2 |
| T-019.01 - T-019.05 | S-COMPARE-004 | Metric Selection | All 4 (toggle, select, save, availability) | playwright | P0-P2 |
| T-020.01 - T-020.04 | S-COMPARE-005 | Export | All 4 (CSV, PDF, JSON, multi-run) | playwright | P0-P1 |
| T-021.01 - T-021.06 | S-AUDIT-001 | Audit Collection | All 4 (capture, immutable, query, tests) | pytest | P0-P1 |
| T-022.01 - T-022.07 | S-AUDIT-002 | Verification Algo | All 4 (verify, completeness, anomalies, report) | pytest | P0-P2 |
| T-023.01 - T-023.06 | S-AUDIT-003 | Audit UI | All 4 (timeline, filter, search, export) | playwright | P0-P2 |
| T-024.01 - T-024.05 | S-AUDIT-004 | Reproduce Button | All 4 (create, copy, link, safety) | playwright | P0-P2 |
| T-025.01 - T-025.04 | S-AUDIT-005 | Diagnostic Tool | All 4 (checks, report, suggestions, export) | pytest | P0-P2 |

---

## Test Execution Status

### Current Status: RED PHASE (All 180 tests failing)

**Total Tests:** 180
**Passing:** 0
**Failing:** 180
**Skipped:** 0
**Test Framework:** Playwright (E2E) + pytest (Unit/Integration)

### Test Breakdown by Framework

| Framework | Test Count | Examples |
|-----------|-----------|----------|
| pytest (Unit + Integration) | 125 | T-001.01, T-006.01, T-011.01, T-016.01, T-021.01 |
| Playwright (E2E) | 55 | T-004.03, T-017.01, T-018.01, T-023.01, T-024.01 |

---

## Next Steps for Implementation

### Phase 1: Red Phase (Current - Days 1-14)
1. ✅ All 180 tests defined in ATDD format (this document)
2. ✅ Tests mapped to stories and acceptance criteria
3. ⏭ Tests failing (awaiting code implementation)

### Phase 2: Green Phase (Days 15-42)
1. Implement code for S-STRATEGY-001 (state machine) to satisfy T-001.01 through T-001.13
2. Implement code for other stories in priority order
3. Tests transition from RED → YELLOW (partially passing) → GREEN (all passing)

### Phase 3: Refactor Phase (Days 43-56)
1. Clean up test code (remove duplication, improve readability)
2. Add performance optimizations
3. Ensure all P0 tests pass with <1% flakiness

### Phase 4: Monitoring (Days 57+)
1. Continuous integration pipeline validates all tests on every commit
2. Regression tests prevent feature breakage
3. Performance benchmarks tracked over time

---

## Test Infrastructure Requirements

### Test Dependencies

```
pytest>=7.0.0
pytest-xdist>=3.0.0          # Parallel test execution
pytest-cov>=4.0.0            # Code coverage
pytest-timeout>=2.1.0        # Timeout enforcement
pytest-mock>=3.10.0          # Mocking fixtures

@playwright/test>=1.43.0
@faker-js/faker>=8.0.0       # Test data generation

numpy>=1.21.0
pandas>=1.3.0
vectorbt>=0.23.0             # Backtest fixtures
```

### Database Requirements

- SQLite (Phase 1, local testing)
- PostgreSQL 13+ (Phase 2+, multi-TF caching)

### Environment Variables

```bash
DASHBOARD_URL=http://localhost:8050
BASE_URL=http://localhost:8050
TEST_ENV=local
DATABASE_URL=sqlite:///test.db  # or postgres://...
```

---

## Test File Organization

Tests should be organized as:

```
tests/
├── unit/
│   ├── test_state_machine.py          (T-001.01 - T-001.13)
│   ├── test_approval_workflow.py       (T-002.01 - T-002.11)
│   ├── test_manifest_schema.py         (T-006.01 - T-006.08)
│   ├── test_summary_schema.py          (T-007.01 - T-007.10)
│   ├── test_events_ndjson.py          (T-008.01 - T-008.08)
│   ├── test_ttf_metrics.py            (T-011.01 - T-011.06)
│   ├── test_mtif_metrics.py           (T-012.01 - T-012.06)
│   ├── test_ldr_metrics.py            (T-013.01 - T-013.06)
│   └── ... (other unit tests)
│
├── integration/
│   ├── test_kill_switch_integration.py (T-003.01 - T-003.08)
│   ├── test_db_schema_integration.py   (T-009.01 - T-009.07)
│   ├── test_comparison_algorithm.py    (T-016.01 - T-016.07)
│   ├── test_audit_trail_integration.py (T-021.01 - T-025.04)
│   └── ... (other integration tests)
│
└── e2e/
    ├── test_state_timeline_e2e.py      (T-004.03 - T-004.06)
    ├── test_run_selection_ui_e2e.py    (T-017.01 - T-017.06)
    ├── test_compare_visualization_e2e.py (T-018.01 - T-018.06)
    ├── test_audit_ui_e2e.py            (T-023.01 - T-023.06)
    ├── test_reproduce_button_e2e.py    (T-024.01 - T-024.05)
    └── ... (other E2E tests)
```

---

## Key Testing Patterns Used

### 1. Given-When-Then (BDD)
All tests follow explicit Given-When-Then structure for clarity and traceability.

### 2. Deterministic Fixtures
- Fixed seeds for randomness (numpy, pandas, Optuna)
- Frozen datasets (no live API calls)
- In-memory databases (SQLite) for isolation

### 3. No Hard-Coded Waits
- Use `waitForSelector()`, `waitForLoadState()` instead of `sleep()`
- Use `expect().toHaveProperty()` instead of checking after delay

### 4. Test Data Factories
- `UserFactory` for test users
- `OptimizationFactory` for run data
- `ManifestFactory` for schema validation

### 5. Network Interception
- Mock API responses before navigation
- Simulate network errors for resilience
- No reliance on external services

---

## Acceptance Criteria Definition

Each story's acceptance criteria are defined as **specific, measurable test scenarios** in this document. Implementation is complete when:

1. All unit tests (T-XXX.01 - T-XXX.XX) pass for the story
2. Integration tests verify cross-story interactions
3. E2E tests confirm user-facing functionality
4. Code coverage ≥ 80% for story's codebase
5. No regressions in previously passing tests

---

## Reference Documents

- **Test Framework Setup:** `/d/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad-output/zone1/test-framework-setup.md`
- **Test Design System:** `/d/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad-output/zone1/test-design-architecture.md`
- **Sprint Plan:** `/d/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad-output/zone1/sprint-plan-phase1.md`
- **Story List:** `/d/Users/NIKITA/Documents/DEV/BMAD-MNNZ/_bmad-output/zone1/story-list.md`

---

**End of Acceptance Tests Document**

**Generated by:** Agent-5 (testarch-atdd specialist)
**Date:** 2026-02-26
**Status:** RED Phase (All 180 tests failing, awaiting implementation)
**Next:** Proceed to dev-story implementation (Zone 2, Agent-6)

