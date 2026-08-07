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
    12.1
==========================================================
"""

from __future__ import annotations

from datetime import datetime

from runtime.skills.base import Skill
from runtime.skills.context import SkillContext
from runtime.skills.models import SkillResult


class DateSkill(Skill):
    """
    Reports date-related information.

    The specific response is chosen based on
    the user's original request.
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

        now = datetime.now()

        #
        # Determine what the user asked.
        #
        request = ""

        if hasattr(context, "request"):
            request = str(context.request).lower()

        #
        # Day of week
        #
        if (
            "what day" in request
            or "day is it" in request
            or request.strip() == "day"
        ):
            return SkillResult(
                message=f"Today is {now.strftime('%A')}."
            )

        #
        # Month
        #
        if "month" in request:
            return SkillResult(
                message=f"It is {now.strftime('%B')}."
            )

        #
        # Year
        #
        if "year" in request:
            return SkillResult(
                message=f"It is {now.strftime('%Y')}."
            )

        #
        # Full date
        #
        return SkillResult(
            message=(
                f"Today is "
                f"{now.strftime('%B %d, %Y')}."
            )
        )