"""
==========================================================
F.R.I.D.A.Y.

Reason Stage

Foundation Release 25.0
==========================================================
"""

from __future__ import annotations

from ..context import BrainContext


class ReasonStage:
    """
    Updates the Brain's internal world model.
    """

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        board.world.pending_actions = len(
            board.actions
        )

        board.world.relevant_memories = len(
            board.memories
        )

        board.world.observations = len(
            board.observations
        )

        board.reasoning.append(
            "World model updated."
        )