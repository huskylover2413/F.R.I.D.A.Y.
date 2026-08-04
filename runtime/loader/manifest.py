"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/loader/manifest.py

Purpose:
    Defines the services that comprise the FRIDAY runtime.

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
from typing import Type

from runtime.doctor import DoctorService
from runtime.registry import Service


@dataclass(frozen=True, slots=True)
class ServiceManifest:
    """
    Defines the services available to the Runtime.
    """

    services: tuple[Type[Service], ...] = (
        DoctorService,
    )