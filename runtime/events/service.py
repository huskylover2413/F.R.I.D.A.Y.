"""
==========================================================
F.R.I.D.A.Y.

Event Service
==========================================================
"""

from runtime.registry import Service
from runtime.registry import ServiceState


class EventService(Service):

    def __init__(self):

        super().__init__("Events")

    def start(self):

        self._state = ServiceState.RUNNING

    def stop(self):

        self._state = ServiceState.STOPPED

    def health_report(self):

        return "Event bus operating normally."