"""
==========================================================
F.R.I.D.A.Y.

Presence Manager

Foundation Release 44.0
==========================================================
"""

from __future__ import annotations

from .models import Presence
from .models import PresenceState


class PresenceManager:

    def __init__(self) -> None:

        self._presence = Presence()

    @property
    def state(self) -> PresenceState:

        return self._presence.state

    def set_state(
        self,
        state: PresenceState,
    ) -> None:

        self._presence.state = state