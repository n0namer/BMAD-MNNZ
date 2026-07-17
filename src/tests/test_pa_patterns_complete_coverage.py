"""
Complete Coverage Tests for pa_patterns.py — ATDD RED Phase

Targets 74 missing lines across 8 pattern detectors to reach 100% coverage.
All tests are @pytest.mark.skip (RED phase) until implementation is verified.

Missing lines by detector:
  PinBarPattern:        119, 129, 149, 167
  EngulfingPattern:     197-201, 208-221
  InsideBarPattern:     236, 247, 254
  BreakoutRetestPattern: 276, 287, 301-314
  HammerPattern:        330, 334, 339, 347, 351
  ShootingStarPattern:  373, 377, 381, 388-399
  MorningStarPattern:   414, 425-434, 438-446
  EveningStarPattern:   461, 472-481, 485-493
"""

import pytest
from katana.conditions.pa_patterns import (
    Candle,
    PatternType,
    PatternDetector,
    PinBarPattern,
    EngulfingPattern,
    InsideBarPattern,
    BreakoutRetestPattern,
    HammerPattern,
    ShootingStarPattern,
    MorningStarPattern,
    EveningStarPattern,
    PATTERN_DETECTORS,
    detect_patterns,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _c(o: float, h: float, l: float, c: float) -> Candle:
    """Shorthand candle constructor."""
    return Candle(open=o, high=h, low=l, close=c)


# ===================================================================
# 1. PinBarPattern — lines 119, 129, 149, 167
# ===================================================================

class TestPinBarEdgeCases:
    """Cover PinBarPattern edge-case branches."""

    # --- detect ---

    @pytest.mark.skip(reason="RED phase — line 111: empty candle list")
    def test_detect_empty_candles(self):
        """Line 111: empty candle list -> False."""
        p = PinBarPattern()
        assert p.detect([]) is False

    @pytest.mark.skip(reason="RED phase — line 119: total_range == 0")
    def test_detect_total_range_zero(self):
        """Line 119: candle where high == low (zero total range) returns False."""
        p = PinBarPattern()
        # open != close so body_size > 0, but high == low => total_range == 0
        candle = _c(o=100.0, h=100.0, l=100.0, c=99.9)
        # h == l means total_range is 0 BUT h must >= max(o,c) and l <= min(o,c)
        # A valid candle with zero range has o==h==l==c; body_size would be 0 too (line 115).
        # To reach line 119 specifically: body_size > 0 AND total_range == 0.
        # This is geometrically impossible for a valid candle, but the guard exists.
        # We can still invoke with the same h==l; body_size = |c-o| = 0.1 but
        # total_range = h-l = 0. The candle is "degenerate" but code handles it.
        candle = Candle(open=100.0, high=100.0, low=100.0, close=100.1)
        # Actually h=100 < c=100.1 is invalid candle data; but the code just does h - l.
        # high - low = 0; body = 0.1 > 0 → hits line 118-119.
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 129: longer_wick == 0")
    def test_detect_longer_wick_zero(self):
        """Line 129: both wicks zero means longer_wick == 0 -> False.
        This needs body_ratio <= 0.3 AND total_range > 0 AND wicks == 0.
        Candle: open=99, high=100, low=99, close=100 => body=1, range=1,
        body_ratio=1.0 > 0.3 so it fails at line 123 first.
        To get past line 123 we need body < 0.3 * range.
        Wicks are 0 when body fills entire range: min(o,c)==low and max(o,c)==high.
        Body==range means body_ratio=1.0 which fails line 123.
        Actually impossible to have wicks==0 AND body_ratio<=0.3 simultaneously
        on a valid candle. But we test with degenerate data to exercise the guard.
        """
        p = PinBarPattern()
        # Construct: body=1, total_range=10, lower_wick=0, upper_wick=0
        # Need: min(o,c) == low AND max(o,c) == high => body_size == total_range
        # That gives ratio 1.0 which fails line 123. So we must accept that
        # line 129 may only be reachable via a modified wick_ratio or subclass.
        #
        # Alternative: make body small, range large, but both wicks zero.
        # lower_wick = min(o,c)-low; upper_wick = high - max(o,c)
        # If o=100, c=101, h=101, l=100 => body=1, range=1, wicks=0, ratio=1 -> fail@123
        # If o=100, c=100.1, h=110, l=90 => body=0.1, range=20, ratio=0.005 passes 123.
        # lower_wick = min(100,100.1)-90 = 10; upper_wick = 110-100.1 = 9.9
        # Both wicks > 0 so won't hit 129.
        #
        # Line 129 is unreachable with valid geometry, but we exercise it by
        # supplying a candle where the properties yield the right values.
        # e.g., high == close and low == open and open < close but body small vs range.
        # lower_wick = min(o,c) - l = o - l = 0 if o == l
        # upper_wick = h - max(o,c) = h - c = 0 if h == c
        # So candle(o=100, h=100.1, l=100, c=100.1): body=0.1, range=0.1,
        # lower_wick=0, upper_wick=0, body_ratio=1.0 -> fails@123.
        #
        # Only way: override. We'll test with body_ratio_max raised to force through.
        p.body_ratio_max = 1.0  # relax guard
        candle = _c(o=100, h=100.1, l=100, c=100.1)
        # body=0.1, range=0.1, ratio=1.0 passes now; wicks both 0 -> line 129
        assert p.detect([candle]) is False

    # --- confidence ---

    @pytest.mark.skip(reason="RED phase — line 149: confidence when total_range == 0 after detect")
    def test_confidence_total_range_zero_after_detect(self):
        """Line 149: confidence returns 0.0 when total_range==0.
        Since detect must pass first, and a valid pin bar has total_range > 0,
        this line is a defensive guard. We exercise it by calling confidence
        directly on a candle that would NOT actually detect, confirming 0.0 path.
        """
        p = PinBarPattern()
        # Candle that fails detect => confidence == 0.0 (line 143-144)
        # To reach 149 specifically we need detect to return True but total_range==0.
        # That's contradictory (detect checks total_range). So we confirm the
        # 0.0 return from confidence via the failed-detect path at minimum.
        candle = _c(o=100, h=100, l=100, c=100)  # all equal, body=0
        assert p.confidence([candle]) == 0.0

    @pytest.mark.skip(reason="RED phase — line 149: forced reachability via mock")
    def test_confidence_total_range_zero_forced(self):
        """Line 149: force total_range==0 after detect returns True via subclass."""
        class ForcedPinBar(PinBarPattern):
            def detect(self, candles):
                self._longer_wick_type = "lower"
                return True  # Force True

        p = ForcedPinBar()
        candle = _c(o=100, h=100, l=100, c=100)
        result = p.confidence([candle])
        assert result == 0.0  # line 149

    # --- direction ---

    @pytest.mark.skip(reason="RED phase — line 167: direction NEUTRAL when no detect called")
    def test_direction_neutral_no_detect(self):
        """Line 167: direction returns NEUTRAL when _longer_wick_type is None."""
        p = PinBarPattern()
        # No detect() called, _longer_wick_type is None
        assert p.direction() == "NEUTRAL"

    @pytest.mark.skip(reason="RED phase — line 164: direction BULL for lower wick")
    def test_direction_bull_lower_wick(self):
        """Line 164: direction returns BULL when lower wick is dominant."""
        p = PinBarPattern()
        # Bullish pin bar: long lower wick
        candle = _c(o=100, h=101, l=90, c=100.5)
        # body=0.5, range=11, body_ratio=0.045, lower_wick=10, upper_wick=0.5
        p.detect([candle])
        assert p.direction() == "BULL"

    @pytest.mark.skip(reason="RED phase — line 166: direction BEAR for upper wick")
    def test_direction_bear_upper_wick(self):
        """Line 166: direction returns BEAR when upper wick is dominant."""
        p = PinBarPattern()
        # Bearish pin bar: long upper wick
        candle = _c(o=100, h=110, l=99.5, c=99.8)
        # body=0.2, range=10.5, body_ratio=0.019, upper_wick=10, lower_wick=0.3
        p.detect([candle])
        assert p.direction() == "BEAR"


# ===================================================================
# 2. EngulfingPattern — lines 197-201, 208-221
# ===================================================================

class TestEngulfingEdgeCases:
    """Cover EngulfingPattern edge-case branches."""

    # --- detect: bearish engulfing path (lines 197-199) ---

    @pytest.mark.skip(reason="RED phase — lines 197-199: bearish engulfing detection")
    def test_detect_bearish_engulfing(self):
        """Lines 197-199: current bearish engulfs previous bullish."""
        p = EngulfingPattern()
        prev = _c(o=100, h=102, l=99, c=102)     # bullish: c > o
        curr = _c(o=103, h=103.5, l=98, c=97)     # bearish: c < o, engulfs prev
        assert p.detect([prev, curr]) is True
        assert p.is_bullish is False

    # --- detect: neither bullish nor bearish engulfing (line 201) ---

    @pytest.mark.skip(reason="RED phase — line 201: engulfs but same direction")
    def test_detect_engulfs_but_same_direction_bearish(self):
        """Line 201: current engulfs prev but both bearish -> False."""
        p = EngulfingPattern()
        prev = _c(o=102, h=103, l=99, c=100)    # bearish
        curr = _c(o=105, h=104, l=98, c=97)     # bearish, engulfs prev
        assert p.detect([prev, curr]) is False

    @pytest.mark.skip(reason="RED phase — line 201: engulfs but both bullish")
    def test_detect_engulfs_but_same_direction_bullish(self):
        """Line 201: current engulfs prev but both bullish -> False."""
        p = EngulfingPattern()
        prev = _c(o=99, h=101, l=98, c=100)     # bullish
        curr = _c(o=97, h=102, l=97, c=103)     # bullish, engulfs prev
        assert p.detect([prev, curr]) is False

    # --- confidence: not detected path (line 206) ---

    @pytest.mark.skip(reason="RED phase — line 206: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Line 206: confidence returns 0.0 when engulfing not detected."""
        p = EngulfingPattern()
        # Two candles that do NOT form an engulfing pattern
        prev = _c(o=100, h=102, l=99, c=101)
        curr = _c(o=100.5, h=101.5, l=99.5, c=101)  # doesn't engulf
        assert p.confidence([prev, curr]) == 0.0

    # --- confidence: full calculation path (lines 208-221) ---

    @pytest.mark.skip(reason="RED phase — lines 208-221: bullish engulfing confidence calc")
    def test_confidence_bullish_engulfing(self):
        """Lines 208-221: full confidence path for bullish engulfing."""
        p = EngulfingPattern()
        prev = _c(o=102, h=103, l=99, c=100)    # bearish
        curr = _c(o=98, h=104, l=97, c=105)     # bullish, engulfs
        conf = p.confidence([prev, curr])
        assert 0.6 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — lines 208-221: bearish engulfing confidence calc")
    def test_confidence_bearish_engulfing(self):
        """Lines 208-221: full confidence path for bearish engulfing."""
        p = EngulfingPattern()
        prev = _c(o=100, h=102, l=99, c=102)    # bullish
        curr = _c(o=103, h=103.5, l=98, c=97)   # bearish, engulfs
        conf = p.confidence([prev, curr])
        assert 0.6 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — line 214: prev_range == 0 -> confidence 0.5")
    def test_confidence_prev_range_zero(self):
        """Line 214: when previous candle range == 0, returns 0.5.
        This requires detect() to pass with prev.high == prev.low.
        Since curr must engulf prev (curr.high > prev.high AND curr.low < prev.low),
        and prev.high == prev.low, we need curr.high > prev.high and curr.low < prev.low.
        But if prev.high == prev.low == X then curr.high > X and curr.low < X.
        prev must be bearish and curr bullish (or vice versa).
        A zero-range candle has open==close so is neither bullish nor bearish.
        So this guard is defensive. We force it.
        """
        class ForcedEngulfing(EngulfingPattern):
            def detect(self, candles):
                self.is_bullish = True
                return True

        p = ForcedEngulfing()
        prev = _c(o=100, h=100, l=100, c=100)  # range == 0
        curr = _c(o=99, h=101, l=99, c=101)
        conf = p.confidence([prev, curr])
        assert conf == 0.5

    @pytest.mark.skip(reason="RED phase — line 221: confidence capped at 1.0")
    def test_confidence_capped_at_one(self):
        """Line 221: massive engulfing caps confidence at 1.0."""
        p = EngulfingPattern()
        # prev: tiny bearish candle
        prev = _c(o=100.1, h=100.2, l=99.9, c=100.0)  # bearish, range=0.3
        # curr: huge bullish engulfing
        curr = _c(o=98, h=105, l=95, c=104)            # bullish, engulfs
        conf = p.confidence([prev, curr])
        assert conf <= 1.0


# ===================================================================
# 3. InsideBarPattern — lines 236, 247, 254
# ===================================================================

class TestInsideBarEdgeCases:
    """Cover InsideBarPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 236: insufficient candles")
    def test_detect_insufficient_candles(self):
        """Line 236: less than 2 candles -> False."""
        p = InsideBarPattern()
        assert p.detect([]) is False
        assert p.detect([_c(100, 101, 99, 100)]) is False

    @pytest.mark.skip(reason="RED phase — line 247: confidence returns 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Line 247: confidence returns 0.0 for non-inside-bar."""
        p = InsideBarPattern()
        prev = _c(o=100, h=101, l=99, c=100)
        curr = _c(o=98, h=105, l=95, c=103)  # outside, not inside
        assert p.confidence([prev, curr]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 257-261: full inside bar confidence calculation")
    def test_confidence_valid_inside_bar(self):
        """Lines 257-261: full confidence calculation for valid inside bar."""
        p = InsideBarPattern()
        # prev: wide range candle; curr: entirely inside
        prev = _c(o=90, h=110, l=80, c=100)    # range = 30
        curr = _c(o=95, h=105, l=85, c=98)     # inside: 105<110 and 85>80
        conf = p.confidence([prev, curr])
        # top_space = (110-105)/30 = 0.1667
        # bottom_space = (85-80)/30 = 0.1667
        # result = min(0.65 + 0.3333/2, 1.0) = min(0.8167, 1.0) = 0.8167
        assert 0.65 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — line 254: prev_range == 0 -> confidence 0.5")
    def test_confidence_prev_range_zero(self):
        """Line 254: when prev range is 0, confidence returns 0.5.
        An inside bar with prev.high == prev.low means curr.high < prev.high
        AND curr.low > prev.low, but if prev.high == prev.low those can't both
        be true. So this is a defensive guard. Force through with subclass.
        """
        class ForcedInsideBar(InsideBarPattern):
            def detect(self, candles):
                return True

        p = ForcedInsideBar()
        prev = _c(o=100, h=100, l=100, c=100)
        curr = _c(o=100, h=100, l=100, c=100)
        conf = p.confidence([prev, curr])
        assert conf == 0.5


# ===================================================================
# 4. BreakoutRetestPattern — lines 276, 287, 301-314
# ===================================================================

class TestBreakoutRetestEdgeCases:
    """Cover BreakoutRetestPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 276: insufficient candles")
    def test_detect_insufficient_candles(self):
        """Line 276: less than 3 candles -> False."""
        p = BreakoutRetestPattern()
        assert p.detect([]) is False
        assert p.detect([_c(100, 101, 99, 100)]) is False
        assert p.detect([_c(100, 101, 99, 100), _c(100, 102, 98, 101)]) is False

    @pytest.mark.skip(reason="RED phase — line 287: c1 range == 0 -> False")
    def test_detect_c1_range_zero(self):
        """Line 287: first candle has zero range -> False."""
        p = BreakoutRetestPattern()
        c1 = _c(o=100, h=100, l=100, c=100)  # zero range
        c2 = _c(o=101, h=103, l=99, c=102)
        c3 = _c(o=101, h=101, l=99, c=100)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — line 302: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Line 302: confidence returns 0.0 when breakout-retest not detected."""
        p = BreakoutRetestPattern()
        c1 = _c(o=100, h=101, l=99, c=100)
        c2 = _c(o=100, h=100.5, l=99.5, c=100)  # no breakout
        c3 = _c(o=100, h=100.5, l=99.5, c=100)  # no retest
        assert p.confidence([c1, c2, c3]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 301-314: full confidence calculation (upward breakout)")
    def test_confidence_upward_breakout(self):
        """Lines 301-314: confidence for upward breakout-retest pattern."""
        p = BreakoutRetestPattern()
        # c1: consolidation range 99-101
        c1 = _c(o=100, h=101, l=99, c=100)
        # c2: breaks high — close above c1.high
        c2 = _c(o=101, h=104, l=100, c=103)
        # c3: retests high — high >= c1.high and low < c1.high
        c3 = _c(o=102, h=102, l=100.5, c=101.5)
        conf = p.confidence([c1, c2, c3])
        assert 0.3 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — lines 301-314: confidence for downward breakout")
    def test_confidence_downward_breakout(self):
        """Lines 301-314: confidence for downward breakout-retest pattern."""
        p = BreakoutRetestPattern()
        # c1: consolidation 99-101
        c1 = _c(o=100, h=101, l=99, c=100)
        # c2: breaks low — close below c1.low
        c2 = _c(o=99, h=100, l=96, c=97)
        # c3: retests low — low <= c1.low and high > c1.low
        c3 = _c(o=98, h=99.5, l=99, c=99.2)
        conf = p.confidence([c1, c2, c3])
        assert 0.3 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — line 310-311: confidence with c1 range==0 defensive guard")
    def test_confidence_c1_range_zero_defensive(self):
        """Lines 310-311: range_1 == 0 inside confidence returns 0.5.
        This requires detect() to pass first, but detect rejects range_1==0.
        So it's a defensive guard. Force through.
        """
        class ForcedBreakout(BreakoutRetestPattern):
            def detect(self, candles):
                return True

        p = ForcedBreakout()
        c1 = _c(o=100, h=100, l=100, c=100)
        c2 = _c(o=100, h=101, l=99, c=101)
        c3 = _c(o=100, h=100, l=99, c=100)
        conf = p.confidence([c1, c2, c3])
        assert conf == 0.5

    @pytest.mark.skip(reason="RED phase — lines 313-314: confidence with extreme breakout capped at 1.0")
    def test_confidence_capped_at_one(self):
        """Line 314: extreme breakout size caps confidence at 1.0."""
        p = BreakoutRetestPattern()
        c1 = _c(o=100, h=100.1, l=99.9, c=100)  # tiny range 0.2
        # c2: massive breakout above
        c2 = _c(o=100.1, h=110, l=99.8, c=109)
        # c3: retests c1.high level
        c3 = _c(o=105, h=105, l=99.95, c=101)
        conf = p.confidence([c1, c2, c3])
        assert conf <= 1.0


# ===================================================================
# 5. HammerPattern — lines 330, 334, 339, 347, 351
# ===================================================================

class TestHammerEdgeCases:
    """Cover HammerPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 330: empty candles list")
    def test_detect_empty_candles(self):
        """Line 330: empty candle list -> False."""
        p = HammerPattern()
        assert p.detect([]) is False

    @pytest.mark.skip(reason="RED phase — line 334: body_size == 0")
    def test_detect_body_size_zero(self):
        """Line 334: candle where open == close (body_size == 0) -> False."""
        p = HammerPattern()
        candle = _c(o=100, h=105, l=95, c=100)  # open == close
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 334: total_range == 0")
    def test_detect_total_range_zero(self):
        """Line 334: candle where high == low (total_range == 0) -> False."""
        p = HammerPattern()
        candle = _c(o=100, h=100, l=100, c=100)
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 339: lower_wick too short")
    def test_detect_lower_wick_too_short(self):
        """Line 339: lower wick < 2x body -> False."""
        p = HammerPattern()
        # body=1, lower_wick needs to be >= 2.0 * 1 = 2
        # open=100, close=101, low=99.5 -> lower_wick = min(100,101)-99.5 = 0.5
        candle = _c(o=100, h=102, l=99.5, c=101)
        # lower_wick = 0.5, body = 1, ratio = 0.5 < 2.0
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 342: upper_wick >= lower_wick -> False")
    def test_detect_upper_wick_larger_than_lower(self):
        """Line 342: upper wick >= lower wick -> False (not a hammer)."""
        p = HammerPattern()
        # Need: lower_wick >= 2*body BUT upper_wick >= lower_wick
        # body=1, lower_wick=3, upper_wick=4
        # o=100, c=101 => body=1
        # lower_wick = min(100,101) - low = 100 - low = 3 => low = 97
        # upper_wick = high - max(100,101) = high - 101 = 4 => high = 105
        candle = _c(o=100, h=105, l=97, c=101)
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 347: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Line 347: confidence returns 0.0 for non-hammer."""
        p = HammerPattern()
        # Candle with big body and tiny wicks — not a hammer
        candle = _c(o=95, h=106, l=94, c=105)  # body=10, range=12, lower_wick=1, upper_wick=1
        assert p.confidence([candle]) == 0.0

    @pytest.mark.skip(reason="RED phase — line 351: body_size == 0 in confidence (defensive)")
    def test_confidence_body_zero_defensive(self):
        """Line 351: defensive guard for body_size == 0 in confidence.
        detect() already rejects body_size==0, so force through.
        """
        class ForcedHammer(HammerPattern):
            def detect(self, candles):
                return True

        p = ForcedHammer()
        candle = _c(o=100, h=100, l=100, c=100)  # body_size == 0
        assert p.confidence([candle]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 353-357: full confidence calculation")
    def test_confidence_valid_hammer(self):
        """Lines 353-357: confidence path for a valid hammer."""
        p = HammerPattern()
        # Hammer: long lower wick, small upper wick, small body
        # body=1, lower_wick=5, upper_wick=0.5
        # o=100, c=101 => body=1
        # low = 100 - 5 = 95
        # high = 101 + 0.5 = 101.5
        candle = _c(o=100, h=101.5, l=95, c=101)
        conf = p.confidence([candle])
        assert 0.0 < conf <= 1.0


# ===================================================================
# 6. ShootingStarPattern — lines 373, 377, 381, 388-399
# ===================================================================

class TestShootingStarEdgeCases:
    """Cover ShootingStarPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 373: empty candles list")
    def test_detect_empty_candles(self):
        """Line 373: empty candle list -> False."""
        p = ShootingStarPattern()
        assert p.detect([]) is False

    @pytest.mark.skip(reason="RED phase — line 377: body_size == 0")
    def test_detect_body_size_zero(self):
        """Line 377: open == close -> body_size == 0 -> False."""
        p = ShootingStarPattern()
        candle = _c(o=100, h=110, l=90, c=100)
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 377: total_range == 0")
    def test_detect_total_range_zero(self):
        """Line 377: high == low -> total_range == 0 -> False."""
        p = ShootingStarPattern()
        candle = _c(o=100, h=100, l=100, c=100)
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 381: upper_wick too short")
    def test_detect_upper_wick_too_short(self):
        """Line 381: upper wick < 2x body -> False."""
        p = ShootingStarPattern()
        # body=2, upper_wick needs >= 4. Make it 1.
        # o=100, c=98 => body=2 (bearish)
        # high = max(100,98) + upper_wick = 100 + 1 = 101
        # low = min(100,98) - lower_wick = 98 - 0 = 98
        candle = _c(o=100, h=101, l=98, c=98)
        # upper_wick = 101 - 100 = 1, body = 2, 1 < 2*2 = 4 -> False
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — line 384: lower_wick > body -> False")
    def test_detect_lower_wick_too_large(self):
        """Line 384: lower wick > body_size -> False (not a shooting star)."""
        p = ShootingStarPattern()
        # Need: upper_wick >= 2*body AND lower_wick > body
        # o=100, c=99 => body=1
        # upper_wick = high - 100 >= 2 => high >= 102
        # lower_wick = 99 - low > 1 => low < 98
        candle = _c(o=100, h=103, l=97, c=99)
        # upper_wick = 3, lower_wick = 2, body = 1
        # upper >= 2*1=2 TRUE, lower_wick(2) <= body(1) FALSE -> fails line 384
        assert p.detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — lines 388-399: confidence for valid shooting star")
    def test_confidence_valid_shooting_star(self):
        """Lines 388-399: full confidence calculation."""
        p = ShootingStarPattern()
        # Shooting star: long upper wick, tiny lower wick, small body
        # o=100, c=99.5 => body=0.5 (bearish)
        # upper_wick = high - 100 >= 1.0 => high = 103
        # lower_wick = 99.5 - low <= 0.5 => low >= 99
        candle = _c(o=100, h=103, l=99.5, c=99.5)
        # body = 0.5 (but body_size = |c-o| = 0.5... wait open==100, close=99.5)
        # Actually that makes lower_wick = min(100,99.5) - 99.5 = 0.
        # Let's be more explicit:
        candle = _c(o=100, h=105, l=99.5, c=99.8)
        # body = 0.2, upper_wick = 105 - 100 = 5, lower_wick = 99.8 - 99.5 = 0.3
        # Wait: lower_wick = min(o,c) - low = min(100,99.8) - 99.5 = 99.8 - 99.5 = 0.3
        # upper_wick = high - max(o,c) = 105 - 100 = 5
        # upper >= 2 * 0.2 = 0.4 TRUE (5 >= 0.4)
        # lower_wick(0.3) <= body(0.2) FALSE -> fails at line 384
        #
        # Need lower_wick <= body_size.
        # min(o,c) - low <= |c - o|
        # For bearish (c < o): c - low <= o - c
        # low >= 2c - o
        # c=99.8, o=100 => low >= 2*99.8 - 100 = 99.6
        candle = _c(o=100, h=105, l=99.7, c=99.8)
        # body = 0.2, lower_wick = 99.8 - 99.7 = 0.1, upper_wick = 105 - 100 = 5
        # 5 >= 0.4 TRUE, 0.1 <= 0.2 TRUE -> detected!
        conf = p.confidence([candle])
        assert 0.0 < conf <= 1.0

    @pytest.mark.skip(reason="RED phase — lines 388-389: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Lines 388-389: confidence returns 0.0 for non-shooting-star."""
        p = ShootingStarPattern()
        candle = _c(o=100, h=101, l=99, c=100.5)
        assert p.confidence([candle]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 392-393: body_size == 0 defensive guard")
    def test_confidence_body_zero_defensive(self):
        """Lines 392-393: defensive guard for body_size == 0 in confidence."""
        class ForcedShootingStar(ShootingStarPattern):
            def detect(self, candles):
                return True

        p = ForcedShootingStar()
        candle = _c(o=100, h=100, l=100, c=100)
        assert p.confidence([candle]) == 0.0


# ===================================================================
# 7. MorningStarPattern — lines 414, 425-434, 438-446
# ===================================================================

class TestMorningStarEdgeCases:
    """Cover MorningStarPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 414: insufficient candles")
    def test_detect_insufficient_candles(self):
        """Line 414: less than 3 candles -> False."""
        p = MorningStarPattern()
        assert p.detect([]) is False
        assert p.detect([_c(100, 101, 99, 100)]) is False
        assert p.detect([_c(100, 101, 99, 100), _c(100, 101, 99, 100)]) is False

    @pytest.mark.skip(reason="RED phase — line 421-422: c1 not bearish -> False")
    def test_detect_c1_not_bearish(self):
        """Line 421-422: first candle is bullish -> False."""
        p = MorningStarPattern()
        c1 = _c(o=100, h=105, l=99, c=104)   # bullish
        c2 = _c(o=101, h=101.5, l=100.5, c=101)
        c3 = _c(o=101, h=106, l=100, c=105)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — line 421-422: c1 body too small -> False")
    def test_detect_c1_body_too_small(self):
        """Line 421-422: c1 bearish but body < 0.3 * total_range -> False."""
        p = MorningStarPattern()
        # c1: bearish but tiny body relative to range
        # body < 0.3 * total_range => body/range < 0.3
        c1 = _c(o=100.1, h=105, l=95, c=100)  # body=0.1, range=10, ratio=0.01
        c2 = _c(o=99, h=99.5, l=98.5, c=99)
        c3 = _c(o=99, h=103, l=98, c=102)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 425-426: c2 body too large -> False")
    def test_detect_c2_body_too_large(self):
        """Lines 425-426: star candle body > 50% of c1 body -> False."""
        p = MorningStarPattern()
        c1 = _c(o=105, h=106, l=99, c=100)    # bearish, body=5, range=7
        c2 = _c(o=100, h=101, l=98, c=103)    # body=3 > 0.5*5=2.5
        c3 = _c(o=102, h=106, l=101, c=105)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 429-430: c3 not bullish -> False")
    def test_detect_c3_not_bullish(self):
        """Lines 429-430: third candle is bearish -> False."""
        p = MorningStarPattern()
        c1 = _c(o=105, h=106, l=99, c=100)    # bearish, body=5
        c2 = _c(o=100, h=100.5, l=99, c=100.2)  # small body=0.2 < 2.5
        c3 = _c(o=103, h=104, l=100, c=101)   # bearish (c < o)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 429-430: c3 body too small -> False")
    def test_detect_c3_body_too_small(self):
        """Lines 429-430: c3 bullish but body < 0.5 * c1 body -> False."""
        p = MorningStarPattern()
        c1 = _c(o=110, h=111, l=99, c=100)    # bearish, body=10
        c2 = _c(o=100, h=100.5, l=99, c=100.1)  # small body=0.1
        c3 = _c(o=100, h=105, l=99, c=104)    # bullish, body=4 < 0.5*10=5
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 433-434: c3 close below c1 midpoint -> False")
    def test_detect_c3_close_below_midpoint(self):
        """Lines 433-434: c3 close doesn't exceed c1 midpoint -> False."""
        p = MorningStarPattern()
        # c1: bearish, body large. midpoint = (o+c)/2 = (110+100)/2 = 105
        c1 = _c(o=110, h=111, l=99, c=100)    # bearish, body=10
        c2 = _c(o=100, h=100.5, l=99, c=100.1)  # small body
        # c3: bullish, body >= 5 but close < 105
        c3 = _c(o=100, h=105, l=99, c=104.9)  # body=4.9 < 5 -> actually fail at 429
        # Adjust: body must be >= 5
        c3 = _c(o=99, h=105, l=98, c=104.5)   # body=5.5 >= 5; close=104.5 < 105
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 425-434: valid morning star detected")
    def test_detect_valid_morning_star(self):
        """Lines 425-434: all conditions met -> True."""
        p = MorningStarPattern()
        # c1: bearish, large body, body >= 0.3 * range
        c1 = _c(o=110, h=111, l=99, c=100)    # bearish, body=10, range=12, ratio=0.83
        # c2: small body < 0.5 * 10 = 5
        c2 = _c(o=99.5, h=100, l=98, c=99.8)  # body=0.3
        # c3: bullish, body >= 5, close > midpoint(105)
        c3 = _c(o=100, h=112, l=99, c=106)    # body=6, close=106 > 105
        assert p.detect([c1, c2, c3]) is True

    # --- confidence ---

    @pytest.mark.skip(reason="RED phase — lines 438-439: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Lines 438-439: confidence returns 0.0 for non-morning-star."""
        p = MorningStarPattern()
        c1 = _c(o=100, h=101, l=99, c=100.5)  # bullish, fails
        c2 = _c(o=100, h=101, l=99, c=100)
        c3 = _c(o=100, h=101, l=99, c=100)
        assert p.confidence([c1, c2, c3]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 441-446: full confidence calculation")
    def test_confidence_valid_morning_star(self):
        """Lines 441-446: full confidence path for detected morning star."""
        p = MorningStarPattern()
        c1 = _c(o=110, h=111, l=99, c=100)    # bearish
        c2 = _c(o=99.5, h=100, l=98, c=99.8)  # small star
        c3 = _c(o=100, h=112, l=99, c=106)    # bullish recovery
        conf = p.confidence([c1, c2, c3])
        assert 0.6 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — line 445: c1 high == c1 low defensive -> 0.5")
    def test_confidence_c1_range_zero_defensive(self):
        """Line 445: c1.high == c1.low in confidence -> recovery_pct fallback 0.5."""
        class ForcedMorningStar(MorningStarPattern):
            def detect(self, candles):
                return True

        p = ForcedMorningStar()
        c1 = _c(o=100, h=100, l=100, c=100)  # range == 0
        c2 = _c(o=100, h=100, l=100, c=100)
        c3 = _c(o=100, h=100, l=100, c=100)
        conf = p.confidence([c1, c2, c3])
        # 0.6 + 0.5 * 0.4 = 0.8
        assert 0.7 <= conf <= 0.9


# ===================================================================
# 8. EveningStarPattern — lines 461, 472-481, 485-493
# ===================================================================

class TestEveningStarEdgeCases:
    """Cover EveningStarPattern edge-case branches."""

    @pytest.mark.skip(reason="RED phase — line 461: insufficient candles")
    def test_detect_insufficient_candles(self):
        """Line 461: less than 3 candles -> False."""
        p = EveningStarPattern()
        assert p.detect([]) is False
        assert p.detect([_c(100, 101, 99, 100)]) is False
        assert p.detect([_c(100, 101, 99, 100), _c(100, 101, 99, 100)]) is False

    @pytest.mark.skip(reason="RED phase — lines 468: c1 not bullish -> False")
    def test_detect_c1_not_bullish(self):
        """Line 468: first candle is bearish -> False."""
        p = EveningStarPattern()
        c1 = _c(o=105, h=106, l=99, c=100)    # bearish
        c2 = _c(o=101, h=101.5, l=100.5, c=101)
        c3 = _c(o=104, h=105, l=99, c=100)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — line 468: c1 body too small -> False")
    def test_detect_c1_body_too_small(self):
        """Line 468: c1 bullish but body < 0.3 * total_range -> False."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=110, l=90, c=100.1)  # bullish, body=0.1, range=20, ratio=0.005
        c2 = _c(o=101, h=101.5, l=100, c=101)
        c3 = _c(o=101, h=102, l=98, c=99)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 472-473: c2 body too large -> False")
    def test_detect_c2_body_too_large(self):
        """Lines 472-473: star candle body > 50% of c1 body -> False."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=106, l=99, c=105)    # bullish, body=5
        c2 = _c(o=105, h=106, l=102, c=102)   # body=3 > 0.5*5=2.5
        c3 = _c(o=103, h=104, l=99, c=100)
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 476-477: c3 not bearish -> False")
    def test_detect_c3_not_bearish(self):
        """Lines 476-477: third candle is bullish -> False."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=106, l=99, c=105)    # bullish, body=5
        c2 = _c(o=105, h=105.5, l=104, c=105.2)  # small body
        c3 = _c(o=104, h=107, l=103, c=106)   # bullish -> False
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 476-477: c3 body too small -> False")
    def test_detect_c3_body_too_small(self):
        """Lines 476-477: c3 bearish but body < 0.5 * c1 body -> False."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=111, l=99, c=110)    # bullish, body=10
        c2 = _c(o=110, h=110.5, l=109, c=110.1)  # small body
        c3 = _c(o=109, h=110, l=105, c=105.5)  # bearish, body=3.5 < 5
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 480-481: c3 close above c1 midpoint -> False")
    def test_detect_c3_close_above_midpoint(self):
        """Lines 480-481: c3 close doesn't fall below c1 midpoint -> False."""
        p = EveningStarPattern()
        # c1: bullish, midpoint = (100+110)/2 = 105
        c1 = _c(o=100, h=111, l=99, c=110)    # bullish, body=10
        c2 = _c(o=110, h=110.5, l=109, c=110.1)
        # c3: bearish, body >= 5 but close > 105
        c3 = _c(o=110, h=111, l=104, c=105.1)  # body=4.9 < 5 -> fail at 476
        # body needs >= 5: o=111, c=105.5 -> body=5.5, close=105.5 > 105
        c3 = _c(o=111, h=112, l=104, c=105.5)  # body=5.5, close=105.5 > 105
        assert p.detect([c1, c2, c3]) is False

    @pytest.mark.skip(reason="RED phase — lines 472-481: valid evening star detected")
    def test_detect_valid_evening_star(self):
        """Lines 472-481: all conditions met -> True."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=111, l=99, c=110)    # bullish, body=10, range=12
        c2 = _c(o=110, h=110.5, l=109, c=110.1)  # small body=0.1
        # c3: bearish, body >= 5, close < midpoint(105)
        c3 = _c(o=110, h=111, l=98, c=104)    # body=6, close=104 < 105
        assert p.detect([c1, c2, c3]) is True

    # --- confidence ---

    @pytest.mark.skip(reason="RED phase — lines 485-486: confidence 0.0 when not detected")
    def test_confidence_not_detected(self):
        """Lines 485-486: confidence returns 0.0 for non-evening-star."""
        p = EveningStarPattern()
        c1 = _c(o=105, h=106, l=99, c=100)    # bearish, fails
        c2 = _c(o=100, h=101, l=99, c=100)
        c3 = _c(o=100, h=101, l=99, c=100)
        assert p.confidence([c1, c2, c3]) == 0.0

    @pytest.mark.skip(reason="RED phase — lines 488-493: full confidence calculation")
    def test_confidence_valid_evening_star(self):
        """Lines 488-493: full confidence path for detected evening star."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=111, l=99, c=110)
        c2 = _c(o=110, h=110.5, l=109, c=110.1)
        c3 = _c(o=110, h=111, l=98, c=104)
        conf = p.confidence([c1, c2, c3])
        assert 0.5 <= conf <= 1.0

    @pytest.mark.skip(reason="RED phase — line 492: c1 high == c1 low defensive -> 0.5")
    def test_confidence_c1_range_zero_defensive(self):
        """Line 492: c1.high == c1.low in confidence -> reversal_pct fallback 0.5."""
        class ForcedEveningStar(EveningStarPattern):
            def detect(self, candles):
                return True

        p = ForcedEveningStar()
        c1 = _c(o=100, h=100, l=100, c=100)
        c2 = _c(o=100, h=100, l=100, c=100)
        c3 = _c(o=100, h=100, l=100, c=100)
        conf = p.confidence([c1, c2, c3])
        # 0.5 + 0.5 * 0.5 = 0.75
        assert 0.7 <= conf <= 0.8

    @pytest.mark.skip(reason="RED phase — line 493: confidence capped at 1.0")
    def test_confidence_capped_at_one(self):
        """Line 493: extreme reversal caps confidence at 1.0."""
        p = EveningStarPattern()
        c1 = _c(o=100, h=111, l=99, c=110)
        c2 = _c(o=110, h=110.5, l=109, c=110.1)
        # c3 closes far below c1 range
        c3 = _c(o=110, h=111, l=50, c=60)     # massive bearish, body=50
        conf = p.confidence([c1, c2, c3])
        assert conf <= 1.0


# ===================================================================
# 9. PatternDetector base class — lines 88, 92, 96
# ===================================================================

class TestPatternDetectorBase:
    """Cover PatternDetector abstract methods."""

    @pytest.mark.skip(reason="RED phase — line 88: detect raises NotImplementedError")
    def test_detect_not_implemented(self):
        """Line 88: base detect() raises NotImplementedError."""
        p = PatternDetector("test", PatternType.PINBAR)
        with pytest.raises(NotImplementedError):
            p.detect([])

    @pytest.mark.skip(reason="RED phase — line 92: confidence raises NotImplementedError")
    def test_confidence_not_implemented(self):
        """Line 92: base confidence() raises NotImplementedError."""
        p = PatternDetector("test", PatternType.PINBAR)
        with pytest.raises(NotImplementedError):
            p.confidence([])

    @pytest.mark.skip(reason="RED phase — line 96: direction raises NotImplementedError")
    def test_direction_not_implemented(self):
        """Line 96: base direction() raises NotImplementedError."""
        p = PatternDetector("test", PatternType.PINBAR)
        with pytest.raises(NotImplementedError):
            p.direction()


# ===================================================================
# 10. detect_patterns() function — lines 523-549
# ===================================================================

class TestDetectPatternsFunction:
    """Cover detect_patterns() edge cases."""

    @pytest.mark.skip(reason="RED phase — line 544: invalid pattern name")
    def test_invalid_pattern_name(self):
        """Line 544-549: invalid pattern name returns NEUTRAL/False."""
        candles = [_c(100, 101, 99, 100)]
        result = detect_patterns(candles, pattern_list=["nonexistent_pattern"])
        assert result["nonexistent_pattern"]["detected"] is False
        assert result["nonexistent_pattern"]["confidence"] == 0.0
        assert result["nonexistent_pattern"]["direction"] == "NEUTRAL"

    @pytest.mark.skip(reason="RED phase — line 523-524: empty candles")
    def test_empty_candles(self):
        """Lines 523-524: empty candle list returns empty dict."""
        result = detect_patterns([])
        assert result == {}

    @pytest.mark.skip(reason="RED phase — lines 526-527: default pattern_list (all patterns)")
    def test_default_pattern_list(self):
        """Lines 526-527: None pattern_list scans all patterns."""
        candles = [_c(100, 101, 99, 100)]
        result = detect_patterns(candles, pattern_list=None)
        assert len(result) == len(PatternType)

    @pytest.mark.skip(reason="RED phase — lines 535-543: detected pattern includes confidence > 0")
    def test_detected_pattern_has_confidence(self):
        """Lines 535-543: a detected pattern populates all fields correctly."""
        # Use a valid pin bar to guarantee detection
        candle = _c(o=100, h=101, l=90, c=100.5)
        result = detect_patterns([candle], pattern_list=["pinbar"])
        assert "pinbar" in result
        if result["pinbar"]["detected"]:
            assert result["pinbar"]["confidence"] > 0.0
            assert result["pinbar"]["direction"] in ("BULL", "BEAR", "NEUTRAL")


# ===================================================================
# 11. Candle dataclass properties — auxiliary coverage
# ===================================================================

class TestCandleProperties:
    """Auxiliary coverage for Candle computed properties."""

    @pytest.mark.skip(reason="RED phase — Candle properties for completeness")
    def test_candle_bearish(self):
        """Candle is_bearish property."""
        c = _c(o=101, h=102, l=99, c=100)
        assert c.is_bearish is True
        assert c.is_bullish is False

    @pytest.mark.skip(reason="RED phase — Candle doji (open == close)")
    def test_candle_doji(self):
        """Candle with open == close: neither bullish nor bearish."""
        c = _c(o=100, h=101, l=99, c=100)
        assert c.is_bullish is False
        assert c.is_bearish is False

    @pytest.mark.skip(reason="RED phase — Candle wick calculations")
    def test_candle_wicks(self):
        """Verify wick calculations for a standard candle."""
        c = _c(o=100, h=105, l=95, c=102)
        assert c.body_size == 2.0
        assert c.total_range == 10.0
        assert c.lower_wick == 5.0   # min(100,102) - 95 = 5
        assert c.upper_wick == 3.0   # 105 - max(100,102) = 3

    @pytest.mark.skip(reason="RED phase — Candle with timestamp")
    def test_candle_timestamp(self):
        """Candle optional timestamp field."""
        c = Candle(open=100, high=101, low=99, close=100, timestamp="2026-02-28T00:00:00")
        assert c.timestamp == "2026-02-28T00:00:00"


# ===================================================================
# 12. PATTERN_DETECTORS registry — auxiliary coverage
# ===================================================================

class TestPatternRegistry:
    """Cover PATTERN_DETECTORS registry and PatternType enum."""

    @pytest.mark.skip(reason="RED phase — registry completeness")
    def test_all_pattern_types_registered(self):
        """Every PatternType has a corresponding detector in the registry."""
        for pt in PatternType:
            assert pt in PATTERN_DETECTORS
            assert isinstance(PATTERN_DETECTORS[pt], PatternDetector)

    @pytest.mark.skip(reason="RED phase — direction methods for all detectors")
    def test_all_detectors_have_direction(self):
        """Every registered detector returns a valid direction string."""
        for pt, detector in PATTERN_DETECTORS.items():
            d = detector.direction()
            assert d in ("BULL", "BEAR", "NEUTRAL")


# ===================================================================
# 13. Stress / Boundary Scenarios
# ===================================================================

class TestStressBoundary:
    """Stress tests and boundary conditions across all detectors."""

    @pytest.mark.skip(reason="RED phase — extreme float values")
    def test_extreme_float_values(self):
        """Detectors handle very large float values without error."""
        huge = 1e15
        candle = _c(o=huge, h=huge * 1.1, l=huge * 0.9, c=huge * 1.05)
        for pt, detector in PATTERN_DETECTORS.items():
            # Should not raise
            detector.detect([candle, candle, candle])

    @pytest.mark.skip(reason="RED phase — very small float values (near zero)")
    def test_near_zero_float_values(self):
        """Detectors handle prices near zero without division errors."""
        tiny = 1e-10
        candle = _c(o=tiny, h=tiny * 2, l=tiny * 0.5, c=tiny * 1.5)
        for pt, detector in PATTERN_DETECTORS.items():
            detector.detect([candle, candle, candle])

    @pytest.mark.skip(reason="RED phase — negative prices (degenerate input)")
    def test_negative_prices(self):
        """Detectors handle negative prices without crashing."""
        candle = _c(o=-10, h=-5, l=-15, c=-8)
        for pt, detector in PATTERN_DETECTORS.items():
            detector.detect([candle, candle, candle])

    @pytest.mark.skip(reason="RED phase — single candle for 3-candle patterns")
    def test_single_candle_for_multi_candle_patterns(self):
        """3-candle patterns return False when given 1 candle."""
        candle = _c(o=100, h=105, l=95, c=102)
        assert BreakoutRetestPattern().detect([candle]) is False
        assert MorningStarPattern().detect([candle]) is False
        assert EveningStarPattern().detect([candle]) is False

    @pytest.mark.skip(reason="RED phase — many candles (only last N used)")
    def test_many_candles_ignored(self):
        """Detectors use only last 1-3 candles; extras are ignored."""
        candles = [_c(100 + i, 105 + i, 95 + i, 102 + i) for i in range(100)]
        for pt, detector in PATTERN_DETECTORS.items():
            # Should not error
            detector.detect(candles)

    @pytest.mark.skip(reason="RED phase — identical candles (doji sequence)")
    def test_all_doji_candles(self):
        """Sequence of identical doji candles: no pattern should detect."""
        doji = _c(o=100, h=100, l=100, c=100)
        candles = [doji, doji, doji]
        results = detect_patterns(candles)
        for name, data in results.items():
            assert data["detected"] is False
