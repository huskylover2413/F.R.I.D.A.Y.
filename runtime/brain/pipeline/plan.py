"""
==========================================================
F.R.I.D.A.Y.

Plan Stage

Foundation Release 45.1
==========================================================
"""

from __future__ import annotations

from ..action import Action
from ..context import BrainContext
from ..services import BrainService


class PlanStage:
    """
    Produces executable actions for the Brain.

    Local skills take priority over AI.
    AI is used only when no local capability
    matches the request.
    """

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        board.actions.clear()

        request = board.metadata.get(
            "clean_request",
            context.request.lower().strip(),
        )

        local_skill = False

        #
        # --------------------------------------------------
        # Time
        # --------------------------------------------------
        #

        if self._is_time_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="time",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Date
        # --------------------------------------------------
        #

        elif self._is_date_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="date",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Greeting
        # --------------------------------------------------
        #

        elif self._is_greeting(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="greeting",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Identity
        # --------------------------------------------------
        #

        elif self._is_identity_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="identity",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Help
        # --------------------------------------------------
        #

        elif self._is_help_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="help",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Math
        # --------------------------------------------------
        #

        elif self._is_math_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="math",
                    priority=100,
                )
            )

            local_skill = True

        #
        # --------------------------------------------------
        # Memory
        # --------------------------------------------------
        #

        if any(
            word in request
            for word in (
                "remember",
                "memory",
            )
        ):

            board.actions.append(
                Action(
                    service=BrainService.MEMORY,
                    operation="search",
                    priority=90,
                )
            )

        #
        # --------------------------------------------------
        # Vision
        # --------------------------------------------------
        #

        if any(
            word in request
            for word in (
                "look",
                "screen",
                "image",
                "photo",
                "picture",
                "see",
            )
        ):

            board.actions.append(
                Action(
                    service=BrainService.VISION,
                    operation="describe",
                    priority=80,
                )
            )

        #
        # --------------------------------------------------
        # AI fallback
        # --------------------------------------------------
        #

        if not local_skill:

            board.actions.append(
                Action(
                    service=BrainService.AI,
                    operation="respond",
                    priority=50,
                )
            )

        #
        # --------------------------------------------------
        # Sort
        # --------------------------------------------------
        #

        board.actions.sort(
            key=lambda action: action.priority,
            reverse=True,
        )

        board.reasoning.append(
            f"Created {len(board.actions)} action(s)."
        )

    #
    # ======================================================
    # Request Detection
    # ======================================================
    #

    @staticmethod
    def _is_time_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what time is it",
                "what's the time",
                "what is the time",
                "current time",
                "tell me the time",
            )
        )

    @staticmethod
    def _is_date_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what date is it",
                "what's the date",
                "what is the date",
                "today's date",
                "todays date",
                "current date",
                "what day is it",
            )
        )

    @staticmethod
    def _is_greeting(
        request: str,
    ) -> bool:

        return request in {
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        }

    @staticmethod
    def _is_identity_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "who are you",
                "what are you",
                "who is friday",
                "what is your name",
                "what's your name",
                "your name",
            )
        )

    @staticmethod
    def _is_help_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "help",
                "what can you do",
                "what do you do",
            )
        )

    @staticmethod
    def _is_math_request(
        request: str,
    ) -> bool:
        """
        Detect mathematical requests.

        Supports both natural language and
        symbolic expressions such as:

            27*14
            100/4
            12+8
            50-17
            2^8
        """

        math_phrases = (
            "calculate",
            "plus",
            "minus",
            "times",
            "multiplied by",
            "divided by",
            "square root",
            "power of",
        )

        if any(
            phrase in request
            for phrase in math_phrases
        ):
            return True

        #
        # Mathematical operators
        #

        if any(
            operator in request
            for operator in (
                "*",
                "/",
                "%",
                "^",
            )
        ):
            return True

        #
        # Addition/subtraction with digits.
        #
        # Avoid treating normal hyphenated text as
        # mathematics.
        #

        if (
            "+" in request
            or (
                "-" in request
                and any(
                    character.isdigit()
                    for character in request
                )
            )
        ):
            return True

        return False