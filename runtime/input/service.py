"""
==========================================================
F.R.I.D.A.Y.

Input Service
==========================================================
"""

from runtime.registry import Service, ServiceState


class InputService(Service):

    def __init__(self) -> None:

        super().__init__("Input")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Input operating normally."