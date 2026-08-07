"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/manager.py

Purpose:
    Central manager for all AI interactions.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.0
==========================================================
"""

from __future__ import annotations

from collections.abc import Callable

from .models import AIResponse
from .ollama_provider import OllamaProvider
from .streaming import StreamingCoordinator


class AIManager:
    """
    Central AI controller.
    """

    def __init__(self) -> None:

        self._provider = OllamaProvider()

        self._system_prompt = """
You are F.R.I.D.A.Y.
(Fully Responsive Intelligent Digital Assistant for You.)

You are Michael's personal AI assistant.

Rules:

- Speak naturally.
- Keep answers short.
- Default to one to three sentences.
- Only elaborate when asked.
- Never say you are a language model.
- Assume every answer will be spoken aloud.
"""

    def _build_prompt(
        self,
        prompt: str,
    ) -> str:

        return (
            self._system_prompt.strip()
            + "\n\nUser: "
            + prompt
            + "\n\nFRIDAY:"
        )

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:

        return self._provider.generate(
            self._build_prompt(
                prompt
            )
        )

    def stream(
        self,
        prompt: str,
        callback: Callable[[str], None],
    ) -> None:

        coordinator = StreamingCoordinator(
            callback
        )

        for chunk in self._provider.stream(
            self._build_prompt(
                prompt
            )
        ):

            coordinator.push(
                chunk
            )

        coordinator.finish()