"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/core/config/config.py

Purpose:
    Defines the application's configuration model.

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


@dataclass(slots=True)
class RuntimeConfig:
    """
    Global configuration for the FRIDAY runtime.
    """

    assistant_name: str = "FRIDAY"

    wake_word: str = "Friday"

    developer_mode: bool = False

    debug_logging: bool = False

    theme: str = "dark"

    voice_enabled: bool = False

    version: str = "0.2.0"