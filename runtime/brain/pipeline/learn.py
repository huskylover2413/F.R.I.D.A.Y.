"""
==========================================================
F.R.I.D.A.Y.

Learn Stage

Foundation Release 38.0
==========================================================
"""

from __future__ import annotations

from runtime.memory.classifier import MemoryClassifier

from ..action import Action
from ..context import BrainContext
from ..services import BrainService


class LearnStage:
    """
    Decides whether the interaction
    should become long-term memory.
    """

    def __init__(self) -> None:

        self._classifier = MemoryClassifier()

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        #
        # Don't queue duplicate
        # remember actions.
        #

        for action in board.actions:

            if action.operation == "remember":

                return

        decision = self._classifier.classify(
            context.request
        )

        if not decision.should_store:

            board.reasoning.append(
                "Learn: nothing worth storing."
            )

            return

        board.actions.append(

            Action(

                service=BrainService.MEMORY,

                operation="remember",

                priority=10,

                arguments={

                    "category": decision.category,

                    "text": context.request,

                },

            )

        )

        board.reasoning.append(

            f"Learn: queued memory ({decision.category})."

        )