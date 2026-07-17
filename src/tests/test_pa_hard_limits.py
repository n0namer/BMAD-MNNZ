"""
Tests for pa_hard_limits.py (US-PA-003)

Coverage target: 100% including line 121 defensive guard in
PatternLimitTracker.increment() that handles a missing key in _counts.
"""

import pytest
from katana.conditions.pa_hard_limits import (
    PatternResult,
    PatternHardLimits,
    PatternLimitTracker,
    FilterStats,
    apply_hard_limits,
)
from katana.conditions.pa_patterns import PatternType


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_result(
    pattern_type: PatternType = PatternType.PINBAR,
    confidence: float = 0.8,
    direction: str = "BULL",
    timestamp: str = "2024-01-01T00:00:00",
    signal_contribution: float = 0.5,
) -> PatternResult:
    return PatternResult(
        pattern_type=pattern_type,
        confidence=confidence,
        direction=direction,
        timestamp=timestamp,
        signal_contribution=signal_contribution,
    )


# ---------------------------------------------------------------------------
# PatternHardLimits
# ---------------------------------------------------------------------------

class TestPatternHardLimits:

    def test_default_confidence_threshold(self):
        limits = PatternHardLimits()
        assert limits.confidence_threshold == 0.6

    def test_get_pattern_limit_pinbar(self):
        limits = PatternHardLimits()
        assert limits.get_pattern_limit(PatternType.PINBAR) == 5

    def test_get_pattern_limit_engulfing(self):
        limits = PatternHardLimits()
        assert limits.get_pattern_limit(PatternType.ENGULFING) == 4

    def test_get_pattern_limit_hammer(self):
        limits = PatternHardLimits()
        assert limits.get_pattern_limit(PatternType.HAMMER) == 3

    def test_get_pattern_limit_other(self):
        limits = PatternHardLimits()
        # INSIDE_BAR falls into 'other'
        assert limits.get_pattern_limit(PatternType.INSIDE_BAR) == 2
        assert limits.get_pattern_limit(PatternType.SHOOTING_STAR) == 2
        assert limits.get_pattern_limit(PatternType.MORNING_STAR) == 2
        assert limits.get_pattern_limit(PatternType.EVENING_STAR) == 2
        assert limits.get_pattern_limit(PatternType.BREAKOUT_RETEST) == 2

    def test_passes_confidence_filter_above_threshold(self):
        limits = PatternHardLimits()
        result = make_result(confidence=0.7)
        assert limits.passes_confidence_filter(result) is True

    def test_passes_confidence_filter_at_threshold(self):
        limits = PatternHardLimits()
        result = make_result(confidence=0.6)
        assert limits.passes_confidence_filter(result) is True

    def test_passes_confidence_filter_below_threshold(self):
        limits = PatternHardLimits()
        result = make_result(confidence=0.59)
        assert limits.passes_confidence_filter(result) is False

    def test_custom_limits(self):
        limits = PatternHardLimits(
            confidence_threshold=0.75,
            pin_bar_max=10,
            engulfing_max=8,
            hammer_max=6,
            other_max=4,
        )
        assert limits.confidence_threshold == 0.75
        assert limits.get_pattern_limit(PatternType.PINBAR) == 10
        assert limits.get_pattern_limit(PatternType.ENGULFING) == 8
        assert limits.get_pattern_limit(PatternType.HAMMER) == 6
        assert limits.get_pattern_limit(PatternType.INSIDE_BAR) == 4


# ---------------------------------------------------------------------------
# PatternLimitTracker
# ---------------------------------------------------------------------------

class TestPatternLimitTracker:

    def test_initial_counts_are_zero(self):
        tracker = PatternLimitTracker()
        for pt in PatternType:
            assert tracker.get_count(pt) == 0

    def test_increment_increases_count(self):
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.PINBAR)
        assert tracker.get_count(PatternType.PINBAR) == 1

    def test_increment_multiple_times(self):
        tracker = PatternLimitTracker()
        for _ in range(3):
            tracker.increment(PatternType.HAMMER)
        assert tracker.get_count(PatternType.HAMMER) == 3

    def test_get_count_returns_zero_for_missing_key(self):
        tracker = PatternLimitTracker()
        # _counts is pre-populated, but get_count uses .get() with default 0
        assert tracker.get_count(PatternType.BREAKOUT_RETEST) == 0

    def test_get_pattern_counts_returns_copy(self):
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.ENGULFING)
        counts = tracker.get_pattern_counts()
        assert counts[PatternType.ENGULFING] == 1
        # Mutating the returned copy does not affect internal state
        counts[PatternType.ENGULFING] = 99
        assert tracker.get_count(PatternType.ENGULFING) == 1

    def test_has_room_below_limit(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        assert tracker.has_room(PatternType.PINBAR, limits) is True

    def test_has_room_at_limit(self):
        limits = PatternHardLimits(pin_bar_max=2)
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.PINBAR)
        tracker.increment(PatternType.PINBAR)
        assert tracker.has_room(PatternType.PINBAR, limits) is False

    def test_is_exhausted_false_when_room(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        assert tracker.is_exhausted(PatternType.PINBAR, limits) is False

    def test_is_exhausted_true_when_at_limit(self):
        limits = PatternHardLimits(hammer_max=1)
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.HAMMER)
        assert tracker.is_exhausted(PatternType.HAMMER, limits) is True

    def test_get_exhausted_patterns_empty(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        assert tracker.get_exhausted_patterns(limits) == []

    def test_get_exhausted_patterns_some_exhausted(self):
        limits = PatternHardLimits(engulfing_max=1)
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.ENGULFING)
        exhausted = tracker.get_exhausted_patterns(limits)
        assert PatternType.ENGULFING in exhausted

    def test_reset_clears_all_counts(self):
        tracker = PatternLimitTracker()
        tracker.increment(PatternType.PINBAR)
        tracker.increment(PatternType.HAMMER)
        tracker.reset()
        for pt in PatternType:
            assert tracker.get_count(pt) == 0

    def test_increment_with_missing_key_initializes_to_zero(self):
        """
        Line 121: `if pattern_type not in self._counts:`

        The __post_init__ method pre-populates _counts for all PatternType
        enum members. The `if pattern_type not in self._counts` guard on
        line 121 is therefore never reached in normal operation.

        To exercise this branch, we directly remove a key from the internal
        _counts dict, then call increment() for that pattern type. The guard
        must detect the missing entry, initialize it to 0, and then increment
        to 1.
        """
        tracker = PatternLimitTracker()

        # Force the defensive branch: remove an existing key so _counts no
        # longer contains it.
        del tracker._counts[PatternType.MORNING_STAR]
        assert PatternType.MORNING_STAR not in tracker._counts

        # increment() must hit line 121 (key absent), set _counts[key] = 0,
        # then add 1, resulting in count == 1.
        tracker.increment(PatternType.MORNING_STAR)

        assert tracker.get_count(PatternType.MORNING_STAR) == 1


# ---------------------------------------------------------------------------
# apply_hard_limits
# ---------------------------------------------------------------------------

class TestApplyHardLimits:

    def test_empty_results(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        filtered, stats = apply_hard_limits([], tracker, limits)
        assert filtered == []
        assert stats.total_input == 0
        assert stats.total_filtered == 0
        assert stats.avg_confidence_passed == 0.0
        assert stats.avg_signal_contribution == 0.0

    def test_all_pass(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        results = [make_result(confidence=0.9, signal_contribution=0.6)]
        filtered, stats = apply_hard_limits(results, tracker, limits)
        assert len(filtered) == 1
        assert stats.total_filtered == 1
        assert stats.confidence_filtered == 0
        assert stats.occurrence_filtered == 0
        assert stats.avg_confidence_passed == pytest.approx(0.9)
        assert stats.avg_signal_contribution == pytest.approx(0.6)

    def test_confidence_filter_rejects_low_confidence(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        results = [make_result(confidence=0.3)]
        filtered, stats = apply_hard_limits(results, tracker, limits)
        assert len(filtered) == 0
        assert stats.confidence_filtered == 1
        assert stats.occurrence_filtered == 0

    def test_occurrence_filter_rejects_over_limit(self):
        limits = PatternHardLimits(pin_bar_max=1)
        tracker = PatternLimitTracker()
        # First result passes, second is rejected by occurrence limit
        results = [
            make_result(pattern_type=PatternType.PINBAR, confidence=0.9),
            make_result(pattern_type=PatternType.PINBAR, confidence=0.9),
        ]
        filtered, stats = apply_hard_limits(results, tracker, limits)
        assert len(filtered) == 1
        assert stats.occurrence_filtered == 1

    def test_both_filters_combined(self):
        limits = PatternHardLimits(pin_bar_max=1)
        tracker = PatternLimitTracker()
        results = [
            make_result(pattern_type=PatternType.PINBAR, confidence=0.2),   # fails confidence
            make_result(pattern_type=PatternType.PINBAR, confidence=0.9),   # passes both
            make_result(pattern_type=PatternType.PINBAR, confidence=0.9),   # fails occurrence
        ]
        filtered, stats = apply_hard_limits(results, tracker, limits)
        assert len(filtered) == 1
        assert stats.confidence_filtered == 1
        assert stats.occurrence_filtered == 1

    def test_pattern_distribution_populated(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        results = [
            make_result(pattern_type=PatternType.PINBAR, confidence=0.8),
            make_result(pattern_type=PatternType.HAMMER, confidence=0.7),
            make_result(pattern_type=PatternType.PINBAR, confidence=0.9),
        ]
        filtered, stats = apply_hard_limits(results, tracker, limits)
        assert stats.pattern_distribution[PatternType.PINBAR] == 2
        assert stats.pattern_distribution[PatternType.HAMMER] == 1

    def test_exhausted_patterns_reported_in_stats(self):
        limits = PatternHardLimits(engulfing_max=1)
        tracker = PatternLimitTracker()
        results = [
            make_result(pattern_type=PatternType.ENGULFING, confidence=0.9),
            make_result(pattern_type=PatternType.ENGULFING, confidence=0.9),
        ]
        _, stats = apply_hard_limits(results, tracker, limits)
        assert PatternType.ENGULFING in stats.exhausted_patterns

    def test_tracker_counts_updated_after_filter(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        results = [make_result(pattern_type=PatternType.HAMMER, confidence=0.8)]
        apply_hard_limits(results, tracker, limits)
        assert tracker.get_count(PatternType.HAMMER) == 1

    def test_avg_confidence_calculated_correctly(self):
        limits = PatternHardLimits()
        tracker = PatternLimitTracker()
        results = [
            make_result(confidence=0.8, signal_contribution=0.4),
            make_result(confidence=0.6, signal_contribution=0.6),
        ]
        _, stats = apply_hard_limits(results, tracker, limits)
        assert stats.avg_confidence_passed == pytest.approx(0.7)
        assert stats.avg_signal_contribution == pytest.approx(0.5)
