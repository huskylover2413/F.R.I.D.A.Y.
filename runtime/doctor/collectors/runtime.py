"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/doctor/collectors/runtime.py

Purpose:
    Collects health information about the Pulse runtime.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from runtime.doctor.collectors.base import Collector
from runtime.doctor.report import HealthReport
from runtime.pulse.state import RuntimeState


class RuntimeCollector(Collector):
    """
    Reports the health of the Pulse runtime.
    """

    def __init__(self, state: RuntimeState) -> None:
        self._state = state

    def collect(self) -> HealthReport:
        """
        Collect runtime health information.
        """

        healthy = self._state is RuntimeState.RUNNING

        return HealthReport(
            subsystem="Runtime",
            healthy=healthy,
            status=self._state.name,
            details="Pulse runtime state.",
        )