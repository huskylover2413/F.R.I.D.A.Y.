"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/cognition/service.py

Purpose:
    Runtime service for Cognition.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.7.0
Release:
    Cognition
==========================================================
"""

from __future__ import annotations

from runtime.registry import Service, ServiceState


class CognitionService(Service):
    """
    Cognition subsystem.
    """

    def __init__(self) -> None:

        super().__init__("Cognition")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Cognition operating normally."