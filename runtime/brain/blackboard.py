"""
==========================================================
F.R.I.D.A.Y.

Brain Blackboard

Foundation Release 26.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .action import Action
from .world import WorldModel


@dataclass(slots=True)
class Blackboard:
    """
    Shared workspace for the Brain.
    """

    world: WorldModel = field(
        default_factory=WorldModel
    )

    memories: list[str] = field(
        default_factory=list
    )

    observations: list[str] = field(
        default_factory=list
    )

    plans: list[str] = field(
        default_factory=list
    )

    actions: list[Action] = field(
        default_factory=list
    )

    reasoning: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    response: str = ""