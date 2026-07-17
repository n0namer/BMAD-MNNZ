"""
UX-001: Live Monitoring Dashboard - Real-time Callback Tests

ATDD Test Suite for real-time event callbacks and data synchronization.
Tests focus on event emission, listener registration, and data flow.

Story: UX-001 - Live Monitoring Dashboard
Acceptance Criteria: AC13-AC18 (Real-time Updates)

Test Execution Order:
  1. test_callback_registration - Register listeners for events
  2. test_callback_deregistration - Unregister callbacks cleanly
  3. test_callback_event_emission - Events fire correctly
  4. test_callback_event_order - Events fire in correct order
  5. test_callback_with_async_handlers - Handle async callbacks
  6. test_callback_context_preservation - Context maintained across calls

All tests SHOULD FAIL until implementation is complete.
"""

import pytest
import asyncio
from typing import Dict, Any, List, Callable, Awaitable
from unittest.mock import Mock, MagicMock, AsyncMock, patch, call
from datetime import datetime, timedelta


class CallbackRegistry:
    """Mock callback registry for testing."""

    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
        self.event_history: List[Dict[str, Any]] = []

    def register(self, event_name: str, callback: Callable):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def emit(self, event_name: str, data: Any):
        self.event_history.append({
            'event': event_name,
            'data': data,
            'timestamp': datetime.now()
        })
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(data)


class TestDashboardCallbacks:
    """Test suite for UX-001 real-time callbacks.

    Tests focus on:
    - Event listener registration/deregistration
    - Event emission and propagation
    - Callback execution and error handling
    - Async callback support
    - Context and state management
    """

    @pytest.fixture
    def callback_registry(self) -> CallbackRegistry:
        """Fixture: Callback registry."""
        return CallbackRegistry()

    # ============================================================================
    # Callback Registration Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_registration(self, callback_registry):
        """Test registering callbacks for events.

        GIVEN: Empty callback registry
        WHEN: Registering callback for event
        THEN: Callback should be stored and ready
        """
        callback_mock = Mock()

        # WHEN: Register callback
        callback_registry.register('position_updated', callback_mock)

        # THEN: Should be registered
        assert 'position_updated' in callback_registry.listeners
        assert callback_mock in callback_registry.listeners['position_updated']

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_multiple_listeners(self, callback_registry):
        """Test registering multiple listeners for same event.

        GIVEN: Event type
        WHEN: Registering multiple callbacks
        THEN: All should be stored
        """
        callback1 = Mock()
        callback2 = Mock()
        callback3 = Mock()

        # WHEN: Register multiple
        callback_registry.register('position_updated', callback1)
        callback_registry.register('position_updated', callback2)
        callback_registry.register('position_updated', callback3)

        # THEN: All should be registered
        listeners = callback_registry.listeners['position_updated']
        assert len(listeners) == 3
        assert callback1 in listeners
        assert callback2 in listeners
        assert callback3 in listeners

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_deregistration(self, callback_registry):
        """Test removing callbacks.

        GIVEN: Registered callbacks
        WHEN: Removing callback
        THEN: Callback should be deregistered
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()
        callback1 = Mock()
        callback2 = Mock()

        # WHEN: Register and deregister
        callback_id_1 = manager.register('event', callback1)
        callback_id_2 = manager.register('event', callback2)

        manager.deregister('event', callback_id_1)

        # THEN: callback1 should be removed, callback2 should remain
        remaining = manager.get_listeners('event')
        assert callback1 not in remaining
        assert callback2 in remaining

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_deregister_all(self, callback_registry):
        """Test clearing all callbacks for an event.

        GIVEN: Multiple callbacks
        WHEN: Clearing all for event
        THEN: All should be removed
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()
        callback1 = Mock()
        callback2 = Mock()
        callback3 = Mock()

        # WHEN: Register callbacks
        manager.register('event', callback1)
        manager.register('event', callback2)
        manager.register('event', callback3)

        # Clear all
        manager.clear_listeners('event')

        # THEN: No listeners remain
        remaining = manager.get_listeners('event')
        assert len(remaining) == 0

    # ============================================================================
    # Event Emission Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_event_emission(self, callback_registry):
        """Test emitting event triggers callbacks.

        GIVEN: Registered callbacks
        WHEN: Event is emitted
        THEN: All callbacks should be called
        """
        callback1 = Mock()
        callback2 = Mock()

        callback_registry.register('position_updated', callback1)
        callback_registry.register('position_updated', callback2)

        # WHEN: Emit event
        event_data = {'symbol': 'AAPL', 'price': 155.0}
        callback_registry.emit('position_updated', event_data)

        # THEN: All callbacks should be called
        callback1.assert_called_once_with(event_data)
        callback2.assert_called_once_with(event_data)

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_event_data_accuracy(self, callback_registry):
        """Test callback receives correct data.

        GIVEN: Event with complex data
        WHEN: Event emitted
        THEN: Callback should receive exact data
        """
        captured_data = {}

        def capture_callback(data):
            captured_data.update(data)

        callback_registry.register('trade_executed', capture_callback)

        # WHEN: Emit with data
        trade_data = {
            'symbol': 'MSFT',
            'side': 'long',
            'entry_price': 300.0,
            'exit_price': 305.0,
            'pnl': 250.0,
            'timestamp': datetime.now()
        }

        callback_registry.emit('trade_executed', trade_data)

        # THEN: Data should be accurate
        assert captured_data['symbol'] == 'MSFT'
        assert captured_data['pnl'] == 250.0
        assert captured_data['entry_price'] == 300.0

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_event_order(self, callback_registry):
        """Test callbacks execute in registration order.

        GIVEN: Multiple callbacks
        WHEN: Event emitted
        THEN: Callbacks should execute in order registered
        """
        call_order = []

        def callback1(data):
            call_order.append(1)

        def callback2(data):
            call_order.append(2)

        def callback3(data):
            call_order.append(3)

        callback_registry.register('event', callback1)
        callback_registry.register('event', callback2)
        callback_registry.register('event', callback3)

        # WHEN: Emit
        callback_registry.emit('event', {})

        # THEN: Should execute in order
        assert call_order == [1, 2, 3], f"Callbacks executed in wrong order: {call_order}"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_event_history_tracking(self, callback_registry):
        """Test event history is tracked.

        GIVEN: Callback system
        WHEN: Multiple events emitted
        THEN: History should be recorded
        """
        callback_registry.register('event1', Mock())
        callback_registry.register('event2', Mock())

        # WHEN: Emit events
        callback_registry.emit('event1', {'data': 'a'})
        callback_registry.emit('event2', {'data': 'b'})
        callback_registry.emit('event1', {'data': 'c'})

        # THEN: History should show all events
        assert len(callback_registry.event_history) == 3
        assert callback_registry.event_history[0]['event'] == 'event1'
        assert callback_registry.event_history[1]['event'] == 'event2'
        assert callback_registry.event_history[2]['event'] == 'event1'

    # ============================================================================
    # Async Callback Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    @pytest.mark.asyncio
    async def test_callback_with_async_handlers(self):
        """Test async callbacks are awaited.

        GIVEN: Async callback functions
        WHEN: Events emitted
        THEN: Async callbacks should complete
        """
        from katana.dashboard.callbacks import AsyncCallbackManager

        manager = AsyncCallbackManager()
        results = []

        async def async_callback(data):
            await asyncio.sleep(0.01)  # Simulate async work
            results.append(data)

        # WHEN: Register async callback
        manager.register('event', async_callback)

        # WHEN: Emit event
        await manager.emit_async('event', {'data': 'test'})

        # THEN: Async callback should complete
        assert len(results) == 1
        assert results[0]['data'] == 'test'

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    @pytest.mark.asyncio
    async def test_callback_mixed_sync_async(self):
        """Test mixing sync and async callbacks.

        GIVEN: Mix of sync and async callbacks
        WHEN: Event emitted
        THEN: Both should execute
        """
        from katana.dashboard.callbacks import AsyncCallbackManager

        manager = AsyncCallbackManager()
        sync_called = False
        async_called = False

        def sync_callback(data):
            nonlocal sync_called
            sync_called = True

        async def async_callback(data):
            nonlocal async_called
            await asyncio.sleep(0.001)
            async_called = True

        manager.register('event', sync_callback)
        manager.register('event', async_callback)

        # WHEN: Emit
        await manager.emit_async('event', {})

        # THEN: Both should execute
        assert sync_called
        assert async_called

    # ============================================================================
    # Error Handling Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_error_isolation(self, callback_registry):
        """Test callback errors don't affect other callbacks.

        GIVEN: Callback that raises exception
        WHEN: Event emitted
        THEN: Other callbacks should still execute
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()
        good_callback = Mock()
        bad_called = False

        def bad_callback(data):
            nonlocal bad_called
            bad_called = True
            raise ValueError("Intentional error")

        manager.register('event', bad_callback)
        manager.register('event', good_callback)

        # WHEN: Emit (with error handling)
        errors = manager.emit_safe('event', {})

        # THEN: Good callback should still be called
        good_callback.assert_called_once()

        # THEN: Bad callback should be called but error caught
        assert bad_called
        assert len(errors) == 1

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_error_logging(self, callback_registry):
        """Test callback errors are logged.

        GIVEN: Callback that fails
        WHEN: Event emitted
        THEN: Error should be logged with context
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()

        def failing_callback(data):
            raise RuntimeError("Test error")

        manager.register('event', failing_callback)

        # WHEN: Emit
        errors = manager.emit_safe('event', {'test': 'data'})

        # THEN: Error should be captured with details
        assert len(errors) == 1
        error_info = errors[0]
        assert 'Test error' in str(error_info)

    # ============================================================================
    # Context and State Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_context_preservation(self):
        """Test callback has access to proper context.

        GIVEN: Callback with closure
        WHEN: Event emitted
        THEN: Callback should access closure variables
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()

        # Closure state
        class Context:
            def __init__(self):
                self.value = 100

        context = Context()

        def context_aware_callback(data):
            context.value += data.get('increment', 0)

        manager.register('update', context_aware_callback)

        # WHEN: Emit events
        manager.emit('update', {'increment': 50})
        manager.emit('update', {'increment': 30})

        # THEN: Context should be modified
        assert context.value == 180

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_listener_state(self):
        """Test callbacks can maintain state.

        GIVEN: Callback that tracks state
        WHEN: Multiple events emitted
        THEN: Callback state should accumulate
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()

        class StatefulListener:
            def __init__(self):
                self.events_received = 0
                self.total_value = 0

            def handle_event(self, data):
                self.events_received += 1
                self.total_value += data.get('value', 0)

        listener = StatefulListener()
        manager.register('event', listener.handle_event)

        # WHEN: Emit multiple events
        manager.emit('event', {'value': 10})
        manager.emit('event', {'value': 20})
        manager.emit('event', {'value': 30})

        # THEN: State should accumulate
        assert listener.events_received == 3
        assert listener.total_value == 60

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_unsubscribe_from_callback(self):
        """Test unsubscribing from within callback.

        GIVEN: Callback that unsubscribes itself
        WHEN: Event emitted
        THEN: Callback should unsubscribe cleanly
        """
        from katana.dashboard.callbacks import CallbackManager

        manager = CallbackManager()
        call_count = [0]
        callback_id = [None]

        def self_unsubscribing_callback(data):
            call_count[0] += 1
            if call_count[0] >= 2:
                manager.deregister('event', callback_id[0])

        callback_id[0] = manager.register('event', self_unsubscribing_callback)

        # WHEN: Emit multiple times
        manager.emit('event', {})
        manager.emit('event', {})
        manager.emit('event', {})

        # THEN: Should only be called twice (then unsubscribes)
        assert call_count[0] == 2

    # ============================================================================
    # Performance Tests
    # ============================================================================

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_latency_measurement(self):
        """Test callback execution latency.

        GIVEN: Callbacks
        WHEN: Events emitted
        THEN: Should measure latency
        """
        from katana.dashboard.callbacks import CallbackManager
        import time

        manager = CallbackManager()
        latencies = []

        def measured_callback(data):
            time.sleep(0.001)  # 1ms work

        manager.register('event', measured_callback)

        # WHEN: Emit and measure
        for _ in range(10):
            start = time.time()
            manager.emit('event', {})
            latencies.append((time.time() - start) * 1000)  # ms

        # THEN: Average latency should be reasonable
        avg_latency = sum(latencies) / len(latencies)
        assert avg_latency < 50, f"Average latency {avg_latency}ms, expected < 50ms"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_throughput(self):
        """Test event emission throughput.

        GIVEN: Multiple callbacks
        WHEN: Many events emitted
        THEN: Should handle high throughput
        """
        from katana.dashboard.callbacks import CallbackManager
        import time

        manager = CallbackManager()

        # Register 10 callbacks
        for i in range(10):
            manager.register('event', Mock())

        # WHEN: Emit many events quickly
        start = time.time()
        for i in range(1000):
            manager.emit('event', {'id': i})
        duration = time.time() - start

        # THEN: Should complete quickly
        # ~10K callback invocations should take < 1 second
        assert duration < 1.0, f"1000 events with 10 callbacks took {duration}s"
        throughput = 10000 / duration
        assert throughput > 10000, f"Throughput {throughput} events/sec, expected > 10K"

    @pytest.mark.ux001
    @pytest.mark.acceptance
    @pytest.mark.callbacks
    def test_callback_memory_efficiency(self):
        """Test callback system doesn't leak memory.

        GIVEN: Callbacks registered and deregistered
        WHEN: Many cycles of register/deregister
        THEN: Memory should be stable
        """
        from katana.dashboard.callbacks import CallbackManager
        import sys

        manager = CallbackManager()

        # WHEN: Register and deregister many times
        for cycle in range(100):
            callbacks = []
            for i in range(50):
                callback = Mock()
                manager.register('event', callback)
                callbacks.append(callback)

            # Deregister all
            for callback in callbacks:
                # Find and deregister (would need ID in real impl)
                pass

        # THEN: Should not have memory leaks
        # Check that listeners dict is clean
        assert len(manager.listeners.get('event', [])) == 0
