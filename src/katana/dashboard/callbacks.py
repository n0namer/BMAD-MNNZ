"""
Dashboard Callback System - Event management and async handling

Provides event-driven architecture for dashboard updates and real-time data streaming.
"""

import asyncio
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
import time


class CallbackEventType(Enum):
    """Types of dashboard events."""
    POSITION_UPDATE = "position_update"
    TRADE_EXECUTED = "trade_executed"
    RISK_ALERT = "risk_alert"
    PERFORMANCE_UPDATE = "performance_update"
    DATA_CHANGE = "data_change"
    ERROR = "error"


@dataclass
class CallbackEvent:
    """Event data structure."""
    event_type: CallbackEventType
    timestamp: float = field(default_factory=time.time)
    data: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary."""
        return {
            'type': self.event_type.value,
            'timestamp': self.timestamp,
            'data': self.data
        }


class CallbackManager:
    """
    Synchronous callback management for dashboard events.
    Handles event registration, emission, and listener management.
    """

    def __init__(self):
        """Initialize callback manager."""
        self._listeners: Dict[str, List[Callable]] = {}
        self._callback_ids: Dict[str, Dict[int, Callable]] = {}
        self._next_id = 0
        self._event_history: List[CallbackEvent] = []
        self._deregistered_listeners: List[Callable] = []
        self.event_count = 0

    def register(self, event_type: str, callback: Callable) -> int:
        """
        Register a callback for an event type.

        Returns:
            int: Callback ID for deregistration
        """
        if event_type not in self._listeners:
            self._listeners[event_type] = []
            self._callback_ids[event_type] = {}

        self._listeners[event_type].append(callback)
        callback_id = self._next_id
        self._callback_ids[event_type][callback_id] = callback
        self._next_id += 1
        return callback_id

    def deregister(self, event_type: str, callback_id: int) -> None:
        """Deregister a callback using its ID."""
        if event_type in self._callback_ids and callback_id in self._callback_ids[event_type]:
            callback = self._callback_ids[event_type][callback_id]
            if callback in self._listeners[event_type]:
                self._listeners[event_type].remove(callback)
            del self._callback_ids[event_type][callback_id]
            self._deregistered_listeners.append(callback)

    def unregister(self, event_type: str, callback: Callable) -> None:
        """Unregister a callback by reference (deprecated, use deregister)."""
        if event_type in self._listeners and callback in self._listeners[event_type]:
            self._listeners[event_type].remove(callback)
            self._deregistered_listeners.append(callback)

    def unregister_all(self, event_type: str) -> None:
        """Unregister all callbacks for an event type (deprecated, use clear_listeners)."""
        if event_type in self._listeners:
            self._deregistered_listeners.extend(self._listeners[event_type])
            self._listeners[event_type] = []

    def clear_listeners(self, event_type: str) -> None:
        """Clear all listeners for an event type."""
        if event_type in self._listeners:
            self._deregistered_listeners.extend(self._listeners[event_type])
            self._listeners[event_type] = []
            self._callback_ids[event_type] = {}

    def emit(self, event_type: str = None, event: CallbackEvent = None, data: Dict[str, Any] = None) -> None:
        """
        Emit an event to all registered listeners.

        Can be called as:
        - emit(event=CallbackEvent(...))
        - emit(event_type='string', data={...})
        """
        if event is None and event_type is not None:
            event = CallbackEvent(
                event_type=CallbackEventType(event_type) if isinstance(event_type, str) else event_type,
                data=data or {}
            )

        if event is None:
            return

        self.event_count += 1
        self._event_history.append(event)

        # Support both CallbackEventType enum and string event types
        event_key = event.event_type.value if hasattr(event.event_type, 'value') else str(event.event_type)

        if event_key in self._listeners:
            for callback in self._listeners[event_key]:
                try:
                    callback(event)
                except Exception as e:
                    # Log error but don't stop other callbacks
                    pass

    def get_event_history(self) -> List[CallbackEvent]:
        """Get all events that have been emitted."""
        return self._event_history.copy()

    def get_listeners(self, event_type: str) -> List[Callable]:
        """Get all listeners for an event type."""
        return self._listeners.get(event_type, []).copy()

    def listener_count(self, event_type: str) -> int:
        """Get count of listeners for an event type."""
        return len(self._listeners.get(event_type, []))

    def clear_history(self) -> None:
        """Clear event history."""
        self._event_history = []

    def measure_latency(self, callback: Callable) -> float:
        """Measure execution latency of a callback."""
        start = time.perf_counter()
        try:
            callback(CallbackEvent(CallbackEventType.PERFORMANCE_UPDATE))
        except:
            pass
        end = time.perf_counter()
        return (end - start) * 1000  # Convert to milliseconds


class AsyncCallbackManager:
    """
    Asynchronous callback management for dashboard events.
    Handles async/await callbacks and concurrent event processing.
    """

    def __init__(self):
        """Initialize async callback manager."""
        self._listeners: Dict[CallbackEventType, List[Callable]] = {}
        self._event_history: List[CallbackEvent] = []
        self._deregistered_listeners: List[Callable] = []
        self._event_queue: asyncio.Queue = asyncio.Queue()
        self.event_count = 0
        self._processing = False

    async def register(self, event_type: CallbackEventType, callback: Callable) -> None:
        """Register an async callback for an event type."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    async def unregister(self, event_type: CallbackEventType, callback: Callable) -> None:
        """Unregister an async callback."""
        if event_type in self._listeners and callback in self._listeners[event_type]:
            self._listeners[event_type].remove(callback)
            self._deregistered_listeners.append(callback)

    async def unregister_all(self, event_type: CallbackEventType) -> None:
        """Unregister all async callbacks for an event type."""
        if event_type in self._listeners:
            self._deregistered_listeners.extend(self._listeners[event_type])
            self._listeners[event_type] = []

    async def emit(self, event: CallbackEvent) -> None:
        """Emit an event to all registered async listeners."""
        self.event_count += 1
        self._event_history.append(event)

        if event.event_type in self._listeners:
            tasks = []
            for callback in self._listeners[event.event_type]:
                if asyncio.iscoroutinefunction(callback):
                    tasks.append(callback(event))
                else:
                    tasks.append(asyncio.create_task(asyncio.to_thread(callback, event)))

            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

    async def get_event_history(self) -> List[CallbackEvent]:
        """Get all events that have been emitted."""
        return self._event_history.copy()

    def get_listeners(self, event_type: str) -> List[Callable]:
        """Get all listeners for an event type."""
        return self._listeners.get(event_type, []).copy()

    def listener_count(self, event_type: str) -> int:
        """Get count of listeners for an event type."""
        return len(self._listeners.get(event_type, []))

    async def measure_latency(self, callback: Callable) -> float:
        """Measure execution latency of an async callback."""
        start = time.perf_counter()
        try:
            if asyncio.iscoroutinefunction(callback):
                await callback(CallbackEvent(CallbackEventType.PERFORMANCE_UPDATE))
            else:
                callback(CallbackEvent(CallbackEventType.PERFORMANCE_UPDATE))
        except:
            pass
        end = time.perf_counter()
        return (end - start) * 1000  # Convert to milliseconds

    async def clear_history(self) -> None:
        """Clear event history."""
        self._event_history = []

    async def start_processing(self) -> None:
        """Start processing events from queue."""
        self._processing = True
        while self._processing:
            try:
                event = await asyncio.wait_for(self._event_queue.get(), timeout=1.0)
                await self.emit(event)
            except asyncio.TimeoutError:
                continue

    def stop_processing(self) -> None:
        """Stop processing events from queue."""
        self._processing = False

    async def enqueue_event(self, event: CallbackEvent) -> None:
        """Add event to processing queue."""
        await self._event_queue.put(event)
