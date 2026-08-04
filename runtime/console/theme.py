"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/console/theme.py

Purpose:
    Defines the visual styling used by the FRIDAY Console.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.2 - Forge
==========================================================
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    title_line: str = "═" * 54
    app_name: str = "F.R.I.D.A.Y."


DEFAULT_THEME = Theme() 