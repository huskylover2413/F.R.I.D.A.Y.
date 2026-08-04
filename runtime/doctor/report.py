"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/doctor/report.py

Purpose:
    Defines the standard health report returned by Doctor
    collectors.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class HealthReport:
    """
    Represents the health of a single subsystem.
    """

    subsystem: str

    healthy: bool

    status: str

    details: str = ""