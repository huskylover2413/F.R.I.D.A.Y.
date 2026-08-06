"""
==========================================================
F.R.I.D.A.Y.

Voice Service
==========================================================
"""

from runtime.registry import Service, ServiceState


class VoiceService(Service):

    def __init__(self) -> None:

        super().__init__("Voice")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Voice operating normally."