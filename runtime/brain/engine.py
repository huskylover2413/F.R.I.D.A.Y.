"""
==========================================================
F.R.I.D.A.Y.

Brain Engine

Foundation Release 42.0
==========================================================
"""

from __future__ import annotations

from runtime.ai.models import AIResponse

from .context import BrainContext
from .loop import BrainLoop


class BrainEngine:
    """
    Public interface to FRIDAY's Brain.
    """

    def __init__(self) -> None:

        self._loop = BrainLoop()

    def ask(
        self,
        request: str,
    ) -> AIResponse:

        context = BrainContext(
            request=request,
        )

        context = self._loop.run(
            context
        )

        #
        # Find the AI response.
        #

        for action in reversed(
            context.blackboard.actions
        ):

            if hasattr(
                action.result,
                "message",
            ):

                return action.result

        #
        # Nothing generated.
        #

        return AIResponse(

            message="I'm not sure how to answer that.",

            provider="Brain",

            success=False,

        )