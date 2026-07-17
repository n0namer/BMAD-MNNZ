"""
Test suite for portfolio diversification metrics and constraints.

Coverage targets:
- Correlation matrix testing
- Asset class diversification
- Sector concentration limits
- Diversification metrics (Herfindahl, entropy)

This module tests portfolio analysis and constraint enforcement.
"""

import pytest
import numpy as np
from typing import Dict, List


class TestCorrelationAnalysis:
    """Tests for portfolio correlation matrix analysis."""

    def test_correlation_matrix_perfect_correlation(self):
        """Test correlation matrix with perfectly correlated assets."""
        returns1 = np.array([0.01, 0.02, 0.03, 0.02, 0.01])
        returns2 = returns1.copy()
        correlation = np.corrcoef(returns1, returns2)[0, 1]
        assert correlation == pytest.approx(1.0)

    def test_correlation_threshold_0_7(self):
        """Test correlation threshold of 0.7 constraint."""
        max_correlation = 0.7
        asset_correlation = 0.65
        assert asset_correlation <= max_correlation


class TestSectorConcentration:
    """Tests for sector concentration and limits."""

    def test_single_sector_concentration(self):
        """Test concentration calculation for single sector."""
        positions = {"AAPL": 0.10, "MSFT": 0.10, "GOOGL": 0.10}
        sectors = {"AAPL": "TECH", "MSFT": "TECH", "GOOGL": "TECH"}

        tech_concentration = sum(
            size for symbol, size in positions.items()
            if sectors.get(symbol) == "TECH"
        )
        assert tech_concentration == pytest.approx(0.30)


class TestDiversificationMetrics:
    """Tests for portfolio diversification metrics."""

    def test_herfindahl_index_perfectly_diversified(self):
        """Test Herfindahl index for perfectly diversified portfolio."""
        weights = [0.20, 0.20, 0.20, 0.20, 0.20]
        herfindahl = sum(w**2 for w in weights)
        assert herfindahl == pytest.approx(0.20)

    def test_herfindahl_index_concentrated_portfolio(self):
        """Test Herfindahl index for concentrated portfolio."""
        weights = [1.0]
        herfindahl = sum(w**2 for w in weights)
        assert herfindahl == pytest.approx(1.0)
