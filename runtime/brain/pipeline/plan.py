"""
==========================================================
F.R.I.D.A.Y.

Plan Stage

Foundation Release 30.0
==========================================================
"""

from __future__ import annotations

from ..action import Action
from ..context import BrainContext


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

                    service="memory",

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

                    service="vision",

                    operation="describe",

                    priority=90,

                )

            )

        #
        # AI
        #

        board.actions.append(

            Action(

                service="ai",

                operation="respond",

                priority=50,

            )

        )

        board.actions.sort(

            key=lambda action: action.priority,

            reverse=True,

        )

        board.reasoning.append(

            f"Created {len(board.actions)} actions."

        )