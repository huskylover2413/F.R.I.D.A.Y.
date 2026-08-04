"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/doctor/service.py

Purpose:
    Implements the Doctor subsystem as a Runtime Service.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.3.0
Release:
    Awakening
==========================================================
"""

from __future__ import annotations

from runtime.registry import Service, ServiceState

from .doctor import Doctor


class DoctorService(Service):
    """
    Runtime service for the Doctor subsystem.
    """

    def __init__(self) -> None:
        super().__init__("Doctor")
        self.doctor = Doctor()

    def start(self) -> None:
        self._state = ServiceState.RUNNING

    def stop(self) -> None:
        self._state = ServiceState.STOPPED

    def health_report(self) -> str:
        return "Doctor operating normally."