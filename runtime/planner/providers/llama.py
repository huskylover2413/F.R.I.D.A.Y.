"""
==========================================================
F.R.I.D.A.Y.

Llama Planner

Foundation Release 24.0
==========================================================
"""

from __future__ import annotations

import json

from runtime.ai.ollama_provider import OllamaProvider

from .base import PlannerProvider


class LlamaPlannerProvider(
    PlannerProvider
):

    def __init__(self):

        self._ai = OllamaProvider(
            model="llama3.2:3b"
        )

    def plan(
        self,
        request: str,
    ) -> list[str]:

        prompt = f"""
You are an AI planner.

Choose which FRIDAY skills
are needed.

Available skills:

Vision
Math
Conversation

Return ONLY JSON.

Example:

["Vision","Math"]

User:

{request}
"""

        response = self._ai.generate(
            prompt
        )

        try:

            return json.loads(
                response.message
            )

        except Exception:

            return [
                "Conversation"
            ]