"""
==========================================================
F.R.I.D.A.Y.

Runtime Events

Foundation Release 47.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class EventType(Enum):

    WAKE = auto()

    SLEEP = auto()

    SPEECH = auto()

    THINKING = auto()

    RESPONSE = auto()


@dataclass(slots=True)
class Event:

    type: EventType

    payload: object | None = None