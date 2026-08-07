"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/provider.py

Purpose:
    Abstract AI provider interface.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.0
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator

from .models import AIResponse


class AIProvider(ABC):
    """
    Base interface implemented by every AI provider.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> AIResponse:
        raise NotImplementedError

    @abstractmethod
    def stream(
        self,
        prompt: str,
    ) -> Iterator[str]:
        """
        Stream text from the provider.

        Returns an iterator of text chunks.
        """
        raise NotImplementedError