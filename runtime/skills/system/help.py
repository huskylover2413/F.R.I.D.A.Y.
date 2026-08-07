"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/help.py

Purpose:
    System Help Skill

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.0
==========================================================
"""

from __future__ import annotations

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult


class HelpSkill(Skill):
    """
    Explains what FRIDAY can currently do.
    """

    @property
    def name(self) -> str:
        return "Help"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:

        return SkillResult(
            message=(
                "I can currently help with greetings, "
                "the current time, today's date, and basic "
                "conversation. My capabilities will continue "
                "to expand as I learn new skills."
            )
        )