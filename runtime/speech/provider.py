"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/speech/provider.py

Purpose:
    Defines the speech provider interface.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.4.1
Release:
    Ears
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import SpeechResult


class SpeechProvider(ABC):
    """
    Base class for speech recognition providers.
    """

    @abstractmethod
    def recognize(self) -> SpeechResult:
        """
        Recognize speech.

        Returns:
            SpeechResult
        """
        raise NotImplementedError