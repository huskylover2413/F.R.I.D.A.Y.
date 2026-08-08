"""
==========================================================
F.R.I.D.A.Y.

Brain Models

Foundation Release:
    18.3
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from .services import BrainService


class BrainAction(Enum):
    """
    High-level action selected by the Brain.
    """

    SKILL = auto()

    AI = auto()

    MEMORY = auto()

    INTERNET = auto()

    AUTOMATION = auto()

    SYSTEM = auto()


@dataclass(slots=True)
class BrainDecision:
    """
    Decision returned by the Brain.
    """

    action: BrainAction

    service: BrainService | None = None

    target: str | None = None

    confidence: float = 1.0

    reason: str = ""

    metadata: dict | None = None