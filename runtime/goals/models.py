"""
==========================================================
F.R.I.D.A.Y.

Goal Models

Foundation Release 26.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Goal:

    title: str

    description: str = ""

    active: bool = True

    progress: float = 0.0

    created: datetime = field(
        default_factory=datetime.now
    )

    updated: datetime = field(
        default_factory=datetime.now
    )