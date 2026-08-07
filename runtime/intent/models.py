"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/intent/models.py
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class IntentType(Enum):
    UNKNOWN = auto()

    GREETING = auto()

    TIME_REQUEST = auto()

    DATE_REQUEST = auto()

    HELP_REQUEST = auto()

    IDENTITY_REQUEST = auto()

    MATH_REQUEST = auto()


@dataclass(slots=True, frozen=True)
class IntentResult:

    intent: IntentType

    confidence: float