"""
==========================================================
F.R.I.D.A.Y.

Memory Classification Models

Foundation Release 2.2
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MemoryDecision:

    should_store: bool

    category: str

    confidence: float