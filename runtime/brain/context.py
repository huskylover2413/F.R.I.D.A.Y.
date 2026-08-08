"""
==========================================================
F.R.I.D.A.Y.

Brain Context

Version 2.3
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BrainContext:
    """
    The Brain's current understanding of the world.

    This object represents what FRIDAY knows
    right now while handling a request.
    """

    request: str

    recalled_memories: list[str] = field(default_factory=list)

    observations: list[str] = field(default_factory=list)

    planned_services: list[str] = field(default_factory=list)

    reasoning: list[str] = field(default_factory=list)

    response: str = ""

    remember_after_response: bool = False