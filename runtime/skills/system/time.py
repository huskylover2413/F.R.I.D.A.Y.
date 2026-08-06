"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/time.py

Purpose:
    System Time Skill

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


class TimeSkill(Skill):
    """
    Reports the current local time.
    """

    @property
    def name(self) -> str:
        return "Time"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:
        """
        Execute the Time skill.
        """

        now = datetime.now().strftime("%I:%M %p")

        return SkillResult(
            message=f"The current time is {now}."
        )