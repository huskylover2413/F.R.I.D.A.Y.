"""
==========================================================
F.R.I.D.A.Y.

Cognition Engine

Foundation Release 47.0
==========================================================
"""

from __future__ import annotations

from runtime.brain import BrainEngine
from runtime.session import SessionManager

from .models import Response


class CognitionEngine:
    """
    Public cognition interface.

    Maintains conversational session state while
    delegating reasoning to the Brain.
    """

    def __init__(self) -> None:

        self._brain = BrainEngine()

        self._session = SessionManager()

    def process(
        self,
        text: str,
    ) -> Response:

        #
        # Capture the previous turn BEFORE
        # recording the new request.
        #

        (
            previous_request,
            previous_response,
        ) = self._session.begin_request(
            text
        )

        state = self._session.state

        #
        # Give the Brain the current request and
        # previous conversational context.
        #

        ai = self._brain.ask(

            text,

            last_request=previous_request,

            last_response=previous_response,

            conversation_turns=(
                state.conversation_turns
            ),

            current_topic=(
                state.current_topic
            ),

            current_project=(
                state.current_project
            ),

            current_task=(
                state.current_task
            ),
        )

        #
        # Store the response for the next turn.
        #

        self._session.finish_request(
            ai.message
        )

        return Response(

            message=ai.message,

            success=ai.success,

        )