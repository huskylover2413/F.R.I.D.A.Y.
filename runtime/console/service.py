"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/console/service.py

Purpose:
    Implements the Console as a FRIDAY service.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.3 - Pulse
==========================================================
"""

from runtime.console.console import console
from runtime.registry import Service, ServiceState


class ConsoleService(Service):
    """
    Runtime service responsible for terminal output.
    """

    def __init__(self) -> None:
        super().__init__("Console")

    def start(self) -> None:
        self._state = ServiceState.STARTING

        console.info("Console starting...")

        self._state = ServiceState.RUNNING

    def stop(self) -> None:
        console.info("Console shutting down...")

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:
        if self.state == ServiceState.RUNNING:
            return "Console operating normally."

        if self.state == ServiceState.DEGRADED:
            return "Console operating with reduced capability."

        if self.state == ServiceState.FAILED:
            return "Console unavailable."

        return f"Console is {self.state.name.lower()}."