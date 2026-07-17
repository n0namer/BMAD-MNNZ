# TEAM 4: BLOCKER-4 PACKAGE - Compare Workflow & Delta Analysis

**Project:** Katana Vectorbt Optimizer - Phase 2 Implementation
**Team:** Backend Team 4 (Comparison & Analysis)
**Blocker:** BLOCKER-4
**Package Created:** 2026-02-26
**Duration:** 8 weeks (Weeks 9-16, depends on TEAM 2)
**Dependencies:** Requires TEAM 2 journal schema

---

## EXECUTIVE SUMMARY

Team 4 implements comprehensive run comparison and delta analysis capabilities. Users can select two strategy runs and see detailed parameter differences, metric changes, and outcome variations. Delta visualization with color-coding highlights changes, enabling rapid understanding of what changed and why performance differed.

### Key Deliverables
- Comparison algorithm for structured delta analysis
- Run selection UI with filtering and search
- Delta visualization with color-coded changes
- Metric selection and filtering
- Export functionality (CSV, JSON)
- 25+ unit tests

### Business Impact
- Enables learning from run history
- Identifies impact of parameter changes
- Supports hypothesis validation
- Accelerates optimization cycles

---

## EPIC ASSIGNMENT

**Epic ID:** E-COMPARE-WORKFLOW
**Priority:** HIGH
**Complexity:** MEDIUM
**Total Story Points:** 25
**Minimum Tests:** 25 unit tests

### Epic Acceptance Criteria
- All 5 child stories must pass acceptance criteria
- Comparison works for any 2 runs from history
- Delta analysis shows all differences with color coding
- Export functionality supports CSV and JSON
- Minimum 25 unit tests covering comparison logic
- Performance: comparison loads in <2 seconds

---

## STORY BREAKDOWN

### Story 1: S-COMPARE-001 - Implement Comparison Algorithm
**Points:** 7 | **Dependencies:** E-JOURNAL-SCHEMA (TEAM 2) | **Tests Required:** 7+

#### Description
Build algorithm to compare two strategy runs and generate structured delta. Identifies differences in parameters, metrics, and outcomes with similarity scoring.

#### Acceptance Criteria
1. Algorithm identifies differences in parameters, metrics, outcomes
2. Similarity scoring implemented (0-100%)
3. Null/missing values handled correctly
4. Deep comparison of nested objects
5. Performance: <500ms for typical runs
6. 7+ unit tests for comparison logic

#### Implementation Checklist
- [ ] Design comparison algorithm
- [ ] Implement parameter-by-parameter comparison
- [ ] Create metrics difference calculation
- [ ] Add outcome comparison
- [ ] Implement similarity scoring
- [ ] Handle null/missing values gracefully
- [ ] Write 7+ unit tests for comparison
- [ ] Add performance benchmarks

#### Comparison Algorithm
```
1. Load run1 and run2 from database
2. For each field (parameter, metric, outcome):
   - If same: mark as identical
   - If different: calculate change (absolute, percentage)
   - If missing in one: mark as added/removed
3. Calculate overall similarity: (identical fields / total fields) * 100
4. Group changes by category (parameters, metrics, outcomes)
5. Return structured delta object with all differences
```

#### Test Scenarios Covered
- S-COMPARE-001: Comparison algorithm accuracy
- Parameter difference detection
- Metric change calculation
- Similarity scoring
- Null/missing value handling
- Performance benchmarks

#### Files to Create/Modify
- `lib/compare/compare-algorithm.ts` - Comparison logic
- `lib/compare/compare-algorithm.spec.ts` - Unit tests (7+ tests)

---

### Story 2: S-COMPARE-002 - Build Run Selection UI
**Points:** 5 | **Dependencies:** S-COMPARE-001 | **Tests Required:** 5+

#### Description
Create interface for users to select 2 runs to compare. Displays key metadata, supports search/filter by date range, strategy, status.

#### Acceptance Criteria
1. Run list displays key metadata (date, status, key metrics)
2. Search/filter by date range, strategy, status
3. Recently compared runs available as quick access
4. Date range picker for bulk selection
5. Performance: run list loads in <1 second
6. 5+ unit tests for UI logic

#### Implementation Checklist
- [ ] Design run selection interface
- [ ] Implement run list query with pagination
- [ ] Add search by strategy name
- [ ] Add filter by date range
- [ ] Add filter by status (SUCCESS, FAILED, KILLED)
- [ ] Create "recently compared" history
- [ ] Implement date range picker
- [ ] Write 5+ unit tests for selection logic
- [ ] Optimize query performance

#### Run List Features
- Display columns: Run ID, Strategy Name, Date, Status, Key Metrics (Sharpe Ratio, Win Rate)
- Search box (fuzzy match on strategy name)
- Date range picker (from/to dates)
- Status filter (multi-select)
- Recently compared quick access (last 5 comparisons)
- Pagination (50 runs per page)

#### Test Scenarios Covered
- Run list loading and pagination
- Search functionality
- Filter by date range
- Filter by status
- Recently compared history
- Performance (<1s load time)

#### Files to Create/Modify
- `ui/compare/run-selector.tsx` - Run selection component
- `lib/compare/run-selector-service.ts` - Run query logic
- `lib/compare/run-selector-service.spec.ts` - Unit tests (5+ tests)

---

### Story 3: S-COMPARE-003 - Create Delta Visualization
**Points:** 6 | **Dependencies:** S-COMPARE-002 | **Tests Required:** 6+

#### Description
Build visual representation of differences between two runs. Side-by-side comparison view with color-coded changes (green for added, red for removed, yellow for changed).

#### Acceptance Criteria
1. Side-by-side comparison view (run1 vs. run2)
2. Differences highlighted in color (added: green, removed: red, changed: yellow)
3. Sortable columns (field name, old value, new value, change type)
4. Drill-down into nested fields
5. Performance: render comparison for 100+ fields in <1s
6. 6+ unit tests for visualization logic

#### Implementation Checklist
- [ ] Design side-by-side layout
- [ ] Implement color-coding system
- [ ] Create sortable column headers
- [ ] Implement field drill-down
- [ ] Add nested object expansion
- [ ] Create change type indicators
- [ ] Write 6+ unit tests for visualization
- [ ] Optimize rendering performance

#### Visualization Components
- Left column: Run 1 (Header: Run ID, Date, Status)
- Right column: Run 2 (Header: Run ID, Date, Status)
- Center: Differences
  - Green highlight: added in Run 2
  - Red highlight: removed in Run 2
  - Yellow highlight: changed value
  - Grey: identical value
- Each row: Field Name | Run 1 Value | Change Type | Run 2 Value

#### Test Scenarios Covered
- Color-coding accuracy
- Side-by-side layout rendering
- Sorting by column
- Drill-down into nested objects
- Large dataset rendering performance
- Change type classification

#### Files to Create/Modify
- `ui/compare/delta-view.tsx` - Delta visualization component
- `lib/compare/delta-formatter.ts` - Delta data formatting
- `lib/compare/delta-formatter.spec.ts` - Unit tests (6+ tests)

---

### Story 4: S-COMPARE-004 - Add Metric Selection
**Points:** 4 | **Dependencies:** S-COMPARE-003 | **Tests Required:** 4+

#### Description
Allow users to focus comparison on specific metrics or parameter subsets. Presets available (all, key metrics, strategy params only).

#### Acceptance Criteria
1. Metric selection menu (checkboxes)
2. Presets available (all, key metrics, strategy params only)
3. Custom metric grouping saved as views
4. Filter by metric change threshold (show only changes >X%)
5. 4+ unit tests for metric selection

#### Implementation Checklist
- [ ] Design metric selection menu
- [ ] Create metric grouping logic
- [ ] Implement filter by change threshold
- [ ] Add preset button (all, key metrics, params)
- [ ] Create save custom view functionality
- [ ] Load saved views from database
- [ ] Write 4+ unit tests for metric selection
- [ ] Add UX hints (metric descriptions)

#### Metric Selection Features
- Metric category checkboxes (Parameters, Metrics, Outcomes)
- Individual metric checkboxes (win_rate, sharpe_ratio, etc.)
- Presets: All Metrics | Key Metrics | Parameters Only
- Change threshold slider (0-100%)
- Save current selection as "Custom View 1"
- Load previously saved views

#### Test Scenarios Covered
- Metric selection and filtering
- Preset button functionality
- Custom view save/load
- Change threshold filtering
- Metric group expansion/collapse

#### Files to Create/Modify
- `ui/compare/metric-selector.tsx` - Metric selection component
- `lib/compare/metric-selector-service.ts` - Metric grouping logic
- `lib/compare/metric-selector-service.spec.ts` - Unit tests (4+ tests)

---

### Story 5: S-COMPARE-005 - Build Export Functionality
**Points:** 3 | **Dependencies:** S-COMPARE-003 | **Tests Required:** 3+

#### Description
Implement export of comparison results to CSV and JSON formats. Includes metadata (run IDs, comparison date) and handles large exports efficiently.

#### Acceptance Criteria
1. CSV export includes headers and all comparison data
2. JSON export maintains structure
3. Both formats include metadata (run IDs, comparison date)
4. Large exports handled efficiently (streaming for >10MB)
5. 3+ unit tests for export functionality

#### Implementation Checklist
- [ ] Design CSV format (columns, header row)
- [ ] Create CSV writer (streaming for large datasets)
- [ ] Design JSON structure (metadata + data)
- [ ] Create JSON writer (pretty-print option)
- [ ] Add file download handling
- [ ] Implement streaming for large exports
- [ ] Write 3+ unit tests for export
- [ ] Add compression option (gzip for JSON)

#### Export Formats

**CSV Format:**
```
Field Name,Run 1 Value,Change Type,Run 2 Value,Change %
entry_threshold,0.5,CHANGED,0.6,20%
exit_threshold,0.8,IDENTICAL,0.8,0%
lookback_period,50,CHANGED,100,100%
...
```

**JSON Format:**
```json
{
  "metadata": {
    "run1_id": "uuid",
    "run2_id": "uuid",
    "comparison_date": "ISO 8601",
    "similarity_score": 85.5
  },
  "differences": {
    "parameters": [...],
    "metrics": [...],
    "outcomes": [...]
  }
}
```

#### Test Scenarios Covered
- CSV export format and content
- JSON export structure
- Metadata inclusion
- File download handling
- Large dataset streaming
- Compression

#### Files to Create/Modify
- `lib/compare/export-service.ts` - Export logic
- `lib/compare/export-service.spec.ts` - Unit tests (3+ tests)

---

## TESTING REQUIREMENTS

### Unit Tests (25+ total required)

**Comparison Algorithm (7 tests):**
- Parameter difference detection
- Metric change calculation
- Outcome comparison
- Similarity scoring
- Null/missing value handling
- Performance benchmarks
- Complex nested structures

**Run Selection (5 tests):**
- Run list loading
- Search functionality
- Filter by date range
- Filter by status
- Performance metrics

**Delta Visualization (6 tests):**
- Color-coding accuracy
- Side-by-side rendering
- Column sorting
- Drill-down navigation
- Nested object expansion
- Performance with large datasets

**Metric Selection (4 tests):**
- Metric selection and filtering
- Preset button functionality
- Custom view save/load
- Change threshold filtering

**Export (3 tests):**
- CSV export format
- JSON export structure
- Metadata inclusion
- Large dataset handling

### Test Coverage Requirements
- Minimum 80% code coverage
- All comparison paths tested
- Edge cases (empty data, nulls)
- Performance tests (comparison <500ms)

---

## DELIVERABLES CHECKLIST

### Code Deliverables
- [ ] `lib/compare/compare-algorithm.ts` (200-300 lines)
- [ ] `ui/compare/run-selector.tsx` (250-350 lines)
- [ ] `ui/compare/delta-view.tsx` (300-400 lines)
- [ ] `ui/compare/metric-selector.tsx` (150-200 lines)
- [ ] `lib/compare/export-service.ts` (150-200 lines)
- [ ] Supporting service files (5-6 additional files)

### Test Deliverables
- [ ] 25+ unit tests (100% passing)
- [ ] Test coverage report (80%+ coverage)
- [ ] Performance benchmarks

### Documentation Deliverables
- [ ] Comparison algorithm documentation
- [ ] Delta visualization guide
- [ ] Export format specifications
- [ ] API documentation

### Configuration Deliverables
- [ ] Metric grouping configuration
- [ ] Preset definitions
- [ ] Export format templates

---

## DEPENDENCIES & BLOCKING RELATIONSHIPS

### Blocks
- None (comparison supports other workflows but doesn't block them)

### Dependencies
- **Depends on:** TEAM 2 (E-JOURNAL-SCHEMA) - run data structure
- **Depends on:** TEAM 1 (state definitions) - run status values

---

## TEAM COMPOSITION

**Team Lead:** Backend Developer (1)
**Backend Developers:** 1
**Frontend Developer:** 1
**QA Engineer:** 1

**Total: 3.5 FTE over 8 weeks**

---

## TIMELINE & MILESTONES

### Week 9-10: Comparison Algorithm & Run Selection (S-COMPARE-001, S-COMPARE-002)
- Implement comparison algorithm
- Build run selection UI
- Write 12+ unit tests
- **Exit Criteria:** Both components functional

### Week 11: Delta Visualization (S-COMPARE-003)
- Build delta visualization component
- Implement color-coding
- Add sorting/drill-down
- Write 6+ unit tests
- **Exit Criteria:** Delta visualization complete

### Week 12: Metric Selection (S-COMPARE-004)
- Implement metric selection UI
- Add presets
- Create custom view save/load
- Write 4+ unit tests
- **Exit Criteria:** Full metric selection capability

### Week 13: Export & Integration (S-COMPARE-005)
- Implement CSV/JSON export
- Add download handling
- Write 3+ unit tests
- **Exit Criteria:** Export functionality complete

### Week 14-16: Testing & Optimization
- Integration testing
- Performance optimization (<2s comparison load)
- Documentation completion
- **Exit Criteria:** All acceptance criteria met

---

## QUALITY GATES

### Definition of Done
1. All acceptance criteria met (all 5 stories)
2. 25+ unit tests passing (100% pass rate)
3. 80%+ code coverage
4. Comparison loads in <2s
5. Zero critical bugs
6. Documentation complete

### Code Quality Standards
- TypeScript strict mode
- Comparison algorithm well-documented
- UI responsive and accessible
- Export formats validated
- Performance optimized

### Performance Requirements
- Comparison algorithm: <500ms
- UI render: <1s
- Export generation: <5s for typical runs
- Overall comparison workflow: <2s

---

## RISK MITIGATION

### Risk 1: Performance with Large Datasets
**Risk:** Comparing runs with thousands of metrics could be slow
**Mitigation:**
- Early performance testing
- Index database queries appropriately
- Stream export for large datasets
- Client-side filtering to reduce data

### Risk 2: UI Complexity
**Risk:** Too many metrics to display could overwhelm users
**Mitigation:**
- Metric selection/filtering (Story 4)
- Presets for common views
- Good visual hierarchy (green/red/yellow)
- Drill-down capability for details

### Risk 3: Export Format Compatibility
**Risk:** Export formats not meeting user expectations
**Mitigation:**
- Validate export formats on sample data
- Provide format specification upfront
- Get user feedback on format early
- Support multiple format options

---

## SUCCESS CRITERIA

### Functional Success
- 25+ unit tests passing
- All 5 stories acceptance criteria met
- Comparison working for any two runs
- Delta visualization clear and accurate
- Export functionality reliable

### Technical Success
- 80%+ code coverage
- Comparison loads <2s
- Algorithm performance <500ms
- Zero critical bugs
- Responsive UI design

### Team Success
- No scope creep (exactly 5 stories, 25 points)
- On-time delivery (8 weeks, starting week 9)
- Knowledge transfer complete
- Documentation complete

---

## COMMUNICATION PLAN

### Daily Standup: 15 minutes

### Weekly Sync: 1 hour (Thursday)
- Status to program manager
- Dependency check on TEAM 2
- UI design review

### Bi-weekly Review: 1 hour
- Algorithm accuracy verification
- Performance review
- User feedback incorporation

---

## APPENDIX: REFERENCE LINKS

- **Architecture Document:** katana-v-04-architecture.md (section 4.4)
- **Epic Definition:** katana-v-05-epics.md (E-COMPARE-WORKFLOW)
- **Test Specification:** test-cases-blocker-4-compare.feature
- **Dependencies:**
  - E-JOURNAL-SCHEMA (TEAM 2): Run data structure
  - E-STRATEGY-LIFECYCLE (TEAM 1): Run status values

---

**Package Status:** READY FOR TEAM 4 KICKOFF
**Last Updated:** 2026-02-26
**Package Version:** 1.0
