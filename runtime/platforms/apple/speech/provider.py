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

Version:
    1.0.0
==========================================================
"""

from __future__ import annotations

from runtime.speech.models import SpeechResult
from runtime.speech.provider import SpeechProvider

from .microphone import AppleMicrophone
from .recognizer import AppleRecognizer


class AppleSpeechProvider(SpeechProvider):
    """
    Native Apple Speech provider.

    Owns one microphone and one recognizer for the
    lifetime of the session.

    The SpeechProvider interface remains synchronous,
    while the underlying Apple recognizer runs
    continuously.
    """

    def __init__(self) -> None:

        self._microphone = AppleMicrophone()

        self._recognizer = AppleRecognizer(
            microphone=self._microphone,
        )

        self._recognizer.start()

    def recognize(self) -> SpeechResult:
        """
        Wait for the next completed utterance.
        """

        text = self._recognizer.next_phrase()

        return SpeechResult(
            text=text,
            confidence=1.0 if text else 0.0,
        )

    def shutdown(self) -> None:
        """
        Shutdown Apple Speech.
        """

        self._recognizer.shutdown()