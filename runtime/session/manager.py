"""
==========================================================
F.R.I.D.A.Y.

Session Manager

Foundation Release 27.0
==========================================================
"""

from __future__ import annotations

from .models import SessionState


class SessionManager:

    def __init__(self) -> None:

        self._state = SessionState()

    @property
    def state(self) -> SessionState:

        return self._state

    def begin_request(
        self,
        request: str,
    ) -> None:

        self._state.last_request = request

        self._state.conversation_turns += 1

    def finish_request(
        self,
        response: str,
    ) -> None:

        self._state.last_response = response