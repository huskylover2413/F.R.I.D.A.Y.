"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/speech/recognizer.py

Purpose:
    High-level speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from __future__ import annotations

from .models import SpeechResult
from .provider import SpeechProvider


class SpeechRecognizer:
    """
    Coordinates speech recognition.
    """

    def __init__(
        self,
        provider: SpeechProvider,
    ) -> None:

        self._provider = provider

    def listen(self) -> SpeechResult:
        """
        Recognize speech.
        """

        return self._provider.recognize()