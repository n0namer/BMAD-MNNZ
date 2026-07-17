"""
Katana Conditions Module

Candlestick pattern detection and signal generation for the Katana trading system.

Includes:
- Pattern Detectors (8 base patterns)
- Pattern Registry and Orchestration
- Confidence Scoring
- Hard Limits and Confidence Filtering (US-PA-003)
"""

from .pa_patterns import (
    Candle,
    PatternDetector,
    PinBarPattern,
    EngulfingPattern,
    InsideBarPattern,
    BreakoutRetestPattern,
    HammerPattern,
    ShootingStarPattern,
    MorningStarPattern,
    EveningStarPattern,
    PatternType,
    PATTERN_DETECTORS,
    detect_patterns,
)

from .pa_hard_limits import (
    PatternResult,
    PatternHardLimits,
    PatternLimitTracker,
    apply_hard_limits,
    FilterStats,
)

__all__ = [
    # Pattern Detection
    "Candle",
    "PatternDetector",
    "PinBarPattern",
    "EngulfingPattern",
    "InsideBarPattern",
    "BreakoutRetestPattern",
    "HammerPattern",
    "ShootingStarPattern",
    "MorningStarPattern",
    "EveningStarPattern",
    "PatternType",
    "PATTERN_DETECTORS",
    "detect_patterns",
    # Hard Limits and Filtering
    "PatternResult",
    "PatternHardLimits",
    "PatternLimitTracker",
    "apply_hard_limits",
    "FilterStats",
]

__version__ = "2.0.0"
