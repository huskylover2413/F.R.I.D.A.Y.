"""
==========================================================
F.R.I.D.A.Y.

Presence Models

Foundation Release 44.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class PresenceState(Enum):
    """
    Current operating state of FRIDAY.
    """

    SLEEPING = auto()

    LISTENING = auto()

    THINKING = auto()

    SPEAKING = auto()

    CONVERSATION = auto()


@dataclass(slots=True)
class Presence:

    state: PresenceState = PresenceState.SLEEPING