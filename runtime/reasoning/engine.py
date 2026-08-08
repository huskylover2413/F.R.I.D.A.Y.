"""
==========================================================
F.R.I.D.A.Y.

Reasoning Engine

Foundation Release 3.2
==========================================================
"""

from __future__ import annotations

from runtime.ai.manager import AIManager


class ReasoningEngine:
    """
    High-level reasoning.

    Eventually this will combine:

        • Memory
        • Vision
        • Planning
        • AI
    """

    def __init__(self):

        self._ai = AIManager()

    def think(
        self,
        prompt: str,
    ) -> str:

        response = self._ai.generate(
            prompt
        )

        return response.message