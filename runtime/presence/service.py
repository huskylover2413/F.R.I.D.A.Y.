"""
==========================================================
F.R.I.D.A.Y.

Presence Service
==========================================================
"""

from runtime.registry import Service
from runtime.registry import ServiceState


class PresenceService(Service):

    def __init__(self):

        super().__init__("Presence")

    def start(self):

        self._state = ServiceState.RUNNING

    def stop(self):

        self._state = ServiceState.STOPPED

    def health_report(self):

        return "Presence operating normally."