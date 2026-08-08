"""
==========================================================
F.R.I.D.A.Y.

Brain Context

Foundation Release 21.4
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .blackboard import Blackboard


@dataclass(slots=True)
class BrainContext:
    """
    Context passed through the Brain Loop.
    """

    request: str

    blackboard: Blackboard = field(
        default_factory=Blackboard
    )

    remember_after_response: bool = False