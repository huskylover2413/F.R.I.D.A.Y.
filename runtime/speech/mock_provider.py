"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/speech/mock_provider.py

Purpose:
    Mock speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from __future__ import annotations

from runtime.devices import MicrophoneDevice

from .models import SpeechResult
from .provider import SpeechProvider


class MockSpeechProvider(SpeechProvider):
    """
    Development speech recognizer.
    """

    def __init__(
        self,
        microphone: MicrophoneDevice,
    ) -> None:

        self._microphone = microphone

    def recognize(self) -> SpeechResult:
        """
        Pretend to recognize speech.
        """

        audio = self._microphone.listen()

        return SpeechResult(
            text=f"Received {len(audio)} bytes of audio.",
            confidence=1.0,
        )