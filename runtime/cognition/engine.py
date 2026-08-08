"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/cognition/engine.py

Purpose:
    Coordinates FRIDAY's reasoning pipeline.

Foundation Release:
    26.2
==========================================================
"""

from __future__ import annotations

from runtime.decision import DecisionEngine
from runtime.intent import IntentEngine
from runtime.profile import ProfileManager
from runtime.services import ServiceContainer
from runtime.skills import SkillContext

from .models import Response


class CognitionEngine:
    """
    FRIDAY Brain.

    Responsibilities

        • Understand requests
        • Build execution plans
        • Execute skills
        • Fall back to AI
    """

    def __init__(self) -> None:

        self._intent = IntentEngine()

        self._decision = DecisionEngine()

        self._services = ServiceContainer()

        #
        # Keep compatibility with existing code.
        #
        self._profile = ProfileManager().load()

    def process(
        self,
        text: str,
    ) -> Response:

        #
        # ===============================
        # 1. Planner
        # ===============================
        #

        plan = self._services.planner.plan(
            text
        )

        if not plan.empty:

            result = self._services.executor.execute(
                plan=plan,
                profile=self._profile,
                request=text,
            )

            return Response(
                message=result.message,
                success=result.success,
            )

        #
        # ===============================
        # 2. Existing Intent System
        # ===============================
        #

        intent = self._intent.analyze(
            text
        )

        decision = self._decision.decide(
            intent
        )

        if decision.skill_name is not None:

            skill = self._services.skills.get(
                decision.skill_name
            )

            if skill is not None:

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

        #
        # ===============================
        # 3. AI Fallback
        # ===============================
        #

        ai = self._services.ai.generate(
            text
        )

        return Response(
            message=ai.message,
            success=ai.success,
        )