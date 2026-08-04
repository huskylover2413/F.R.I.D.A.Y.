"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/cognition/engine.py

Purpose:
    Coordinates FRIDAY reasoning.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.7.0
Release:
    Cognition
==========================================================
"""

from __future__ import annotations

from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine
from runtime.skills import SkillRegistry
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
                "I'm not sure how to help with that yet.",
                success=False,
            )

        skill = self._skills.get(
            decision.skill_name
        )

        result = skill.execute()

        return Response(
            message=result.message,
            success=result.success,
        )