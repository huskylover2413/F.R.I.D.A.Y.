"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/brain/services.py

Purpose:
    Registry of Brain service types.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    18.2
==========================================================
"""

from __future__ import annotations

from enum import Enum, auto


class BrainService(Enum):
    """
    Services the Brain can delegate work to.
    """

    SKILLS = auto()

    AI = auto()

    MEMORY = auto()

    INTERNET = auto()

    AUTOMATION = auto()

    SYSTEM = auto()