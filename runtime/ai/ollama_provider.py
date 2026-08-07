"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/ollama_provider.py

Purpose:
    Ollama implementation of AIProvider with
    streaming support.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.0
==========================================================
"""

from __future__ import annotations

from collections.abc import Iterator

import requests

from .models import AIResponse
from .provider import AIProvider


class OllamaProvider(AIProvider):
    """
    Local Ollama provider.
    """

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
        """
        Traditional blocking response.
        """

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": self._model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return AIResponse(
            message=data["response"].strip(),
            provider=self.name,
            success=True,
        )

    def stream(
        self,
        prompt: str,
    ) -> Iterator[str]:
        """
        Stream text from Ollama.

        Yields small chunks exactly as the
        model generates them.
        """

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": self._model,
                "prompt": prompt,
                "stream": True,
            },
            stream=True,
            timeout=300,
        )

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            data = line.decode("utf-8")

            try:

                import json

                payload = json.loads(data)

            except Exception:

                continue

            chunk = payload.get(
                "response",
                "",
            )

            if chunk:

                yield chunk

            if payload.get(
                "done",
                False,
            ):
                break