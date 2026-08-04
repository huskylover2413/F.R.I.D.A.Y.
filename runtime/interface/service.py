"""
==========================================================
F.R.I.D.A.Y.

Interface Service
==========================================================
"""

from runtime.registry import Service, ServiceState


class InterfaceService(Service):
    """
    Hosts FRIDAY user interfaces.
    """

    def __init__(self) -> None:

        super().__init__("Interface")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Interface operating normally."