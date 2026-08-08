"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/provider.py

Purpose:
    Apple Speech provider.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.1
==========================================================
"""

from __future__ import annotations

from runtime.speech.models import SpeechResult
from runtime.speech.provider import SpeechProvider

from .recognizer import AppleRecognizer


class AppleSpeechProvider(SpeechProvider):
    """
    Apple implementation of SpeechProvider.
    """

    def __init__(self) -> None:

        self._recognizer = AppleRecognizer()

    def recognize(self) -> SpeechResult:

        text = self._recognizer.recognize()

        return SpeechResult(
            text=text,
            confidence=1.0 if text else 0.0,
        )

    def shutdown(self) -> None:

        self._recognizer.shutdown()