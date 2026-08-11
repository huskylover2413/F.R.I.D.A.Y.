"""
==========================================================
F.R.I.D.A.Y.

Decision Stage

Foundation Release 58.2
==========================================================
"""

from __future__ import annotations

from ..context import BrainContext


class DecisionStage:
    """
    Determines whether the Brain should use a local
    capability or fall back to AI.
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
        "who are you",
        "what are you",
        "your name",
        "good morning",
        "good afternoon",
        "good evening",
        "hello",
        "hi",
        "help",
        "what can you do",
        "what do you do",

        #
        # Apple Music
        #

        "what's playing",
        "what is playing",
        "what song is playing",
        "what song is this",
        "who is playing",
        "who's playing",
        "who is singing",
        "who's singing",
    }

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        request = board.metadata.get(
            "resolved_request",
            context.request.lower().strip(),
        )

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