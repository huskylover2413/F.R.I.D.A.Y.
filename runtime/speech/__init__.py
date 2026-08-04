"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/speech/__init__.py

Purpose:
    Public interface for FRIDAY speech recognition.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from .mock_provider import MockSpeechProvider
from .models import SpeechResult
from .provider import SpeechProvider
from .recognizer import SpeechRecognizer

__all__ = [
    "SpeechResult",
    "SpeechProvider",
    "SpeechRecognizer",
    "MockSpeechProvider",
]