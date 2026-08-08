"""
==========================================================
F.R.I.D.A.Y.
Vision Models

Foundation Release:
    20.3
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class ScreenCapture:
    """
    Represents one captured screen.
    """

    path: Path

    image: bytes

    width: int

    height: int

    created: datetime