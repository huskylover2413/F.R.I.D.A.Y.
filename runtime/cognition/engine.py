"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/cognition/engine.py

Purpose:
    Coordinates the complete FRIDAY reasoning pipeline.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    8.1
==========================================================
"""

from __future__ import annotations

from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine
from runtime.profile import ProfileManager
from runtime.skills import SkillContext, SkillRegistry
from runtime.skills.system import (
    DateSkill,
    GreetingSkill,
    TimeSkill,
)

from .models import Response


class CognitionEngine:
    """
    Coordinates FRIDAY's reasoning pipeline.
    """

    def __init__(self) -> None:

        self._intent = IntentEngine()
        self._decision = DecisionEngine()

        #
        # Load the active user profile.
        #
        self._profile = ProfileManager().load()

        #
        # Register available skills.
        #
        self._skills = SkillRegistry()

        self._skills.register(GreetingSkill())
        self._skills.register(TimeSkill())
        self._skills.register(DateSkill())

    def process(
        self,
        text: str,
    ) -> Response:
        """
        Process a user request.
        """

        intent = self._intent.analyze(text)

        decision = self._decision.decide(intent)

        if decision.skill_name is None:

            return Response(
                message="I'm not sure how to help with that yet.",
                success=False,
            )

        skill = self._skills.get(
            decision.skill_name
        )

        context = SkillContext(
            profile=self._profile,
        )

        result = skill.execute(context)

        return Response(
            message=result.message,
            success=result.success,
        )