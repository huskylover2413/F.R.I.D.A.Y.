"""
==========================================================
F.R.I.D.A.Y.

Wake Service
==========================================================
"""

from runtime.registry import Service
from runtime.registry import ServiceState


class WakeService(Service):

    def __init__(self):

        super().__init__("Wake")

    def start(self):

        self._state = ServiceState.RUNNING

    def stop(self):

        self._state = ServiceState.STOPPED

    def health_report(self):

        return "Wake operating normally."