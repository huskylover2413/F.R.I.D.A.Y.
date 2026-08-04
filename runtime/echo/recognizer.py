"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/echo/recognizer.py

Purpose:
    High-level speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.0
Release:
    Echo
==========================================================
"""

from __future__ import annotations

from .models import SpeechResult
from .provider import SpeechProvider


class SpeechRecognizer:
    """
    Wraps a speech provider.
    """

    def __init__(
        self,
        provider: SpeechProvider,
    ) -> None:

        self._provider = provider

    def listen(self) -> SpeechResult:
        """
        Listen for speech.
        """

        return self._provider.recognize()