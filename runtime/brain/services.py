"""
==========================================================
F.R.I.D.A.Y.

Brain Services

Foundation Release 22.1
==========================================================
"""

from __future__ import annotations

from enum import Enum, auto


class BrainService(Enum):
    """
    Types of work the Brain can delegate.
    """

    SKILLS = auto()

    AI = auto()

    MEMORY = auto()

    INTERNET = auto()

    AUTOMATION = auto()

    SYSTEM = auto()

    VISION = auto()