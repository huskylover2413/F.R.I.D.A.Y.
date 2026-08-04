"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/context/context.py

Purpose:
    Defines the shared Service Context provided to every
    FRIDAY subsystem.

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

from runtime.core import CoreServices
from runtime.registry import ServiceRegistry


@dataclass(slots=True, frozen=True)
class ServiceContext:
    """
    Shared application context for every Service.
    """

    core: CoreServices
    registry: ServiceRegistry