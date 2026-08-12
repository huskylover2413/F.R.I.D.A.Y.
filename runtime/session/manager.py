"""
==========================================================
F.R.I.D.A.Y.

Session Manager

Foundation Release 47.0
==========================================================
"""

from __future__ import annotations

from .models import SessionState


class SessionManager:
    """
    Maintains the current conversational session.
    """

    def __init__(self) -> None:

        self._state = SessionState()

    @property
    def state(self) -> SessionState:

        return self._state

    def begin_request(
        self,
        request: str,
    ) -> tuple[str, str]:

        previous_request = self._state.last_request
        previous_response = self._state.last_response

        self._state.last_request = request
        self._state.conversation_turns += 1

        return (
            previous_request,
            previous_response,
        )

    def finish_request(
        self,
        response: str,
    ) -> None:

        self._state.last_response = response