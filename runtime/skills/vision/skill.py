"""
==========================================================
F.R.I.D.A.Y.

Vision Skill

Foundation Release 23.0
==========================================================
"""

from __future__ import annotations

from runtime.skills import Skill
from runtime.skills import SkillContext
from runtime.skills import SkillResult

from runtime.vision import VisionService


class VisionSkill(Skill):
    """
    Allows FRIDAY to understand
    the user's current screen.
    """

    @property
    def name(self) -> str:

        return "Vision"

    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:

        vision = VisionService()

        prompt = (
            "Describe what the user is "
            "currently looking at. "
            "Keep the response concise "
            "and helpful."
        )

        answer = vision.describe(
            prompt
        )

        return SkillResult(
            success=True,
            message=answer,
        )