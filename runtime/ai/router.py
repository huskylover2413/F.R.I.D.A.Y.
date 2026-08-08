"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/router.py

Purpose:
    Chooses which local AI model should answer
    each request.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    17.0
==========================================================
"""

from __future__ import annotations


class AIRouter:
    """
    Selects the appropriate AI model.
    """

    def choose_model(
        self,
        request: str,
    ) -> str:

        text = request.lower()

        #
        # Complex reasoning
        #
        complex_words = (
            "prove",
            "derive",
            "integral",
            "differentiate",
            "derivative",
            "calculus",
            "optimize",
            "optimization",
            "program",
            "python",
            "code",
            "algorithm",
            "research",
            "analyze",
            "compare",
            "investment",
            "medical",
            "physics",
            "chemistry",
        )

        if any(
            word in text
            for word in complex_words
        ):
            return "qwen3:8b"

        #
        # Everything else
        #
        return "llama3.2:3b"