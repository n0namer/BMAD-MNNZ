"""
Dashboard Panels - Visualization components for trading metrics.

Provides Position, Risk, and Performance panels for real-time trading dashboards.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
import numpy as np
from enum import Enum


class PositionStatusColor(Enum):
    """Color coding for position status."""
    LONG_PROFITABLE = "green"
    LONG_LOSS = "red"
    SHORT_PROFITABLE = "darkgreen"
    SHORT_LOSS = "darkred"
    NEUTRAL = "gray"


@dataclass
class Position:
    """Position data structure."""
    symbol: str
    size: float
    entry_price: float
    current_price: float
    pnl: float = 0.0
    pnl_percent: float = 0.0

    def __post_init__(self):
        """Calculate PnL if not provided."""
        if self.pnl == 0.0:
            self.pnl = (self.current_price - self.entry_price) * self.size
            self.pnl_percent = ((self.current_price - self.entry_price) / self.entry_price) * 100


@dataclass
class PositionPanel:
    """
    Position Panel - Displays active positions with size, entry, current price, and PnL.
    """

    positions: Dict[str, Position] = field(default_factory=dict)
    color_scheme: Dict[str, str] = field(default_factory=dict)
    refresh_interval: float = 1.0  # seconds

    def add_position(self, position: Position) -> None:
        """Add a position to the panel."""
        self.positions[position.symbol] = position

    def remove_position(self, symbol: str) -> None:
        """Remove a position from the panel."""
        if symbol in self.positions:
            del self.positions[symbol]

    def update_position(self, symbol: str, current_price: float) -> None:
        """Update a position with current price."""
        if symbol in self.positions:
            pos = self.positions[symbol]
            pos.current_price = current_price
            pos.pnl = (current_price - pos.entry_price) * pos.size
            pos.pnl_percent = ((current_price - pos.entry_price) / pos.entry_price) * 100

    def get_color(self, symbol: str) -> str:
        """Get color for a position based on P&L."""
        if symbol not in self.positions:
            return PositionStatusColor.NEUTRAL.value

        pos = self.positions[symbol]
        if pos.size > 0:  # Long position
            return PositionStatusColor.LONG_PROFITABLE.value if pos.pnl > 0 else PositionStatusColor.LONG_LOSS.value
        else:  # Short position
            return PositionStatusColor.SHORT_PROFITABLE.value if pos.pnl > 0 else PositionStatusColor.SHORT_LOSS.value

    def render(self) -> Dict[str, Any]:
        """Render panel data for display."""
        return {
            'title': 'Positions',
            'positions': [
                {
                    'symbol': pos.symbol,
                    'size': pos.size,
                    'entry_price': pos.entry_price,
                    'current_price': pos.current_price,
                    'pnl': pos.pnl,
                    'pnl_percent': pos.pnl_percent,
                    'color': self.get_color(pos.symbol)
                }
                for pos in self.positions.values()
            ],
            'total_pnl': sum(pos.pnl for pos in self.positions.values()),
            'num_positions': len(self.positions)
        }

    def displays_symbols(self) -> List[str]:
        """Get list of displayed symbols."""
        return list(self.positions.keys())

    def shows_size_and_pnl(self) -> bool:
        """Check if panel shows size and PnL information."""
        return True  # This panel always shows size and PnL


@dataclass
class RiskMetric:
    """Risk metric data."""
    name: str
    value: float
    threshold: Optional[float] = None
    alert_level: str = "normal"  # normal, warning, critical


@dataclass
class RiskPanel:
    """
    Risk Panel - Displays risk metrics and alerts.
    """

    metrics: Dict[str, RiskMetric] = field(default_factory=dict)
    thresholds: Dict[str, float] = field(default_factory=dict)
    alerts: List[Dict[str, Any]] = field(default_factory=list)
    refresh_interval: float = 1.0
    callback: Optional[Callable] = None

    def add_metric(self, metric: RiskMetric) -> None:
        """Add a risk metric."""
        self.metrics[metric.name] = metric
        self._check_threshold(metric.name)

    def update_metric(self, name: str, value: float) -> None:
        """Update a risk metric value."""
        if name in self.metrics:
            self.metrics[name].value = value
            self._check_threshold(name)

    def set_threshold(self, metric_name: str, threshold: float) -> None:
        """Set alert threshold for a metric."""
        self.thresholds[metric_name] = threshold
        if metric_name in self.metrics:
            self.metrics[metric_name].threshold = threshold

    def _check_threshold(self, metric_name: str) -> None:
        """Check if metric exceeds threshold and trigger alert."""
        if metric_name not in self.metrics:
            return

        metric = self.metrics[metric_name]
        threshold = self.thresholds.get(metric_name)

        if threshold and metric.value > threshold:
            alert = {
                'metric': metric_name,
                'value': metric.value,
                'threshold': threshold,
                'timestamp': datetime.now(),
                'level': 'critical' if metric.value > threshold * 1.5 else 'warning'
            }
            self.alerts.append(alert)

            # Call callback if set
            if self.callback:
                self.callback(alert)

    def render(self) -> Dict[str, Any]:
        """Render panel data for display."""
        return {
            'title': 'Risk Metrics',
            'metrics': [
                {
                    'name': metric.name,
                    'value': metric.value,
                    'threshold': metric.threshold,
                    'alert_level': metric.alert_level
                }
                for metric in self.metrics.values()
            ],
            'alerts': self.alerts[-10:],  # Last 10 alerts
            'has_critical_alerts': any(a['level'] == 'critical' for a in self.alerts)
        }

    def shows_metrics(self) -> bool:
        """Check if panel shows risk metrics."""
        return len(self.metrics) > 0

    def updates_on_data_change(self) -> bool:
        """Check if panel updates on data changes."""
        return True

    def has_alert_threshold(self) -> bool:
        """Check if panel has alert thresholds configured."""
        return len(self.thresholds) > 0


@dataclass
class PerformanceMetrics:
    """Performance metrics container."""
    equity_curve: List[float] = field(default_factory=list)
    timestamps: List[datetime] = field(default_factory=list)
    returns: List[float] = field(default_factory=list)
    drawdown: List[float] = field(default_factory=list)
    sharpe_ratio: float = 0.0
    max_drawdown: float = 0.0
    win_rate: float = 0.0
    total_return: float = 0.0


@dataclass
class PerformancePanel:
    """
    Performance Panel - Displays equity curve, returns, and performance metrics.
    """

    metrics: PerformanceMetrics = field(default_factory=PerformanceMetrics)
    max_history: int = 1000
    refresh_interval: float = 1.0

    def add_equity_point(self, value: float, timestamp: Optional[datetime] = None) -> None:
        """Add a point to the equity curve."""
        if len(self.metrics.equity_curve) >= self.max_history:
            self.metrics.equity_curve.pop(0)
            self.metrics.timestamps.pop(0)

        self.metrics.equity_curve.append(value)
        self.metrics.timestamps.append(timestamp or datetime.now())
        self._calculate_metrics()

    def add_return(self, return_value: float) -> None:
        """Add a period return."""
        if len(self.metrics.returns) >= self.max_history:
            self.metrics.returns.pop(0)

        self.metrics.returns.append(return_value)
        self._calculate_metrics()

    def _calculate_metrics(self) -> None:
        """Calculate performance metrics from data."""
        if len(self.metrics.equity_curve) < 2:
            return

        # Calculate returns from equity curve
        equity = np.array(self.metrics.equity_curve)
        returns = np.diff(equity) / equity[:-1]

        # Sharpe Ratio (assuming 252 trading days)
        if len(returns) > 0:
            daily_return = np.mean(returns)
            daily_std = np.std(returns)
            self.metrics.sharpe_ratio = (daily_return / daily_std * np.sqrt(252)) if daily_std > 0 else 0

        # Maximum Drawdown
        cummax = np.maximum.accumulate(equity)
        drawdown = (equity - cummax) / cummax
        self.metrics.max_drawdown = np.min(drawdown) if len(drawdown) > 0 else 0
        self.metrics.drawdown = drawdown.tolist()

        # Total Return
        if len(equity) > 0:
            self.metrics.total_return = (equity[-1] - equity[0]) / equity[0]

        # Win Rate
        if len(returns) > 0:
            self.metrics.win_rate = np.sum(returns > 0) / len(returns)

    def render(self) -> Dict[str, Any]:
        """Render panel data for display."""
        return {
            'title': 'Performance',
            'equity_curve': self.metrics.equity_curve,
            'timestamps': [t.isoformat() for t in self.metrics.timestamps],
            'returns': self.metrics.returns,
            'drawdown': self.metrics.drawdown,
            'sharpe_ratio': self.metrics.sharpe_ratio,
            'max_drawdown': self.metrics.max_drawdown,
            'win_rate': self.metrics.win_rate,
            'total_return': self.metrics.total_return
        }

    def has_equity_curve(self) -> bool:
        """Check if panel has equity curve data."""
        return len(self.metrics.equity_curve) > 0

    def has_period_returns(self) -> bool:
        """Check if panel has period returns data."""
        return len(self.metrics.returns) > 0

    def has_drawdown_chart(self) -> bool:
        """Check if panel has drawdown data."""
        return len(self.metrics.drawdown) > 0
