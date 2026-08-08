"""
==========================================================
F.R.I.D.A.Y.

Goal Stage

Foundation Release 26.1
==========================================================
"""

from __future__ import annotations

from runtime.goals import GoalManager

from ..context import BrainContext


class GoalStage:
    """
    Loads active goals into the Blackboard.
    """

    def __init__(self) -> None:

        self._goals = GoalManager()

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        active = self._goals.active()

        board.reasoning.append(
            f"Loaded {len(active)} active goals."
        )

        for goal in active:

            board.metadata.setdefault(
                "goals",
                []
            ).append(
                goal.title
            )