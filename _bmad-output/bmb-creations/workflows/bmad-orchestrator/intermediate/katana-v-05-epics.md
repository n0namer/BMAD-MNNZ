# Katana V05 - Epics Definition

**Project:** Katana Vectorbt Optimizer
**Version:** 05
**Date Created:** 2026-02-26
**Total Epics:** 5
**Total Stories:** 25

---

## EPIC 1: E-STRATEGY-LIFECYCLE

**Epic ID:** E-STRATEGY-LIFECYCLE
**Source Blocker:** BLOCKER-1
**Priority:** CRITICAL
**Complexity:** HIGH

### Description
Strategy lifecycle management with state machine implementation. Enables strategies to transition through defined states with approval workflows, rejection handling, and kill-switch mechanisms.

### Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Minimum 30 unit tests covering all state transitions
- State machine diagram documented
- Approval workflow tested with 5+ scenarios
- Kill-switch functionality verified for all states

### Stories

#### S-STRATEGY-001: Implement State Machine Transitions
- **Description:** Build state machine for strategy lifecycle (DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED/CANCELLED)
- **Acceptance Criteria:**
  - State transitions defined and validated
  - Invalid transitions rejected
  - Audit trail tracks all transitions
  - 10+ unit tests
- **Estimated Points:** 13
- **Dependencies:** None

#### S-STRATEGY-002: Build Approval Workflow
- **Description:** Implement approval workflow with reviewer assignment, approval/rejection decision, and comments
- **Acceptance Criteria:**
  - Reviewers can be assigned to pending strategies
  - Approval and rejection decisions recorded
  - Comments captured with approval decisions
  - Notification system alerts reviewers
  - 8+ unit tests
- **Estimated Points:** 8
- **Dependencies:** S-STRATEGY-001

#### S-STRATEGY-003: Add Kill-Switch Mechanism
- **Description:** Implement kill-switch to immediately stop strategy execution from any state
- **Acceptance Criteria:**
  - Kill-switch callable from ACTIVE state
  - Graceful shutdown of running strategy
  - Final state recorded as KILLED
  - Cleanup operations executed
  - 5+ unit tests
- **Estimated Points:** 5
- **Dependencies:** S-STRATEGY-001

#### S-STRATEGY-004: Create State Timeline
- **Description:** Build visual timeline showing all state transitions with timestamps and responsible actors
- **Acceptance Criteria:**
  - Timeline displays all transitions chronologically
  - Actors and timestamps shown for each transition
  - Zoom and filter capabilities
  - Export timeline as JSON/CSV
  - 4+ unit tests
- **Estimated Points:** 5
- **Dependencies:** S-STRATEGY-001

#### S-STRATEGY-005: Build Rejection/Resubmit Logic
- **Description:** Implement workflow for rejected strategies to be resubmitted with updated parameters
- **Acceptance Criteria:**
  - Rejected strategy can be edited
  - Resubmit creates new approval request
  - Previous rejection reason visible to submitter
  - Audit trail shows resubmission chain
  - 3+ unit tests
- **Estimated Points:** 3
- **Dependencies:** S-STRATEGY-002

### Deliverables
- State machine implementation (lib/state-machine.ts)
- Approval workflow service (lib/approval-service.ts)
- Kill-switch handler (lib/kill-switch.ts)
- Timeline visualization component (ui/timeline.tsx)
- Resubmission logic (lib/resubmit.ts)

---

## EPIC 2: E-JOURNAL-SCHEMA

**Epic ID:** E-JOURNAL-SCHEMA
**Source Blocker:** BLOCKER-2
**Priority:** CRITICAL
**Complexity:** VERY HIGH

### Description
Run journal schema and reproducibility tracking. Establishes standardized JSON schema for capturing strategy execution details, enabling full reproducibility of runs.

### Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Schema validated against sample data (10+ runs)
- Database migration scripts tested on fresh and existing databases
- Minimum 40 unit tests covering all schema components
- Schema documentation published

### Stories

#### S-JOURNAL-001: Create manifest.json Structure
- **Description:** Define manifest.json schema containing metadata about a strategy run
- **Acceptance Criteria:**
  - Schema includes: strategy_id, version, start_time, end_time, parameters, environment
  - JSON Schema (.json) created and validated
  - TypeScript types generated
  - Sample manifests created
  - 8+ unit tests
- **Estimated Points:** 8
- **Dependencies:** None

#### S-JOURNAL-002: Create summary.json v3.0
- **Description:** Build summary.json schema for high-level run results and metrics
- **Acceptance Criteria:**
  - Schema includes: total_runs, win_rate, sharpe_ratio, max_drawdown, final_equity
  - Aggregation logic implemented
  - Summary auto-calculated from detailed results
  - Backward compatible with v2.0 format
  - 10+ unit tests
- **Estimated Points:** 10
- **Dependencies:** S-JOURNAL-001

#### S-JOURNAL-003: Implement events.ndjson
- **Description:** Create NDJSON event log format for detailed strategy events (trades, signals, errors)
- **Acceptance Criteria:**
  - Event schema defined (type, timestamp, data)
  - Streaming write capability implemented
  - Event filtering/query supported
  - Compression tested (.ndjson.gz)
  - 8+ unit tests
- **Estimated Points:** 8
- **Dependencies:** S-JOURNAL-001

#### S-JOURNAL-004: Build Database Schema (Postgres)
- **Description:** Create Postgres schema for persisting journal data with relational structure
- **Acceptance Criteria:**
  - Tables: runs, strategies, events, metrics, audit_trail
  - Indexes created for performance queries
  - Constraints enforced (FK, unique)
  - Migration scripts (up/down) created
  - 8+ unit tests
- **Estimated Points:** 8
- **Dependencies:** S-JOURNAL-002, S-JOURNAL-003

#### S-JOURNAL-005: Create Reproducibility Verifier
- **Description:** Implement verification tool to confirm a run can be reproduced with captured parameters
- **Acceptance Criteria:**
  - Verifier reads journal data and reruns strategy
  - Tolerance thresholds configurable (±0.01%)
  - Detailed diff report on mismatches
  - Supports deterministic verification
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** S-JOURNAL-001, S-JOURNAL-004

### Deliverables
- manifest.json schema (schemas/manifest-v1.json)
- summary.json v3.0 (schemas/summary-v3.json)
- events.ndjson format spec (schemas/events.ndjson.md)
- Postgres migration files (db/migrations/)
- Reproducibility verifier (lib/reproducibility-verifier.ts)

---

## EPIC 3: E-TELEMETRY-METRICS

**Epic ID:** E-TELEMETRY-METRICS
**Source Blocker:** BLOCKER-3
**Priority:** HIGH
**Complexity:** HIGH

### Description
Success metrics and telemetry instrumentation. Implements tracking of critical operational metrics including Time-to-Status, Mean Time In Flight, and Log Diving Rate.

### Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Dashboard displays all 3 core metrics
- Metrics collected on 100% of strategy runs
- Alert rules evaluated in real-time
- Minimum 30 unit tests covering all metric calculations
- SLA targets defined and monitored

### Stories

#### S-TELEMETRY-001: Instrument Time-to-Status
- **Description:** Implement metric tracking time from strategy submission to status change (DRAFT → PENDING, PENDING → APPROVED, etc.)
- **Acceptance Criteria:**
  - Tracking captures all state transition times
  - Percentile aggregations (p50, p95, p99) calculated
  - Historical trending stored
  - Real-time metric emission
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** E-STRATEGY-LIFECYCLE

#### S-TELEMETRY-002: Implement MTIF Calculation
- **Description:** Calculate Mean Time In Flight - average time from ACTIVE state to completion
- **Acceptance Criteria:**
  - MTIF calculated per strategy
  - Aggregation across time windows (daily, weekly, monthly)
  - Outlier detection applied
  - Trend analysis capability
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** E-STRATEGY-LIFECYCLE

#### S-TELEMETRY-003: Implement Log Diving Rate
- **Description:** Track Log Diving Rate - frequency of error logs requiring investigation
- **Acceptance Criteria:**
  - Error log volume tracked
  - Rate calculated per time window
  - Error classification supported
  - Severity weighting applied
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** S-TELEMETRY-001

#### S-TELEMETRY-004: Build Metrics Dashboard
- **Description:** Create dashboard visualizing Time-to-Status, MTIF, and Log Diving Rate metrics
- **Acceptance Criteria:**
  - Dashboard displays all 3 metrics with sparklines
  - Time range selection (1d, 7d, 30d, custom)
  - Comparison view (current vs. baseline)
  - Drill-down to individual runs
  - 8+ unit tests
- **Estimated Points:** 8
- **Dependencies:** S-TELEMETRY-001, S-TELEMETRY-002, S-TELEMETRY-003

#### S-TELEMETRY-005: Create Alert Rules
- **Description:** Implement alert rules based on metric thresholds
- **Acceptance Criteria:**
  - Rules engine evaluates metrics against thresholds
  - Multiple alert channels supported (Slack, email, PagerDuty)
  - Alert deduplication prevents spam
  - Alert history and muting capability
  - 4+ unit tests
- **Estimated Points:** 4
- **Dependencies:** S-TELEMETRY-004

### Deliverables
- Time-to-Status instrumentation (lib/metrics/time-to-status.ts)
- MTIF calculator (lib/metrics/mtif.ts)
- Log Diving Rate tracker (lib/metrics/log-diving-rate.ts)
- Dashboard component (ui/dashboard/metrics-dashboard.tsx)
- Alert rules engine (lib/alerts/alert-engine.ts)

---

## EPIC 4: E-COMPARE-WORKFLOW

**Epic ID:** E-COMPARE-WORKFLOW
**Source Blocker:** BLOCKER-4
**Priority:** HIGH
**Complexity:** MEDIUM

### Description
Compare strategy runs with delta analysis. Enables users to select two runs and view detailed comparison of parameters, metrics, and outcomes.

### Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Comparison works for any 2 runs from history
- Delta analysis shows all differences with color coding
- Export functionality supports CSV and JSON formats
- Minimum 25 unit tests covering comparison logic
- Performance: comparison loads in <2 seconds

### Stories

#### S-COMPARE-001: Implement Comparison Algorithm
- **Description:** Build algorithm to compare two strategy runs and generate structured delta
- **Acceptance Criteria:**
  - Algorithm identifies differences in parameters, metrics, outcomes
  - Similarity scoring implemented (0-100%)
  - Null/missing values handled correctly
  - Performance: <500ms for typical runs
  - 7+ unit tests
- **Estimated Points:** 7
- **Dependencies:** E-JOURNAL-SCHEMA

#### S-COMPARE-002: Build Run Selection UI
- **Description:** Create interface for users to select 2 runs to compare
- **Acceptance Criteria:**
  - Run list displays key metadata (date, status, key metrics)
  - Search/filter by date range, strategy, status
  - Recently compared runs available as quick access
  - Date range picker for bulk selection
  - 5+ unit tests
- **Estimated Points:** 5
- **Dependencies:** S-COMPARE-001

#### S-COMPARE-003: Create Delta Visualization
- **Description:** Build visual representation of differences between two runs
- **Acceptance Criteria:**
  - Side-by-side comparison view
  - Differences highlighted in color (added: green, removed: red, changed: yellow)
  - Sortable columns (field name, old value, new value, change type)
  - Drill-down into nested fields
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** S-COMPARE-002

#### S-COMPARE-004: Add Metric Selection
- **Description:** Allow users to focus comparison on specific metrics
- **Acceptance Criteria:**
  - Metric selection menu (checkboxes)
  - Presets available (all, key metrics, strategy params only)
  - Custom metric grouping saved as views
  - Filter by metric change threshold
  - 4+ unit tests
- **Estimated Points:** 4
- **Dependencies:** S-COMPARE-003

#### S-COMPARE-005: Build Export Functionality
- **Description:** Implement export of comparison results to CSV and JSON formats
- **Acceptance Criteria:**
  - CSV export includes headers and all comparison data
  - JSON export maintains structure
  - Both formats include metadata (run IDs, comparison date)
  - Large exports handled efficiently (streaming)
  - 3+ unit tests
- **Estimated Points:** 3
- **Dependencies:** S-COMPARE-003

### Deliverables
- Comparison algorithm (lib/compare/compare-algorithm.ts)
- Run selection UI (ui/compare/run-selector.tsx)
- Delta visualization component (ui/compare/delta-view.tsx)
- Metric selector component (ui/compare/metric-selector.tsx)
- Export service (lib/compare/export-service.ts)

---

## EPIC 5: E-AUDIT-TRAIL

**Epic ID:** E-AUDIT-TRAIL
**Source Blocker:** BLOCKER-5
**Priority:** HIGH
**Complexity:** MEDIUM

### Description
Reproducibility audit trail and verification. Captures complete provenance of strategy runs and provides tools to reproduce or verify historical executions.

### Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Audit trail captures 100% of critical events
- Verification algorithm achieves >95% reproducibility confidence
- UI displays full provenance chain
- Reproduce Run button successfully reexecutes strategies
- Minimum 25 unit tests covering audit and verification logic

### Stories

#### S-AUDIT-001: Implement Audit Trail Collection
- **Description:** Build comprehensive audit trail capturing all events relevant to strategy reproducibility
- **Acceptance Criteria:**
  - Events captured: creation, edits, approvals, rejections, execution, completion
  - Actor and timestamp recorded for each event
  - Event details stored (old value, new value for changes)
  - Immutable audit log (no deletion/modification)
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** E-JOURNAL-SCHEMA

#### S-AUDIT-002: Build Verification Algorithm
- **Description:** Implement algorithm to verify a historical run can be reproduced with captured data
- **Acceptance Criteria:**
  - Algorithm checks: code version, parameters, data inputs, environment
  - Verification confidence score generated (0-100%)
  - Reasons for any verification failures documented
  - Supports deterministic and stochastic strategies
  - 7+ unit tests
- **Estimated Points:** 7
- **Dependencies:** S-AUDIT-001

#### S-AUDIT-003: Create Audit UI
- **Description:** Build UI displaying full audit trail with timeline and event details
- **Acceptance Criteria:**
  - Timeline view shows all events chronologically
  - Event details expand on click
  - Filter by event type, actor, date range
  - Search capability for specific changes
  - 6+ unit tests
- **Estimated Points:** 6
- **Dependencies:** S-AUDIT-002

#### S-AUDIT-004: Add "Reproduce Run" Button
- **Description:** Implement button to trigger re-execution of a historical strategy run
- **Acceptance Criteria:**
  - Button available on run details page
  - Pre-verification checks executed
  - Parameters and environment matched to original run
  - New run created with reference to original
  - Comparison auto-generated after completion
  - 4+ unit tests
- **Estimated Points:** 4
- **Dependencies:** S-AUDIT-002, S-AUDIT-003

#### S-AUDIT-005: Build Diagnostic Tool
- **Description:** Create diagnostic tool to help troubleshoot reproducibility issues
- **Acceptance Criteria:**
  - Tool compares original vs. reproduction run
  - Identifies specific differences causing divergence
  - Suggests possible causes (version, env, data)
  - Provides remediation recommendations
  - 2+ unit tests
- **Estimated Points:** 2
- **Dependencies:** S-AUDIT-004

### Deliverables
- Audit trail collection service (lib/audit/audit-collector.ts)
- Verification algorithm (lib/audit/verification-algorithm.ts)
- Audit UI components (ui/audit/audit-trail.tsx)
- Reproduce Run handler (lib/audit/reproduce-handler.ts)
- Diagnostic tool (lib/audit/diagnostic-tool.ts)

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Epics | 5 |
| Total Stories | 25 |
| Total Story Points | 122 |
| CRITICAL Priority | 2 |
| HIGH Priority | 3 |
| Estimated Duration | 12-16 weeks |

### Story Point Distribution
- E-STRATEGY-LIFECYCLE: 34 points
- E-JOURNAL-SCHEMA: 40 points
- E-TELEMETRY-METRICS: 30 points
- E-COMPARE-WORKFLOW: 25 points
- E-AUDIT-TRAIL: 25 points

### Timeline (Recommended Sequencing)
1. **Weeks 1-3:** E-STRATEGY-LIFECYCLE (foundation for all others)
2. **Weeks 2-5:** E-JOURNAL-SCHEMA (parallel with Epic 1)
3. **Weeks 6-8:** E-TELEMETRY-METRICS (depends on Epics 1-2)
4. **Weeks 9-11:** E-COMPARE-WORKFLOW (depends on Epic 2)
5. **Weeks 11-13:** E-AUDIT-TRAIL (depends on Epics 1-2)

---

**Document Created:** 2026-02-26
**Last Updated:** 2026-02-26
**Status:** READY FOR SPRINT PLANNING
