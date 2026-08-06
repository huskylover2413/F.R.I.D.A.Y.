"""
==========================================================
F.R.I.D.A.Y.
Profile Service
==========================================================
"""

from runtime.registry import Service, ServiceState

from .manager import ProfileManager


class ProfileService(Service):
    """
    Runtime profile service.
    """

    def __init__(self) -> None:

        super().__init__("Profile")

        self.manager = ProfileManager()

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Profile loaded."