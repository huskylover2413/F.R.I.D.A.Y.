"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/input/microphone.py

Purpose:
    Apple microphone input adapter.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    14.1
==========================================================
"""

from __future__ import annotations

from runtime.platforms.apple.speech.recognizer import AppleRecognizer

from .source import InputSource


class MicrophoneInput(InputSource):
    """
    Microphone input backed by the Apple Speech recognizer.
    """

    def __init__(self) -> None:

        self._recognizer = AppleRecognizer()

    def read(self) -> str:

        return self._recognizer.recognize()

    def shutdown(self) -> None:

        self._recognizer.shutdown()