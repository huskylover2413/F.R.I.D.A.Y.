"""
==========================================================
F.R.I.D.A.Y.
Brain Models

Foundation Release:
    18.2
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from .services import BrainService


@dataclass(slots=True)
class BrainDecision:
    """
    Decision returned by the Brain.
    """

    service: BrainService

    target: str | None = None

    confidence: float = 1.0

    reason: str = ""

    metadata: dict | None = None