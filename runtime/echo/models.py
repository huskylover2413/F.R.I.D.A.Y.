"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/echo/models.py

Purpose:
    Defines speech recognition data models.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.0
Release:
    Echo
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SpeechResult:
    """
    Represents recognized speech.
    """

    text: str

    confidence: float