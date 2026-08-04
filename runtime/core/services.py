"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/core/services.py

Purpose:
    Provides the shared infrastructure services used by
    every major FRIDAY subsystem.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.2.0
Release:
    Foundation Release 2
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from runtime.console import console

from .config import ConfigurationManager
from .events import EventBus


@dataclass(slots=True)
class CoreServices:
    """
    Shared infrastructure available throughout FRIDAY.

    This object owns the common services that should exist
    only once during the lifetime of the application.
    """

    event_bus: EventBus
    console: object
    config: ConfigurationManager

    @classmethod
    def create(cls) -> "CoreServices":
        """
        Construct the default Core Services.
        """

        return cls(
            event_bus=EventBus(),
            console=console,
            config=ConfigurationManager(),
        )