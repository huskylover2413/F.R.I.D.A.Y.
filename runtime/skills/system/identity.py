"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/identity.py

Purpose:
    System Identity Skill

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.1
==========================================================
"""

from __future__ import annotations

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult


class IdentitySkill(Skill):
    """
    Explains who FRIDAY is.
    """

    @property
    def name(self) -> str:
        return "Identity"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:

        return SkillResult(
            message=(
                "I am F.R.I.D.A.Y., your Fully Responsive "
                "Intelligent Digital Assistant for You. "
                "My purpose is to help you through natural "
                "voice interaction, reasoning, memory, and "
                "modular skills."
            )
        )