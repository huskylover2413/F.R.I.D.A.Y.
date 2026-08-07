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
    15.0
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import AIResponse


class AIProvider(ABC):
    """
    Base class for every AI provider.

    FRIDAY communicates only through this interface.
    Providers may be cloud based or local.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable provider name.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> AIResponse:
        """
        Generate a response.

        Parameters
        ----------
        prompt:
            User request.

        Returns
        -------
        AIResponse
        """
        raise NotImplementedError