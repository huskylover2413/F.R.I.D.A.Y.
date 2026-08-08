"""
==========================================================
F.R.I.D.A.Y.

Decision Stage

Foundation Release 37.0
==========================================================
"""

from __future__ import annotations

from ..context import BrainContext
from ..services import BrainService


class DecisionStage:
    """
    Determines whether the Brain
    needs AI for this request.
    """

    LOCAL_KEYWORDS = {

        "remember",
        "memory",
        "time",
        "date",
        "calculator",
        "math",
        "weather",
        "timer",
        "stopwatch",
        "settings",
        "status",

    }

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        request = context.request.lower()

        board.metadata["needs_ai"] = True

        if any(

            keyword in request

            for keyword in self.LOCAL_KEYWORDS

        ):

            board.metadata["needs_ai"] = False

            board.reasoning.append(
                "Decision: local execution preferred."
            )

        else:

            board.reasoning.append(
                "Decision: AI required."
            )