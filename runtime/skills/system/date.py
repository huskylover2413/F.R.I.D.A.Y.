"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/date.py

Purpose:
    System Date Skill

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    8.1
==========================================================
"""

from __future__ import annotations

from datetime import datetime

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult


class DateSkill(Skill):
    """
    Reports today's date.
    """

    @property
    def name(self) -> str:
        return "Date"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:
        """
        Execute the Date skill.
        """

        today = datetime.now().strftime("%B %d, %Y")

        return SkillResult(
            message=f"Today is {today}."
        )