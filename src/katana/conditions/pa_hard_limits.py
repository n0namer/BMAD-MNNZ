"""
Pattern Analysis Hard Limits and Confidence Filter Module (US-PA-003)

Implements:
- Confidence threshold filtering (min 0.6 for signal generation)
- Pattern occurrence hard limits:
  * Pin Bar: max 5 per session
  * Engulfing: max 4 per session
  * Hammer: max 3 per session
  * Other patterns: max 2 per session
- Result filtering function with combined constraints
- Pattern exhaustion tracking and detection

This module enforces both confidence and occurrence-based filtering to ensure
high-quality signal generation while preventing pattern dominance bias.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum

from .pa_patterns import PatternType


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class PatternResult:
    """Represents a detected pattern result."""

    pattern_type: PatternType
    """Type of the detected pattern."""

    confidence: float
    """Confidence score (0.0-1.0) for the pattern."""

    direction: str
    """Bullish ('BULL') or bearish ('BEAR') direction."""

    timestamp: str
    """ISO timestamp when pattern was detected."""

    signal_contribution: float
    """How much this pattern contributes to overall signal (0.0-1.0)."""


@dataclass
class PatternHardLimits:
    """Configuration for pattern hard limits."""

    confidence_threshold: float = 0.6
    """Minimum confidence required for pattern to pass filter."""

    pin_bar_max: int = 5
    """Maximum Pin Bar occurrences per session."""

    engulfing_max: int = 4
    """Maximum Engulfing occurrences per session."""

    hammer_max: int = 3
    """Maximum Hammer occurrences per session."""

    other_max: int = 2
    """Maximum occurrences for all other patterns per session."""

    def get_pattern_limit(self, pattern_type: PatternType) -> int:
        """
        Get the occurrence limit for a specific pattern type.

        Args:
            pattern_type: The pattern type to get limit for.

        Returns:
            The maximum occurrences allowed for this pattern.
        """
        if pattern_type == PatternType.PINBAR:
            return self.pin_bar_max
        elif pattern_type == PatternType.ENGULFING:
            return self.engulfing_max
        elif pattern_type == PatternType.HAMMER:
            return self.hammer_max
        else:
            # All other patterns share the same limit
            return self.other_max

    def passes_confidence_filter(self, result: PatternResult) -> bool:
        """
        Check if a pattern result passes the confidence threshold filter.

        Args:
            result: The pattern result to check.

        Returns:
            True if confidence >= threshold, False otherwise.
        """
        return result.confidence >= self.confidence_threshold


@dataclass
class PatternLimitTracker:
    """Tracks pattern occurrences and enforces hard limits."""

    _counts: Dict[PatternType, int] = field(default_factory=dict)
    """Internal counter for each pattern type."""

    def __post_init__(self):
        """Initialize counters for all pattern types."""
        if not self._counts:
            for pattern_type in PatternType:
                self._counts[pattern_type] = 0

    def increment(self, pattern_type: PatternType) -> None:
        """
        Increment the count for a pattern type.

        Args:
            pattern_type: The pattern type to increment.
        """
        if pattern_type not in self._counts:
            self._counts[pattern_type] = 0
        self._counts[pattern_type] += 1

    def get_count(self, pattern_type: PatternType) -> int:
        """
        Get the current count for a pattern type.

        Args:
            pattern_type: The pattern type to get count for.

        Returns:
            The current occurrence count.
        """
        return self._counts.get(pattern_type, 0)

    def get_pattern_counts(self) -> Dict[PatternType, int]:
        """
        Get all pattern counts.

        Returns:
            Dictionary mapping pattern types to their counts.
        """
        return self._counts.copy()

    def has_room(
        self, pattern_type: PatternType, limits: PatternHardLimits
    ) -> bool:
        """
        Check if a pattern still has room (hasn't hit its limit).

        Args:
            pattern_type: The pattern type to check.
            limits: The hard limits configuration.

        Returns:
            True if count < limit, False if at or above limit.
        """
        current_count = self.get_count(pattern_type)
        limit = limits.get_pattern_limit(pattern_type)
        return current_count < limit

    def is_exhausted(
        self, pattern_type: PatternType, limits: PatternHardLimits
    ) -> bool:
        """
        Check if a pattern has reached its hard limit (exhausted).

        Args:
            pattern_type: The pattern type to check.
            limits: The hard limits configuration.

        Returns:
            True if count >= limit, False otherwise.
        """
        return not self.has_room(pattern_type, limits)

    def get_exhausted_patterns(
        self, limits: PatternHardLimits
    ) -> List[PatternType]:
        """
        Get list of patterns that have reached their hard limits.

        Args:
            limits: The hard limits configuration.

        Returns:
            List of exhausted pattern types.
        """
        exhausted = []
        for pattern_type in PatternType:
            if self.is_exhausted(pattern_type, limits):
                exhausted.append(pattern_type)
        return exhausted

    def reset(self) -> None:
        """Reset all pattern counts to zero."""
        for pattern_type in PatternType:
            self._counts[pattern_type] = 0


# ============================================================================
# FILTERING FUNCTIONS
# ============================================================================

@dataclass
class FilterStats:
    """Statistics from hard limits filtering operation."""

    total_input: int = 0
    """Total number of input results."""

    total_filtered: int = 0
    """Number of results that passed both filters."""

    confidence_filtered: int = 0
    """Number of results rejected by confidence threshold."""

    occurrence_filtered: int = 0
    """Number of results rejected by occurrence limit."""

    avg_confidence_passed: float = 0.0
    """Average confidence of results that passed filters."""

    avg_signal_contribution: float = 0.0
    """Average signal contribution of filtered results."""

    pattern_distribution: Dict[PatternType, int] = field(default_factory=dict)
    """Distribution of filtered patterns by type."""

    exhausted_patterns: List[PatternType] = field(default_factory=list)
    """Patterns that reached their hard limits."""


def apply_hard_limits(
    results: List[PatternResult],
    tracker: PatternLimitTracker,
    limits: PatternHardLimits,
) -> Tuple[List[PatternResult], FilterStats]:
    """
    Apply hard limits and confidence filtering to pattern results.

    This function applies two levels of filtering:
    1. Confidence threshold filter: Patterns below min confidence are rejected
    2. Occurrence limit filter: Patterns that hit their hard limit are rejected

    After filtering, the tracker is updated with successful patterns and
    comprehensive statistics are generated.

    Args:
        results: List of pattern results to filter.
        tracker: Tracker to maintain pattern occurrence counts.
        limits: Hard limits configuration.

    Returns:
        Tuple of (filtered_results, stats)
        - filtered_results: List of results that passed both filters
        - stats: FilterStats dataclass with filtering statistics

    Example:
        >>> limits = PatternHardLimits()
        >>> tracker = PatternLimitTracker()
        >>> results = [...]  # List of PatternResult
        >>> filtered, stats = apply_hard_limits(results, tracker, limits)
        >>> print(f"Passed: {len(filtered)}/{len(results)}")
        >>> print(f"Confidence filtered: {stats.confidence_filtered}")
    """
    filtered_results = []
    confidence_rejected = 0
    occurrence_rejected = 0
    pattern_counts = {}
    confidence_sum = 0.0
    contribution_sum = 0.0

    for result in results:
        # Stage 1: Confidence threshold filter
        if not limits.passes_confidence_filter(result):
            confidence_rejected += 1
            continue

        # Stage 2: Occurrence limit filter
        if not tracker.has_room(result.pattern_type, limits):
            occurrence_rejected += 1
            continue

        # Result passed both filters
        filtered_results.append(result)
        tracker.increment(result.pattern_type)

        # Update statistics
        pattern_counts[result.pattern_type] = (
            pattern_counts.get(result.pattern_type, 0) + 1
        )
        confidence_sum += result.confidence
        contribution_sum += result.signal_contribution

    # Calculate final statistics
    avg_confidence = (
        confidence_sum / len(filtered_results)
        if filtered_results
        else 0.0
    )
    avg_contribution = (
        contribution_sum / len(filtered_results)
        if filtered_results
        else 0.0
    )

    exhausted = tracker.get_exhausted_patterns(limits)

    stats = FilterStats(
        total_input=len(results),
        total_filtered=len(filtered_results),
        confidence_filtered=confidence_rejected,
        occurrence_filtered=occurrence_rejected,
        avg_confidence_passed=avg_confidence,
        avg_signal_contribution=avg_contribution,
        pattern_distribution=pattern_counts,
        exhausted_patterns=exhausted,
    )

    return filtered_results, stats
