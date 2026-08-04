"""
==========================================================
F.R.I.D.A.Y.
System Time Skill
==========================================================
"""

from __future__ import annotations

from datetime import datetime

from runtime.skills.base import Skill
from runtime.skills.models import SkillResult


class TimeSkill(Skill):

    @property
    def name(self) -> str:

        return "Time"

    def execute(self) -> SkillResult:

        now = datetime.now().strftime("%I:%M %p")

        return SkillResult(
            message=f"The current time is {now}."
        )