"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/core/events/bus.py

Purpose:
    Provides the central publish/subscribe event bus.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.2.0
Release:
    Foundation Release 2
==========================================================
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

from .event import Event

EventHandler = Callable[[Event], None]


class EventBus:
    """
    Central event dispatcher for FRIDAY.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Register a handler for an event.
        """

        if handler not in self._subscribers[event_name]:
            self._subscribers[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: EventHandler) -> None:
        """
        Remove a handler.
        """

        if handler in self._subscribers[event_name]:
            self._subscribers[event_name].remove(handler)

    def publish(self, event: Event) -> None:
        """
        Publish an event to all subscribers.
        """

        for handler in self._subscribers[event.name]:
            handler(event)

    def subscriber_count(self, event_name: str) -> int:
        """
        Return the number of subscribers for an event.
        """

        return len(self._subscribers[event_name])

    def clear(self) -> None:
        """
        Remove every subscription.
        """

        self._subscribers.clear()