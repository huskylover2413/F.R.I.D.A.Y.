"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/base.py

Purpose:
    Base class for all FRIDAY Skills.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.0
Release:
    Skills
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import SkillResult


class Skill(ABC):
    """
    Base class for every FRIDAY Skill.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human readable skill name.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self) -> SkillResult:
        """
        Execute the skill.
        """
        raise NotImplementedError