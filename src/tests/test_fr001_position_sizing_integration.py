"""
FR-001: Position Sizing Integration - Acceptance Tests

ATDD Test Suite for position sizing with Kelly Criterion and Optuna optimization.
Tests are intentionally failing (red) before implementation (green).

Story: FR-001 - Position Sizing Integration
Acceptance Criteria: 13 tests covering:
  - AC1-AC4: Kelly criterion sizing in backtests
  - AC5-AC7: Optuna optimization with position parameters
  - AC8-AC13: Portfolio constraints and risk management

Test Execution Order:
  1. test_kelly_criterion_basic - Basic Kelly formula calculation
  2. test_kelly_with_win_rate - Kelly sizing with win/loss rates
  3. test_kelly_fractional_kelly - Fractional Kelly to reduce leverage
  4. test_kelly_position_constraints - Kelly respects position limits
  5. test_optuna_optimization_basic - Optuna finds optimal parameters
  6. test_optuna_position_size_optimization - Optuna optimizes position sizes
  7. test_optuna_constraint_respect - Optuna respects constraints
  8. test_portfolio_constraint_max_allocation - Max allocation per symbol
  9. test_portfolio_constraint_sector_limits - Sector allocation limits
  10. test_portfolio_constraint_leverage_limit - Leverage constraints
  11. test_portfolio_constraint_correlation - Position correlation limits
  12. test_portfolio_risk_management_vix - Risk adjustment based on VIX
  13. test_integration_kelly_optuna_constraints - End-to-end integration

All tests SHOULD FAIL until implementation is complete.
"""

import pytest
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple
from unittest.mock import Mock, patch, MagicMock
from dataclasses import dataclass


@dataclass
class MockTrade:
    """Mock trade object for testing."""
    symbol: str
    entry_price: float
    exit_price: float
    quantity: int
    position_side: str  # 'long' or 'short'
    timestamp: datetime
    pnl: float
    return_pct: float


@dataclass
class MockPosition:
    """Mock position object for testing."""
    symbol: str
    quantity: int
    entry_price: float
    current_price: float
    position_side: str
    pnl: float
    allocation_pct: float


@dataclass
class MockBacktestResult:
    """Mock backtest result for testing."""
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    win_rate: float
    trades: List[MockTrade]
    equity_curve: List[float]


class TestFR001PositionSizingIntegration:
    """Test suite for FR-001 Position Sizing Integration.

    BDD Scenario: As a trader, I need position sizing based on Kelly Criterion
    so that I can optimize returns while managing risk through Optuna optimization
    and portfolio constraints.

    Feature: Position Sizing Integration
      - Calculate position sizes using Kelly Criterion formula
      - Optimize position parameters with Optuna
      - Apply portfolio-level constraints
      - Risk management with VIX adjustment
      - End-to-end integration test
    """

    @pytest.fixture
    def sample_trade_history(self) -> List[MockTrade]:
        """Fixture: Sample trade history for Kelly calculation."""
        base_time = datetime.now()
        return [
            MockTrade(
                symbol="AAPL",
                entry_price=150.0,
                exit_price=155.0,
                quantity=100,
                position_side="long",
                timestamp=base_time,
                pnl=500.0,
                return_pct=0.033
            ),
            MockTrade(
                symbol="AAPL",
                entry_price=155.0,
                exit_price=152.0,
                quantity=100,
                position_side="long",
                timestamp=base_time + timedelta(days=1),
                pnl=-300.0,
                return_pct=-0.0194
            ),
            MockTrade(
                symbol="AAPL",
                entry_price=152.0,
                exit_price=158.0,
                quantity=100,
                position_side="long",
                timestamp=base_time + timedelta(days=2),
                pnl=600.0,
                return_pct=0.0395
            ),
        ]

    @pytest.fixture
    def sample_portfolio(self) -> Dict[str, MockPosition]:
        """Fixture: Sample portfolio positions."""
        return {
            "AAPL": MockPosition(
                symbol="AAPL",
                quantity=100,
                entry_price=150.0,
                current_price=155.0,
                position_side="long",
                pnl=500.0,
                allocation_pct=0.30
            ),
            "MSFT": MockPosition(
                symbol="MSFT",
                quantity=50,
                entry_price=300.0,
                current_price=310.0,
                position_side="long",
                pnl=500.0,
                allocation_pct=0.25
            ),
            "GOOGL": MockPosition(
                symbol="GOOGL",
                quantity=30,
                entry_price=140.0,
                current_price=142.0,
                position_side="long",
                pnl=60.0,
                allocation_pct=0.20
            ),
        }

    @pytest.fixture
    def backtest_result(self, sample_trade_history) -> MockBacktestResult:
        """Fixture: Backtest result with trades."""
        return MockBacktestResult(
            total_return=0.12,
            sharpe_ratio=1.5,
            max_drawdown=0.08,
            win_rate=0.667,  # 2 wins out of 3 trades
            trades=sample_trade_history,
            equity_curve=[100000, 100500, 100200, 100800]
        )

    # ============================================================================
    # AC1-AC4: Kelly Criterion Sizing in Backtests
    # ============================================================================

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.kelly_criterion
    def test_kelly_criterion_basic(self, backtest_result: MockBacktestResult):
        """AC1: Calculate basic Kelly Criterion position size.

        GIVEN: A backtest result with trade history
        WHEN: Calculating Kelly position size
        THEN: Position size should be calculated using Kelly formula:
              f* = (b*p - q) / b
              where: b = odds (win/loss ratio)
                     p = probability of win
                     q = probability of loss (1-p)

        Expected Output:
            - Kelly fraction is between 0 and 1
            - Position size scales appropriately with win rate
            - Formula correctly applies odds ratio

        Status: FAILING (Kelly calculator not implemented)
        """
        # WHEN: Calculate Kelly position size from backtest
        # This should call a function like: kelly_fraction = calculate_kelly(backtest_result)
        # Currently failing because function doesn't exist

        # THEN: Kelly fraction should be valid
        # assert 0 <= kelly_fraction <= 1, "Kelly fraction must be between 0 and 1"

        # THEN: For 66.7% win rate with 1:1 odds, Kelly should be ~33.3%
        # assert kelly_fraction > 0.2, "Kelly fraction should be > 20% for good win rate"
        # assert kelly_fraction < 0.5, "Kelly fraction should be < 50% to reduce ruin risk"

        # Placeholder assertion (will fail)
        from katana.live.position_sizer import KellyCriterion
        sizer = KellyCriterion()
        kelly_frac = sizer.calculate(
            win_rate=backtest_result.win_rate,
            avg_win=0.033,
            avg_loss=-0.0194
        )

        # THEN: Result must be a valid fraction
        assert isinstance(kelly_frac, (int, float)), "Kelly fraction must be numeric"
        assert 0 <= kelly_frac <= 1, "Kelly fraction must be between 0 and 1"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.kelly_criterion
    def test_kelly_with_win_rate(self):
        """AC2: Kelly Criterion respects historical win rate.

        GIVEN: Trade history with known win rate
        WHEN: Calculating Kelly position size with varying win rates
        THEN: Higher win rates should result in higher Kelly fractions

        Test Cases:
            - 50% win rate → Kelly ~0%
            - 60% win rate → Kelly ~10-15%
            - 70% win rate → Kelly ~20-25%
            - 80% win rate → Kelly ~30-35%

        Expected Output:
            - Kelly fraction increases monotonically with win rate
            - 50% win rate results in minimal position sizing
            - Each 10% improvement in win rate increases Kelly by ~5-8%

        Status: FAILING (win rate impact not calculated)
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion()

        # WHEN: Calculate Kelly for different win rates
        kelly_50 = sizer.calculate(win_rate=0.50, avg_win=0.02, avg_loss=-0.02)
        kelly_60 = sizer.calculate(win_rate=0.60, avg_win=0.02, avg_loss=-0.02)
        kelly_70 = sizer.calculate(win_rate=0.70, avg_win=0.02, avg_loss=-0.02)

        # THEN: Kelly should increase with win rate
        assert kelly_60 > kelly_50, "Kelly should increase with win rate"
        assert kelly_70 > kelly_60, "Kelly should increase with win rate"

        # THEN: 50% win rate should result in minimal sizing
        assert kelly_50 <= 0.05, "50% win rate should yield Kelly <= 5%"

        # THEN: Reasonable position sizes for good strategies
        assert kelly_70 >= 0.10, "70% win rate should yield Kelly >= 10%"
        assert kelly_70 <= 0.40, "Even 70% should use Kelly <= 40%"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.kelly_criterion
    def test_kelly_fractional_kelly(self):
        """AC3: Apply fractional Kelly to reduce leverage and ruin risk.

        GIVEN: A calculated full Kelly fraction
        WHEN: Applying fractional Kelly (typically 1/4 to 1/2)
        THEN: Position size should be reduced to manage ruin risk

        Implementation:
            - 1/4 Kelly uses 25% of full Kelly
            - 1/3 Kelly uses 33% of full Kelly
            - 1/2 Kelly uses 50% of full Kelly
            - Position size = full_kelly * fraction_multiplier

        Expected Output:
            - Fractional Kelly is < full Kelly
            - Position reductions are proportional
            - Configuration is adjustable

        Status: FAILING (fractional Kelly not applied)
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion(fraction=0.5)  # 1/2 Kelly

        # WHEN: Calculate fractional Kelly
        kelly_full = sizer.calculate(win_rate=0.60, avg_win=0.02, avg_loss=-0.02)

        # THEN: Result should be reduced
        assert kelly_full <= 0.15, "1/2 Kelly at 60% win should be <= 15%"

        # WHEN: Use 1/4 Kelly
        sizer_quarter = KellyCriterion(fraction=0.25)
        kelly_quarter = sizer_quarter.calculate(win_rate=0.60, avg_win=0.02, avg_loss=-0.02)

        # THEN: 1/4 Kelly should be smaller than 1/2 Kelly
        assert kelly_quarter < kelly_full, "1/4 Kelly should be smaller than 1/2 Kelly"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.kelly_criterion
    def test_kelly_position_constraints(self, sample_trade_history):
        """AC4: Kelly position sizes respect minimum and maximum constraints.

        GIVEN: Kelly calculations with constraint limits
        WHEN: Applying position size constraints
        THEN: Position sizes should not exceed:
              - Minimum: Usually 0.01 (1% per position)
              - Maximum: Usually 0.10 (10% per position)

        Expected Output:
            - Calculated size is clamped to [min_size, max_size]
            - Minimum constraint prevents oversized positions
            - Maximum constraint prevents under-diversification

        Status: FAILING (constraints not enforced)
        """
        from katana.live.position_sizer import KellyCriterion

        sizer = KellyCriterion(
            min_position=0.01,
            max_position=0.10
        )

        # WHEN: Calculate with high win rate (might exceed max)
        kelly_size = sizer.calculate(
            win_rate=0.90,  # Very high win rate
            avg_win=0.05,
            avg_loss=-0.05
        )

        # THEN: Should be constrained to maximum
        assert kelly_size <= 0.10, "Position size should not exceed max_position"

        # WHEN: Calculate with marginal win rate (might be below min)
        kelly_size_low = sizer.calculate(
            win_rate=0.50,
            avg_win=0.01,
            avg_loss=-0.02
        )

        # THEN: Should be at least minimum
        assert kelly_size_low >= 0.01, "Position size should meet min_position"

    # ============================================================================
    # AC5-AC7: Optuna Optimization with Position Parameters
    # ============================================================================

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.optuna
    def test_optuna_optimization_basic(self, backtest_result):
        """AC5: Optuna optimization finds optimal parameters.

        GIVEN: Backtest environment with variable parameters
        WHEN: Running Optuna optimization
        THEN: Optimization should:
              - Complete successfully without errors
              - Improve upon baseline Sharpe ratio
              - Log trial results for analysis

        Expected Output:
            - Study object with N completed trials
            - Best parameters identified
            - Best trial Sharpe ratio > baseline

        Status: FAILING (Optuna integration not implemented)
        """
        from katana.live.position_sizer import OptunaOptimizer

        optimizer = OptunaOptimizer(n_trials=10)

        # WHEN: Run optimization
        best_params = optimizer.optimize(
            backtest_func=lambda params: MockBacktestResult(
                total_return=0.12 + params.get('kelly_fraction', 0.3) * 0.05,
                sharpe_ratio=1.5,
                max_drawdown=0.08,
                win_rate=0.667,
                trades=[],
                equity_curve=[]
            ),
            param_space={
                'kelly_fraction': (0.1, 0.5),
                'position_size': (0.01, 0.20),
            }
        )

        # THEN: Should return valid parameters
        assert best_params is not None, "Optimization should return best parameters"
        assert isinstance(best_params, dict), "Parameters must be a dictionary"
        assert 'kelly_fraction' in best_params, "Should optimize kelly_fraction"
        assert 'position_size' in best_params, "Should optimize position_size"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.optuna
    def test_optuna_position_size_optimization(self):
        """AC6: Optuna optimizes position sizing parameters.

        GIVEN: Range of position size parameters
        WHEN: Optimizing position sizing strategy
        THEN: Optimization should:
              - Test multiple position sizes (0.01 to 0.20)
              - Find size that maximizes risk-adjusted returns
              - Respect portfolio constraints

        Test Cases:
            - Small positions (0.01-0.05) → Lower Sharpe but safer
            - Medium positions (0.05-0.10) → Balanced
            - Large positions (0.10-0.20) → Higher returns but riskier

        Expected Output:
            - Optimal size balances returns and drawdown
            - Trade-off between aggression and safety visible

        Status: FAILING (position optimization not implemented)
        """
        from katana.live.position_sizer import OptunaOptimizer

        optimizer = OptunaOptimizer(n_trials=20)

        # WHEN: Optimize position size
        best_params = optimizer.optimize(
            backtest_func=lambda params: MockBacktestResult(
                total_return=0.12,
                sharpe_ratio=1.5,
                max_drawdown=0.08,
                win_rate=0.667,
                trades=[],
                equity_curve=[]
            ),
            param_space={
                'position_size': (0.01, 0.20),
            }
        )

        # THEN: Optimal position size should be in reasonable range
        assert 0.01 <= best_params['position_size'] <= 0.20, \
            "Optimal position size should be in search space"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.optuna
    def test_optuna_constraint_respect(self, sample_portfolio):
        """AC7: Optuna optimization respects hard constraints.

        GIVEN: Portfolio constraints (leverage, allocation limits, etc.)
        WHEN: Running Optuna with constraints
        THEN: All trials should:
              - Respect maximum leverage limit (2.0x)
              - Respect sector allocation limits (20% per sector)
              - Respect per-symbol limits (10% per symbol)
              - Not violate any hard constraints

        Expected Output:
            - All trials satisfy constraints
            - Constraint violations logged if any
            - Optimization converges to valid parameters

        Status: FAILING (constraint enforcement not implemented)
        """
        from katana.live.position_sizer import OptunaOptimizer

        def backtest_with_constraints(params):
            # Simulate constraint violation detection
            total_allocation = sum(params.get(f'size_{sym}', 0)
                                  for sym in sample_portfolio.keys())
            if total_allocation > 2.0:  # Max 2x leverage
                return MockBacktestResult(
                    total_return=-0.50,  # Penalize violations
                    sharpe_ratio=-10,
                    max_drawdown=1.0,
                    win_rate=0.0,
                    trades=[],
                    equity_curve=[]
                )
            return MockBacktestResult(
                total_return=0.12,
                sharpe_ratio=1.5,
                max_drawdown=0.08,
                win_rate=0.667,
                trades=[],
                equity_curve=[]
            )

        optimizer = OptunaOptimizer(n_trials=10)

        # WHEN: Optimize with constraints
        best_params = optimizer.optimize(
            backtest_func=backtest_with_constraints,
            param_space={
                'size_AAPL': (0.01, 0.10),
                'size_MSFT': (0.01, 0.10),
                'size_GOOGL': (0.01, 0.10),
            }
        )

        # THEN: Total allocation should not exceed leverage limit
        total_alloc = sum(best_params.get(f'size_{sym}', 0)
                         for sym in sample_portfolio.keys())
        assert total_alloc <= 2.0, "Total allocation must respect leverage limit"

    # ============================================================================
    # AC8-AC13: Portfolio Constraints
    # ============================================================================

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.constraints
    def test_portfolio_constraint_max_allocation(self, sample_portfolio):
        """AC8: Portfolio respects maximum allocation per symbol.

        GIVEN: Portfolio with allocation limits
        WHEN: Checking position sizes
        THEN: No position should exceed maximum allocation:
              - Typical max: 10% per symbol
              - Can be configured per symbol
              - Prevents over-concentration

        Expected Output:
            - All positions <= max_allocation
            - Enforcement happens before position sizing
            - Prevents single-stock risk

        Status: FAILING (allocation limits not enforced)
        """
        from katana.live.position_sizer import PortfolioConstraints

        constraints = PortfolioConstraints(max_per_symbol=0.10)

        # WHEN: Check if positions violate constraints
        for symbol, position in sample_portfolio.items():
            # THEN: Allocation should not exceed limit
            assert position.allocation_pct <= 0.10, \
                f"Position {symbol} exceeds max allocation: {position.allocation_pct}"

        # WHEN: Create position that violates constraint
        oversized = MockPosition(
            symbol="TSLA",
            quantity=1000,
            entry_price=250.0,
            current_price=250.0,
            position_side="long",
            pnl=0.0,
            allocation_pct=0.15  # Exceeds 10% limit
        )

        # THEN: Constraint should detect violation
        is_valid = constraints.check_allocation(oversized)
        assert not is_valid, "Oversized position should violate constraint"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.constraints
    def test_portfolio_constraint_sector_limits(self, sample_portfolio):
        """AC9: Portfolio respects sector allocation limits.

        GIVEN: Portfolio with multiple positions in same sector
        WHEN: Checking sector-level constraints
        THEN: No sector should exceed allocation limit:
              - Typical max: 25% per sector
              - Technology (AAPL, MSFT, GOOGL): 75% → VIOLATES
              - Need to reduce some positions

        Expected Output:
            - Sector allocation calculated from positions
            - Violations detected and reported
            - Rebalancing recommendations provided

        Status: FAILING (sector constraint logic not implemented)
        """
        from katana.live.position_sizer import PortfolioConstraints

        constraints = PortfolioConstraints(max_per_sector=0.25)

        # Define sector mapping
        sector_map = {
            'AAPL': 'Technology',
            'MSFT': 'Technology',
            'GOOGL': 'Technology',
        }

        # WHEN: Calculate sector allocations
        sector_allocations = {}
        for symbol, position in sample_portfolio.items():
            sector = sector_map.get(symbol)
            sector_allocations[sector] = sector_allocations.get(sector, 0) + position.allocation_pct

        # THEN: Sector should not exceed limit
        for sector, allocation in sector_allocations.items():
            if allocation > 0.25:
                # Should be flagged as violation
                is_valid = constraints.check_sector_allocation(sector, allocation)
                assert not is_valid, f"Sector {sector} exceeds limit"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.constraints
    def test_portfolio_constraint_leverage_limit(self, sample_portfolio):
        """AC10: Portfolio respects maximum leverage limit.

        GIVEN: Portfolio with multiple positions
        WHEN: Calculating total leverage
        THEN: Total leverage should not exceed limit:
              - Typical max: 2.0x (100% capital + 100% margin)
              - Can be configured
              - Prevents over-leveraging

        Calculation:
            - Long positions add to leverage
            - Short positions add to leverage
            - Total = sum of absolute allocations
            - Must be <= max_leverage

        Expected Output:
            - Current leverage calculated correctly
            - Limit enforced
            - Warnings for high leverage

        Status: FAILING (leverage constraint not implemented)
        """
        from katana.live.position_sizer import PortfolioConstraints

        constraints = PortfolioConstraints(max_leverage=2.0)

        # WHEN: Calculate current leverage
        current_leverage = sum(abs(p.allocation_pct) for p in sample_portfolio.values())

        # THEN: Should be within limits
        assert current_leverage <= 2.0, \
            f"Current leverage {current_leverage} exceeds limit 2.0x"

        # WHEN: Add more positions to exceed leverage
        sample_portfolio['NVDA'] = MockPosition(
            symbol="NVDA",
            quantity=200,
            entry_price=500.0,
            current_price=500.0,
            position_side="long",
            pnl=0.0,
            allocation_pct=0.50  # This would cause > 2x leverage
        )

        # THEN: Total leverage should be checked
        new_leverage = sum(abs(p.allocation_pct) for p in sample_portfolio.values())
        if new_leverage > 2.0:
            is_valid = constraints.check_leverage(new_leverage)
            assert not is_valid, "Over-leveraged portfolio should violate constraint"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.constraints
    def test_portfolio_constraint_correlation(self, sample_portfolio):
        """AC11: Portfolio respects position correlation limits.

        GIVEN: Portfolio with highly correlated positions
        WHEN: Checking correlation constraints
        THEN: Highly correlated positions should:
              - Be identified
              - Have reduced combined allocation
              - Maintain diversification

        Correlation thresholds:
            - > 0.8: Very high correlation → Reduce one position
            - 0.6-0.8: High correlation → Monitor
            - < 0.6: Acceptable

        Expected Output:
            - Correlation matrix calculated
            - High-correlation pairs identified
            - Rebalancing recommendations

        Status: FAILING (correlation analysis not implemented)
        """
        from katana.live.position_sizer import PortfolioConstraints
        import numpy as np

        constraints = PortfolioConstraints(max_correlation=0.7)

        # Create mock correlation matrix
        # AAPL-MSFT: 0.85 (high), AAPL-GOOGL: 0.75 (moderate)
        symbols = list(sample_portfolio.keys())
        corr_matrix = np.array([
            [1.0, 0.85, 0.75],   # AAPL
            [0.85, 1.0, 0.80],   # MSFT
            [0.75, 0.80, 1.0],   # GOOGL
        ])

        # WHEN: Check correlations
        for i, sym1 in enumerate(symbols):
            for j, sym2 in enumerate(symbols):
                if i < j:
                    corr = corr_matrix[i, j]
                    if corr > 0.7:
                        # THEN: High correlation should be detected
                        is_valid = constraints.check_correlation(sym1, sym2, corr)
                        assert not is_valid, \
                            f"High correlation {corr} between {sym1} and {sym2} should violate"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    @pytest.mark.constraints
    def test_portfolio_risk_management_vix(self):
        """AC12: Risk management adjusts position sizing based on VIX.

        GIVEN: Current market volatility (VIX)
        WHEN: Calculating position sizes with volatility adjustment
        THEN: Position sizes should scale inversely with VIX:
              - VIX < 15: Normal sizing
              - VIX 15-25: Reduce to 75% of normal
              - VIX 25-35: Reduce to 50% of normal
              - VIX > 35: Reduce to 25% of normal

        Adjustment formula:
            adjusted_size = base_size * vix_adjustment_factor

        Expected Output:
            - VIX adjustment calculated correctly
            - Position sizes reduced during high volatility
            - Automatic de-risking in uncertainty

        Status: FAILING (VIX adjustment not implemented)
        """
        from katana.live.position_sizer import VIXAdjustment

        adjuster = VIXAdjustment()

        # WHEN: Calculate adjustment for different VIX levels
        adj_vix10 = adjuster.get_adjustment_factor(vix_level=10.0)  # Low volatility
        adj_vix20 = adjuster.get_adjustment_factor(vix_level=20.0)  # Moderate
        adj_vix30 = adjuster.get_adjustment_factor(vix_level=30.0)  # High
        adj_vix50 = adjuster.get_adjustment_factor(vix_level=50.0)  # Very high

        # THEN: Adjustments should decrease with VIX
        assert adj_vix10 >= adj_vix20, "Low VIX should allow more aggressive sizing"
        assert adj_vix20 >= adj_vix30, "Higher VIX should reduce sizing"
        assert adj_vix30 >= adj_vix50, "Very high VIX should significantly reduce sizing"

        # THEN: Extreme VIX should not eliminate positions
        assert adj_vix50 > 0, "Even extreme VIX should allow minimum sizing"
        assert adj_vix50 <= 0.3, "Very high VIX should limit to < 30% of normal"

    @pytest.mark.fr001
    @pytest.mark.acceptance
    def test_integration_kelly_optuna_constraints(self, backtest_result, sample_portfolio):
        """AC13: Full integration of Kelly, Optuna, and constraints.

        GIVEN: Backtest results, portfolio positions, and market conditions
        WHEN: Running full position sizing pipeline
        THEN: System should:
              1. Calculate Kelly fractions
              2. Apply Optuna optimization
              3. Enforce portfolio constraints
              4. Adjust for market conditions (VIX)
              5. Return final position recommendations

        Expected Output:
            - Position recommendations for all symbols
            - All constraints satisfied
            - Positions ready for execution
            - Risk metrics calculated

        Status: FAILING (integration not implemented)
        """
        from katana.live.position_sizer import PositionSizer

        sizer = PositionSizer(
            kelly_fraction=0.5,
            max_per_symbol=0.10,
            max_leverage=2.0,
            use_optuna=True,
            vix_adjustment=True,
        )

        # WHEN: Calculate recommended positions
        recommendations = sizer.calculate_positions(
            backtest_result=backtest_result,
            current_portfolio=sample_portfolio,
            vix_level=20.0,
            account_size=100000.0,
        )

        # THEN: Should return valid recommendations
        assert recommendations is not None, "Should return position recommendations"
        assert isinstance(recommendations, dict), "Should be a dictionary"

        # THEN: Should contain all portfolio symbols
        for symbol in sample_portfolio.keys():
            assert symbol in recommendations, f"Should recommend size for {symbol}"

        # THEN: All allocations should be valid
        for symbol, rec in recommendations.items():
            assert isinstance(rec, dict), "Recommendation must be a dictionary"
            assert 'size' in rec, "Recommendation must include position size"
            assert 'allocation' in rec, "Recommendation must include allocation %"
            assert 0 <= rec['allocation'] <= 0.10, "Allocation must respect limit"

        # THEN: Total leverage should be within limit
        total_leverage = sum(rec['allocation'] for rec in recommendations.values())
        assert total_leverage <= 2.0, "Total leverage must respect limit"
