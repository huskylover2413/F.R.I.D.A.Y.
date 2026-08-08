"""
==========================================================
F.R.I.D.A.Y.

Status Manager

Version 1.1
==========================================================
"""

from __future__ import annotations

from .models import SystemStatus


class StatusManager:

    def check(self) -> list[SystemStatus]:

        return [

            SystemStatus(
                "Speech",
                True,
                "Ready",
            ),

            SystemStatus(
                "Vision",
                True,
                "Ready",
            ),

            SystemStatus(
                "Memory",
                True,
                "Ready",
            ),

            SystemStatus(
                "Planner",
                True,
                "Ready",
            ),

            SystemStatus(
                "Reasoning",
                True,
                "Ready",
            ),

        ]