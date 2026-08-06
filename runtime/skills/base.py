"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/base.py

Purpose:
    Base class for every FRIDAY Skill.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    8.1
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .context import SkillContext
from .models import SkillResult


class Skill(ABC):
    """
    Base class for every FRIDAY Skill.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable skill name.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        context: SkillContext,
    ) -> SkillResult:
        """
        Execute the skill.
        """
        raise NotImplementedError