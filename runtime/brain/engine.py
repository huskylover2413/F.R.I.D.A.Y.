"""
==========================================================
F.R.I.D.A.Y.

Brain Engine

Foundation Release 55.0
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
        **kwargs,
    ) -> AIResponse:

        #
        # Create Brain context.
        #
        context = BrainContext(
            request=request,
        )

        #
        # Preserve conversational information
        # supplied by the Session layer.
        #
        context.blackboard.metadata.update(
            {
                key: value
                for key, value in kwargs.items()
                if value is not None
            }
        )

        #
        # Run the Brain.
        #
        context = self._loop.run(
            context
        )

        #
        # Find the most recent successful action.
        #
        for action in reversed(
            context.blackboard.actions
        ):

            result = action.result

            #
            # AI / Skill response
            #
            if hasattr(
                result,
                "message",
            ):

                return result

            #
            # System / Mac response
            #
            if isinstance(
                result,
                str,
            ):

                return AIResponse(
                    message=result,
                    provider="FRIDAY",
                    success=True,
                )

        #
        # Nothing generated.
        #
        return AIResponse(

            message="I'm not sure how to answer that.",

            provider="Brain",

            success=False,

        )