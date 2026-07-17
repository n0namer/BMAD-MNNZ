"""
Kelly Criterion Sizing Tests - Unit Tests

Deep dive into Kelly Criterion formula, edge cases, and mathematical correctness.
Tests validate the mathematical foundation before integration tests.

All tests SHOULD FAIL until implementation is complete.
"""

import pytest
import math
from typing import Tuple
from dataclasses import dataclass


@dataclass
class TradeStats:
    """Statistics from trade history."""
    win_rate: float
    avg_win: float
    avg_loss: float
    num_trades: int
    winning_trades: int
    losing_trades: int


class TestKellyCriterion:
    """Test suite for Kelly Criterion formula and calculations.

    The Kelly Criterion formula:
        f* = (bp - q) / b
        where:
            b = odds (average win / average loss)
            p = probability of win
            q = probability of loss (1 - p)
            f* = fractional position size

    Properties:
        - f* between 0 and 1 indicates position should be taken
        - f* > 1 indicates overbetting (should use fractional Kelly)
        - f* < 0 indicates strategy should not be traded
        - f* = 0 at 50% win rate with even odds
    """

    @pytest.fixture
    def good_strategy(self) -> TradeStats:
        """Strategy with positive expectancy."""
        return TradeStats(
            win_rate=0.60,
            avg_win=0.03,
            avg_loss=-0.02,
            num_trades=100,
            winning_trades=60,
            losing_trades=40
        )

    @pytest.fixture
    def marginal_strategy(self) -> TradeStats:
        """Strategy at breakeven."""
        return TradeStats(
            win_rate=0.50,
            avg_win=0.02,
            avg_loss=-0.02,
            num_trades=100,
            winning_trades=50,
            losing_trades=50
        )

    @pytest.fixture
    def excellent_strategy(self) -> TradeStats:
        """High win rate strategy."""
        return TradeStats(
            win_rate=0.75,
            avg_win=0.04,
            avg_loss=-0.02,
            num_trades=100,
            winning_trades=75,
            losing_trades=25
        )

    # ============================================================================
    # Formula Validation Tests
    # ============================================================================

    @pytest.mark.kelly
    def test_kelly_formula_basic_calculation(self, good_strategy: TradeStats):
        """Validate basic Kelly formula calculation.

        f* = (bp - q) / b

        For 60% win, 2:1 odds:
            p = 0.60, q = 0.40
            b = 0.03 / 0.02 = 1.5
            f* = (1.5 * 0.60 - 0.40) / 1.5
            f* = (0.90 - 0.40) / 1.5
            f* = 0.50 / 1.5
            f* = 0.333 (33.3%)
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=good_strategy.win_rate,
            avg_win=good_strategy.avg_win,
            avg_loss=good_strategy.avg_loss
        )

        # Manual calculation
        p = good_strategy.win_rate
        q = 1 - p
        b = good_strategy.avg_win / abs(good_strategy.avg_loss)
        expected = (b * p - q) / b

        assert abs(kelly - expected) < 0.001, \
            f"Kelly calculation incorrect: {kelly} vs expected {expected}"

        # For this strategy, Kelly should be ~33%
        assert 0.30 < kelly < 0.35, "Kelly should be approximately 33%"

    @pytest.mark.kelly
    def test_kelly_breakeven_win_rate(self, marginal_strategy: TradeStats):
        """Kelly should be ~0 at breakeven win rate.

        At 50% win rate with equal odds:
            p = 0.50, q = 0.50
            b = 1.0 (equal odds)
            f* = (1.0 * 0.50 - 0.50) / 1.0
            f* = 0 / 1.0
            f* = 0
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=marginal_strategy.win_rate,
            avg_win=marginal_strategy.avg_win,
            avg_loss=marginal_strategy.avg_loss
        )

        # At breakeven, Kelly should be very close to 0
        assert abs(kelly) < 0.01, \
            f"Kelly at breakeven should be ~0, got {kelly}"

    @pytest.mark.kelly
    def test_kelly_increasing_with_win_rate(self):
        """Kelly should increase monotonically with win rate.

        As win rate increases from 50% to 75%, Kelly should always increase.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kellys = []
        for win_rate in [0.50, 0.55, 0.60, 0.65, 0.70, 0.75]:
            k = sizer.calculate(
                win_rate=win_rate,
                avg_win=0.02,
                avg_loss=-0.02
            )
            kellys.append(k)

        # Each value should be greater than previous
        for i in range(1, len(kellys)):
            assert kellys[i] > kellys[i-1], \
                f"Kelly should increase with win rate: {kellys}"

    @pytest.mark.kelly
    def test_kelly_excellent_strategy(self, excellent_strategy: TradeStats):
        """Kelly for high-quality strategy.

        75% win rate with 2:1 odds:
            p = 0.75, q = 0.25
            b = 0.04 / 0.02 = 2.0
            f* = (2.0 * 0.75 - 0.25) / 2.0
            f* = (1.50 - 0.25) / 2.0
            f* = 1.25 / 2.0
            f* = 0.625 (62.5%)
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=excellent_strategy.win_rate,
            avg_win=excellent_strategy.avg_win,
            avg_loss=excellent_strategy.avg_loss
        )

        # For excellent strategy, Kelly will be high
        assert kelly > 0.50, "Excellent strategy should have Kelly > 50%"

        # Manual verification
        p = excellent_strategy.win_rate
        q = 1 - p
        b = excellent_strategy.avg_win / abs(excellent_strategy.avg_loss)
        expected = (b * p - q) / b

        assert abs(kelly - expected) < 0.001, \
            f"Kelly calculation incorrect: {kelly} vs {expected}"

    # ============================================================================
    # Edge Cases and Boundary Tests
    # ============================================================================

    @pytest.mark.kelly
    def test_kelly_zero_win_rate(self):
        """Kelly should be very negative with 0% win rate.

        A strategy that always loses should have negative Kelly.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=0.0,
            avg_win=0.02,
            avg_loss=-0.02
        )

        # Should be negative (don't trade this strategy)
        assert kelly < 0, "0% win rate should give negative Kelly"

    @pytest.mark.kelly
    def test_kelly_equal_odds(self):
        """Kelly with equal odds (1:1 ratio).

        When avg_win equals absolute value of avg_loss:
            b = 1.0 (equal odds)
            f* = (1.0 * p - q) / 1.0
            f* = 2p - 1
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        # 60% win, 1:1 odds
        kelly = sizer.calculate(
            win_rate=0.60,
            avg_win=0.02,
            avg_loss=-0.02
        )

        # f* = 2(0.60) - 1 = 0.20
        assert abs(kelly - 0.20) < 0.001, \
            f"Kelly with 1:1 odds should be 0.20, got {kelly}"

    @pytest.mark.kelly
    def test_kelly_unequal_odds(self):
        """Kelly with unequal win/loss sizes.

        When avg_win > abs(avg_loss), odds are favorable.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        # 60% win, 3:1 odds
        kelly = sizer.calculate(
            win_rate=0.60,
            avg_win=0.06,
            avg_loss=-0.02
        )

        # b = 0.06 / 0.02 = 3.0
        # f* = (3.0 * 0.60 - 0.40) / 3.0
        # f* = (1.80 - 0.40) / 3.0
        # f* = 1.40 / 3.0 = 0.467

        expected = (3.0 * 0.60 - 0.40) / 3.0
        assert abs(kelly - expected) < 0.001, \
            f"Kelly calculation incorrect: {kelly} vs {expected}"

    @pytest.mark.kelly
    def test_kelly_very_high_win_rate(self):
        """Kelly behavior with very high win rate.

        95% win rate should give high Kelly but not extreme.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly = sizer.calculate(
            win_rate=0.95,
            avg_win=0.02,
            avg_loss=-0.02
        )

        # f* = (1.0 * 0.95 - 0.05) / 1.0 = 0.90
        assert kelly > 0.80, "95% win rate should give high Kelly"
        assert kelly <= 1.0, "Even 95% win should respect Kelly bounds"

    # ============================================================================
    # Fractional Kelly Tests
    # ============================================================================

    @pytest.mark.kelly
    def test_fractional_kelly_quarter(self, good_strategy: TradeStats):
        """1/4 Kelly should be 25% of full Kelly.

        Reduces bet size to minimize ruin risk.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer_full = KellyCriterion(fraction=1.0)
        sizer_quarter = KellyCriterion(fraction=0.25)

        kelly_full = sizer_full.calculate(
            win_rate=good_strategy.win_rate,
            avg_win=good_strategy.avg_win,
            avg_loss=good_strategy.avg_loss
        )

        kelly_quarter = sizer_quarter.calculate(
            win_rate=good_strategy.win_rate,
            avg_win=good_strategy.avg_win,
            avg_loss=good_strategy.avg_loss
        )

        # Quarter Kelly should be ~25% of full
        assert abs(kelly_quarter - kelly_full * 0.25) < 0.001, \
            f"1/4 Kelly incorrect: {kelly_quarter} vs {kelly_full * 0.25}"

    @pytest.mark.kelly
    def test_fractional_kelly_half(self, good_strategy: TradeStats):
        """1/2 Kelly should be 50% of full Kelly."""
        from katana.live.position_sizer import KellyCriterion

        sizer_full = KellyCriterion(fraction=1.0)
        sizer_half = KellyCriterion(fraction=0.5)

        kelly_full = sizer_full.calculate(
            win_rate=good_strategy.win_rate,
            avg_win=good_strategy.avg_win,
            avg_loss=good_strategy.avg_loss
        )

        kelly_half = sizer_half.calculate(
            win_rate=good_strategy.win_rate,
            avg_win=good_strategy.avg_win,
            avg_loss=good_strategy.avg_loss
        )

        # Half Kelly should be ~50% of full
        assert abs(kelly_half - kelly_full * 0.5) < 0.001, \
            f"1/2 Kelly incorrect: {kelly_half} vs {kelly_full * 0.5}"

    @pytest.mark.kelly
    def test_fractional_kelly_monotonic(self, good_strategy: TradeStats):
        """Fractional Kelly should decrease monotonically.

        1/4 < 1/3 < 1/2 < 2/3 < Full Kelly
        """
        from katana.live.position_sizer import KellyCriterion

        fractions = [0.25, 0.33, 0.50, 0.67, 1.0]
        kellys = []

        for frac in fractions:
            sizer = KellyCriterion(fraction=frac)
            k = sizer.calculate(
                win_rate=good_strategy.win_rate,
                avg_win=good_strategy.avg_win,
                avg_loss=good_strategy.avg_loss
            )
            kellys.append(k)

        # Each should be less than next
        for i in range(1, len(kellys)):
            assert kellys[i] > kellys[i-1], \
                f"Fractional Kelly should increase with fraction: {kellys}"

    # ============================================================================
    # Risk Management Tests
    # ============================================================================

    @pytest.mark.kelly
    def test_kelly_drawdown_relationship(self):
        """Kelly sizing affects maximum drawdown.

        Full Kelly: ~19% max drawdown (from Kelly theory)
        1/2 Kelly: ~5-10% max drawdown
        1/4 Kelly: ~1-3% max drawdown
        """
        from katana.live.position_sizer import KellyCriterion

        # This is a theoretical relationship test
        # Verify Kelly sizes are appropriate for risk levels

        sizer_quarter = KellyCriterion(fraction=0.25)
        sizer_half = KellyCriterion(fraction=0.5)
        sizer_full = KellyCriterion(fraction=1.0)

        kelly_q = sizer_quarter.calculate(
            win_rate=0.60, avg_win=0.02, avg_loss=-0.02
        )
        kelly_h = sizer_half.calculate(
            win_rate=0.60, avg_win=0.02, avg_loss=-0.02
        )
        kelly_f = sizer_full.calculate(
            win_rate=0.60, avg_win=0.02, avg_loss=-0.02
        )

        # Conservative sizing
        assert kelly_q < kelly_h < kelly_f

    @pytest.mark.kelly
    def test_kelly_overbetting_detection(self):
        """Detect when Kelly exceeds 1.0 (overbetting).

        Some strategies (very high win rate) might give Kelly > 1.
        This should be detected and fractional Kelly applied.
        """
        from katana.live.position_sizer import KellyCriterion

        # Very high win rate might give Kelly > 1
        # This should trigger 1/2 Kelly or similar
        sizer = KellyCriterion(auto_fractional=True)

        kelly = sizer.calculate(
            win_rate=0.95,
            avg_win=0.10,
            avg_loss=-0.02
        )

        # With auto_fractional, should never exceed 1.0
        assert kelly <= 1.0, "Overbetting should be capped with auto_fractional"

    # ============================================================================
    # Statistical Tests
    # ============================================================================

    @pytest.mark.kelly
    def test_kelly_with_many_trades(self):
        """Kelly stability with large trade samples.

        With 1000 trades, Kelly should be stable and reliable.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        # Calculate Kelly multiple times (simulating batches)
        kellys = []
        for batch in range(5):
            # Simulate 200 trades per batch
            k = sizer.calculate(
                win_rate=0.60 + (batch - 2) * 0.02,  # Slight variation
                avg_win=0.02,
                avg_loss=-0.02
            )
            kellys.append(k)

        # All should be within reasonable range
        assert all(0.10 < k < 0.40 for k in kellys), \
            "Kelly should be stable across samples"

    @pytest.mark.kelly
    def test_kelly_sensitivity_to_win_rate(self):
        """Kelly is highly sensitive to win rate changes.

        1% change in win rate should cause measurable Kelly change.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly_60 = sizer.calculate(
            win_rate=0.60, avg_win=0.02, avg_loss=-0.02
        )

        kelly_61 = sizer.calculate(
            win_rate=0.61, avg_win=0.02, avg_loss=-0.02
        )

        # 1% change should result in meaningful Kelly change
        change = kelly_61 - kelly_60
        assert change > 0.001, "Kelly should be sensitive to win rate"

    @pytest.mark.kelly
    def test_kelly_sensitivity_to_odds(self):
        """Kelly is sensitive to win/loss ratio.

        Better odds (larger average wins) increase Kelly.
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        kelly_1to1 = sizer.calculate(
            win_rate=0.60, avg_win=0.02, avg_loss=-0.02
        )

        kelly_2to1 = sizer.calculate(
            win_rate=0.60, avg_win=0.04, avg_loss=-0.02
        )

        # Better odds should increase Kelly
        assert kelly_2to1 > kelly_1to1, \
            "Better odds should increase Kelly"
