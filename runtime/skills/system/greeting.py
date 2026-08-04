"""
==========================================================
F.R.I.D.A.Y.
System Greeting Skill
==========================================================
"""

from __future__ import annotations

from runtime.skills.base import Skill
from runtime.skills.models import SkillResult


class GreetingSkill(Skill):

    @property
    def name(self) -> str:

        return "Greeting"

    def execute(self) -> SkillResult:

        return SkillResult(
            message="Good afternoon, Shae."
        )