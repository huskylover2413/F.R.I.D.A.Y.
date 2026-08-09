"""
==========================================================
F.R.I.D.A.Y.

Decision Stage

Foundation Release 45.0
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
    }

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        request = context.request.lower().strip()

        #
        # Remove the wake phrase when it is included
        # in the recognized speech.
        #

        request = self._remove_wake_phrase(
            request
        )

        board.metadata["clean_request"] = request

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

    @staticmethod
    def _remove_wake_phrase(
        request: str,
    ) -> str:

        wake_phrases = (
            "hey friday",
            "hey fri",
            "friday",
            "fri",
        )

        cleaned = request.strip()

        changed = True

        while changed:

            changed = False

            for phrase in wake_phrases:

                if cleaned == phrase:

                    return ""

                prefix = phrase + " "

                if cleaned.startswith(prefix):

                    cleaned = (
                        cleaned[len(prefix):]
                        .strip()
                    )

                    changed = True

                    break

        return cleaned