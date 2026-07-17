# Feature: BLOCKER-4 - Run Comparison & Analysis
# Author: QA Agent
# Created: 2026-02-26
# Description: Comprehensive test cases for comparison algorithm, UI workflow, and edge cases

Feature: Run Comparison & Analysis (BLOCKER-4)
  Background:
    Given a Journal Keeper System with comparison module
    And multiple completed run executions are available
    And metrics are collected and stored for each run
    And comparison results storage is ready

  # ========================================
  # COMPARISON ALGORITHM (10 tests)
  # ========================================

  Scenario: CA-001 - Metric delta calculation (absolute)
    Given Run A with metric X = 100
    And Run B with metric X = 120
    When absolute delta is calculated
    Then delta should be 20 (120 - 100)
    And delta should be positive (B > A)
    And delta_direction should be "increased"
    And Pass Criteria: Delta calculated correctly, sign correct, direction set

  Scenario: CA-002 - Metric delta calculation (percentage)
    Given Run A with metric X = 100
    And Run B with metric X = 120
    When percentage delta is calculated
    Then percentage_delta should be 20% ((120-100)/100 * 100)
    And Percentage should always be positive (absolute change)
    And Change direction should be indicated separately
    And Pass Criteria: Percentage calculated correctly, absolute, direction separate

  Scenario: CA-003 - Statistical significance testing
    Given Run A with metric X: mean=100, std_dev=5, n=100 samples
    And Run B with metric X: mean=102, std_dev=5, n=100 samples
    When t-test is performed
    Then p-value should indicate if difference is statistically significant
    And If p-value < 0.05, difference is significant
    And If p-value >= 0.05, difference is not significant (could be noise)
    And Effect size should also be calculated (Cohen's d)
    And Pass Criteria: t-test performed, p-value correct, effect size calculated

  Scenario: CA-004 - Multi-metric comparison ranking
    Given Run A and Run B compared on 10 metrics
    And some metrics improved, some regressed
    When ranking algorithm is applied
    Then Overall improvement score should be calculated
    And Should weight important metrics higher
    And Run with better overall score should be ranked higher
    And Ranking should be stable (deterministic)
    And Pass Criteria: Score calculated, weights applied, ranking stable

  Scenario: CA-005 - Correlation analysis between metrics
    Given metrics M1, M2, M3 from Run A and Run B
    When correlation is calculated for M1 vs M2
    Then Correlation coefficient should be between -1 and 1
    And Positive correlation if both increase together
    And Negative correlation if one increases while other decreases
    And Strength should be indicated (weak, moderate, strong)
    And Pass Criteria: Correlation calculated, range correct, strength indicated

  Scenario: CA-006 - Regression detection
    Given Run A = baseline with metrics at expected levels
    And Run B with same configuration as Run A
    When comparison is performed
    Then Any metric drop of > 5% should be flagged as possible regression
    And Regression severity should be calculated
    And CRITICAL regressions (>20% drop) should be highlighted
    And And regression recommendations should be generated
    And Pass Criteria: Regressions detected, severity set, recommendations generated

  Scenario: CA-007 - Improvement detection
    Given Run B showing significant improvements over Run A
    When comparison detects improvement
    Then Improvement should be flagged and highlighted
    And Improvements >10% should be marked as significant
    And Root cause analysis suggestions should be provided
    And Successful optimization techniques should be noted
    And Pass Criteria: Improvements flagged, threshold applied, analysis provided

  Scenario: CA-008 - Comparison with confidence intervals
    Given metrics with 95% confidence intervals calculated
    When comparing Run A and Run B
    Then If confidence intervals don't overlap, difference is significant
    And If confidence intervals overlap, result may be inconclusive
    And Visualization should show confidence bands
    And Recommendation should reflect confidence level
    And Pass Criteria: CI compared, overlap detected, visualization clear, recommendation confident

  Scenario: CA-009 - Trend analysis across 5+ runs
    Given sequential runs showing metric evolution: R1→R2→R3→R4→R5
    When trend analysis is performed
    Then Linear regression should show trend direction
    And Momentum should indicate acceleration/deceleration
    And Forecast should estimate next run's metrics
    And Anomalies in trend should be flagged
    And Pass Criteria: Trend detected, momentum calculated, forecast provided, anomalies flagged

  Scenario: CA-010 - Comparison performance with large datasets
    Given two runs each with 1 million metric samples
    When comparison algorithm executes
    Then Comparison should complete within 10 seconds
    And Memory usage should not exceed 2GB
    And Results should be accurate despite size
    And And sampling strategy should maintain accuracy if needed
    And Pass Criteria: Completion <10s, memory <2GB, accuracy maintained

  # ========================================
  # UI WORKFLOW (8 tests)
  # ========================================

  Scenario: UW-001 - Run selection interface
    Given a list of 50 completed runs displayed in UI
    When user clicks on two runs to compare
    Then Both runs should be highlighted/selected
    And Selected run metadata should be shown (date, config, metrics count)
    And "Compare" button should become active
    And User should be able to clear selection and reselect
    And Pass Criteria: Runs selected, metadata shown, button active, selection changeable

  Scenario: UW-002 - Comparison results rendering
    Given results from comparison algorithm
    When results are rendered in UI
    Then Side-by-side comparison table should show metrics
    And Positive/negative deltas should be color-coded (green/red)
    And Percentage changes should be clearly displayed
    And Statistical significance indicators should be visible
    And Pass Criteria: Table rendered, colors correct, percentages visible, stats shown

  Scenario: UW-003 - Interactive delta visualization
    Given comparison results with metric deltas
    When user hovers over a metric
    Then Tooltip should show: metric name, Run A value, Run B value, delta, significance
    And Clicking metric should highlight related metrics (correlated)
    And Visual indicators (arrows, icons) should show improvement/regression
    And Pass Criteria: Tooltip complete, related highlighted, indicators visible

  Scenario: UW-004 - Filtering and sorting in UI
    Given comparison results with 20 metrics
    When user filters to show only "regressions"
    Then Only metrics with delta < -5% should be displayed
    And Sorting by delta magnitude should work (largest first)
    And Filter should be removable to show all metrics again
    And And filter state should be shown clearly
    And Pass Criteria: Filter applied, sorting works, filter removable, state visible

  Scenario: UW-005 - Drill-down to detailed analysis
    Given a metric showing regression in comparison results
    When user clicks on that metric
    Then Detailed panel should open showing historical trend
    And Scatter plot should show all samples from both runs
    And Statistical summary should be displayed
    And Recommendations should be provided
    And Pass Criteria: Panel opens, trend shown, scatter visible, stats/recommendations present

  Scenario: UW-006 - Export comparison results
    Given comparison results displayed in UI
    When user clicks "Export" button
    Then User should be able to choose format (CSV, PDF, JSON)
    And Export file should be generated successfully
    And Exported data should match displayed results
    And File should be downloadable
    And Pass Criteria: Formats available, file generated, matches display, downloadable

  Scenario: UW-007 - Comparison history tracking
    Given user has compared Run A vs Run B previously
    When user returns to comparison view
    Then Previous comparison should be shown in history
    And User should be able to quickly rerun same comparison
    And Historical comparisons should have timestamps
    And User should be able to delete old comparisons
    And Pass Criteria: History shown, quick rerun available, timestamps present, deletion works

  Scenario: UW-008 - Multi-run comparison mode
    Given runs R1, R2, R3, R4 selected
    When user switches to multi-run comparison
    Then Metrics should be shown across all 4 runs (columns)
    And Trends should be visible across all runs
    And Group statistics (min, max, mean) should be calculated
    And Performance visualization should show evolution
    And Pass Criteria: All runs displayed, trends visible, stats calculated, visualization clear

  # ========================================
  # EDGE CASES (7 tests)
  # ========================================

  Scenario: EC-001 - Comparison of identical runs
    Given Run A and Run B with identical configuration and results
    When comparison is performed
    Then All deltas should be zero
    And Statistical significance should indicate no difference (p-value = 1.0)
    And Message should indicate runs are identical
    And No improvements or regressions should be flagged
    And Pass Criteria: Deltas zero, p-value = 1.0, message clear, nothing flagged

  Scenario: EC-002 - Comparison with missing metrics
    Given Run A with 20 metrics
    And Run B with only 15 metrics (5 missing)
    When comparison is performed
    Then Missing metrics should be noted clearly
    And Comparison should proceed with available metrics
    And Warning should indicate incomplete comparison
    And And recommendations should account for missing data
    And Pass Criteria: Missing noted, comparison proceeds, warning shown, recommendations cautious

  Scenario: EC-003 - Extreme value handling
    Given Run A with normal metrics
    And Run B with one metric showing extreme value (1000x normal)
    When comparison is performed
    Then Extreme value should be flagged as outlier
    And Statistical tests should account for outliers (robust statistics)
    And Visualization should scale properly (log scale if needed)
    And User warning should be issued
    And Pass Criteria: Outlier flagged, stats robust, visualization scaled, warning issued

  Scenario: EC-004 - Division by zero prevention
    Given metric in Run A with value = 0
    And calculation would require division by this value
    When comparison algorithm executes
    Then Division by zero should be prevented
    And Result should be handled gracefully (null, infinity, or special value)
    And Error should be logged and reported
    And And calculation should continue for other metrics
    And Pass Criteria: Division prevented, handled gracefully, logged, others calculated

  Scenario: EC-005 - NaN and Infinity handling
    Given metrics containing NaN or Infinity values
    When comparison attempts to include these
    Then These values should be filtered or flagged
    And Statistical tests should not use NaN/Infinity
    And Visualization should handle these gracefully
    And User should be warned about data quality issues
    And Pass Criteria: Values filtered/flagged, stats valid, visualization OK, warning issued

  Scenario: EC-006 - Very large time gap between runs
    Given Run A executed on 2024-01-01
    And Run B executed on 2026-02-26 (2+ years later)
    When comparison is performed
    Then Comparison should still be valid
    And Time gap should be noted as important context
    And Trend analysis should account for time gap
    And Seasonal factors or external changes should be considered
    And Pass Criteria: Comparison valid, gap noted, trends contextualized, factors considered

  Scenario: EC-007 - Concurrent comparison requests
    Given 10 users simultaneously requesting comparison of different run pairs
    When all requests are processed
    Then All comparisons should complete without interference
    And Results should be accurate for each request
    And Resource usage should be reasonable
    And No data corruption should occur
    And Pass Criteria: All complete, results accurate, resources reasonable, no corruption

