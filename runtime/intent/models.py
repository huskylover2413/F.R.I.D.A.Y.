"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/intent/models.py

Purpose:
    Defines Intent models used throughout FRIDAY.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.5.0
Release:
    Intent
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class IntentType(Enum):
    """
    Supported intents.
    """

    UNKNOWN = auto()
    GREETING = auto()
    TIME_REQUEST = auto()
    DATE_REQUEST = auto()


@dataclass(slots=True, frozen=True)
class IntentResult:
    """
    Result returned by the Intent Engine.
    """

    intent: IntentType

    confidence: float