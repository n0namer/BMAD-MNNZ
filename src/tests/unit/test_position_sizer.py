"""Unit tests for position sizing module.

Tests for RiskResult, PositionSizer implementations, and Kelly criterion.
"""

import pytest
import numpy as np
from katana.live.position_sizer import (
    RiskResult,
    PositionSizer,
    FixedPercentSizer,
    KellySizer,
    ATRSizer,
    KellyCriterion,
    OptunaOptimizer,
    PortfolioConstraints,
    VIXAdjustment,
)


class TestRiskResult:
    """Test RiskResult dataclass."""

    def test_risk_result_creation(self):
        """Test creating a RiskResult."""
        result = RiskResult(
            position_size=100.0,
            risk_amount=200.0,
            reward_amount=400.0,
            rr_ratio=2.0,
            confidence=0.9,
            rationale="Test position",
        )
        assert result.position_size == 100.0
        assert result.risk_amount == 200.0
        assert result.reward_amount == 400.0
        assert result.rr_ratio == 2.0
        assert result.confidence == 0.9
        assert result.rationale == "Test position"

    def test_risk_result_auto_calculate_rr(self):
        """Test that RiskResult auto-calculates R/R ratio."""
        result = RiskResult(
            position_size=100.0,
            risk_amount=100.0,
            reward_amount=300.0,
            rr_ratio=2.0,  # Will be overridden
        )
        assert result.rr_ratio == 3.0  # 300 / 100

    def test_risk_result_zero_risk_error(self):
        """Test that zero risk_amount raises error."""
        with pytest.raises(ValueError, match="risk_amount cannot be zero"):
            RiskResult(
                position_size=0,
                risk_amount=0,
                reward_amount=100.0,
                rr_ratio=0,
            )


class TestFixedPercentSizer:
    """Test FixedPercentSizer."""

    def test_fixed_percent_sizing(self):
        """Test fixed percentage position sizing."""
        sizer = FixedPercentSizer(account_balance=10000, risk_percent=0.02)

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
        }

        result = sizer.calculate_position_size(signal, 10000, {})

        assert result.position_size == 100.0  # 200 / 2 = 100
        assert result.risk_amount == 200.0  # 10000 * 0.02
        assert result.reward_amount == 500.0  # 100 * 5
        assert result.rr_ratio == 2.5

    def test_fixed_percent_with_leverage(self):
        """Test fixed percentage sizing with leverage."""
        sizer = FixedPercentSizer(
            account_balance=10000,
            risk_percent=0.02,
            leverage=2.0,
        )

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
        }

        result = sizer.calculate_position_size(signal, 10000, {})

        # With 2x leverage, position size doubles
        assert result.position_size == 200.0  # 100 * 2


class TestKellySizer:
    """Test KellySizer with Kelly criterion."""

    def test_kelly_sizing_basic(self):
        """Test basic Kelly sizing."""
        sizer = KellySizer(
            account_balance=10000,
            kelly_fraction=0.25,
        )

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
        }

        risk_params = {
            'win_rate': 0.60,
            'risk_reward_ratio': 2.5,
        }

        result = sizer.calculate_position_size(signal, 10000, risk_params)

        assert result.position_size > 0
        assert result.confidence > 0.5
        assert "Kelly" in result.rationale

    def test_kelly_sizing_edge_case_breakeven(self):
        """Test Kelly sizing with near-breakeven win rate."""
        sizer = KellySizer(account_balance=10000)

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 102,  # 1:1 RR = 1.0
        }

        risk_params = {
            'win_rate': 0.51,  # Slightly above breakeven (0.50)
            'risk_reward_ratio': 1.0,
        }

        result = sizer.calculate_position_size(signal, 10000, risk_params)
        # Near-breakeven win rate should result in minimal position size
        assert result.position_size > 0
        assert result.risk_amount > 0  # Must have positive risk for valid position

    def test_kelly_with_volatility_adjustment(self):
        """Test Kelly sizing with volatility adjustment."""
        sizer = KellySizer(
            account_balance=10000,
            volatility_adjustment=True,
            baseline_volatility=0.01,
        )

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
        }

        risk_params = {
            'win_rate': 0.60,
            'risk_reward_ratio': 2.5,
            'volatility': 0.02,  # 2x baseline
        }

        result = sizer.calculate_position_size(signal, 10000, risk_params)
        # Higher volatility should reduce position size
        assert result.position_size > 0


class TestATRSizer:
    """Test ATRSizer."""

    def test_atr_sizing_basic(self):
        """Test basic ATR-based sizing."""
        sizer = ATRSizer(account_balance=10000, risk_percent=0.01)

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
            'high': np.array([105, 107, 106]),
            'low': np.array([100, 103, 104]),
            'close': np.array([104, 106, 105]),
        }

        result = sizer.calculate_position_size(signal, 10000, {})

        assert result.position_size > 0
        assert result.risk_amount > 0
        assert "ATR" in result.rationale

    def test_atr_sizing_without_price_data(self):
        """Test ATR sizing when price data not available."""
        sizer = ATRSizer(account_balance=10000, risk_percent=0.01)

        signal = {
            'entry': 100,
            'stop_loss': 98,
            'target': 105,
        }

        result = sizer.calculate_position_size(signal, 10000, {})

        assert result.position_size > 0


class TestKellyCriterion:
    """Test KellyCriterion calculator."""

    def test_kelly_calculation_basic(self):
        """Test basic Kelly formula calculation."""
        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=0.60,
            avg_win=0.03,
            avg_loss=-0.02,
        )

        assert 0 <= kelly <= 1.0
        assert kelly > 0  # Positive expected value

    def test_kelly_calculation_breakeven(self):
        """Test Kelly with breakeven win rate."""
        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=0.50,
            avg_win=0.02,
            avg_loss=-0.02,
        )

        assert kelly == 0.0  # No edge

    def test_kelly_calculation_losing_strategy(self):
        """Test Kelly with losing strategy."""
        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=0.40,
            avg_win=0.02,
            avg_loss=-0.02,
        )

        # Losing strategy (40% win rate) results in negative Kelly
        # Shows no edge, position should be small/avoid
        assert kelly < 0  # Negative Kelly for losing strategy

    def test_kelly_fractional(self):
        """Test fractional Kelly."""
        sizer_full = KellyCriterion(fraction=1.0)
        sizer_half = KellyCriterion(fraction=0.5)
        sizer_quarter = KellyCriterion(fraction=0.25)

        kelly_full = sizer_full.calculate(0.60, 0.03, -0.02)
        kelly_half = sizer_half.calculate(0.60, 0.03, -0.02)
        kelly_quarter = sizer_quarter.calculate(0.60, 0.03, -0.02)

        assert kelly_quarter < kelly_half < kelly_full

    def test_kelly_with_constraints(self):
        """Test Kelly with min/max position constraints."""
        sizer = KellyCriterion(
            min_position=0.02,
            max_position=0.08,
        )

        # High win rate would give > 0.08, should be clamped
        kelly = sizer.calculate(
            win_rate=0.80,
            avg_win=0.05,
            avg_loss=-0.05,
        )

        assert kelly <= 0.08


class TestPortfolioConstraints:
    """Test PortfolioConstraints."""

    def test_check_allocation(self):
        """Test position allocation checking."""
        constraints = PortfolioConstraints(max_per_symbol=0.10)

        from dataclasses import dataclass

        @dataclass
        class MockPosition:
            allocation_pct: float

        valid_pos = MockPosition(allocation_pct=0.08)
        invalid_pos = MockPosition(allocation_pct=0.12)

        assert constraints.check_allocation(valid_pos) is True
        assert constraints.check_allocation(invalid_pos) is False

    def test_check_leverage(self):
        """Test leverage constraint."""
        constraints = PortfolioConstraints(max_leverage=2.0)

        assert constraints.check_leverage(1.5) is True
        assert constraints.check_leverage(2.0) is True
        assert constraints.check_leverage(2.5) is False


class TestVIXAdjustment:
    """Test VIXAdjustment."""

    def test_vix_adjustment_low(self):
        """Test VIX adjustment for low volatility."""
        adjuster = VIXAdjustment()

        factor = adjuster.get_adjustment_factor(10.0)
        assert factor == 1.0

    def test_vix_adjustment_moderate(self):
        """Test VIX adjustment for moderate volatility."""
        adjuster = VIXAdjustment()

        factor = adjuster.get_adjustment_factor(20.0)
        assert factor == 0.75

    def test_vix_adjustment_high(self):
        """Test VIX adjustment for high volatility."""
        adjuster = VIXAdjustment()

        factor = adjuster.get_adjustment_factor(30.0)
        assert factor == 0.50

    def test_vix_adjustment_extreme(self):
        """Test VIX adjustment for extreme volatility."""
        adjuster = VIXAdjustment()

        factor = adjuster.get_adjustment_factor(50.0)
        assert factor == 0.25


class TestOptunaOptimizer:
    """Test OptunaOptimizer stub implementation."""

    def test_optimizer_creation(self):
        """Test OptunaOptimizer creation."""
        optimizer = OptunaOptimizer(n_trials=50)
        assert optimizer.n_trials == 50

    def test_optimizer_with_backtest_func(self):
        """Test optimizer with backtest function."""
        from dataclasses import dataclass

        @dataclass
        class MockResult:
            sharpe_ratio: float

        def backtest_func(params):
            return MockResult(sharpe_ratio=1.5)

        optimizer = OptunaOptimizer(n_trials=10)
        best_params = optimizer.optimize(
            backtest_func=backtest_func,
            param_space={
                'kelly_fraction': (0.1, 0.5),
                'position_size': (0.01, 0.20),
            },
        )

        assert isinstance(best_params, dict)
        assert 'kelly_fraction' in best_params
        assert 'position_size' in best_params


class TestIntegration:
    """Integration tests for position sizing module."""

    def test_full_position_sizing_workflow(self):
        """Test complete position sizing workflow."""
        # Fixed percent sizing
        fixed_sizer = FixedPercentSizer(account_balance=100000, risk_percent=0.02)

        signal = {
            'entry': 100,
            'stop_loss': 95,
            'target': 110,
        }

        fixed_result = fixed_sizer.calculate_position_size(signal, 100000, {})
        assert fixed_result.position_size > 0

        # Kelly sizing
        kelly_sizer = KellySizer(account_balance=100000)
        kelly_result = kelly_sizer.calculate_position_size(
            signal,
            100000,
            {'win_rate': 0.60, 'risk_reward_ratio': 2.0},
        )
        assert kelly_result.position_size > 0

        # Verify Kelly is typically smaller than fixed (more conservative)
        # (This depends on specific parameters)

    def test_position_sizing_error_handling(self):
        """Test error handling in position sizing."""
        sizer = FixedPercentSizer(account_balance=10000)

        # Invalid signal
        with pytest.raises(ValueError):
            sizer.calculate_position_size(
                {'entry': -100, 'stop_loss': 98},
                10000,
                {},
            )

        # Invalid risk params for Kelly
        kelly_sizer = KellySizer(account_balance=10000)
        with pytest.raises(ValueError):
            kelly_sizer._calculate_kelly_fraction(1.5, 2.0)  # Invalid win rate


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
