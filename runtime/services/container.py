"""
==========================================================
F.R.I.D.A.Y.

Service Container

Foundation Release 26.0
==========================================================
"""

from __future__ import annotations

from runtime.ai.manager import AIManager
from runtime.planner import Planner
from runtime.executor import TaskExecutor
from runtime.profile import ProfileManager
from runtime.skills import (
    SkillRegistry,
    VisionSkill,
)
from runtime.skills.system import (
    DateSkill,
    GreetingSkill,
    HelpSkill,
    IdentitySkill,
    MathSkill,
    TimeSkill,
)


class ServiceContainer:
    """
    Owns every long-lived service used by FRIDAY.
    """

    def __init__(self) -> None:

        #
        # User Profile
        #

        self.profile = (
            ProfileManager()
            .load()
        )

        #
        # AI
        #

        self.ai = AIManager()

        #
        # Planner
        #

        self.planner = Planner()

        #
        # Skills
        #

        self.skills = SkillRegistry()

        self.skills.register(
            GreetingSkill()
        )

        self.skills.register(
            TimeSkill()
        )

        self.skills.register(
            DateSkill()
        )

        self.skills.register(
            HelpSkill()
        )

        self.skills.register(
            IdentitySkill()
        )

        self.skills.register(
            MathSkill()
        )

        self.skills.register(
            VisionSkill()
        )

        #
        # Executor
        #

        self.executor = TaskExecutor(
            self.skills
        )