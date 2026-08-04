"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/service.py

Purpose:
    Runtime service for the Skill subsystem.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.0
Release:
    Skills
==========================================================
"""

from __future__ import annotations

from runtime.registry import Service, ServiceState


class SkillService(Service):
    """
    Skill subsystem.
    """

    def __init__(self) -> None:

        super().__init__("Skills")

    def start(self) -> None:

        self._state = ServiceState.RUNNING

    def stop(self) -> None:

        self._state = ServiceState.STOPPED

    def health_report(self) -> str:

        return "Skill system operating normally."