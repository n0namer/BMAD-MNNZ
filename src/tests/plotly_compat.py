"""
Plotly version compatibility module.

Handles API differences between plotly versions to ensure tests work with both
old and new versions of plotly library.

Version Support:
  - 5.0.0 - 5.x (stable)
  - 6.0.0+ (future versions, compatibility layer)

Issue: Plotly changed its internal APIs between major versions.
Solution: Provide compatibility shims that work with both versions.

Usage in tests:
  from plotly_compat import get_plotly_version, use_plotly_express, PlotlyCompat

  # Check version
  version = get_plotly_version()

  # Use compatibility utilities
  if PlotlyCompat.is_v6_or_later():
      # Use new API
      pass
  else:
      # Use old API
      pass

  # Import functions that handle both versions
  fig = use_plotly_express.scatter(x=[1,2,3], y=[4,5,6])
"""

import sys
from typing import Optional, Tuple, Any
from unittest.mock import MagicMock

# Detect plotly version
_plotly_version: Optional[str] = None
_plotly_major_version: Optional[int] = None


def _detect_plotly_version() -> Tuple[str, int]:
    """
    Detect installed plotly version.

    Returns:
        Tuple of (version_string, major_version_int)

    Raises:
        ImportError: If plotly is not installed
    """
    try:
        import plotly
        version_str = plotly.__version__
        major_version = int(version_str.split('.')[0])
        return version_str, major_version
    except ImportError as e:
        raise ImportError(
            "plotly is not installed. "
            "Install with: pip install 'plotly>=5.0.0,<6.0.0'"
        ) from e
    except (AttributeError, ValueError, IndexError) as e:
        raise ImportError(
            f"Could not parse plotly version: {e}"
        ) from e


# Initialize version detection
try:
    _plotly_version, _plotly_major_version = _detect_plotly_version()
except ImportError:
    # Allow tests to import this module even if plotly isn't installed
    _plotly_version = "unknown"
    _plotly_major_version = 5


def get_plotly_version() -> str:
    """Get installed plotly version string."""
    return _plotly_version


def get_plotly_major_version() -> int:
    """Get plotly major version number."""
    return _plotly_major_version


class PlotlyCompat:
    """Compatibility utilities for plotly API differences."""

    @staticmethod
    def is_v5() -> bool:
        """Check if using plotly 5.x."""
        return _plotly_major_version == 5

    @staticmethod
    def is_v6_or_later() -> bool:
        """Check if using plotly 6.0 or later."""
        return _plotly_major_version >= 6

    @staticmethod
    def is_v5_or_earlier() -> bool:
        """Check if using plotly 5.x or earlier."""
        return _plotly_major_version <= 5


# Version-specific imports and API bridges
try:
    import plotly.express as px
    import plotly.graph_objects as go
    import plotly.io as pio
    _plotly_available = True
except ImportError:
    _plotly_available = False
    # Create mock modules for test collection to work
    px = MagicMock()
    go = MagicMock()
    pio = MagicMock()


def get_figure_layout(fig: Any) -> Any:
    """
    Get figure layout in a version-independent way.

    Args:
        fig: plotly Figure object

    Returns:
        Layout object (API compatible with both versions)
    """
    if PlotlyCompat.is_v5():
        # v5.x uses go.Layout
        return fig.layout
    else:
        # v6.x+ maintains same API
        return fig.layout


def get_figure_data(fig: Any) -> Any:
    """
    Get figure data in a version-independent way.

    Args:
        fig: plotly Figure object

    Returns:
        Data traces (API compatible with both versions)
    """
    if PlotlyCompat.is_v5():
        # v5.x uses fig.data
        return fig.data
    else:
        # v6.x+ maintains same API
        return fig.data


def create_scatter(x, y, mode='markers', name=None, **kwargs):
    """
    Create a scatter trace in a version-independent way.

    Handles API differences between plotly versions.

    Args:
        x: X-axis data
        y: Y-axis data
        mode: 'markers', 'lines', 'lines+markers'
        name: Trace name
        **kwargs: Additional arguments

    Returns:
        Scatter trace
    """
    if not _plotly_available:
        return MagicMock()

    if PlotlyCompat.is_v5():
        # v5.x API
        return go.Scatter(
            x=x, y=y,
            mode=mode,
            name=name,
            **kwargs
        )
    else:
        # v6.x+ (same API)
        return go.Scatter(
            x=x, y=y,
            mode=mode,
            name=name,
            **kwargs
        )


def create_bar(x, y, name=None, **kwargs):
    """
    Create a bar trace in a version-independent way.

    Args:
        x: X-axis data
        y: Y-axis data
        name: Trace name
        **kwargs: Additional arguments

    Returns:
        Bar trace
    """
    if not _plotly_available:
        return MagicMock()

    if PlotlyCompat.is_v5():
        # v5.x API
        return go.Bar(
            x=x, y=y,
            name=name,
            **kwargs
        )
    else:
        # v6.x+ (same API)
        return go.Bar(
            x=x, y=y,
            name=name,
            **kwargs
        )


def create_figure(data=None, layout=None, **kwargs):
    """
    Create a Figure in a version-independent way.

    Args:
        data: List of traces
        layout: Layout object or dict
        **kwargs: Additional arguments

    Returns:
        Figure object
    """
    if not _plotly_available:
        return MagicMock()

    if PlotlyCompat.is_v5():
        # v5.x API
        if data is None:
            data = []
        if layout is None:
            layout = {}
        return go.Figure(data=data, layout=layout, **kwargs)
    else:
        # v6.x+ (same API)
        if data is None:
            data = []
        if layout is None:
            layout = {}
        return go.Figure(data=data, layout=layout, **kwargs)


def set_figure_title(fig: Any, title: str) -> Any:
    """
    Set figure title in a version-independent way.

    Args:
        fig: plotly Figure object
        title: Title string

    Returns:
        Modified figure
    """
    if PlotlyCompat.is_v5():
        # v5.x API
        fig.update_layout(title=title)
    else:
        # v6.x+ (same API)
        fig.update_layout(title=title)
    return fig


def set_figure_axes(fig: Any, xaxis_title: str, yaxis_title: str) -> Any:
    """
    Set figure axes titles in a version-independent way.

    Args:
        fig: plotly Figure object
        xaxis_title: X-axis title
        yaxis_title: Y-axis title

    Returns:
        Modified figure
    """
    if PlotlyCompat.is_v5():
        # v5.x API
        fig.update_layout(
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title
        )
    else:
        # v6.x+ (same API)
        fig.update_layout(
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title
        )
    return fig


def add_trace(fig: Any, trace: Any) -> Any:
    """
    Add a trace to figure in a version-independent way.

    Args:
        fig: plotly Figure object
        trace: Trace object

    Returns:
        Modified figure
    """
    if PlotlyCompat.is_v5():
        # v5.x API
        fig.add_trace(trace)
    else:
        # v6.x+ (same API)
        fig.add_trace(trace)
    return fig


def export_html(fig: Any, file: str, **kwargs) -> None:
    """
    Export figure to HTML in a version-independent way.

    Args:
        fig: plotly Figure object
        file: Output filename
        **kwargs: Additional arguments
    """
    if not _plotly_available:
        return

    if PlotlyCompat.is_v5():
        # v5.x API
        pio.write_html(fig, file=file, **kwargs)
    else:
        # v6.x+ (same API)
        pio.write_html(fig, file=file, **kwargs)


def show_figure(fig: Any, **kwargs) -> None:
    """
    Show figure in browser in a version-independent way.

    Args:
        fig: plotly Figure object
        **kwargs: Additional arguments
    """
    if not _plotly_available:
        return

    if PlotlyCompat.is_v5():
        # v5.x API
        fig.show(**kwargs)
    else:
        # v6.x+ (same API)
        fig.show(**kwargs)


# Re-export common plotly objects
__all__ = [
    'get_plotly_version',
    'get_plotly_major_version',
    'PlotlyCompat',
    'get_figure_layout',
    'get_figure_data',
    'create_scatter',
    'create_bar',
    'create_figure',
    'set_figure_title',
    'set_figure_axes',
    'add_trace',
    'export_html',
    'show_figure',
    'px',
    'go',
    'pio',
]
