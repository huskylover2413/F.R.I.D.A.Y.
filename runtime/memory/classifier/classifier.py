"""
==========================================================
F.R.I.D.A.Y.

Memory Classifier

Version 2.1
==========================================================
"""

from __future__ import annotations

from .models import MemoryDecision


class MemoryClassifier:
    """
    Determines whether something should become
    long-term memory.
    """

    def classify(
        self,
        text: str,
    ) -> MemoryDecision:

        value = text.lower().strip()

        #
        # Explicit memory requests
        #

        if any(

            phrase in value

            for phrase in (

                "remember",

                "don't forget",

                "do not forget",

            )

        ):

            return MemoryDecision(

                should_store=True,

                category="memory",

                confidence=1.0,

            )

        #
        # Preferences
        #

        if any(

            phrase in value

            for phrase in (

                "my favorite",

                "i prefer",

                "i like",

                "i love",

                "i hate",

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
        # Stable personal facts
        #

        if any(

            phrase in value

            for phrase in (

                "i am",

                "i'm",

                "i attend",

                "i work at",

                "i live in",

                "my major is",

            )

        ):

            return MemoryDecision(

                should_store=True,

                category="profile",

                confidence=0.90,

            )

        #
        # Active projects
        #

        if any(

            phrase in value

            for phrase in (

                "i'm building",

                "i am building",

                "my project",

                "working on",

                "developing",

            )

        ):

            return MemoryDecision(

                should_store=True,

                category="project",

                confidence=0.85,

            )

        #
        # Temporary conversation
        #

        return MemoryDecision(

            should_store=False,

            category="",

            confidence=0.0,

        )