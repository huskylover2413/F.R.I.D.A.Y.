"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/doctor/doctor.py

Purpose:
    Coordinates all health collectors and produces a
    complete system health report.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from runtime.doctor.collectors import Collector
from runtime.doctor.report import HealthReport


class Doctor:
    """
    Coordinates all registered health collectors.
    """

    def __init__(self) -> None:
        self._collectors: list[Collector] = []

    def register(self, collector: Collector) -> None:
        """
        Register a health collector.
        """

        self._collectors.append(collector)

    def run(self) -> list[HealthReport]:
        """
        Execute every registered collector.
        """

        reports: list[HealthReport] = []

        for collector in self._collectors:
            reports.append(collector.collect())

        return reports