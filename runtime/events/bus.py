"""
==========================================================
F.R.I.D.A.Y.

Event Bus

Foundation Release 47.0
==========================================================
"""

from __future__ import annotations

from collections import defaultdict

from .models import Event
from .models import EventType


class EventBus:
    """
    Lightweight publish/subscribe event bus.
    """

    def __init__(self) -> None:

        self._subscribers = defaultdict(list)

    def subscribe(

        self,

        event: EventType,

        callback,

    ) -> None:

        self._subscribers[event].append(
            callback
        )

    def publish(

        self,

        event: Event,

    ) -> None:

        for callback in self._subscribers[
            event.type
        ]:

            callback(event)