"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/models.py

Purpose:
    AI response models.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    15.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AIResponse:
    """
    Response returned by an AI provider.
    """

    message: str

    provider: str

    success: bool = True