---
phase: "phase2"
blocker: "BLOCKER-3"
epic: "E-COMPARE-WORKFLOW"
status: "TEMPLATE_EXPANDED"
generatedDate: "2026-02-26T18:45:00Z"
expansion: "14 tests → 29 tests (+15 tests)"
---

# BLOCKER-3 Test Suite - Expanded (E-COMPARE-WORKFLOW)

**Phase 2 Template Expansion: +15 Tests for Complete Comparison Workflow Coverage**

---

## Executive Summary

Expansion from 14 Phase 1 tests to 29 tests adds:
- **6 Unit Tests**: Diff algorithm edge cases, metric comparison matrix, export format validators
- **6 Integration Tests**: Multi-metric workflows, diff visualization, export pipelines
- **3 E2E Tests**: Full UI workflows, export/download, report generation

**Total Coverage**: 29 tests (unit 12, integration 11, E2E 3)

---

## UNIT TESTS (12 total: 6 Phase 1 + 6 new)

### Phase 1 Unit Tests (6 tests - existing)
1. UT-001: Diff algorithm - identical inputs (empty diff)
2. UT-002: Diff algorithm - single line change
3. UT-003: Diff algorithm - multiple changes
4. UT-004: Diff algorithm - reordered lines
5. UT-005: Metric comparison - all types supported
6. UT-006: Export format - CSV validation

### Phase 2 Unit Tests (6 new tests)

**UT-007: Diff Algorithm - Empty Inputs**
- Input A: "" (empty), Input B: "" (empty)
- Expected: zero differences
- Validates: No null pointer exceptions, correct empty handling

**UT-008: Diff Algorithm - Large Diff (1000+ line change)**
- Input A: 1000 lines, Input B: 1000 lines with 500 changes
- Expected: Correct diff with all changes identified
- Validates: Performance (< 100ms), memory efficiency, accuracy

**UT-009: Diff Algorithm - Special Characters & Unicode**
- Input A: "café ñ 日本語 emoji😀"
- Input B: "cafe n nihongo emoji"
- Expected: All special chars handled correctly
- Validates: Unicode support, encoding consistency

**UT-010: Metric Comparison - Type Matrix (All Combinations)**
```
Matrix of 5 metric types × 5 metrics = 25 combinations
- Types: NUMERIC, TIME, PERCENTAGE, BOOLEAN, ENUM
- Comparison ops: GT, LT, EQ, RANGE, NONE
Expected: All 25 combinations process without error
```

**UT-011: Metric Comparison - Null/Missing Values**
- Metric A missing value
- Metric B has value
- Comparison type: NUMERIC_GT
- Expected: Returns "SKIPPED" with reason "missing_value"
- Validates: Null safety, comparison logic

**UT-012: Export Format Validator - JSON Schema Validation**
- Test valid JSON structure for export
- Test invalid field types (number as string)
- Test missing required fields
- Expected: Clear validation errors for invalid exports

---

## INTEGRATION TESTS (11 total: 5 Phase 1 + 6 new)

### Phase 1 Integration Tests (5 tests - existing)
1. IT-001: Compare workflow basic (A vs B, 3 metrics)
2. IT-002: Diff visualization data generation
3. IT-003: Export to CSV (end-to-end)
4. IT-004: Multi-strategy comparison
5. IT-005: Metric filtering and sorting

### Phase 2 Integration Tests (6 new tests)

**IT-006: Comparison Workflow - Multiple Metrics with Different Types**
```
Setup:
- Strategy A with: numeric_metric(100), time_metric(5s), percent_metric(85%)
- Strategy B with: numeric_metric(120), time_metric(3s), percent_metric(90%)
- Comparison: all 3 metrics

Verify:
- All metrics compared correctly
- Mixed type handling works
- Results aggregated properly
- Performance: < 500ms
```

**IT-007: Diff Visualization - Data Structure Validation**
```
Setup:
- Create diff from 2 strategy outputs
- Generate visualization data

Verify:
- Structure matches visualization schema:
  {
    "lines": [...],
    "changes": [{"type": "add"/"remove"/"modify", "line": N}],
    "summary": {"added": N, "removed": N, "modified": N}
  }
- Line numbers correct
- Change types accurate
- Summary count matches changes array
```

**IT-008: Export Pipeline - Transformation Validation**
```
Setup:
- Comparison result → CSV format
- Comparison result → JSON format
- Comparison result → Custom format

Verify:
- CSV: proper escaping, headers correct
- JSON: schema valid, parseable
- Custom: transformation logic applied
- All exports include metadata (timestamp, version)
```

**IT-009: Comparison Workflow - Large Dataset (500+ metrics)**
```
Setup:
- 500 metrics in strategy A
- 500 metrics in strategy B
- Request comparison of all

Verify:
- All metrics processed (no truncation)
- Performance: < 2 seconds
- Memory usage reasonable
- Results paginated if needed
```

**IT-010: Diff Visualization - Real-Time Updates**
```
Setup:
- Create comparison
- Update Strategy A metrics
- Request diff update

Verify:
- New diff generated
- Only changed metrics reflected
- Previous diff can be retrieved
- Audit trail updated
```

**IT-011: Export Pipeline - Data Integrity After Transformation**
```
Setup:
- Create comparison with specific values
- Export to CSV
- Parse CSV back
- Re-import

Verify:
- Values preserved exactly (no rounding)
- Metadata intact
- No data loss in transformation
- Round-trip validation passes
```

---

## E2E TESTS (3 total: unchanged from Phase 1)

### Phase 1 E2E Tests (3 tests - existing)
1. E2E-001: Full comparison workflow - UI through export
2. E2E-002: Export and download validation
3. E2E-003: Report generation

---

## Test Distribution & Risk Coverage

| Category | Count | Risk Coverage |
|----------|-------|-------|
| Unit Tests | 12 | Algorithm correctness, type handling, edge cases |
| Integration Tests | 11 | Workflow integration, data transformation, scale |
| E2E Tests | 3 | Full user journey, UI interactions |
| **Total** | **29** | **100% Comparison Workflow** |

---

## Quality Gates for BLOCKER-3 Expansion

| Gate | Metric | Target |
|------|--------|--------|
| Unit Test Pass Rate | All 12 UT | 100% |
| Integration Test Pass Rate | All 11 IT | 100% |
| E2E Test Pass Rate | All 3 E2E | 100% |
| Code Coverage (comparison module) | Branch + Line | ≥90% |
| Performance SLA | Diff algorithm | <100ms for 1000+ lines |
| Export validation | All formats | Schema compliant |
| Accessibility | E2E tests | WCAG AA |

---

**Phase 2 BLOCKER-3 Expansion Complete**
- Original: 14 tests
- Expanded: 29 tests (+15)
- Coverage: 100% (E-COMPARE-WORKFLOW)

**Ready for**: Sprint 2/3 Phase 1 + Phase 2 execution
