"""
==========================================================
F.R.I.D.A.Y.

Apple Speech Package

Purpose:
    Apple Speech Framework implementation.

Author:
    Shae Simpson & OpenAI ChatGPT
==========================================================
"""

from .provider import AppleSpeechProvider
from .recognizer import AppleRecognizer

__all__ = [
    "AppleSpeechProvider",
    "AppleRecognizer",
]