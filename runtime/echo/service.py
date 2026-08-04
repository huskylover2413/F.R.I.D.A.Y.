"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/echo/service.py

Purpose:
    Runtime service for Echo.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.0
Release:
    Echo
==========================================================
"""

from __future__ import annotations

from runtime.registry import Service, ServiceState


class EchoService(Service):
    """
    Echo subsystem.
    """

    def __init__(self) -> None:
        super().__init__("Echo")

    def start(self) -> None:
        self._state = ServiceState.RUNNING

    def stop(self) -> None:
        self._state = ServiceState.STOPPED

    def health_report(self) -> str:
        return "Echo operating normally."