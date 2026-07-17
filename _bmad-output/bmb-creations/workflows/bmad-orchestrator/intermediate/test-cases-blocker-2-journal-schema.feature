# Feature: BLOCKER-2 - Journal Schema & Data Persistence
# Author: QA Agent
# Created: 2026-02-26
# Description: Comprehensive test cases for schema validation, database operations, and reproducibility verification

Feature: Journal Schema & Data Persistence (BLOCKER-2)
  Background:
    Given a Journal Keeper System is initialized
    And the database schema is loaded
    And a test database instance is ready

  # ========================================
  # SCHEMA VALIDATION (15 tests)
  # ========================================

  Scenario: SV-001 - Manifest structure validation
    Given a journal manifest document
    When the manifest is parsed
    Then it should have all required top-level keys: title, description, version, entries
    And manifest.title should be a non-empty string
    And manifest.version should follow semantic versioning (X.Y.Z)
    And manifest.entries should be an array
    And Pass Criteria: All keys present, string valid, version valid, array valid

  Scenario: SV-002 - Entry structure validation
    Given a journal entry in the manifest
    When the entry is validated against schema
    Then it should have all required fields: id, timestamp, title, content, state, tags
    And entry.id should be a valid UUID
    And entry.timestamp should be ISO 8601 format
    And entry.state should be one of [IDLE, CANDIDATE, PAPER, MICRO_LIVE, COMPLETED, REJECTED, EXPIRED]
    And entry.tags should be a non-empty array of strings
    And Pass Criteria: All required fields present, UUID valid, timestamp ISO 8601, state valid, tags array

  Scenario: SV-003 - Extended entry metadata validation
    Given a journal entry with extended metadata
    When metadata is validated
    Then optional fields (author, reviewer, category) should be strings if present
    And metadata.author should match email or handle pattern
    And metadata.category should be from predefined list
    And metadata.created_at and updated_at should be ISO 8601
    And Pass Criteria: Optional fields valid, author matches pattern, category in list, dates ISO 8601

  Scenario: SV-004 - Event array validation
    Given a journal entry with events array
    When events are validated
    Then each event should have: type, timestamp, details, status
    And event.type should be one of [CREATED, UPDATED, REVIEWED, SUBMITTED, REJECTED, APPROVED, COMPLETED]
    And event.timestamp should be ISO 8601 and later than previous event
    And event.status should be one of [PENDING, SUCCESS, FAILED, SKIPPED]
    And Pass Criteria: All events have required fields, types valid, timestamps ordered, status valid

  Scenario: SV-005 - Nested object depth validation
    Given a journal entry with nested objects (reviewer info, history, etc.)
    When depth is validated
    Then maximum nesting depth should not exceed 5 levels
    And circular references should not exist
    And all nested objects should be properly typed
    And And missing required nested fields should trigger validation error
    And Pass Criteria: Max depth 5, no circular refs, types correct, required fields present

  Scenario: SV-006 - Field length constraints
    Given journal entry fields with content
    When field lengths are validated
    Then title should be 5-255 characters
    And content should be max 100,000 characters
    And tags should be 1-50 characters each
    And author should be max 100 characters
    And Pass Criteria: Title length valid, content <100k, tags <50, author <100

  Scenario: SV-007 - Data type validation
    Given a journal entry with all fields populated
    When data types are validated
    Then all string fields should be strings (not null, not numeric)
    And all numeric fields should be numbers (not strings)
    And all boolean fields should be true/false
    And all array fields should be arrays (not objects)
    And Pass Criteria: All types correct, no type mismatches

  Scenario: SV-008 - Required vs optional field validation
    Given various journal entries with different field combinations
    When validation is run
    Then required fields (id, timestamp, title, state) must always be present
    And optional fields should not cause validation failure if missing
    And If optional field is present, it should still be validated
    And Pass Criteria: Required fields enforced, optional fields flexible, present optionals validated

  Scenario: SV-009 - Enum constraint validation
    Given entries with enumerated fields (state, event.type, event.status)
    When enum constraints are validated
    Then state field should only accept predefined enum values
    And invalid enum values should trigger validation error with clear message
    And enum list should be consistent across schema definitions
    And Pass Criteria: Enum constraints enforced, invalid values rejected, list consistent

  Scenario: SV-010 - Relationship validation
    Given multiple journal entries with cross-references (paper_id, idea_id, project_id)
    When relationships are validated
    Then referenced IDs must exist in database
    And relationship type must match (e.g., idea → paper is valid)
    And Circular dependencies should be detected
    And And reverse relationships should be consistent
    And Pass Criteria: References exist, types match, no cycles, relationships consistent

  Scenario: SV-011 - Schema evolution validation
    Given a schema version upgrade (e.g., v1.0 → v2.0)
    When migration validation runs
    Then new required fields should have default values for old entries
    And old optional fields should be preserved (backwards compatibility)
    And deprecated fields should be marked and handled gracefully
    And migration should not lose data
    And Pass Criteria: Defaults applied, compat maintained, deprecated handled, no data loss

  Scenario: SV-012 - Summary document validation
    Given a summary document for a journal/project
    When summary is validated
    Then required fields should be: project_name, metrics, status, last_updated
    And metrics should contain: ideas_count, papers_count, projects_count, completion_rate
    And completion_rate should be a number between 0-100
    And last_updated should be ISO 8601 timestamp
    And Pass Criteria: Summary has required fields, metrics complete, rate valid, timestamp valid

  Scenario: SV-013 - Metrics object validation
    Given metrics within a summary or entry
    When metrics are validated
    Then each metric should have: name, value, unit, timestamp
    And metric.value should be numeric
    And metric.unit should be from predefined units list (days, hours, count, percentage, etc.)
    And metric.timestamp should be ISO 8601
    And Pass Criteria: Metrics complete, value numeric, unit valid, timestamp ISO 8601

  Scenario: SV-014 - Unicode and special character handling
    Given journal entries with unicode, emoji, and special characters in content
    When content is validated
    Then unicode characters should be preserved correctly
    And emoji should be handled without encoding issues
    And Special characters (quotes, backslashes, etc.) should be escaped properly
    And And content should remain readable after serialization/deserialization
    And Pass Criteria: Unicode preserved, emoji handled, special chars escaped, readable

  Scenario: SV-015 - Schema validation error reporting
    Given a journal entry with multiple schema violations
    When validation is run
    Then error report should list all violations (not just first)
    And each error should include: field name, expected type/value, actual value
    And Error messages should be human-readable and actionable
    And Pass Criteria: All violations reported, errors detailed, messages clear

  # ========================================
  # DATABASE OPERATIONS (15 tests)
  # ========================================

  Scenario: DB-001 - Insert valid journal entry
    Given a valid journal entry object
    When the entry is inserted into the database
    Then the entry should be stored successfully
    And the returned ID should match expected UUID format
    And the timestamp should be recorded
    And the entry should be retrievable by ID
    And Pass Criteria: Insert successful, ID valid, timestamp recorded, retrievable

  Scenario: DB-002 - Insert with duplicate ID detection
    Given an entry with ID that already exists in database
    When insert is attempted
    Then the operation should fail with duplicate key error
    And original entry should be unchanged
    And error message should clearly indicate duplicate
    And Pass Criteria: Duplicate rejected, original unchanged, error clear

  Scenario: DB-003 - Update entry successfully
    Given an existing journal entry in the database
    When fields (content, state, tags) are updated
    Then the update should succeed
    And updated_at timestamp should be changed
    And previous values should be preserved in history
    And retrieval should show updated values
    And Pass Criteria: Update successful, timestamp changed, history preserved, values updated

  Scenario: DB-004 - Update with optimistic locking
    Given an entry with version 1
    And two concurrent update attempts with version 1
    When both updates are executed
    Then first update should succeed (version 1 → 2)
    And second update should fail (version mismatch)
    And Data should not be corrupted
    And And failure should indicate version conflict
    And Pass Criteria: First succeeds, second fails, no corruption, conflict indicated

  Scenario: DB-005 - Delete entry and verify cascading
    Given an entry with 5 linked child records
    When the entry is deleted
    Then the entry should be removed from database
    And child records should be handled appropriately (cascade delete or orphan)
    And Deletion timestamp should be recorded
    And Hard delete or soft delete logic should match specification
    And Pass Criteria: Entry deleted, children handled, timestamp recorded, logic correct

  Scenario: DB-006 - Query by state filter
    Given 100 entries with various states (IDLE, CANDIDATE, PAPER, MICRO_LIVE, COMPLETED)
    When query is executed with state filter (e.g., state = PAPER)
    Then only entries in PAPER state should be returned
    And Query should complete within SLA (< 100ms)
    And Total count should match expected count
    And Pass Criteria: Only matching entries, query fast, count correct

  Scenario: DB-007 - Query with multiple filters
    Given entries with various state, author, and category combinations
    When query is executed with multiple filters (state=PAPER AND author=alice AND category=AI)
    Then only matching entries should be returned
    And Filters should be applied conjunctively (AND logic)
    And Results should be sorted by timestamp descending
    And Pass Criteria: Matches correct, AND logic applied, sorted by timestamp

  Scenario: DB-008 - Pagination support
    Given 1000 entries in database
    When paginated query is run (page=2, size=50)
    Then 50 entries should be returned (entries 51-100)
    And total_count should be 1000
    And has_next_page should be true
    And has_previous_page should be true
    And Pass Criteria: Correct entries returned, count correct, pagination flags correct

  Scenario: DB-009 - Index performance verification
    Given 50,000 entries indexed on (state, timestamp)
    When query is executed with state filter and timestamp range
    Then query should use index (explain plan should show index usage)
    And Query should complete within 50ms
    And Results should be correct
    And Pass Criteria: Index used, query fast, results correct

  Scenario: DB-010 - Transaction rollback on error
    Given a multi-step database operation (insert entry, update summary, log event)
    When an error occurs during step 2
    Then all changes should be rolled back
    And Database should return to pre-transaction state
    And Error should be returned to caller
    And Pass Criteria: Rollback complete, state restored, error returned

  Scenario: DB-011 - Batch insert operations
    Given 1000 valid journal entries
    When batch insert is executed
    Then all 1000 entries should be inserted
    And Operation should complete in < 5 seconds
    And No entries should be partially inserted
    And Audit log should record batch operation
    And Pass Criteria: All 1000 inserted, time <5s, no partial inserts, logged

  Scenario: DB-012 - Database connection pool management
    Given 10 concurrent database operations
    When operations are executed simultaneously
    Then connection pool should be efficiently utilized
    And No connection pool exhaustion should occur
    And Query performance should not degrade
    And And pool statistics should show healthy distribution
    And Pass Criteria: Efficient utilization, no exhaustion, performance stable, stats healthy

  Scenario: DB-013 - Backup and restore verification
    Given a database with 10,000 entries
    When backup is created
    Then backup file should be created successfully
    And Backup size should be reasonable (not corrupted)
    When backup is restored to new database
    Then restored database should have all 10,000 entries
    And Checksums should match original
    And Pass Criteria: Backup created, restored complete, checksums match

  Scenario: DB-014 - Data consistency check
    Given database with entries and cross-references
    When consistency check is run
    Then all foreign keys should be valid
    And No orphaned records should exist
    And Checksums should match expected values
    And No data corruption should be detected
    And Pass Criteria: Foreign keys valid, no orphans, checksums match, no corruption

  Scenario: DB-015 - Concurrent write conflict resolution
    Given two concurrent operations modifying same entry
    When both operations execute (first commit wins strategy)
    Then first operation should succeed
    And second operation should fail with conflict error
    And Database should not show merged/corrupted state
    And Error should be informative
    And Pass Criteria: First succeeds, second fails, no corruption, error informative

  # ========================================
  # REPRODUCIBILITY (10 tests)
  # ========================================

  Scenario: RP-001 - Entry hash generation
    Given a journal entry with fixed content and metadata
    When hash is generated (SHA-256)
    Then hash should be deterministic (same input = same hash)
    And hash should be 64 hex characters
    And Any change to content should change hash
    And Pass Criteria: Hash deterministic, 64 chars, changes with content

  Scenario: RP-002 - Reproducibility seed verification
    Given a journal entry with reproducibility_seed field
    When seed is extracted
    Then seed should be a valid string (alphanumeric + special chars)
    And seed should enable reproduction of entry's execution/generation
    And seed should be immutable after entry creation
    And Pass Criteria: Seed valid, enables reproduction, immutable

  Scenario: RP-003 - Code version matching
    Given a journal entry created with code version v1.5.2
    When the entry is retrieved later
    Then code_version field should be v1.5.2
    And Compatibility check should verify if current code (e.g., v1.5.3) is compatible
    And If incompatible, warning should be issued
    And Pass Criteria: Version recorded, compatibility checked, warning if incompatible

  Scenario: RP-004 - Exact reproduction with seed
    Given a journal entry with seed S and code version V
    When another execution uses the same seed and code version
    Then output should be byte-for-byte identical
    And Metrics should match exactly
    And Hash should be identical
    And Pass Criteria: Output identical, metrics match, hash identical

  Scenario: RP-005 - Seed entropy verification
    Given 100 generated journal entries
    When seeds are extracted from all entries
    Then no two seeds should be identical
    And Seed distribution should show good entropy
    And And seed length should be consistent
    And Pass Criteria: All unique, good entropy, consistent length

  Scenario: RP-006 - Reproducibility failure detection
    Given a journal entry with seed S, code version V, and expected hash H
    When reproduction is attempted but actual hash is H'
    Then reproducibility check should FAIL
    And Detailed diff should show what changed
    And Root cause analysis should be triggered (code diff, seed issue, version conflict)
    And Alert should be issued
    And Pass Criteria: Failure detected, diff shown, analysis triggered, alert issued

  Scenario: RP-007 - Cross-environment reproducibility
    Given a journal entry created on Windows with Python 3.9
    When the same entry is reproduced on Linux with Python 3.9 (same code version)
    Then output should be identical across environments
    And Platform-specific operations should be handled correctly
    And And no environment-specific differences should affect reproducibility
    And Pass Criteria: Output identical across platforms, operations handled, no env drift

  Scenario: RP-008 - Reproducibility with floating point precision
    Given a journal entry with metrics containing floating point numbers
    When the entry is reproduced
    Then floating point precision should be maintained (to tolerance level)
    And Rounding differences should be acceptable (e.g., ±1e-9)
    And Comparison should not fail due to insignificant precision loss
    And Pass Criteria: Precision maintained, rounding acceptable, comparison robust

  Scenario: RP-009 - Dependency version reproducibility
    Given a journal entry that depends on external libraries (numpy v1.19.5, pandas v1.1.4)
    When reproducibility is verified
    Then dependency versions must match exactly
    And If different versions are used, reproducibility should fail with clear message
    And Dependency lock file should be included in entry metadata
    And Pass Criteria: Versions match, failure clear, lock file included

  Scenario: RP-010 - Reproducibility audit trail
    Given a journal entry with reproducibility history (creation, last reproduction, all attempts)
    When audit trail is queried
    Then all reproduction attempts should be logged
    And Success/failure should be recorded for each attempt
    And Timestamps should show when each attempt occurred
    And Environment metadata should be captured for each attempt
    And Pass Criteria: All attempts logged, success/failure recorded, timestamps accurate, env captured

