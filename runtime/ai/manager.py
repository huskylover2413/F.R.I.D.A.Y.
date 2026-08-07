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
    15.2
==========================================================
"""

from __future__ import annotations

from .models import AIResponse
from .ollama_provider import OllamaProvider


class AIManager:
    """
    Central AI controller.

    Handles prompt construction and delegates
    generation to the configured provider.
    """

    def __init__(self) -> None:

        self._provider = OllamaProvider()

        self._system_prompt = """
You are F.R.I.D.A.Y.
(Fully Responsive Intelligent Digital Assistant for You.)

You are Michael's personal AI assistant.

Rules:

- Speak naturally.
- Be concise.
- Default to 1–3 sentences.
- Only give long answers if asked.
- Never mention being an AI language model.
- If you do not know something, say so.
- If a local skill already answered the question,
  it should never reach you.
- Prioritize helping over explaining.
- Assume responses will be spoken aloud.
"""

    @property
    def provider_name(self) -> str:

        return self._provider.name

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:

        full_prompt = (
            self._system_prompt.strip()
            + "\n\n"
            + "User: "
            + prompt
            + "\n\nFRIDAY:"
        )

        return self._provider.generate(
            full_prompt
        )