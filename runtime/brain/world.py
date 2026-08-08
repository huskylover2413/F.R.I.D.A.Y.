"""
==========================================================
F.R.I.D.A.Y.

World Model

Foundation Release 25.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WorldModel:
    """
    FRIDAY's current understanding
    of the user's world.
    """

    current_project: str | None = None

    current_goal: str | None = None

    current_application: str | None = None

    current_window: str | None = None

    current_location: str | None = None

    active_conversation: bool = True

    pending_actions: int = 0

    relevant_memories: int = 0

    observations: int = 0

    confidence: float = 1.0

    metadata: dict = field(
        default_factory=dict
    )