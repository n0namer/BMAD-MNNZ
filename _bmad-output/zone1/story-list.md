# Story List - Katana Vectorbt Optimizer Phase 1

**Project:** Katana Vectorbt Optimizer
**Generated:** 2026-02-26
**Total Stories:** 25
**Total Story Points:** 154 (see note in sprint-plan-phase1.md regarding discrepancy with epics file)

---

## Story Index

| Story ID | Title | Epic | Points | Sprint | Priority | Dependencies |
|----------|-------|------|--------|--------|----------|--------------|
| S-STRATEGY-001 | Implement State Machine Transitions | E-STRATEGY-LIFECYCLE | 13 | 1 | CRITICAL | None |
| S-STRATEGY-002 | Build Approval Workflow | E-STRATEGY-LIFECYCLE | 8 | 2 | CRITICAL | S-STRATEGY-001 |
| S-STRATEGY-003 | Add Kill-Switch Mechanism | E-STRATEGY-LIFECYCLE | 5 | 2 | CRITICAL | S-STRATEGY-001 |
| S-STRATEGY-004 | Create State Timeline | E-STRATEGY-LIFECYCLE | 5 | 3 | CRITICAL | S-STRATEGY-001 |
| S-STRATEGY-005 | Build Rejection/Resubmit Logic | E-STRATEGY-LIFECYCLE | 3 | 3 | CRITICAL | S-STRATEGY-002 |
| S-JOURNAL-001 | Create manifest.json Structure | E-JOURNAL-SCHEMA | 8 | 1 | CRITICAL | None |
| S-JOURNAL-002 | Create summary.json v3.0 | E-JOURNAL-SCHEMA | 10 | 2 | CRITICAL | S-JOURNAL-001 |
| S-JOURNAL-003 | Implement events.ndjson | E-JOURNAL-SCHEMA | 8 | 3 | CRITICAL | S-JOURNAL-001 |
| S-JOURNAL-004 | Build Database Schema (Postgres) | E-JOURNAL-SCHEMA | 8 | 3 | CRITICAL | S-JOURNAL-002, S-JOURNAL-003 |
| S-JOURNAL-005 | Create Reproducibility Verifier | E-JOURNAL-SCHEMA | 6 | 4 | CRITICAL | S-JOURNAL-001, S-JOURNAL-004 |
| S-TELEMETRY-001 | Instrument Time-to-Status | E-TELEMETRY-METRICS | 6 | 4 | HIGH | E-STRATEGY-LIFECYCLE |
| S-TELEMETRY-002 | Implement MTIF Calculation | E-TELEMETRY-METRICS | 6 | 4 | HIGH | E-STRATEGY-LIFECYCLE |
| S-TELEMETRY-003 | Implement Log Diving Rate | E-TELEMETRY-METRICS | 6 | 5 | HIGH | S-TELEMETRY-001 |
| S-TELEMETRY-004 | Build Metrics Dashboard | E-TELEMETRY-METRICS | 8 | 6 | HIGH | S-TELEMETRY-001, S-TELEMETRY-002, S-TELEMETRY-003 |
| S-TELEMETRY-005 | Create Alert Rules | E-TELEMETRY-METRICS | 4 | 6 | HIGH | S-TELEMETRY-004 |
| S-COMPARE-001 | Implement Comparison Algorithm | E-COMPARE-WORKFLOW | 7 | 5 | HIGH | E-JOURNAL-SCHEMA |
| S-COMPARE-002 | Build Run Selection UI | E-COMPARE-WORKFLOW | 5 | 6 | HIGH | S-COMPARE-001 |
| S-COMPARE-003 | Create Delta Visualization | E-COMPARE-WORKFLOW | 6 | 7 | HIGH | S-COMPARE-002 |
| S-COMPARE-004 | Add Metric Selection | E-COMPARE-WORKFLOW | 4 | 7 | HIGH | S-COMPARE-003 |
| S-COMPARE-005 | Build Export Functionality | E-COMPARE-WORKFLOW | 3 | 7 | HIGH | S-COMPARE-003 |
| S-AUDIT-001 | Implement Audit Trail Collection | E-AUDIT-TRAIL | 6 | 5 | HIGH | E-JOURNAL-SCHEMA |
| S-AUDIT-002 | Build Verification Algorithm | E-AUDIT-TRAIL | 7 | 6 | HIGH | S-AUDIT-001 |
| S-AUDIT-003 | Create Audit UI | E-AUDIT-TRAIL | 6 | 7 | HIGH | S-AUDIT-002 |
| S-AUDIT-004 | Add "Reproduce Run" Button | E-AUDIT-TRAIL | 4 | 7 | HIGH | S-AUDIT-002, S-AUDIT-003 |
| S-AUDIT-005 | Build Diagnostic Tool | E-AUDIT-TRAIL | 2 | 7 | HIGH | S-AUDIT-004 |

---

## Stories by Epic

### Epic 1: E-STRATEGY-LIFECYCLE (34 points)

#### S-STRATEGY-001: Implement State Machine Transitions
- **Sprint:** 1
- **Points:** 13
- **Priority:** CRITICAL
- **Dependencies:** None
- **Status:** backlog
- **Acceptance Criteria:**
  - State transitions defined: DRAFT → PENDING → APPROVED → ACTIVE → COMPLETED/CANCELLED
  - Invalid transitions rejected
  - Audit trail tracks all transitions
  - 10+ unit tests
- **Deliverable:** `lib/state-machine.ts`
- **File Key (for status tracking):** `strategy-001-implement-state-machine-transitions`

#### S-STRATEGY-002: Build Approval Workflow
- **Sprint:** 2
- **Points:** 8
- **Priority:** CRITICAL
- **Dependencies:** S-STRATEGY-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Reviewers can be assigned to pending strategies
  - Approval and rejection decisions recorded
  - Comments captured with approval decisions
  - Notification system alerts reviewers
  - 8+ unit tests
- **Deliverable:** `lib/approval-service.ts`
- **File Key:** `strategy-002-build-approval-workflow`

#### S-STRATEGY-003: Add Kill-Switch Mechanism
- **Sprint:** 2
- **Points:** 5
- **Priority:** CRITICAL
- **Dependencies:** S-STRATEGY-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Kill-switch callable from ACTIVE state
  - Graceful shutdown of running strategy
  - Final state recorded as KILLED
  - Cleanup operations executed
  - 5+ unit tests
- **Deliverable:** `lib/kill-switch.ts`
- **File Key:** `strategy-003-add-kill-switch-mechanism`

#### S-STRATEGY-004: Create State Timeline
- **Sprint:** 3
- **Points:** 5
- **Priority:** CRITICAL
- **Dependencies:** S-STRATEGY-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Timeline displays all transitions chronologically
  - Actors and timestamps shown for each transition
  - Zoom and filter capabilities
  - Export timeline as JSON/CSV
  - 4+ unit tests
- **Deliverable:** `ui/timeline.tsx`
- **File Key:** `strategy-004-create-state-timeline`

#### S-STRATEGY-005: Build Rejection/Resubmit Logic
- **Sprint:** 3
- **Points:** 3
- **Priority:** CRITICAL
- **Dependencies:** S-STRATEGY-002
- **Status:** backlog
- **Acceptance Criteria:**
  - Rejected strategy can be edited
  - Resubmit creates new approval request
  - Previous rejection reason visible to submitter
  - Audit trail shows resubmission chain
  - 3+ unit tests
- **Deliverable:** `lib/resubmit.ts`
- **File Key:** `strategy-005-build-rejection-resubmit-logic`

---

### Epic 2: E-JOURNAL-SCHEMA (40 points)

#### S-JOURNAL-001: Create manifest.json Structure
- **Sprint:** 1
- **Points:** 8
- **Priority:** CRITICAL
- **Dependencies:** None
- **Status:** backlog
- **Acceptance Criteria:**
  - Schema includes: strategy_id, version, start_time, end_time, parameters, environment
  - JSON Schema (.json) created and validated
  - TypeScript types generated
  - Sample manifests created
  - 8+ unit tests
- **Deliverable:** `schemas/manifest-v1.json`
- **File Key:** `journal-001-create-manifest-json-structure`

#### S-JOURNAL-002: Create summary.json v3.0
- **Sprint:** 2
- **Points:** 10
- **Priority:** CRITICAL
- **Dependencies:** S-JOURNAL-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Schema includes: total_runs, win_rate, sharpe_ratio, max_drawdown, final_equity
  - Aggregation logic implemented
  - Summary auto-calculated from detailed results
  - Backward compatible with v2.0 format
  - 10+ unit tests
- **Deliverable:** `schemas/summary-v3.json`
- **File Key:** `journal-002-create-summary-json-v30`

#### S-JOURNAL-003: Implement events.ndjson
- **Sprint:** 3
- **Points:** 8
- **Priority:** CRITICAL
- **Dependencies:** S-JOURNAL-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Event schema defined (type, timestamp, data)
  - Streaming write capability implemented
  - Event filtering/query supported
  - Compression tested (.ndjson.gz)
  - 8+ unit tests
- **Deliverable:** `schemas/events.ndjson.md`
- **File Key:** `journal-003-implement-events-ndjson`

#### S-JOURNAL-004: Build Database Schema (Postgres)
- **Sprint:** 3
- **Points:** 8
- **Priority:** CRITICAL
- **Dependencies:** S-JOURNAL-002, S-JOURNAL-003
- **Status:** backlog
- **Acceptance Criteria:**
  - Tables: runs, strategies, events, metrics, audit_trail
  - Indexes created for performance queries
  - Constraints enforced (FK, unique)
  - Migration scripts (up/down) created
  - 8+ unit tests
- **Deliverable:** `db/migrations/`
- **File Key:** `journal-004-build-database-schema-postgres`

#### S-JOURNAL-005: Create Reproducibility Verifier
- **Sprint:** 4
- **Points:** 6
- **Priority:** CRITICAL
- **Dependencies:** S-JOURNAL-001, S-JOURNAL-004
- **Status:** backlog
- **Acceptance Criteria:**
  - Verifier reads journal data and reruns strategy
  - Tolerance thresholds configurable (±0.01%)
  - Detailed diff report on mismatches
  - Supports deterministic verification
  - 6+ unit tests
- **Deliverable:** `lib/reproducibility-verifier.ts`
- **File Key:** `journal-005-create-reproducibility-verifier`

---

### Epic 3: E-TELEMETRY-METRICS (30 points)

#### S-TELEMETRY-001: Instrument Time-to-Status
- **Sprint:** 4
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** E-STRATEGY-LIFECYCLE (complete)
- **Status:** backlog
- **Acceptance Criteria:**
  - Tracking captures all state transition times
  - Percentile aggregations (p50, p95, p99) calculated
  - Historical trending stored
  - Real-time metric emission
  - 6+ unit tests
- **Deliverable:** `lib/metrics/time-to-status.ts`
- **File Key:** `telemetry-001-instrument-time-to-status`

#### S-TELEMETRY-002: Implement MTIF Calculation
- **Sprint:** 4
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** E-STRATEGY-LIFECYCLE (complete)
- **Status:** backlog
- **Acceptance Criteria:**
  - MTIF calculated per strategy
  - Aggregation across time windows (daily, weekly, monthly)
  - Outlier detection applied
  - Trend analysis capability
  - 6+ unit tests
- **Deliverable:** `lib/metrics/mtif.ts`
- **File Key:** `telemetry-002-implement-mtif-calculation`

#### S-TELEMETRY-003: Implement Log Diving Rate
- **Sprint:** 5
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** S-TELEMETRY-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Error log volume tracked
  - Rate calculated per time window
  - Error classification supported
  - Severity weighting applied
  - 6+ unit tests
- **Deliverable:** `lib/metrics/log-diving-rate.ts`
- **File Key:** `telemetry-003-implement-log-diving-rate`

#### S-TELEMETRY-004: Build Metrics Dashboard
- **Sprint:** 6
- **Points:** 8
- **Priority:** HIGH
- **Dependencies:** S-TELEMETRY-001, S-TELEMETRY-002, S-TELEMETRY-003
- **Status:** backlog
- **Acceptance Criteria:**
  - Dashboard displays all 3 metrics with sparklines
  - Time range selection (1d, 7d, 30d, custom)
  - Comparison view (current vs. baseline)
  - Drill-down to individual runs
  - 8+ unit tests
- **Deliverable:** `ui/dashboard/metrics-dashboard.tsx`
- **File Key:** `telemetry-004-build-metrics-dashboard`

#### S-TELEMETRY-005: Create Alert Rules
- **Sprint:** 6
- **Points:** 4
- **Priority:** HIGH
- **Dependencies:** S-TELEMETRY-004
- **Status:** backlog
- **Acceptance Criteria:**
  - Rules engine evaluates metrics against thresholds
  - Multiple alert channels supported (Slack, email, PagerDuty)
  - Alert deduplication prevents spam
  - Alert history and muting capability
  - 4+ unit tests
- **Deliverable:** `lib/alerts/alert-engine.ts`
- **File Key:** `telemetry-005-create-alert-rules`

---

### Epic 4: E-COMPARE-WORKFLOW (25 points)

#### S-COMPARE-001: Implement Comparison Algorithm
- **Sprint:** 5
- **Points:** 7
- **Priority:** HIGH
- **Dependencies:** E-JOURNAL-SCHEMA (complete)
- **Status:** backlog
- **Acceptance Criteria:**
  - Algorithm identifies differences in parameters, metrics, outcomes
  - Similarity scoring implemented (0-100%)
  - Null/missing values handled correctly
  - Performance: <500ms for typical runs
  - 7+ unit tests
- **Deliverable:** `lib/compare/compare-algorithm.ts`
- **File Key:** `compare-001-implement-comparison-algorithm`

#### S-COMPARE-002: Build Run Selection UI
- **Sprint:** 6
- **Points:** 5
- **Priority:** HIGH
- **Dependencies:** S-COMPARE-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Run list displays key metadata (date, status, key metrics)
  - Search/filter by date range, strategy, status
  - Recently compared runs available as quick access
  - Date range picker for bulk selection
  - 5+ unit tests
- **Deliverable:** `ui/compare/run-selector.tsx`
- **File Key:** `compare-002-build-run-selection-ui`

#### S-COMPARE-003: Create Delta Visualization
- **Sprint:** 7
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** S-COMPARE-002
- **Status:** backlog
- **Acceptance Criteria:**
  - Side-by-side comparison view
  - Differences highlighted in color (added: green, removed: red, changed: yellow)
  - Sortable columns (field name, old value, new value, change type)
  - Drill-down into nested fields
  - 6+ unit tests
- **Deliverable:** `ui/compare/delta-view.tsx`
- **File Key:** `compare-003-create-delta-visualization`

#### S-COMPARE-004: Add Metric Selection
- **Sprint:** 7
- **Points:** 4
- **Priority:** HIGH
- **Dependencies:** S-COMPARE-003
- **Status:** backlog
- **Acceptance Criteria:**
  - Metric selection menu (checkboxes)
  - Presets available (all, key metrics, strategy params only)
  - Custom metric grouping saved as views
  - Filter by metric change threshold
  - 4+ unit tests
- **Deliverable:** `ui/compare/metric-selector.tsx`
- **File Key:** `compare-004-add-metric-selection`

#### S-COMPARE-005: Build Export Functionality
- **Sprint:** 7
- **Points:** 3
- **Priority:** HIGH
- **Dependencies:** S-COMPARE-003
- **Status:** backlog
- **Acceptance Criteria:**
  - CSV export includes headers and all comparison data
  - JSON export maintains structure
  - Both formats include metadata (run IDs, comparison date)
  - Large exports handled efficiently (streaming)
  - 3+ unit tests
- **Deliverable:** `lib/compare/export-service.ts`
- **File Key:** `compare-005-build-export-functionality`

---

### Epic 5: E-AUDIT-TRAIL (25 points)

#### S-AUDIT-001: Implement Audit Trail Collection
- **Sprint:** 5
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** E-JOURNAL-SCHEMA (complete)
- **Status:** backlog
- **Acceptance Criteria:**
  - Events captured: creation, edits, approvals, rejections, execution, completion
  - Actor and timestamp recorded for each event
  - Event details stored (old value, new value for changes)
  - Immutable audit log (no deletion/modification)
  - 6+ unit tests
- **Deliverable:** `lib/audit/audit-collector.ts`
- **File Key:** `audit-001-implement-audit-trail-collection`

#### S-AUDIT-002: Build Verification Algorithm
- **Sprint:** 6
- **Points:** 7
- **Priority:** HIGH
- **Dependencies:** S-AUDIT-001
- **Status:** backlog
- **Acceptance Criteria:**
  - Algorithm checks: code version, parameters, data inputs, environment
  - Verification confidence score generated (0-100%)
  - Reasons for any verification failures documented
  - Supports deterministic and stochastic strategies
  - 7+ unit tests
- **Deliverable:** `lib/audit/verification-algorithm.ts`
- **File Key:** `audit-002-build-verification-algorithm`

#### S-AUDIT-003: Create Audit UI
- **Sprint:** 7
- **Points:** 6
- **Priority:** HIGH
- **Dependencies:** S-AUDIT-002
- **Status:** backlog
- **Acceptance Criteria:**
  - Timeline view shows all events chronologically
  - Event details expand on click
  - Filter by event type, actor, date range
  - Search capability for specific changes
  - 6+ unit tests
- **Deliverable:** `ui/audit/audit-trail.tsx`
- **File Key:** `audit-003-create-audit-ui`

#### S-AUDIT-004: Add "Reproduce Run" Button
- **Sprint:** 7
- **Points:** 4
- **Priority:** HIGH
- **Dependencies:** S-AUDIT-002, S-AUDIT-003
- **Status:** backlog
- **Acceptance Criteria:**
  - Button available on run details page
  - Pre-verification checks executed
  - Parameters and environment matched to original run
  - New run created with reference to original
  - Comparison auto-generated after completion
  - 4+ unit tests
- **Deliverable:** `lib/audit/reproduce-handler.ts`
- **File Key:** `audit-004-add-reproduce-run-button`

#### S-AUDIT-005: Build Diagnostic Tool
- **Sprint:** 7
- **Points:** 2
- **Priority:** HIGH
- **Dependencies:** S-AUDIT-004
- **Status:** backlog
- **Acceptance Criteria:**
  - Tool compares original vs. reproduction run
  - Identifies specific differences causing divergence
  - Suggests possible causes (version, env, data)
  - Provides remediation recommendations
  - 2+ unit tests
- **Deliverable:** `lib/audit/diagnostic-tool.ts`
- **File Key:** `audit-005-build-diagnostic-tool`

---

## Minimum Test Requirements

| Epic | Required Tests |
|------|---------------|
| E-STRATEGY-LIFECYCLE | 30 tests minimum |
| E-JOURNAL-SCHEMA | 40 tests minimum |
| E-TELEMETRY-METRICS | 30 tests minimum |
| E-COMPARE-WORKFLOW | 25 tests minimum |
| E-AUDIT-TRAIL | 25 tests minimum |
| **TOTAL** | **150 tests minimum** |

---

*Document generated by BMAD Sprint Planning Workflow*
*Date: 2026-02-26*
