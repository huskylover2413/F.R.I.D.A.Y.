"""
==========================================================
F.R.I.D.A.Y.

Memory Classifier

Foundation Release 2.2
==========================================================
"""

from __future__ import annotations

from .models import MemoryDecision


class MemoryClassifier:
    """
    Determines whether information should
    become long-term memory.
    """

    def classify(
        self,
        text: str,
    ) -> MemoryDecision:

        value = text.lower()

        #
        # Preferences
        #

        if any(

            phrase in value

            for phrase in (

                "i prefer",

                "my favorite",

                "remember that",

                "always",

                "never",

            )

        ):

            return MemoryDecision(
                should_store=True,
                category="preference",
                confidence=0.95,
            )

        #
        # Personal facts
        #

        if any(

            phrase in value

            for phrase in (

                "i am",

                "i'm",

                "i attend",

                "i work",

                "i live",

            )

        ):

            return MemoryDecision(
                should_store=True,
                category="profile",
                confidence=0.90,
            )

        #
        # Projects
        #

        if any(

            phrase in value

            for phrase in (

                "project",

                "building",

                "developing",

            )

        ):

            return MemoryDecision(
                should_store=True,
                category="project",
                confidence=0.85,
            )

        return MemoryDecision(
            should_store=False,
            category="",
            confidence=0.0,
        )