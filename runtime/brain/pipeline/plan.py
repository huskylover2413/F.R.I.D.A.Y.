"""
==========================================================
F.R.I.D.A.Y.

Plan Stage

Foundation Release 37.0
==========================================================
"""

from __future__ import annotations

from ..action import Action
from ..context import BrainContext
from ..services import BrainService


class PlanStage:
    """
    Produces executable Action objects.
    """

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        board.actions.clear()

        request = context.request.lower()

        #
        # Memory
        #

        if any(

            word in request

            for word in [

                "remember",

                "my",

                "mine",

            ]

        ):

            board.actions.append(

                Action(

                    service=BrainService.MEMORY,

                    operation="search",

                    priority=100,

                )

            )

        #
        # Vision
        #

        if any(

            word in request

            for word in [

                "look",

                "screen",

                "image",

                "photo",

                "picture",

                "see",

            ]

        ):

            board.actions.append(

                Action(

                    service=BrainService.VISION,

                    operation="describe",

                    priority=90,

                )

            )

        #
        # AI
        #

        if board.metadata.get("needs_ai", True):

            board.actions.append(

                Action(

                    service=BrainService.AI,

                    operation="respond",

                    priority=50,

                )

            )

        #
        # Highest priority first
        #

        board.actions.sort(

            key=lambda action: action.priority,

            reverse=True,

        )

        board.reasoning.append(

            f"Created {len(board.actions)} action(s)."

        )