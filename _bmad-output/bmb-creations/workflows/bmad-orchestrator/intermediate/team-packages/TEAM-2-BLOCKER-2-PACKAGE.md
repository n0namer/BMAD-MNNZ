# TEAM 2: BLOCKER-2 PACKAGE - Journal Schema & Data Persistence

**Project:** Katana Vectorbt Optimizer - Phase 2 Implementation
**Team:** Backend Team 2 (Data & Schema)
**Blocker:** BLOCKER-2
**Package Created:** 2026-02-26
**Duration:** 8 weeks (Weeks 2-9, parallel with TEAM 1)
**Dependencies:** Requires TEAM 1 state machine definitions

---

## EXECUTIVE SUMMARY

Team 2 implements the foundational data persistence layer that captures complete reproducibility information for every strategy run. This includes manifest.json, summary.json, events.ndjson, and Postgres schema. All run data flows through this schema, making it critical for reproducibility verification (TEAM 5) and comparison workflows (TEAM 4).

### Key Deliverables
- manifest.json schema with TypeScript types
- summary.json v3.0 with aggregation logic
- events.ndjson streaming event format
- Postgres database schema (5 tables + indexes)
- Reproducibility verification tool
- 40+ unit tests

### Business Impact
- Enables complete historical reproducibility
- Provides structured data for analytics and comparison
- Creates audit trail for compliance
- Foundation for metrics collection (TEAM 3)

---

## EPIC ASSIGNMENT

**Epic ID:** E-JOURNAL-SCHEMA
**Priority:** CRITICAL
**Complexity:** VERY HIGH
**Total Story Points:** 40
**Minimum Tests:** 40 unit tests

### Epic Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Schema validated against 10+ sample runs
- Database migration scripts tested on fresh and existing databases
- Minimum 40 unit tests covering all schema components
- Schema documentation published

---

## STORY BREAKDOWN

### Story 1: S-JOURNAL-001 - Create manifest.json Structure
**Points:** 8 | **Dependencies:** None | **Tests Required:** 8+

#### Description
Define manifest.json schema containing metadata about a strategy run. The manifest is the top-level document that references all other run data (summary, events, metrics).

#### Acceptance Criteria
1. Schema includes required fields: strategy_id, version, start_time, end_time, parameters, environment
2. JSON Schema (.json) created and validated against real data
3. TypeScript types generated from schema
4. Sample manifests created for testing (3+ examples)
5. Backward compatibility considered for future versions
6. 8+ unit tests for manifest parsing and validation

#### Implementation Checklist
- [ ] Design manifest.json schema (fields, types, constraints)
- [ ] Create JSON Schema file (manifest-v1.json)
- [ ] Generate TypeScript types from schema
- [ ] Add validation logic with clear error messages
- [ ] Create 3+ sample manifest files
- [ ] Write 8+ unit tests for manifest validation
- [ ] Document manifest format and examples
- [ ] Add versioning support for future schema changes

#### Schema Structure Example
```json
{
  "strategy_id": "uuid",
  "version": "1.0.0",
  "run_id": "uuid",
  "start_time": "ISO 8601",
  "end_time": "ISO 8601",
  "duration_ms": "number",
  "parameters": {
    "entry_threshold": "number",
    "exit_threshold": "number",
    "lookback_period": "number"
  },
  "environment": {
    "python_version": "string",
    "vectorbt_version": "string",
    "data_source": "string"
  },
  "status": "SUCCESS|FAILED|KILLED",
  "summary_ref": "reference to summary.json",
  "events_ref": "reference to events.ndjson"
}
```

#### Test Scenarios Covered
- SV-001: Manifest structure validation (required fields)
- Valid manifest parsing
- Invalid manifest rejection
- Schema evolution (v1.0 → v2.0 compatibility)

#### Files to Create/Modify
- `schemas/manifest-v1.json` - JSON Schema
- `lib/manifest.ts` - Manifest types and validation
- `lib/manifest.spec.ts` - Unit tests (8+ tests)

---

### Story 2: S-JOURNAL-002 - Create summary.json v3.0
**Points:** 10 | **Dependencies:** S-JOURNAL-001 | **Tests Required:** 10+

#### Description
Build summary.json schema for high-level run results and metrics. Summary provides quick overview of run performance (win rate, Sharpe ratio, drawdown, etc.) calculated from detailed events.

#### Acceptance Criteria
1. Schema includes: total_runs, win_rate, sharpe_ratio, max_drawdown, final_equity
2. Aggregation logic implemented (calculates summary from events)
3. Summary auto-calculated from detailed results
4. Backward compatible with v2.0 format (migration logic)
5. 10+ unit tests for aggregation and calculations

#### Implementation Checklist
- [ ] Design summary.json schema
- [ ] Implement aggregation engine
- [ ] Add calculation functions (win_rate, Sharpe, max_drawdown)
- [ ] Create backward compatibility layer for v2.0
- [ ] Write aggregation functions for 5+ metrics
- [ ] Write 10+ unit tests for calculations
- [ ] Add migration script (v2.0 → v3.0)
- [ ] Document calculation methodologies

#### Schema Structure Example
```json
{
  "run_id": "uuid",
  "strategy_id": "uuid",
  "total_runs": "number",
  "win_rate": "percentage",
  "sharpe_ratio": "number",
  "max_drawdown": "percentage",
  "final_equity": "number",
  "total_trades": "number",
  "avg_trade_duration": "number",
  "calculated_at": "ISO 8601",
  "version": "3.0"
}
```

#### Test Scenarios Covered
- SV-002: Summary document validation
- SV-013: Metrics object validation
- Correct win rate calculation
- Sharpe ratio calculation
- Max drawdown calculation
- v2.0 → v3.0 migration
- Backward compatibility

#### Files to Create/Modify
- `schemas/summary-v3.json` - JSON Schema
- `lib/summary.ts` - Summary types and aggregation
- `lib/summary.spec.ts` - Unit tests (10+ tests)
- `lib/aggregation-engine.ts` - Metric calculations
- `lib/migration/v2-to-v3.ts` - Migration logic

---

### Story 3: S-JOURNAL-003 - Implement events.ndjson
**Points:** 8 | **Dependencies:** S-JOURNAL-001 | **Tests Required:** 8+

#### Description
Create NDJSON event log format for detailed strategy events (trades, signals, errors). Events are stored as newline-delimited JSON for efficient streaming and querying.

#### Acceptance Criteria
1. Event schema defined (type, timestamp, data, status)
2. Streaming write capability implemented (append-only)
3. Event filtering/query supported (by type, date range)
4. Compression tested (.ndjson.gz)
5. Performance: streaming write <1ms per event
6. 8+ unit tests for event handling

#### Implementation Checklist
- [ ] Design event schema (type enum, required fields)
- [ ] Implement streaming writer
- [ ] Add event validation
- [ ] Implement event filtering/query
- [ ] Add compression support (gzip)
- [ ] Implement streaming decompression
- [ ] Write 8+ unit tests
- [ ] Add performance benchmarks

#### Event Schema Example
```
{"type":"TRADE_OPENED","timestamp":"2026-02-26T10:00:00Z","data":{"symbol":"BTC","qty":1.0,"price":45000},"status":"SUCCESS"}
{"type":"SIGNAL_GENERATED","timestamp":"2026-02-26T10:00:01Z","data":{"signal":"BUY","confidence":0.95},"status":"SUCCESS"}
{"type":"ERROR_CAUGHT","timestamp":"2026-02-26T10:00:02Z","data":{"error":"DataFetchError","message":"API timeout"},"status":"FAILED"}
```

#### Test Scenarios Covered
- SV-003: Entry structure validation (events array)
- SV-004: Event array validation (type, timestamp ordering)
- Streaming write performance
- Event filtering by type
- Event filtering by date range
- Compression/decompression
- Query on large event sets (1M+ events)

#### Files to Create/Modify
- `schemas/events.ndjson.md` - Event format specification
- `lib/events.ts` - Event types and streaming
- `lib/events.spec.ts` - Unit tests (8+ tests)
- `lib/event-writer.ts` - Streaming write logic
- `lib/event-query.ts` - Event filtering/query

---

### Story 4: S-JOURNAL-004 - Build Database Schema (Postgres)
**Points:** 8 | **Dependencies:** S-JOURNAL-002, S-JOURNAL-003 | **Tests Required:** 8+

#### Description
Create Postgres schema for persisting journal data with relational structure. Schema includes 5 tables: runs, strategies, events, metrics, audit_trail.

#### Acceptance Criteria
1. Tables created: runs, strategies, events, metrics, audit_trail
2. Indexes created for performance queries (composite indexes for common filters)
3. Foreign key constraints enforced
4. Unique constraints enforced
5. Migration scripts (up/down) created and tested
6. 8+ unit tests for database operations

#### Implementation Checklist
- [ ] Design relational schema (5 tables)
- [ ] Create migration UP script (create tables, indexes, constraints)
- [ ] Create migration DOWN script (rollback)
- [ ] Test migration on fresh database
- [ ] Test migration on existing database (backward compatibility)
- [ ] Add 10+ indexes for performance queries
- [ ] Write 8+ unit tests for database operations
- [ ] Add database connection pooling configuration

#### Table Structure
```sql
-- runs table (parent of events)
CREATE TABLE runs (
  id UUID PRIMARY KEY,
  strategy_id UUID NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP,
  status VARCHAR(20),
  created_at TIMESTAMP DEFAULT NOW()
);

-- strategies table
CREATE TABLE strategies (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  version VARCHAR(10),
  parameters JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- events table (large, streaming writes)
CREATE TABLE events (
  id BIGSERIAL PRIMARY KEY,
  run_id UUID NOT NULL REFERENCES runs(id),
  type VARCHAR(50),
  timestamp TIMESTAMP,
  data JSONB,
  status VARCHAR(20)
);

-- metrics table (aggregated results)
CREATE TABLE metrics (
  id UUID PRIMARY KEY,
  run_id UUID NOT NULL REFERENCES runs(id),
  name VARCHAR(100),
  value NUMERIC,
  unit VARCHAR(50),
  calculated_at TIMESTAMP
);

-- audit_trail table (immutable log)
CREATE TABLE audit_trail (
  id BIGSERIAL PRIMARY KEY,
  entity_type VARCHAR(50),
  entity_id UUID,
  action VARCHAR(50),
  actor VARCHAR(100),
  timestamp TIMESTAMP DEFAULT NOW()
);
```

#### Test Scenarios Covered
- SV-010: Relationship validation (foreign keys)
- DB-001: Insert valid journal entry
- DB-002: Duplicate ID detection
- DB-003: Update entry successfully
- DB-004: Concurrent updates with versioning
- DB-005: Delete with cascade
- DB-006: Query by state filter
- DB-007: Index performance verification

#### Files to Create/Modify
- `db/migrations/001-create-schema.up.sql` - Create tables and indexes
- `db/migrations/001-create-schema.down.sql` - Rollback
- `lib/db/schema.ts` - Database type definitions
- `lib/db/schema.spec.ts` - Unit tests (8+ tests)
- `lib/db/pool.ts` - Connection pool configuration

---

### Story 5: S-JOURNAL-005 - Create Reproducibility Verifier
**Points:** 6 | **Dependencies:** S-JOURNAL-001, S-JOURNAL-004 | **Tests Required:** 6+

#### Description
Implement verification tool to confirm a run can be reproduced with captured parameters. Verifier reads journal data and reruns strategy with captured parameters, comparing results.

#### Acceptance Criteria
1. Verifier reads journal data and reruns strategy
2. Tolerance thresholds configurable (±0.01% for deterministic, ±1% for stochastic)
3. Detailed diff report on mismatches (parameter diffs, metric diffs)
4. Supports both deterministic and stochastic strategy verification
5. 6+ unit tests for verification logic

#### Implementation Checklist
- [ ] Design reproducibility verification algorithm
- [ ] Implement parameter capture and reapplication
- [ ] Add tolerance threshold configuration
- [ ] Implement diff algorithm (parameter, metric diffs)
- [ ] Create verification report generation
- [ ] Add support for stochastic strategies (seed-based)
- [ ] Write 6+ unit tests for verification
- [ ] Add verification performance benchmarks

#### Verification Algorithm
```
1. Load original run from journal (parameters, environment, data source)
2. Re-execute strategy with captured parameters
3. Compare results:
   - Parameter set matches
   - Metrics within tolerance threshold
   - Event sequence matches (for deterministic)
   - Metric distribution matches (for stochastic)
4. Generate detailed diff report if mismatches found
5. Return verification confidence score (0-100%)
```

#### Test Scenarios Covered
- Successful reproducibility verification
- Parameter mismatch detection
- Metric mismatch detection
- Tolerance threshold enforcement
- Deterministic strategy verification
- Stochastic strategy verification (with seed)
- Diff report generation

#### Files to Create/Modify
- `lib/reproducibility-verifier.ts` - Verification logic
- `lib/reproducibility-verifier.spec.ts` - Unit tests (6+ tests)
- `lib/diff-engine.ts` - Parameter and metric diff calculation

---

## TESTING REQUIREMENTS

### Unit Tests (40+ total required)

**Schema Validation (15 tests):** SV-001 through SV-015
- Manifest, entry, metadata validation
- Event array, nested object, field length validation
- Data type, enum, relationship validation
- Schema evolution, summary, metrics validation
- Unicode and error reporting

**Database Operations (15 tests):** DB-001 through DB-015
- CRUD operations
- Duplicate detection, optimistic locking
- Cascading delete, filtering, aggregation
- Indexing, relationships, performance
- Large dataset handling

**Schema-Specific (10+ tests):**
- Manifest parsing and validation (8 tests)
- Summary aggregation (10 tests)
- Event streaming and filtering (8 tests)
- Database migration testing (8 tests)
- Reproducibility verification (6 tests)

### Test Coverage Requirements
- Minimum 80% code coverage
- All validation paths tested
- Edge cases (empty, null, oversized values)
- Performance tests (insert/query latency)
- Large dataset handling (1M+ events)

---

## DELIVERABLES CHECKLIST

### Schema Deliverables
- [ ] `schemas/manifest-v1.json` - Manifest JSON Schema
- [ ] `schemas/summary-v3.json` - Summary JSON Schema
- [ ] `schemas/events.ndjson.md` - Events format specification
- [ ] Schema documentation with examples

### Code Deliverables
- [ ] `lib/manifest.ts` - Manifest types and validation
- [ ] `lib/summary.ts` - Summary types and aggregation
- [ ] `lib/events.ts` - Event types and streaming
- [ ] `lib/aggregation-engine.ts` - Metric calculation
- [ ] `lib/reproducibility-verifier.ts` - Verification tool
- [ ] `lib/event-writer.ts` - Streaming write (estimated 150-200 lines)
- [ ] `lib/event-query.ts` - Event filtering (estimated 150-200 lines)

### Database Deliverables
- [ ] `db/migrations/001-create-schema.up.sql` - Create schema
- [ ] `db/migrations/001-create-schema.down.sql` - Rollback
- [ ] `lib/db/schema.ts` - TypeScript definitions
- [ ] `lib/db/pool.ts` - Connection pool configuration
- [ ] Migration testing scripts

### Test Deliverables
- [ ] 40+ unit tests (100% passing)
- [ ] Test coverage report (80%+ coverage)
- [ ] Migration test report (forward and backward)
- [ ] Performance benchmarks

### Documentation Deliverables
- [ ] Schema documentation with ERD
- [ ] Migration guide
- [ ] API documentation
- [ ] Reproducibility verification guide

---

## DEPENDENCIES & BLOCKING RELATIONSHIPS

### Blocks
- **Blocks TEAM 3** (E-TELEMETRY-METRICS): Requires metric schema and storage
- **Blocks TEAM 4** (E-COMPARE-WORKFLOW): Requires journal schema for comparison
- **Blocks TEAM 5** (E-AUDIT-TRAIL): Requires audit trail table and data

### Dependencies
- **Depends on:** TEAM 1 state definitions (for run states)
- **Depends on:** Database infrastructure (Postgres)
- **Depends on:** Data access layer (can provide as needed)

---

## TEAM COMPOSITION

**Team Lead:** Data Architect (1)
**Senior Backend Developers (Database):** 2
**Junior Backend Developers:** 1
**Database Administrator:** 0.5 (shared)
**QA Engineer:** 1

**Total: 4.5 FTE over 8 weeks**

---

## TIMELINE & MILESTONES

### Week 2: Manifest & Summary (S-JOURNAL-001, S-JOURNAL-002 start)
- Design manifest schema
- Implement manifest validation
- Design summary schema
- Implement aggregation engine
- Write 8+ manifest tests
- **Exit Criteria:** Manifest and summary schemas defined and validated

### Week 3-4: Events & Database (S-JOURNAL-003, S-JOURNAL-004)
- Implement events.ndjson streaming
- Create Postgres schema
- Write database migration scripts
- Write 8+ event tests, 8+ database tests
- **Exit Criteria:** Event streaming and database schema complete

### Week 5: Reproducibility Verifier (S-JOURNAL-005)
- Implement verification algorithm
- Add diff engine
- Create verification reports
- Write 6+ unit tests
- **Exit Criteria:** Reproducibility verifier functional

### Week 6-7: Integration & Testing
- Integration tests for all components
- Migration testing (fresh and existing databases)
- Performance optimization
- Schema documentation
- **Exit Criteria:** All components integrated, 80%+ coverage

### Week 8-9: Hardening & Handoff
- Performance tuning
- Load testing (event streaming at scale)
- Migration dry-runs
- Handoff to TEAM 3 and TEAM 4
- **Exit Criteria:** All acceptance criteria met, ready for other teams

---

## QUALITY GATES

### Definition of Done
1. All acceptance criteria met (all 5 stories)
2. 40+ unit tests passing (100% pass rate)
3. 80%+ code coverage
4. Schema validation on 10+ real datasets
5. Migration tested on fresh and existing databases
6. Zero critical bugs

### Code Quality Standards
- TypeScript strict mode
- Schema validation on all inputs
- Detailed error messages for validation failures
- SQL query optimization (explain plans reviewed)
- Connection pool configuration tuned

### Performance Requirements
- Manifest parsing: <100ms
- Summary aggregation for 1000-event run: <500ms
- Event streaming write: <1ms per event
- Event query (filter by type, date range): <1s for 1M events
- Database queries (indexed): <100ms

---

## RISK MITIGATION

### Risk 1: Schema Complexity
**Risk:** Complex schema with many relationships
**Mitigation:**
- Start with core tables, add complexity incrementally
- Entity-Relationship Diagram (ERD) reviewed early
- Database review by senior DBA
- Test migrations thoroughly before production

### Risk 2: Performance at Scale
**Risk:** Event streaming with millions of events
**Mitigation:**
- Performance tests with 1M+ events early
- Index strategy reviewed and optimized
- Compression tested for storage efficiency
- Batch operations for bulk inserts

### Risk 3: Migration Challenges
**Risk:** Data migration from existing systems
**Mitigation:**
- Backward compatibility tested
- Migration dry-runs on production-like data
- Rollback procedures tested and documented
- Zero-downtime migration approach considered

### Risk 4: Reproducibility Accuracy
**Risk:** Floating-point precision in comparisons
**Mitigation:**
- Tolerance thresholds carefully calibrated
- Deterministic strategies verified exactly
- Stochastic strategies allow larger tolerance
- Diff reports help diagnose mismatches

---

## SUCCESS CRITERIA

### Functional Success
- 40+ unit tests passing
- All acceptance criteria met for all 5 stories
- Schema validated on 10+ real dataset samples
- Reproducibility verifier achieving >95% confidence
- Migration tested on fresh and existing databases
- Performance benchmarks met

### Technical Success
- 80%+ code coverage
- Zero critical bugs
- Event streaming performance <1ms/event
- Query performance <1s for large datasets
- Schema documentation complete with ERD
- All code reviewed and approved

### Team Success
- No scope creep (exactly 5 stories, 40 points)
- On-time delivery (8 weeks, overlapping with TEAM 1)
- Knowledge transfer complete to TEAM 3, 4, 5
- Handoff documentation ready

---

## COMMUNICATION PLAN

### Daily Standup: 15 minutes (same time as other teams)
- Status update
- Blockers
- Coordination with TEAM 1 on state definitions

### Weekly Sync: 1 hour (Thursday)
- Status to program manager
- Integration point review with TEAM 1
- Next week planning

### Bi-weekly Architecture Review: 1 hour
- Schema review and feedback
- Performance review
- Integration impact assessment

---

## APPENDIX: REFERENCE LINKS

- **Architecture Document:** katana-v-04-architecture.md (section 4.2)
- **Epic Definition:** katana-v-05-epics.md (E-JOURNAL-SCHEMA)
- **Test Specification:** test-cases-blocker-2-journal-schema.feature
- **Related Epics:**
  - E-STRATEGY-LIFECYCLE (TEAM 1): State definitions
  - E-TELEMETRY-METRICS (TEAM 3): Metric storage
  - E-COMPARE-WORKFLOW (TEAM 4): Run comparison
  - E-AUDIT-TRAIL (TEAM 5): Audit trail storage

---

**Package Status:** READY FOR TEAM 2 KICKOFF
**Last Updated:** 2026-02-26
**Package Version:** 1.0
