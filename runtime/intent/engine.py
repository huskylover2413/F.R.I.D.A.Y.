"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/intent/engine.py

Purpose:
    Determines user intent from recognized speech.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.5.0
Release:
    Intent
==========================================================
"""

from __future__ import annotations

from .models import IntentResult, IntentType


class IntentEngine:
    """
    Simple rule-based Intent Engine.
    """

    def analyze(self, text: str) -> IntentResult:
        """
        Determine user intent.
        """

        value = text.lower()

        if "hello" in value:
            return IntentResult(
                IntentType.GREETING,
                1.0,
            )

        if "time" in value:
            return IntentResult(
                IntentType.TIME_REQUEST,
                1.0,
            )

        if "date" in value:
            return IntentResult(
                IntentType.DATE_REQUEST,
                1.0,
            )

        return IntentResult(
            IntentType.UNKNOWN,
            0.0,
        )