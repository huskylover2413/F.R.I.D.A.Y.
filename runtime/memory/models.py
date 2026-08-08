"""
==========================================================
F.R.I.D.A.Y.

Memory Models

Foundation Release 2.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Memory:
    """
    A single long-term memory.
    """

    category: str

    key: str

    value: str

    created: datetime

    updated: datetime