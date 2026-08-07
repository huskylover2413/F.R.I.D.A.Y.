"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/ollama_provider.py

Purpose:
    Ollama implementation of AIProvider.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    15.1
==========================================================
"""

from __future__ import annotations

import requests

from .models import AIResponse
from .provider import AIProvider


class OllamaProvider(AIProvider):

    def __init__(
        self,
        model: str = "qwen3:8b",
    ) -> None:

        self._model = model

    @property
    def name(self) -> str:

        return "Ollama"

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": self._model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return AIResponse(
            message=data["response"].strip(),
            provider=self.name,
            success=True,
        )