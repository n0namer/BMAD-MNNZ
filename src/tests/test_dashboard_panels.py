"""
UX-001: Live Monitoring Dashboard - Panel Component Tests

ATDD Test Suite for dashboard panel components and display logic.
Tests are intentionally failing (red) before implementation (green).

Story: UX-001 - Live Monitoring Dashboard
Acceptance Criteria:
  - AC1-AC4: Position panel display
  - AC5-AC8: Risk metrics display
  - AC9-AC12: Performance analytics display
  - AC13-AC18: Real-time update callbacks

Test Execution Order:
  1. test_position_panel_renders - Panel renders without errors
  2. test_position_panel_displays_symbols - Shows all open positions
  3. test_position_panel_shows_size_and_pnl - Displays size, P&L, return %
  4. test_position_panel_color_coding - Green for profit, red for loss
  5. test_risk_panel_renders - Risk panel displays without errors
  6. test_risk_panel_shows_metrics - Current Sharpe, max DD, leverage
  7. test_risk_panel_updates_on_data_change - Updates when data changes
  8. test_risk_panel_alerts_on_threshold - Shows warnings for limits
  9. test_performance_panel_renders - Performance panel displays
  10. test_performance_panel_equity_curve - Plots equity curve
  11. test_performance_panel_period_returns - Shows daily/weekly/monthly
  12. test_performance_panel_drawdown_chart - Displays max drawdown chart
  13. test_callbacks_on_position_update - Calls callback on position change
  14. test_callbacks_on_trade_executed - Calls callback on new trade
  15. test_callbacks_on_risk_alert - Calls callback on risk threshold breach
  16. test_callbacks_data_consistency - Multiple callbacks don't corrupt state
  17. test_callbacks_error_handling - Callback errors don't crash dashboard
  18. test_callbacks_performance_monitoring - Callbacks complete quickly

All tests SHOULD FAIL until implementation is complete.
"""

import pytest
from datetime import datetime, timedelta
from typing import Dict, Any, List, Callable
from unittest.mock import Mock, MagicMock, patch, call
from dataclasses import dataclass


@dataclass
class DashboardPosition:
    """Position data for dashboard."""
    symbol: str
    quantity: int
    entry_price: float
    current_price: float
    pnl: float
    return_pct: float
    allocation_pct: float


@dataclass
class DashboardMetrics:
    """Risk and performance metrics."""
    sharpe_ratio: float
    max_drawdown: float
    current_leverage: float
    win_rate: float
    profit_factor: float
    total_return: float


@dataclass
class DashboardTrade:
    """Trade execution record."""
    symbol: str
    side: str
    entry_time: datetime
    entry_price: float
    exit_time: datetime
    exit_price: float
    pnl: float
    return_pct: float


class TestDashboardPanels:
    """Test suite for UX-001 Live Monitoring Dashboard panels.

    BDD Scenario: As a trader, I need live position and risk monitoring
    so that I can react quickly to market changes and manage risk effectively.

    Feature: Live Monitoring Dashboard
      - Position panel shows all open positions with current P&L
      - Risk metrics display current risk exposure and performance
      - Performance analytics show equity curve and returns
      - Real-time callbacks trigger on market events
    """

    @pytest.fixture
    def sample_positions(self) -> Dict[str, DashboardPosition]:
        """Fixture: Sample open positions."""
        return {
            'AAPL': DashboardPosition(
                symbol='AAPL',
                quantity=100,
                entry_price=150.0,
                current_price=155.0,
                pnl=500.0,
                return_pct=0.0333,
                allocation_pct=0.30
            ),
            'MSFT': DashboardPosition(
                symbol='MSFT',
                quantity=50,
                entry_price=300.0,
                current_price=295.0,
                pnl=-250.0,
                return_pct=-0.0167,
                allocation_pct=0.25
            ),
            'GOOGL': DashboardPosition(
                symbol='GOOGL',
                quantity=30,
                entry_price=140.0,
                current_price=145.0,
                pnl=150.0,
                return_pct=0.0357,
                allocation_pct=0.20
            ),
        }

    @pytest.fixture
    def sample_metrics(self) -> DashboardMetrics:
        """Fixture: Sample metrics."""
        return DashboardMetrics(
            sharpe_ratio=1.5,
            max_drawdown=0.08,
            current_leverage=1.75,
            win_rate=0.65,
            profit_factor=1.8,
            total_return=0.12
        )

    @pytest.fixture
    def sample_trades(self) -> List[DashboardTrade]:
        """Fixture: Sample trade history."""
        base_time = datetime.now()
        return [
            DashboardTrade(
                symbol='AAPL',
                side='long',
                entry_time=base_time - timedelta(days=5),
                entry_price=150.0,
                exit_time=base_time - timedelta(days=4),
                exit_price=155.0,
                pnl=500.0,
                return_pct=0.0333
            ),
            DashboardTrade(
                symbol='MSFT',
                side='long',
                entry_time=base_time - timedelta(days=3),
                entry_price=300.0,
                exit_time=base_time - timedelta(days=2),
                exit_price=305.0,
                pnl=250.0,
                return_pct=0.0167
            ),
        ]

    # ============================================================================
    # AC1-AC4: Position Panel Display
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_panel
    def test_position_panel_renders(self, sample_positions):
        """AC1: Position panel renders without errors.

        GIVEN: Dashboard with open positions
        WHEN: Rendering position panel
        THEN: Panel should display without errors
              - Component renders
              - No missing data warnings
              - Responsive layout

        Expected Output:
            - Panel visible
            - All sections populated
            - No console errors

        Status: FAILING (component not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        panel = PositionPanel(positions=sample_positions)

        # WHEN: Render panel
        rendered = panel.render()

        # THEN: Should render without errors
        assert rendered is not None, "Panel should render"
        assert isinstance(rendered, str), "Should return HTML/JSX string"
        assert len(rendered) > 100, "Rendered output should be substantive"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_panel
    def test_position_panel_displays_symbols(self, sample_positions):
        """AC2: Position panel displays all open position symbols.

        GIVEN: Portfolio with multiple positions
        WHEN: Rendering position panel
        THEN: All symbols should be visible
              - AAPL, MSFT, GOOGL all present
              - Sorted consistently
              - Updated in real-time

        Expected Output:
            - All 3 symbols displayed
            - No missing positions
            - Clear labeling

        Status: FAILING (symbol display not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        panel = PositionPanel(positions=sample_positions)
        rendered = panel.render()

        # THEN: All symbols should be in rendered output
        for symbol in sample_positions.keys():
            assert symbol in rendered, f"Symbol {symbol} should be displayed"

        # THEN: Should show all positions
        symbol_count = sum(
            rendered.count(symbol) for symbol in sample_positions.keys()
        )
        assert symbol_count >= len(sample_positions), \
            "All positions should be displayed"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_panel
    def test_position_panel_shows_size_and_pnl(self, sample_positions):
        """AC3: Position panel displays size, P&L, and return percentage.

        GIVEN: Open positions with current prices
        WHEN: Displaying position details
        THEN: Each position should show:
              - Quantity held
              - Entry price
              - Current price
              - P&L ($)
              - Return percentage (%)
              - Allocation %

        Expected Output:
            AAPL: 100 @ $150 → $155 | +$500 (+3.33%) | 30% alloc
            MSFT: 50 @ $300 → $295 | -$250 (-1.67%) | 25% alloc
            GOOGL: 30 @ $140 → $145 | +$150 (+3.57%) | 20% alloc

        Status: FAILING (detailed display not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        panel = PositionPanel(positions=sample_positions)
        panel_data = panel.get_position_details()

        # THEN: Should include all required fields
        for symbol, position in sample_positions.items():
            details = panel_data[symbol]

            assert details['quantity'] == position.quantity
            assert details['entry_price'] == position.entry_price
            assert details['current_price'] == position.current_price
            assert details['pnl'] == position.pnl
            assert details['return_pct'] == position.return_pct
            assert details['allocation_pct'] == position.allocation_pct

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_panel
    def test_position_panel_color_coding(self, sample_positions):
        """AC4: Position panel uses color coding for P&L.

        GIVEN: Positions with varying P&L
        WHEN: Rendering position colors
        THEN: Colors should indicate:
              - Green for positive P&L (profit)
              - Red for negative P&L (loss)
              - Gray/neutral for break-even

        Test Cases:
            - AAPL: +$500 → Green
            - MSFT: -$250 → Red
            - GOOGL: +$150 → Green

        Expected Output:
            - CSS classes or style attributes
            - color: green/red based on PnL sign
            - Consistent across all positions

        Status: FAILING (color coding not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        panel = PositionPanel(positions=sample_positions)
        colors = panel.get_position_colors()

        # THEN: Positive P&L should be green
        assert colors['AAPL'] == 'green', "Positive P&L should be green"
        assert colors['GOOGL'] == 'green', "Positive P&L should be green"

        # THEN: Negative P&L should be red
        assert colors['MSFT'] == 'red', "Negative P&L should be red"

    # ============================================================================
    # AC5-AC8: Risk Metrics Display
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_risk
    def test_risk_panel_renders(self, sample_metrics):
        """AC5: Risk panel renders without errors.

        GIVEN: Dashboard with current metrics
        WHEN: Rendering risk panel
        THEN: Panel should display
              - Sharpe Ratio
              - Max Drawdown
              - Current Leverage
              - Win Rate

        Expected Output:
            - Risk panel visible
            - All metrics populated
            - Updated values shown

        Status: FAILING (risk panel not implemented)
        """
        from katana.dashboard.components.panels import RiskPanel

        panel = RiskPanel(metrics=sample_metrics)

        # WHEN: Render
        rendered = panel.render()

        # THEN: Should render
        assert rendered is not None, "Risk panel should render"
        assert isinstance(rendered, str)
        assert len(rendered) > 100

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_risk
    def test_risk_panel_shows_metrics(self, sample_metrics):
        """AC6: Risk panel displays key risk metrics.

        GIVEN: Current portfolio metrics
        WHEN: Displaying risk panel
        THEN: Should show:
              - Sharpe Ratio (1.5)
              - Max Drawdown (8%)
              - Current Leverage (1.75x)
              - Win Rate (65%)
              - Profit Factor (1.8)

        Expected Output:
            Sharpe: 1.50
            Max DD: 8.00%
            Leverage: 1.75x
            Win Rate: 65%
            PF: 1.80

        Status: FAILING (metric display not implemented)
        """
        from katana.dashboard.components.panels import RiskPanel

        panel = RiskPanel(metrics=sample_metrics)
        metric_display = panel.get_metric_values()

        # THEN: All metrics should be accessible and formatted
        assert metric_display['sharpe_ratio'] == 1.5
        assert metric_display['max_drawdown'] == 0.08
        assert metric_display['current_leverage'] == 1.75
        assert metric_display['win_rate'] == 0.65
        assert metric_display['profit_factor'] == 1.8

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_risk
    def test_risk_panel_updates_on_data_change(self, sample_metrics):
        """AC7: Risk panel updates when data changes.

        GIVEN: Risk panel displaying metrics
        WHEN: Metrics update (new trade executed)
        THEN: Panel should refresh immediately
              - Sharpe Ratio updates
              - Leverage recalculated
              - No stale data shown

        Expected Output:
            - Before: Sharpe 1.50
            - After: Sharpe 1.55 (updates immediately)
            - View reflects current state

        Status: FAILING (update mechanism not implemented)
        """
        from katana.dashboard.components.panels import RiskPanel

        panel = RiskPanel(metrics=sample_metrics)

        # WHEN: Metrics update
        updated_metrics = DashboardMetrics(
            sharpe_ratio=1.55,  # Changed
            max_drawdown=0.08,
            current_leverage=1.70,  # Changed
            win_rate=0.65,
            profit_factor=1.8,
            total_return=0.12
        )
        panel.update_metrics(updated_metrics)

        # THEN: Displayed values should reflect updates
        metric_display = panel.get_metric_values()
        assert metric_display['sharpe_ratio'] == 1.55, "Should update Sharpe"
        assert metric_display['current_leverage'] == 1.70, "Should update leverage"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_risk
    def test_risk_panel_alerts_on_threshold(self, sample_metrics):
        """AC8: Risk panel alerts when metrics breach thresholds.

        GIVEN: Risk panel with alert thresholds
        WHEN: Metrics exceed safe limits
        THEN: Alerts should show:
              - Leverage > 2.5x: Alert
              - Max DD > 20%: Alert
              - Sharpe < 0.5: Alert
              - Win Rate < 40%: Alert

        Expected Output:
            - Alert icon visible
            - Alert message displayed
            - Color change (orange/red)
            - Sound/notification (optional)

        Status: FAILING (alert logic not implemented)
        """
        from katana.dashboard.components.panels import RiskPanel

        # Create over-leveraged metrics
        bad_metrics = DashboardMetrics(
            sharpe_ratio=0.3,  # Below threshold
            max_drawdown=0.25,  # Above threshold
            current_leverage=2.8,  # Above threshold
            win_rate=0.35,  # Below threshold
            profit_factor=1.1,
            total_return=-0.05
        )

        panel = RiskPanel(metrics=bad_metrics)
        alerts = panel.get_alerts()

        # THEN: Should generate alerts for violations
        assert len(alerts) > 0, "Should have alerts for threshold breaches"

        alert_types = [a['type'] for a in alerts]
        assert 'leverage' in alert_types, "Should alert on high leverage"
        assert 'drawdown' in alert_types, "Should alert on high drawdown"
        assert 'sharpe' in alert_types, "Should alert on low Sharpe"
        assert 'win_rate' in alert_types, "Should alert on low win rate"

    # ============================================================================
    # AC9-AC12: Performance Analytics Display
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_performance
    def test_performance_panel_renders(self):
        """AC9: Performance panel renders without errors.

        GIVEN: Dashboard with performance data
        WHEN: Rendering performance panel
        THEN: Panel should display
              - Charts
              - Statistics
              - Time period selector

        Expected Output:
            - Performance panel visible
            - Chart area populated
            - Controls available

        Status: FAILING (performance panel not implemented)
        """
        from katana.dashboard.components.panels import PerformancePanel

        # Create mock equity curve
        equity_curve = [100000 + i * 500 for i in range(30)]

        panel = PerformancePanel(equity_curve=equity_curve)

        # WHEN: Render
        rendered = panel.render()

        # THEN: Should render
        assert rendered is not None
        assert isinstance(rendered, str)
        assert len(rendered) > 200

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_performance
    def test_performance_panel_equity_curve(self):
        """AC10: Performance panel displays equity curve.

        GIVEN: Historical equity values
        WHEN: Displaying equity curve
        THEN: Chart should show:
              - Starting capital: $100,000
              - Current capital: $115,000 (+15%)
              - Smooth curve through time
              - Interactive tooltip on hover

        Expected Output:
            - Line chart with equity progression
            - X-axis: Time (days/weeks/months)
            - Y-axis: Equity ($)
            - Peak and valley marked

        Status: FAILING (chart not implemented)
        """
        from katana.dashboard.components.panels import PerformancePanel

        # Create realistic equity curve
        equity_curve = [100000]
        for i in range(29):
            # Simulate returns with some volatility
            daily_return = 0.0005 + (i % 7) * 0.0002
            equity_curve.append(equity_curve[-1] * (1 + daily_return))

        panel = PerformancePanel(equity_curve=equity_curve)
        chart_data = panel.get_equity_curve_data()

        # THEN: Chart data should be formatted for plotting
        assert 'values' in chart_data
        assert 'dates' in chart_data
        assert len(chart_data['values']) == len(equity_curve)

        # THEN: Starting and ending values should match
        assert chart_data['values'][0] == 100000
        assert chart_data['values'][-1] > 100000

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_performance
    def test_performance_panel_period_returns(self):
        """AC11: Performance panel shows returns by period.

        GIVEN: Trade history
        WHEN: Calculating period returns
        THEN: Should show:
              - Daily returns
              - Weekly returns
              - Monthly returns
              - YTD returns

        Expected Output:
            Today: +0.50%
            Week: +2.15%
            Month: +8.30%
            YTD: +12.00%

        Status: FAILING (period calculation not implemented)
        """
        from katana.dashboard.components.panels import PerformancePanel

        # Create equity curve spanning multiple periods
        equity_curve = [100000]
        for i in range(30):  # 30 days
            equity_curve.append(equity_curve[-1] * 1.004)  # 0.4% daily

        panel = PerformancePanel(equity_curve=equity_curve)
        returns = panel.get_period_returns()

        # THEN: Should have all periods
        assert 'daily' in returns
        assert 'weekly' in returns
        assert 'monthly' in returns

        # THEN: Returns should be positive (our curve goes up)
        assert returns['daily'] > 0
        assert returns['weekly'] > 0
        assert returns['monthly'] > 0

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_performance
    def test_performance_panel_drawdown_chart(self, sample_trades):
        """AC12: Performance panel displays drawdown chart.

        GIVEN: Equity curve with periods of drawdown
        WHEN: Calculating drawdown
        THEN: Should show:
              - Running maximum
              - Drawdown from peak
              - Drawdown as % and $
              - Time to recovery

        Expected Output:
            Max DD: 8% from $115,000 peak
            Time to recovery: 5 days
            Duration: 5 trades

        Status: FAILING (drawdown chart not implemented)
        """
        from katana.dashboard.components.panels import PerformancePanel

        # Create equity curve with a drawdown
        equity_curve = [100000]
        for i in range(10):
            equity_curve.append(equity_curve[-1] * 1.01)  # Up 1%
        for i in range(5):
            equity_curve.append(equity_curve[-1] * 0.97)  # Down 3%
        for i in range(10):
            equity_curve.append(equity_curve[-1] * 1.01)  # Back up

        panel = PerformancePanel(equity_curve=equity_curve)
        dd_data = panel.get_drawdown_data()

        # THEN: Should calculate drawdown metrics
        assert 'drawdown' in dd_data  # Percent
        assert 'max_drawdown' in dd_data
        assert 'recovery_date' in dd_data

        # THEN: Max drawdown should be reasonable
        assert dd_data['max_drawdown'] > 0
        assert dd_data['max_drawdown'] < 0.20  # Less than 20%

    # ============================================================================
    # AC13-AC18: Real-time Update Callbacks
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_on_position_update(self, sample_positions):
        """AC13: Dashboard triggers callback on position update.

        GIVEN: Position panel with callback registered
        WHEN: Position is updated (price change)
        THEN: Callback should be called with:
              - Updated position data
              - Change details (price, P&L change)
              - Timestamp

        Expected Output:
            callback_called: True
            callback_data: {symbol: 'AAPL', new_price: 155.5, ...}

        Status: FAILING (callback mechanism not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        callback_mock = Mock()

        panel = PositionPanel(
            positions=sample_positions,
            on_position_update=callback_mock
        )

        # WHEN: Position updates
        updated_position = DashboardPosition(
            symbol='AAPL',
            quantity=100,
            entry_price=150.0,
            current_price=156.0,  # Price changed
            pnl=600.0,
            return_pct=0.04,
            allocation_pct=0.30
        )

        panel.update_position(updated_position)

        # THEN: Callback should be called
        callback_mock.assert_called_once()

        # THEN: Callback data should include position info
        call_args = callback_mock.call_args
        assert call_args is not None
        assert call_args[0][0]['symbol'] == 'AAPL'
        assert call_args[0][0]['current_price'] == 156.0

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_on_trade_executed(self):
        """AC14: Dashboard triggers callback on trade execution.

        GIVEN: Dashboard monitoring trades
        WHEN: Trade is executed
        THEN: Callback should be called with:
              - Trade details (symbol, side, entry, exit)
              - P&L result
              - Return percentage
              - Execution timestamp

        Expected Output:
            callback: on_trade_executed({
                symbol: 'AAPL',
                side: 'long',
                entry_price: 150,
                exit_price: 155,
                pnl: 500,
                ...
            })

        Status: FAILING (trade callback not implemented)
        """
        from katana.dashboard.components.panels import PerformancePanel

        callback_mock = Mock()

        panel = PerformancePanel(
            equity_curve=[100000],
            on_trade_executed=callback_mock
        )

        # WHEN: Execute a trade
        trade = DashboardTrade(
            symbol='AAPL',
            side='long',
            entry_time=datetime.now() - timedelta(hours=1),
            entry_price=150.0,
            exit_time=datetime.now(),
            exit_price=155.0,
            pnl=500.0,
            return_pct=0.0333
        )

        panel.record_trade(trade)

        # THEN: Callback should be called
        callback_mock.assert_called_once()

        # THEN: Should include trade details
        call_args = callback_mock.call_args[0][0]
        assert call_args['symbol'] == 'AAPL'
        assert call_args['pnl'] == 500.0
        assert call_args['return_pct'] == 0.0333

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_on_risk_alert(self, sample_metrics):
        """AC15: Dashboard triggers callback on risk threshold breach.

        GIVEN: Risk panel with alert thresholds
        WHEN: Metric exceeds threshold
        THEN: Callback should be called with:
              - Alert type (leverage, drawdown, sharpe, etc.)
              - Alert level (warning, critical)
              - Current value
              - Threshold value
              - Recommended action

        Expected Output:
            on_risk_alert({
                type: 'leverage',
                level: 'warning',
                current_value: 2.1,
                threshold: 2.0,
                recommendation: 'Reduce positions by 5%'
            })

        Status: FAILING (risk alert callback not implemented)
        """
        from katana.dashboard.components.panels import RiskPanel

        callback_mock = Mock()

        panel = RiskPanel(
            metrics=sample_metrics,
            on_risk_alert=callback_mock
        )

        # WHEN: Metrics exceed threshold
        bad_metrics = DashboardMetrics(
            sharpe_ratio=0.3,
            max_drawdown=0.25,
            current_leverage=2.6,  # Exceeds 2.5x threshold
            win_rate=0.35,
            profit_factor=1.1,
            total_return=-0.05
        )

        panel.update_metrics(bad_metrics)

        # THEN: Callback should be called for each alert
        assert callback_mock.called, "Alert callback should be called"

        # THEN: Should include alert details
        for call_obj in callback_mock.call_args_list:
            alert_data = call_obj[0][0]
            assert 'type' in alert_data
            assert 'level' in alert_data
            assert 'current_value' in alert_data
            assert 'threshold' in alert_data

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_data_consistency(self, sample_positions):
        """AC16: Multiple callbacks don't corrupt data consistency.

        GIVEN: Panel with multiple callbacks registered
        WHEN: Multiple updates happen quickly
        THEN: Data should remain consistent
              - No race conditions
              - No lost updates
              - Callbacks execute in order

        Expected Output:
            - All callbacks executed
            - Final state is consistent
            - No data corruption

        Status: FAILING (concurrency handling not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        callback1 = Mock()
        callback2 = Mock()
        callback3 = Mock()

        panel = PositionPanel(
            positions=sample_positions,
            on_position_update=callback1
        )

        panel.register_callback('on_position_update', callback2)
        panel.register_callback('on_position_update', callback3)

        # WHEN: Multiple updates happen
        for i in range(5):
            updated = DashboardPosition(
                symbol='AAPL',
                quantity=100,
                entry_price=150.0,
                current_price=155.0 + i,
                pnl=500.0 + i * 100,
                return_pct=0.0333 + i * 0.001,
                allocation_pct=0.30
            )
            panel.update_position(updated)

        # THEN: All callbacks should be called
        assert callback1.call_count == 5
        assert callback2.call_count == 5
        assert callback3.call_count == 5

        # THEN: Final position should be consistent
        final_position = panel.get_position('AAPL')
        assert final_position.current_price == 159.0

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_error_handling(self, sample_positions):
        """AC17: Callback errors don't crash dashboard.

        GIVEN: Callback that raises an exception
        WHEN: Callback is triggered
        THEN: Dashboard should:
              - Catch exception
              - Log error
              - Continue processing
              - Call other callbacks

        Expected Output:
            - Exception logged
            - Other callbacks still called
            - Dashboard still responsive

        Status: FAILING (error handling not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel

        def broken_callback(data):
            raise ValueError("Callback error!")

        good_callback = Mock()

        panel = PositionPanel(positions=sample_positions)
        panel.register_callback('on_position_update', broken_callback)
        panel.register_callback('on_position_update', good_callback)

        # WHEN: Update triggers callbacks
        updated = DashboardPosition(
            symbol='AAPL',
            quantity=100,
            entry_price=150.0,
            current_price=156.0,
            pnl=600.0,
            return_pct=0.04,
            allocation_pct=0.30
        )

        # Should not raise even though callback errors
        panel.update_position(updated)

        # THEN: Good callback should still be called
        good_callback.assert_called_once()

        # THEN: Should have logged error
        error_logs = panel.get_error_logs()
        assert len(error_logs) > 0

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.dashboard_callbacks
    def test_callbacks_performance_monitoring(self, sample_positions):
        """AC18: Callbacks complete quickly (performance monitoring).

        GIVEN: Dashboard with callbacks
        WHEN: Updates are processed
        THEN: Callbacks should complete within time limit:
              - Per callback: < 50ms
              - All callbacks: < 200ms
              - Dashboard remains responsive

        Expected Output:
            - Update latency: < 50ms per callback
            - No UI freezing
            - Smooth animations

        Status: FAILING (performance monitoring not implemented)
        """
        from katana.dashboard.components.panels import PositionPanel
        import time

        callback_times = []

        def tracked_callback(data):
            # Simulate some work
            time.sleep(0.01)
            callback_times.append(time.time())

        panel = PositionPanel(positions=sample_positions)
        panel.register_callback('on_position_update', tracked_callback)

        # WHEN: Process multiple updates
        start_time = time.time()

        for i in range(10):
            updated = DashboardPosition(
                symbol='AAPL',
                quantity=100,
                entry_price=150.0,
                current_price=155.0 + i * 0.1,
                pnl=500.0,
                return_pct=0.0333,
                allocation_pct=0.30
            )
            panel.update_position(updated)

        total_time = time.time() - start_time

        # THEN: Should complete quickly
        assert total_time < 0.5, f"Updates took {total_time}s, should be < 0.5s"

        # THEN: Callbacks should be performant
        avg_callback_time = total_time / 10
        assert avg_callback_time < 0.05, \
            f"Avg callback time {avg_callback_time}s, should be < 0.05s"
