"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/service.py

Purpose:
    Runtime service for the AI subsystem.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    15.0
==========================================================
"""

from __future__ import annotations

from runtime.registry import Service, ServiceState


class AIService(Service):
    """
    AI subsystem runtime service.
    """

    def __init__(self) -> None:

        super().__init__("AI")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "AI subsystem operating normally."