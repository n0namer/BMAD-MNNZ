"""
Pattern Analysis Pattern Detection Module

Implements 8 candlestick patterns for price action analysis:
- pinbar: Pin Bar (long wick, small body)
- engulfing: Engulfing (large candle engulfs previous)
- inside_bar: Inside Bar (smaller candle within previous)
- breakout_retest: Breakout Retest (break and return to level)
- hammer: Hammer (long lower wick, small body)
- shooting_star: Shooting Star (long upper wick, small body)
- morning_star: Morning Star (3-candle reversal pattern)
- evening_star: Evening Star (3-candle reversal pattern)

Each pattern provides:
- detect() -> bool: Pattern detection logic
- confidence() -> float: Confidence score (0.0-1.0)
- direction() -> str: 'BULL' or 'BEAR'
"""

from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class PatternType(Enum):
    """Enumeration of supported patterns."""
    PINBAR = "pinbar"
    ENGULFING = "engulfing"
    INSIDE_BAR = "inside_bar"
    BREAKOUT_RETEST = "breakout_retest"
    HAMMER = "hammer"
    SHOOTING_STAR = "shooting_star"
    MORNING_STAR = "morning_star"
    EVENING_STAR = "evening_star"


@dataclass
class Candle:
    """Represents a single candlestick."""
    open: float
    high: float
    low: float
    close: float
    timestamp: Optional[str] = None

    @property
    def body_size(self) -> float:
        """Size of candle body (absolute difference between open and close)."""
        return abs(self.close - self.open)

    @property
    def total_range(self) -> float:
        """Total range from low to high."""
        return self.high - self.low

    @property
    def lower_wick(self) -> float:
        """Size of lower wick."""
        min_price = min(self.open, self.close)
        return min_price - self.low

    @property
    def upper_wick(self) -> float:
        """Size of upper wick."""
        max_price = max(self.open, self.close)
        return self.high - max_price

    @property
    def is_bullish(self) -> bool:
        """True if close > open."""
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        """True if close < open."""
        return self.close < self.open


class PatternDetector:
    """Base class for pattern detection."""

    def __init__(self, name: str, pattern_type: PatternType):
        self.name = name
        self.pattern_type = pattern_type

    def detect(self, candles: List[Candle]) -> bool:
        """Detect if pattern matches. Override in subclasses."""
        raise NotImplementedError

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence score (0.0-1.0). Override in subclasses."""
        raise NotImplementedError

    def direction(self) -> str:
        """Return 'BULL' for bullish patterns, 'BEAR' for bearish."""
        raise NotImplementedError


class PinBarPattern(PatternDetector):
    """Pin Bar: Long wick with small body (reversal pattern)."""

    def __init__(self):
        super().__init__("Pin Bar", PatternType.PINBAR)
        self.wick_ratio_min = 2.0  # Wick must be 2x+ larger than body
        self.body_ratio_max = 0.3  # Body must be <30% of total range
        self._longer_wick_type = None  # Track which wick was longer

    def detect(self, candles: List[Candle]) -> bool:
        """Detect pin bar pattern."""
        if len(candles) < 1:
            return False

        candle = candles[-1]
        if candle.body_size == 0:
            return False

        total_range = candle.total_range
        if total_range == 0:
            return False

        # Check body ratio
        body_ratio = candle.body_size / total_range
        if body_ratio > self.body_ratio_max:
            return False

        # Check wick ratio (must have longer wick)
        longer_wick = max(candle.lower_wick, candle.upper_wick)
        if longer_wick == 0:
            return False

        wick_ratio = longer_wick / candle.body_size

        # Track which wick is dominant
        if candle.lower_wick > candle.upper_wick:
            self._longer_wick_type = "lower"
        else:
            self._longer_wick_type = "upper"

        return wick_ratio >= self.wick_ratio_min

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence (0.0-1.0)."""
        if not self.detect(candles):
            return 0.0

        candle = candles[-1]
        total_range = candle.total_range
        if total_range == 0:
            return 0.0

        body_ratio = candle.body_size / total_range
        longer_wick = max(candle.lower_wick, candle.upper_wick)
        wick_ratio = longer_wick / candle.body_size if candle.body_size > 0 else 0

        # Higher wick ratio = higher confidence
        # Lower body ratio = higher confidence
        wick_score = min(wick_ratio / 3.0, 1.0)  # Normalize to 0-1
        body_score = 1.0 - body_ratio
        return (wick_score * 0.6 + body_score * 0.4)

    def direction(self) -> str:
        """Pin bar direction based on which wick is longer."""
        if self._longer_wick_type == "lower":
            return "BULL"  # Lower wick = bullish rejection
        elif self._longer_wick_type == "upper":
            return "BEAR"  # Upper wick = bearish rejection
        return "NEUTRAL"


class EngulfingPattern(PatternDetector):
    """Engulfing: Current candle completely engulfs previous candle."""

    def __init__(self):
        super().__init__("Engulfing", PatternType.ENGULFING)
        self.is_bullish = True  # Set by detect()

    def detect(self, candles: List[Candle]) -> bool:
        """Detect engulfing pattern."""
        if len(candles) < 2:
            return False

        prev = candles[-2]
        curr = candles[-1]

        # Check if current completely engulfs previous (high and low contain previous range)
        engulfs = curr.high > prev.high and curr.low < prev.low

        if not engulfs:
            return False

        # Bullish engulfing: current candle is bullish (close > open) after bearish prev
        if curr.is_bullish and prev.is_bearish:
            self.is_bullish = True
            return True

        # Bearish engulfing: current candle is bearish (close < open) after bullish prev
        if curr.is_bearish and prev.is_bullish:
            self.is_bullish = False
            return True

        return False

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        prev = candles[-2]
        curr = candles[-1]

        # Confidence based on how much current engulfs previous
        prev_range = prev.high - prev.low
        if prev_range == 0:
            return 0.5

        # How much lower does current go below previous?
        lower_excess = max(0, prev.low - curr.low) / prev_range
        # How much higher does current go above previous?
        upper_excess = max(0, curr.high - prev.high) / prev_range

        return min(0.6 + (lower_excess + upper_excess) / 2.5, 1.0)

    def direction(self) -> str:
        return "BULL" if self.is_bullish else "BEAR"


class InsideBarPattern(PatternDetector):
    """Inside Bar: Current candle is completely inside previous candle's range."""

    def __init__(self):
        super().__init__("Inside Bar", PatternType.INSIDE_BAR)

    def detect(self, candles: List[Candle]) -> bool:
        """Detect inside bar pattern."""
        if len(candles) < 2:
            return False

        prev = candles[-2]
        curr = candles[-1]

        # Current must be completely inside previous range
        return curr.high < prev.high and curr.low > prev.low

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        prev = candles[-2]
        curr = candles[-1]

        prev_range = prev.high - prev.low
        if prev_range == 0:
            return 0.5

        # How much space is there from current to previous boundaries?
        top_space = (prev.high - curr.high) / prev_range
        bottom_space = (curr.low - prev.low) / prev_range

        # More space = more inside = more reliable
        return min(0.65 + (top_space + bottom_space) / 2.0, 1.0)

    def direction(self) -> str:
        return "BULL"  # Neutral pattern


class BreakoutRetestPattern(PatternDetector):
    """Breakout Retest: Price breaks level then returns to test it."""

    def __init__(self):
        super().__init__("Breakout Retest", PatternType.BREAKOUT_RETEST)

    def detect(self, candles: List[Candle]) -> bool:
        """Detect breakout retest (simplified: 3-candle pattern)."""
        if len(candles) < 3:
            return False

        # Candle 1: Consolidation
        # Candle 2: Breakout beyond candle 1
        # Candle 3: Retest back into candle 1 range
        c1 = candles[-3]
        c2 = candles[-2]
        c3 = candles[-1]

        range_1 = c1.high - c1.low
        if range_1 == 0:
            return False

        # Candle 2 should break above or below candle 1
        breaks_high = c2.high > c1.high and c2.close > c1.high
        breaks_low = c2.low < c1.low and c2.close < c1.low

        # Candle 3 should retest the level
        retests_high = c3.high >= c1.high and c3.low < c1.high
        retests_low = c3.low <= c1.low and c3.high > c1.low

        return (breaks_high and retests_high) or (breaks_low and retests_low)

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        c1 = candles[-3]
        c2 = candles[-2]
        c3 = candles[-1]

        # More extreme breakout = higher confidence
        range_1 = c1.high - c1.low
        if range_1 == 0:
            return 0.5

        breakout_size = max(abs(c2.high - c1.high), abs(c2.low - c1.low)) / range_1
        return min(0.3 + breakout_size * 0.7, 1.0)

    def direction(self) -> str:
        return "BULL"


class HammerPattern(PatternDetector):
    """Hammer: Long lower wick with small body at top (bullish reversal)."""

    def __init__(self):
        super().__init__("Hammer", PatternType.HAMMER)
        self.wick_body_ratio = 2.0

    def detect(self, candles: List[Candle]) -> bool:
        """Detect hammer pattern."""
        if len(candles) < 1:
            return False

        candle = candles[-1]
        if candle.body_size == 0 or candle.total_range == 0:
            return False

        # Hammer: lower wick is 2x+ longer than body
        # Upper wick should be minimal (less than lower wick)
        if candle.lower_wick < self.wick_body_ratio * candle.body_size:
            return False

        # Upper wick should be smaller than lower wick
        return candle.upper_wick < candle.lower_wick

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        candle = candles[-1]
        if candle.body_size == 0:
            return 0.0

        wick_ratio = candle.lower_wick / candle.body_size
        wick_score = min(wick_ratio / 3.0, 1.0)
        upper_wick_score = 1.0 - (candle.upper_wick / candle.total_range)

        return wick_score * 0.7 + upper_wick_score * 0.3

    def direction(self) -> str:
        return "BULL"


class ShootingStarPattern(PatternDetector):
    """Shooting Star: Long upper wick with small body at bottom (bearish reversal)."""

    def __init__(self):
        super().__init__("Shooting Star", PatternType.SHOOTING_STAR)
        self.wick_body_ratio = 2.0

    def detect(self, candles: List[Candle]) -> bool:
        """Detect shooting star pattern."""
        if len(candles) < 1:
            return False

        candle = candles[-1]
        if candle.body_size == 0 or candle.total_range == 0:
            return False

        # Shooting star: upper wick is 2x+ longer than body
        if candle.upper_wick < self.wick_body_ratio * candle.body_size:
            return False

        # Lower wick should be minimal
        return candle.lower_wick <= candle.body_size

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        candle = candles[-1]
        if candle.body_size == 0:
            return 0.0

        wick_ratio = candle.upper_wick / candle.body_size
        wick_score = min(wick_ratio / 3.0, 1.0)
        lower_wick_score = 1.0 - (candle.lower_wick / candle.total_range)

        return wick_score * 0.7 + lower_wick_score * 0.3

    def direction(self) -> str:
        return "BEAR"


class MorningStarPattern(PatternDetector):
    """Morning Star: 3-candle bullish reversal (bearish, small, bullish)."""

    def __init__(self):
        super().__init__("Morning Star", PatternType.MORNING_STAR)

    def detect(self, candles: List[Candle]) -> bool:
        """Detect morning star pattern."""
        if len(candles) < 3:
            return False

        c1 = candles[-3]  # Bearish
        c2 = candles[-2]  # Small body (star)
        c3 = candles[-1]  # Bullish

        # C1 must be bearish and large
        if not c1.is_bearish or c1.body_size < c1.total_range * 0.3:
            return False

        # C2 must have small body
        if c2.body_size > c1.body_size * 0.5:
            return False

        # C3 must be bullish and large
        if not c3.is_bullish or c3.body_size < c1.body_size * 0.5:
            return False

        # C3 must close above C1 midpoint (recovery)
        c1_midpoint = (c1.open + c1.close) / 2
        return c3.close > c1_midpoint

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        c1 = candles[-3]
        c3 = candles[-1]

        # How much does C3 recover from C1 low?
        recovery_pct = (c3.close - c1.low) / (c1.high - c1.low) if c1.high != c1.low else 0.5
        return min(0.6 + recovery_pct * 0.4, 1.0)

    def direction(self) -> str:
        return "BULL"


class EveningStarPattern(PatternDetector):
    """Evening Star: 3-candle bearish reversal (bullish, small, bearish)."""

    def __init__(self):
        super().__init__("Evening Star", PatternType.EVENING_STAR)

    def detect(self, candles: List[Candle]) -> bool:
        """Detect evening star pattern."""
        if len(candles) < 3:
            return False

        c1 = candles[-3]  # Bullish
        c2 = candles[-2]  # Small body (star)
        c3 = candles[-1]  # Bearish

        # C1 must be bullish and large
        if not c1.is_bullish or c1.body_size < c1.total_range * 0.3:
            return False

        # C2 must have small body
        if c2.body_size > c1.body_size * 0.5:
            return False

        # C3 must be bearish and large
        if not c3.is_bearish or c3.body_size < c1.body_size * 0.5:
            return False

        # C3 must close below C1 midpoint (reversal)
        c1_midpoint = (c1.open + c1.close) / 2
        return c3.close < c1_midpoint

    def confidence(self, candles: List[Candle]) -> float:
        """Calculate confidence."""
        if not self.detect(candles):
            return 0.0

        c1 = candles[-3]
        c3 = candles[-1]

        # How much does C3 reverse from C1 high?
        reversal_pct = (c1.high - c3.close) / (c1.high - c1.low) if c1.high != c1.low else 0.5
        return min(0.5 + reversal_pct * 0.5, 1.0)

    def direction(self) -> str:
        return "BEAR"


# Pattern registry
PATTERN_DETECTORS = {
    PatternType.PINBAR: PinBarPattern(),
    PatternType.ENGULFING: EngulfingPattern(),
    PatternType.INSIDE_BAR: InsideBarPattern(),
    PatternType.BREAKOUT_RETEST: BreakoutRetestPattern(),
    PatternType.HAMMER: HammerPattern(),
    PatternType.SHOOTING_STAR: ShootingStarPattern(),
    PatternType.MORNING_STAR: MorningStarPattern(),
    PatternType.EVENING_STAR: EveningStarPattern(),
}


def detect_patterns(candles: List[Candle], pattern_list: Optional[List[str]] = None) -> dict:
    """
    Detect all enabled patterns in candle sequence.

    Args:
        candles: List of Candle objects
        pattern_list: List of pattern names to check (default: all)

    Returns:
        Dictionary with pattern results: {pattern_name: {'detected': bool, 'confidence': float, 'direction': str}}
    """
    if not candles:
        return {}

    if pattern_list is None:
        pattern_list = [p.value for p in PatternType]

    results = {}
    for pattern_name in pattern_list:
        try:
            pattern_type = PatternType(pattern_name)
            detector = PATTERN_DETECTORS[pattern_type]

            detected = detector.detect(candles)
            confidence = detector.confidence(candles) if detected else 0.0
            direction = detector.direction()

            results[pattern_name] = {
                'detected': detected,
                'confidence': round(confidence, 3),
                'direction': direction
            }
        except (ValueError, KeyError):
            results[pattern_name] = {
                'detected': False,
                'confidence': 0.0,
                'direction': 'NEUTRAL'
            }

    return results
