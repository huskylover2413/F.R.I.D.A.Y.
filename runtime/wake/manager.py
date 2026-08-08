"""
==========================================================
F.R.I.D.A.Y.

Wake Manager

Foundation Release 46.0
==========================================================
"""

from __future__ import annotations

from runtime.presence import PresenceManager
from runtime.presence import PresenceState

from .detector import WakeDetector
from .models import WakeResult


class WakeManager:
    """
    Coordinates wake detection and
    presence state transitions.
    """

    def __init__(self) -> None:

        self._detector = WakeDetector()

        self._presence = PresenceManager()

    @property
    def state(self):

        return self._presence.state

    def process(
        self,
        text: str,
    ) -> bool:

        event = self._detector.detect(
            text
        )

        if event.result == WakeResult.WAKE:

            self._presence.set_state(
                PresenceState.LISTENING
            )

            return True

        return False

    def sleep(self) -> None:

        self._presence.set_state(
            PresenceState.SLEEPING
        )