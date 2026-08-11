"""
==========================================================
F.R.I.D.A.Y.

Decision Stage

Foundation Release 56.2
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
        #
        # --------------------------------------------------
        # Memory
        # --------------------------------------------------
        #

        "remember",
        "memory",

        #
        # --------------------------------------------------
        # Time / Date
        # --------------------------------------------------
        #

        "time",
        "date",
        "what day",
        "what is today",
        "what's today",
        "tomorrow",
        "yesterday",
        "month",
        "year",

        #
        # --------------------------------------------------
        # Math
        # --------------------------------------------------
        #

        "calculator",
        "calculate",
        "math",

        #
        # --------------------------------------------------
        # System
        # --------------------------------------------------
        #

        "weather",
        "timer",
        "stopwatch",
        "settings",
        "status",

        #
        # --------------------------------------------------
        # Identity
        # --------------------------------------------------
        #

        "who are you",
        "what are you",
        "your name",

        #
        # --------------------------------------------------
        # Greetings
        # --------------------------------------------------
        #

        "good morning",
        "good afternoon",
        "good evening",
        "hello",
        "hi",
        "hey",

        #
        # --------------------------------------------------
        # Help
        # --------------------------------------------------
        #

        "help",
        "what can you do",
        "what do you do",

        #
        # --------------------------------------------------
        # Apple Music
        # --------------------------------------------------
        #

        "play music",
        "play my music",
        "play the music",
        "play ",
        "pause",
        "pause music",
        "stop music",
        "stop the music",
        "next song",
        "next track",
        "skip song",
        "skip this song",
        "skip track",
        "skip this track",
        "previous song",
        "previous track",
        "last song",
        "go back",
        "go to the previous song",
        "go to the previous track",
        "start this song over",
        "start the song over",
        "restart this song",
        "restart the song",
        "restart song",
        "start this track over",
        "restart this track",
        "restart the current song",
        "restart the current track",
        "play this again",
        "play the song again",
        "play this song again",
        "repeat this song",
        "repeat the song",
        "loop this song",
        "loop the song",
        "repeat this",
        "loop this",
        "stop looping",
        "stop the loop",
        "turn repeat off",
        "turn off repeat",
        "repeat off",
        "stop repeating",
        "stop repeat",
        "open apple music",
        "open music",
        "launch apple music",
        "launch music",
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

        #
        # Local capability detection
        #

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