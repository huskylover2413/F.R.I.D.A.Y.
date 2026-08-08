"""
==========================================================
F.R.I.D.A.Y.

Brain Stages

Foundation Release 19.0
==========================================================
"""

from __future__ import annotations

from enum import Enum, auto


class BrainStage(Enum):
    """
    Ordered stages of FRIDAY's thinking process.
    """

    RECALL = auto()

    OBSERVE = auto()

    PLAN = auto()

    REASON = auto()

    EXECUTE = auto()

    LEARN = auto()