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
    15.2
==========================================================
"""

from __future__ import annotations

from runtime.ai.manager import AIManager
from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine
from runtime.profile import ProfileManager
from runtime.skills import SkillContext, SkillRegistry
from runtime.skills.system import (
    DateSkill,
    GreetingSkill,
    HelpSkill,
    IdentitySkill,
    MathSkill,
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

        self._profile = ProfileManager().load()

        #
        # AI Manager
        #
        self._ai = AIManager()

        #
        # Built-in Skills
        #
        self._skills = SkillRegistry()

        self._skills.register(GreetingSkill())
        self._skills.register(TimeSkill())
        self._skills.register(DateSkill())
        self._skills.register(HelpSkill())
        self._skills.register(IdentitySkill())
        self._skills.register(MathSkill())

    def process(
        self,
        text: str,
    ) -> Response:
        """
        Process a single user request.
        """

        intent = self._intent.analyze(
            text
        )

        decision = self._decision.decide(
            intent
        )

        #
        # Unknown requests are handled by AI.
        #
        if decision.skill_name is None:

            ai_response = self._ai.generate(
                text
            )

            return Response(
                message=ai_response.message,
                success=ai_response.success,
            )

        skill = self._skills.get(
            decision.skill_name
        )

        context = SkillContext(
            profile=self._profile,
            request=text,
        )

        result = skill.execute(
            context
        )

        return Response(
            message=result.message,
            success=result.success,
        )