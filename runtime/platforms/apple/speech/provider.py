"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/provider.py

Purpose:
<<<<<<< HEAD
    Apple Speech Provider

Author:
    Shae Simpson & OpenAI ChatGPT
=======
    Apple Speech provider.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    1.0.0
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
==========================================================
"""

from __future__ import annotations

from runtime.speech.models import SpeechResult
from runtime.speech.provider import SpeechProvider

<<<<<<< HEAD
=======
from .microphone import AppleMicrophone
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
from .recognizer import AppleRecognizer


class AppleSpeechProvider(SpeechProvider):
    """
<<<<<<< HEAD
    Apple implementation of SpeechProvider.
    """

    def __init__(self) -> None:
        self._recognizer = AppleRecognizer()

    def recognize(self) -> SpeechResult:

        text = self._recognizer.recognize()
=======
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
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

        return SpeechResult(
            text=text,
            confidence=1.0 if text else 0.0,
<<<<<<< HEAD
        )
=======
        )

    def shutdown(self) -> None:
        """
        Shutdown Apple Speech.
        """

        self._recognizer.shutdown()
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
