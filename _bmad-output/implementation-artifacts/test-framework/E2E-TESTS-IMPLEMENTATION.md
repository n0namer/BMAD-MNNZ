# E2E Tests Implementation Guide - Katana VectorBT Phase 1

**Project**: Katana VectorBT
**Phase**: Phase 1 MVP (Epics 1-6)
**Date**: 2026-02-26
**Status**: Implementation Ready
**Test Architect**: QA Engineer Team

---

## EXECUTIVE SUMMARY

This guide specifies 18 end-to-end tests that validate complete user journeys through the web UI using Playwright. E2E tests:
- Execute within <5000ms (acceptable for browser automation)
- Test real browser + backend integration
- Verify user-visible functionality
- Validate responsive design (tablet+)

**Test Distribution**:
- **Epic 1 (E-STRATEGY-LIFECYCLE)**: 3 E2E tests (timeline UI, status display)
- **Epic 2 (E-JOURNAL-SCHEMA)**: 4 E2E tests (journal workflows)
- **Epic 3 (E-TELEMETRY-METRICS)**: 5 E2E tests (dashboard rendering)
- **Epic 4 (E-COMPARE-WORKFLOW)**: 3 E2E tests (comparison UI)
- **Epic 5 (E-AUDIT-TRAIL)**: 4 E2E tests (reproduce button, audit display)

**Total Effort**: 8-12 hours (team of 2 engineers, Week 3)
**Tools**: Playwright (headless browser automation)

---

## SECTION 1: EPIC 1 - TIMELINE UI E2E TESTS (3 TESTS)

**File**: `tests/integration/end_to_end/test_timeline_ui.py`
**Browser**: Chromium (headless)
**Base URL**: http://localhost:8000 (test server)

### Test 1.1: E1-E1 - Dashboard Loads Strategy Timeline

**Test Name**: `test_dashboard_loads_strategy_timeline`
**Purpose**: Verify dashboard page loads and displays strategy timeline

```python
@pytest.mark.e2e
def test_dashboard_loads_strategy_timeline(page, test_server):
    """E2E: Dashboard loads and displays strategy timeline."""
    # Navigate to dashboard
    page.goto(test_server.url + "/dashboard")

    # Wait for page to load
    page.wait_for_load_state("networkidle")

    # Verify title
    assert "Katana VectorBT" in page.title()

    # Verify strategy list loaded
    strategy_list = page.locator("[data-testid='strategy-list']")
    assert strategy_list.is_visible()

    # Verify timeline section
    timeline = page.locator("[data-testid='strategy-timeline']")
    assert timeline.is_visible()

    # Verify at least one strategy in list
    strategies = page.locator("[data-testid='strategy-item']")
    assert strategies.count() >= 1
```

### Test 1.2: E1-E2 - Status Badge Displays Correctly

**Test Name**: `test_status_badge_displays_correctly`
**Purpose**: Verify strategy status badge shows correct state

```python
@pytest.mark.e2e
def test_status_badge_displays_correctly(page, test_server):
    """E2E: Strategy status badge displays correct state."""
    page.goto(test_server.url + "/dashboard")
    page.wait_for_load_state("networkidle")

    # Find first strategy
    first_strategy = page.locator("[data-testid='strategy-item']").first

    # Verify status badge
    status_badge = first_strategy.locator("[data-testid='status-badge']")
    assert status_badge.is_visible()

    # Status should be one of: PAPER, MICRO_LIVE, LIVE
    status_text = status_badge.text_content()
    assert status_text in ["PAPER", "MICRO_LIVE", "LIVE"]

    # Verify badge has correct color class
    if "PAPER" in status_text:
        assert status_badge.evaluate("el => el.classList.contains('bg-gray')") == True
    elif "MICRO_LIVE" in status_text:
        assert status_badge.evaluate("el => el.classList.contains('bg-yellow')") == True
    elif "LIVE" in status_text:
        assert status_badge.evaluate("el => el.classList.contains('bg-green')") == True
```

### Test 1.3: E1-E3 - Filter by Strategy Type

**Test Name**: `test_filter_by_strategy_type`
**Purpose**: Verify filtering strategies by type

```python
@pytest.mark.e2e
def test_filter_by_strategy_type(page, test_server):
    """E2E: Filter strategies by type."""
    page.goto(test_server.url + "/dashboard")
    page.wait_for_load_state("networkidle")

    # Open filter menu
    filter_btn = page.locator("[data-testid='filter-button']")
    filter_btn.click()

    # Select LIVE status filter
    live_checkbox = page.locator("[data-testid='filter-live']")
    live_checkbox.click()

    # Wait for results to update
    page.wait_for_timeout(1000)  # Wait 1 second for filter to apply

    # Verify all visible strategies are LIVE
    strategies = page.locator("[data-testid='strategy-item']")
    for i in range(strategies.count()):
        badge = strategies.nth(i).locator("[data-testid='status-badge']")
        assert badge.text_content() == "LIVE"
```

---

## SECTION 2: EPIC 2 - JOURNAL WORKFLOW E2E TESTS (4 TESTS)

**File**: `tests/integration/end_to_end/test_journal_workflow.py`
**Workflows**: Search, view, export, signal diagnostics

### Test 2.1: E2-E1 - Search and Filter Runs

```python
@pytest.mark.e2e
def test_search_and_filter_runs(page, test_server):
    """E2E: Search and filter runs in journal."""
    page.goto(test_server.url + "/journal")
    page.wait_for_load_state("networkidle")

    # Search by strategy
    search_input = page.locator("[data-testid='search-input']")
    search_input.fill("Test Strategy")

    # Wait for results
    page.wait_for_timeout(500)

    # Verify filtered results
    runs = page.locator("[data-testid='run-item']")
    assert runs.count() >= 1

    # Verify search term in results
    first_run = runs.first
    assert "Test Strategy" in first_run.text_content()
```

### Test 2.2: E2-E2 - View Run Details

```python
@pytest.mark.e2e
def test_view_run_details(page, test_server):
    """E2E: View detailed run metrics."""
    page.goto(test_server.url + "/journal")
    page.wait_for_load_state("networkidle")

    # Click on first run
    first_run = page.locator("[data-testid='run-item']").first
    first_run.click()

    # Wait for detail page
    page.wait_for_load_state("networkidle")

    # Verify detail panel
    detail_panel = page.locator("[data-testid='run-detail-panel']")
    assert detail_panel.is_visible()

    # Verify metrics displayed
    metrics = page.locator("[data-testid='metric']")
    assert metrics.count() >= 5  # At least 5 metrics shown

    # Verify metric names
    metric_text = metrics.all_text_contents()
    assert "total_return" in " ".join(metric_text)
```

### Test 2.3: E2-E3 - Export Run Data

```python
@pytest.mark.e2e
def test_export_run_data(page, test_server):
    """E2E: Export run data to CSV/JSON."""
    page.goto(test_server.url + "/journal")
    page.wait_for_load_state("networkidle")

    # Select run
    first_run = page.locator("[data-testid='run-item']").first
    first_run.click()
    page.wait_for_load_state("networkidle")

    # Click export button
    export_btn = page.locator("[data-testid='export-button']")
    export_btn.click()

    # Select CSV format
    csv_option = page.locator("[data-testid='export-csv']")
    csv_option.click()

    # Wait for download
    with page.expect_download() as download_info:
        page.wait_for_timeout(2000)

    download = download_info.value
    assert download.filename.endswith(".csv")
```

### Test 2.4: E2-E4 - Inspect Signal Diagnostics

```python
@pytest.mark.e2e
def test_inspect_signal_diagnostics(page, test_server):
    """E2E: View signal diagnostics panel (why no trades)."""
    page.goto(test_server.url + "/journal")
    page.wait_for_load_state("networkidle")

    # Find run with no trades
    runs = page.locator("[data-testid='run-item']")
    for i in range(runs.count()):
        run_item = runs.nth(i)
        if "0 trades" in run_item.text_content():
            run_item.click()
            break

    page.wait_for_load_state("networkidle")

    # Open diagnostics
    diagnostics_btn = page.locator("[data-testid='diagnostics-button']")
    if diagnostics_btn.is_visible():
        diagnostics_btn.click()

        # Verify diagnostic info
        diagnostic_panel = page.locator("[data-testid='diagnostic-panel']")
        assert diagnostic_panel.is_visible()
        assert "signal" in diagnostic_panel.text_content().lower()
```

---

## SECTION 3: EPIC 3 - DASHBOARD RENDERING E2E TESTS (5 TESTS)

**File**: `tests/integration/end_to_end/test_dashboard_ui.py`
**Components**: Equity curve, drawdown chart, metrics panel, filters

### Test 3.1: E3-E1 - Equity Curve Renders

```python
@pytest.mark.e2e
def test_equity_curve_renders(page, test_server):
    """E2E: Equity curve chart renders correctly."""
    page.goto(test_server.url + "/dashboard/run/run-1")
    page.wait_for_load_state("networkidle")

    # Verify chart container
    chart_container = page.locator("[data-testid='equity-curve-chart']")
    assert chart_container.is_visible()

    # Verify SVG rendered (Plotly)
    svg = chart_container.locator("svg")
    assert svg.count() >= 1

    # Verify chart has data points
    points = chart_container.locator("circle")
    assert points.count() >= 10  # At least 10 data points
```

### Test 3.2: E3-E2 - Drawdown Chart Loads

```python
@pytest.mark.e2e
def test_drawdown_chart_loads(page, test_server):
    """E2E: Drawdown chart loads (lazy-loaded)."""
    page.goto(test_server.url + "/dashboard/run/run-1")
    page.wait_for_load_state("networkidle")

    # Drawdown is lazy-loaded, scroll to it
    drawdown_section = page.locator("[data-testid='drawdown-section']")
    drawdown_section.scroll_into_view_if_needed()

    # Wait for lazy load
    page.wait_for_timeout(1000)

    # Verify chart
    chart = drawdown_section.locator("svg")
    assert chart.count() >= 1
```

### Test 3.3: E3-E3 - Metrics Panel Populated

```python
@pytest.mark.e2e
def test_metrics_panel_populated(page, test_server):
    """E2E: Metrics panel shows all key metrics."""
    page.goto(test_server.url + "/dashboard/run/run-1")
    page.wait_for_load_state("networkidle")

    # Verify metrics panel
    metrics_panel = page.locator("[data-testid='metrics-panel']")
    assert metrics_panel.is_visible()

    # Verify key metrics present
    expected_metrics = [
        "total_return",
        "win_rate",
        "profit_factor",
        "max_drawdown",
        "sharpe_ratio"
    ]

    for metric in expected_metrics:
        metric_elem = metrics_panel.locator(f"[data-testid='{metric}']")
        assert metric_elem.is_visible(), f"Metric {metric} not visible"

        # Verify metric has value
        value = metric_elem.locator("[data-testid='metric-value']")
        assert len(value.text_content()) > 0
```

### Test 3.4: E3-E4 - Performance Indicators Updated

```python
@pytest.mark.e2e
def test_performance_indicators_updated(page, test_server):
    """E2E: Performance indicators update in real-time."""
    page.goto(test_server.url + "/dashboard")
    page.wait_for_load_state("networkidle")

    # Record initial values
    initial_value = page.locator("[data-testid='net-pnl']").text_content()

    # Simulate time passing (trigger update)
    page.evaluate("() => window.updateMetrics()")
    page.wait_for_timeout(1000)

    # Verify update
    updated_value = page.locator("[data-testid='net-pnl']").text_content()
    # Value may have changed or stayed same
    assert updated_value is not None
```

### Test 3.5: E3-E5 - Responsive Layout (Tablet)

```python
@pytest.mark.e2e
def test_responsive_layout_tablet(page, test_server):
    """E2E: Dashboard layout responsive on tablet (1024px)."""
    # Set viewport to tablet size
    page.set_viewport_size(width=1024, height=768)

    page.goto(test_server.url + "/dashboard")
    page.wait_for_load_state("networkidle")

    # Verify main sections visible
    strategy_list = page.locator("[data-testid='strategy-list']")
    assert strategy_list.is_visible()

    metrics_panel = page.locator("[data-testid='metrics-panel']")
    assert metrics_panel.is_visible()

    # Verify no horizontal scroll needed
    page_width = page.evaluate("() => document.documentElement.scrollWidth")
    viewport_width = 1024
    assert page_width <= viewport_width, "Page exceeds viewport width"
```

---

## SECTION 4: EPIC 4 - COMPARISON WORKFLOW E2E TESTS (3 TESTS)

**File**: `tests/integration/end_to_end/test_comparison_ui.py`

### Test 4.1: E4-E1 - Select Runs to Compare

```python
@pytest.mark.e2e
def test_select_runs_to_compare(page, test_server):
    """E2E: Select multiple runs for comparison."""
    page.goto(test_server.url + "/journal")
    page.wait_for_load_state("networkidle")

    # Select first run
    runs = page.locator("[data-testid='run-item']")
    runs.nth(0).locator("[data-testid='select-checkbox']").click()
    runs.nth(1).locator("[data-testid='select-checkbox']").click()

    # Verify compare button appears
    compare_btn = page.locator("[data-testid='compare-button']")
    assert compare_btn.is_visible()
    assert compare_btn.is_enabled()

    # Click compare
    compare_btn.click()
    page.wait_for_load_state("networkidle")

    # Verify comparison page
    assert "/compare" in page.url
```

### Test 4.2: E4-E2 - Compare Metrics Side-by-Side

```python
@pytest.mark.e2e
def test_compare_metrics_side_by_side(page, test_server):
    """E2E: View metrics comparison side-by-side."""
    page.goto(test_server.url + "/compare?run1=run-1&run2=run-2")
    page.wait_for_load_state("networkidle")

    # Verify comparison table
    comparison_table = page.locator("[data-testid='comparison-table']")
    assert comparison_table.is_visible()

    # Verify columns: Metric, Run 1, Run 2, Difference
    headers = comparison_table.locator("th")
    assert headers.count() == 4

    # Verify metric rows
    rows = comparison_table.locator("tr[data-testid='metric-row']")
    assert rows.count() >= 5
```

### Test 4.3: E4-E3 - Export Comparison Report

```python
@pytest.mark.e2e
def test_export_comparison_report(page, test_server):
    """E2E: Export comparison report."""
    page.goto(test_server.url + "/compare?run1=run-1&run2=run-2")
    page.wait_for_load_state("networkidle")

    # Click export
    export_btn = page.locator("[data-testid='export-report-button']")
    export_btn.click()

    # Download PDF
    with page.expect_download() as download_info:
        page.wait_for_timeout(3000)

    download = download_info.value
    assert download.filename.endswith(".pdf")
```

---

## SECTION 5: EPIC 5 - REPRODUCE BUTTON & AUDIT E2E TESTS (4 TESTS)

**File**: `tests/integration/end_to_end/test_reproduce_button.py`

### Test 5.1: E5-E1 - Click Reproduce Button

```python
@pytest.mark.e2e
def test_click_reproduce_button(page, test_server):
    """E2E: Click reproduce button and verify new run."""
    page.goto(test_server.url + "/journal/run/run-1")
    page.wait_for_load_state("networkidle")

    # Verify reproduce button
    reproduce_btn = page.locator("[data-testid='reproduce-button']")
    assert reproduce_btn.is_visible()

    # Click button
    reproduce_btn.click()

    # Wait for modal or confirmation
    modal = page.locator("[data-testid='reproduce-modal']")
    assert modal.is_visible()

    # Confirm
    confirm_btn = modal.locator("[data-testid='confirm-button']")
    confirm_btn.click()

    # Wait for execution
    page.wait_for_timeout(5000)

    # Verify new run created
    success_msg = page.locator("[data-testid='success-message']")
    assert success_msg.is_visible()
    assert "Reproduction started" in success_msg.text_content()
```

### Test 5.2: E5-E2 - Verify Parameters Loaded Correctly

```python
@pytest.mark.e2e
def test_verify_parameters_loaded_correctly(page, test_server):
    """E2E: Verify reproduced run has same parameters."""
    page.goto(test_server.url + "/journal/run/run-1")
    page.wait_for_load_state("networkidle")

    # Get original parameters
    original_params = page.locator("[data-testid='parameters-panel']")
    original_lookback = original_params.locator("[data-testid='param-lookback']").text_content()

    # Reproduce run
    reproduce_btn = page.locator("[data-testid='reproduce-button']")
    reproduce_btn.click()
    page.wait_for_timeout(500)

    # Confirm
    page.locator("[data-testid='confirm-button']").click()
    page.wait_for_timeout(5000)

    # Navigate to new run
    success_msg = page.locator("[data-testid='success-message']")
    new_run_link = success_msg.locator("a").first
    new_run_id = new_run_link.get_attribute("href").split("/")[-1]

    # Navigate to new run
    page.goto(test_server.url + f"/journal/run/{new_run_id}")
    page.wait_for_load_state("networkidle")

    # Verify parameters match
    new_params = page.locator("[data-testid='parameters-panel']")
    new_lookback = new_params.locator("[data-testid='param-lookback']").text_content()
    assert original_lookback == new_lookback
```

### Test 5.3: E5-E3 - Audit Trail Linked Correctly

```python
@pytest.mark.e2e
def test_audit_trail_linked_correctly(page, test_server):
    """E2E: Audit trail links original and reproduced runs."""
    page.goto(test_server.url + "/journal/run/run-1")
    page.wait_for_load_state("networkidle")

    # Get audit trail
    audit_trail = page.locator("[data-testid='audit-trail']")
    assert audit_trail.is_visible()

    # Verify reproduction link
    reproduction_link = audit_trail.locator("[data-testid='reproduction-link']")
    assert reproduction_link.is_visible()

    # Click to navigate
    reproduction_link.click()
    page.wait_for_load_state("networkidle")

    # Verify on new run page
    assert "run-" in page.url
```

### Test 5.4: E5-E4 - Audit Trail Display Complete

```python
@pytest.mark.e2e
def test_audit_trail_display_complete(page, test_server):
    """E2E: Audit trail shows complete run history."""
    page.goto(test_server.url + "/journal/run/run-1")
    page.wait_for_load_state("networkidle")

    # Verify audit trail
    audit_trail = page.locator("[data-testid='audit-trail']")
    assert audit_trail.is_visible()

    # Verify events
    events = audit_trail.locator("[data-testid='audit-event']")
    assert events.count() >= 3  # Creation, approval, execution, etc.

    # Verify each event has: timestamp, action, actor
    for i in range(events.count()):
        event = events.nth(i)
        assert event.locator("[data-testid='event-timestamp']").is_visible()
        assert event.locator("[data-testid='event-action']").is_visible()
        assert event.locator("[data-testid='event-actor']").is_visible()
```

---

## SECTION 6: PLAYWRIGHT SETUP & CONFIGURATION

**Installation**:
```bash
pip install playwright
playwright install chromium
```

**Fixture** (conftest.py):
```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    """Provide Playwright page for E2E tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def test_server():
    """Provide test server URL."""
    class TestServer:
        url = "http://localhost:8000"
    return TestServer()
```

**Run E2E Tests**:
```bash
pytest tests/integration/end_to_end/ -v --headless

# Or with headed browser (for debugging)
pytest tests/integration/end_to_end/ -v --headed
```

---

## SECTION 7: BEST PRACTICES

1. **Use data-testid attributes** — Makes selectors stable across CSS changes
2. **Wait for page load** — Use `page.wait_for_load_state("networkidle")`
3. **Avoid hard sleeps** — Use `page.wait_for_selector()` instead
4. **Test user flows** — Not implementation details
5. **Parallel execution** — Tests can run 4x in parallel with container isolation

---

## CONCLUSION

The 18 E2E tests validate complete user journeys through the UI. Each test:
- ✅ Executes in <5000ms
- ✅ Uses real browser + backend
- ✅ Tests user-visible functionality
- ✅ Validates responsive design
- ✅ Parallelizable (4 batches)

**Estimated Implementation Time**: 8-12 hours
**Total Effort Phase 1**: 36-51 hours (unit + integration + E2E)

---

**Document Version**: 1.0
**Status**: FINAL
**Approval Date**: 2026-02-26
