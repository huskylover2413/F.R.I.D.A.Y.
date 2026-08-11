"""
==========================================================
F.R.I.D.A.Y.

Context Resolution Stage

Foundation Release 48.0
==========================================================
"""

from __future__ import annotations

from ..context import BrainContext


class ContextStage:
    """
    Resolves simple conversational follow-ups using
    the previous session turn.
    """

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        request = context.request.lower().strip()

        previous = context.last_request.lower().strip()

        #
        # No previous conversation.
        #

        if not previous:

            board.metadata["resolved_request"] = request

            return

        #
        # --------------------------------------------------
        # Previous-request questions
        # --------------------------------------------------
        #

        if self._is_previous_request_question(
            request
        ):

            board.metadata[
                "context_operation"
            ] = "previous_request"

            board.metadata[
                "resolved_request"
            ] = previous

            board.reasoning.append(
                "Context: user asked about the previous request."
            )

            return

        #
        # --------------------------------------------------
        # Date follow-up
        # --------------------------------------------------
        #

        if self._is_date_followup(request):

            board.metadata[
                "resolved_request"
            ] = "what is today's date"

            board.reasoning.append(
                "Context: resolved date follow-up."
            )

            return

        #
        # --------------------------------------------------
        # Time follow-up
        # --------------------------------------------------
        #

        if self._is_time_followup(request):

            board.metadata[
                "resolved_request"
            ] = "what time is it"

            board.reasoning.append(
                "Context: resolved time follow-up."
            )

            return

        #
        # Default
        #

        board.metadata[
            "resolved_request"
        ] = request

    @staticmethod
    def _is_previous_request_question(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what did i just ask",
                "what did i ask",
                "what was my last question",
                "what was my previous question",
                "what did i just say",
            )
        )

    @staticmethod
    def _is_date_followup(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what about the date",
                "what about date",
                "and the date",
                "what about today's date",
                "what about todays date",
            )
        )

    @staticmethod
    def _is_time_followup(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what about the time",
                "what about time",
                "and the time",
            )
        )