"""
==========================================================
F.R.I.D.A.Y.
Brain

Foundation Release:
    18.1
==========================================================
"""

from __future__ import annotations

from runtime.intent import IntentEngine, IntentType

from .models import BrainAction, BrainDecision


class Brain:

    def __init__(self) -> None:

        self._intent = IntentEngine()

    def think(
        self,
        request: str,
    ) -> BrainDecision:

        intent = self._intent.analyze(
            request
        )

        #
        # Existing local skills
        #

        if intent.intent in {

            IntentType.GREETING,
            IntentType.TIME_REQUEST,
            IntentType.DATE_REQUEST,
            IntentType.HELP_REQUEST,
            IntentType.IDENTITY_REQUEST,
            IntentType.MATH_REQUEST,

        }:

            return BrainDecision(

                action=BrainAction.SKILL,

                target=intent.intent.name,

                confidence=intent.confidence,

                reason="Local Skill",

            )

        #
        # Everything else goes to AI.
        #

        return BrainDecision(

            action=BrainAction.AI,

            confidence=1.0,

            reason="General Knowledge",

        )