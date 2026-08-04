"""
==========================================================
F.R.I.D.A.Y.
System Date Skill
==========================================================
"""

from __future__ import annotations

from datetime import datetime

from runtime.skills.base import Skill
from runtime.skills.models import SkillResult


class DateSkill(Skill):

    @property
    def name(self) -> str:

        return "Date"

    def execute(self) -> SkillResult:

        today = datetime.now().strftime("%B %d, %Y")

        return SkillResult(
            message=f"Today is {today}."
        )