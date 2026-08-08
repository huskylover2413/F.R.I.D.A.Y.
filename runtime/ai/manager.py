"""
==========================================================
F.R.I.D.A.Y.
AI Manager

Foundation Release 17.0
==========================================================
"""

from __future__ import annotations

from .models import AIResponse
from .ollama_provider import OllamaProvider
from .router import AIRouter


class AIManager:

    def __init__(self) -> None:

        self._router = AIRouter()

        self._system_prompt = (
            "You are FRIDAY. "
            "Answer naturally. "
            "Be concise unless asked for more."
        )

    def generate(
        self,
        prompt: str,
    ) -> AIResponse:

        model = self._router.choose_model(
            prompt
        )

        provider = OllamaProvider(
            model=model
        )

        print()
        print(f"AI Model : {model}")
        print()

        return provider.generate(
            self._system_prompt
            + "\n\nUser: "
            + prompt
            + "\nFRIDAY:"
        )