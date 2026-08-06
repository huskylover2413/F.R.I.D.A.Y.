"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/profile/models.py

Purpose:
    Profile models.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    8
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class UserProfile:
    """
    Represents the active FRIDAY user.
    """

    display_name: str

    greeting: str

    language: str

    voice: str

    timezone: str