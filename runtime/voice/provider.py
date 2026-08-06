"""
==========================================================
F.R.I.D.A.Y.

Voice Provider

Defines the interface for speech synthesis.
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class VoiceProvider(ABC):
    """
    Base class for all voice providers.
    """

    @abstractmethod
    def speak(
        self,
        message: str,
    ) -> None:
        """
        Speak a message.
        """
        raise NotImplementedError