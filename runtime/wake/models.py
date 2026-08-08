"""
==========================================================
F.R.I.D.A.Y.

Wake Models

Foundation Release 45.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class WakeResult(Enum):
    """
    Result of evaluating audio input.
    """

    SLEEP = auto()

    WAKE = auto()


@dataclass(slots=True)
class WakeEvent:

    phrase: str

    result: WakeResult