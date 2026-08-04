"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/doctor/collectors/base.py

Purpose:
    Defines the base interface for all Doctor collectors.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from runtime.doctor.report import HealthReport


class Collector(ABC):
    """
    Base class for every Doctor collector.

    Each collector inspects one specific part of FRIDAY
    and returns a HealthReport.
    """

    @abstractmethod
    def collect(self) -> HealthReport:
        """
        Collect health information.
        """
        raise NotImplementedError