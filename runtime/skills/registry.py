"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/registry.py

Purpose:
    Stores registered FRIDAY Skills.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.0
Release:
    Skills
==========================================================
"""

from __future__ import annotations

from .base import Skill


class SkillRegistry:
    """
    Registry of installed skills.
    """

    def __init__(self) -> None:

        self._skills: dict[str, Skill] = {}

    def register(
        self,
        skill: Skill,
    ) -> None:

        self._skills[skill.name] = skill

    def get(
        self,
        name: str,
    ) -> Skill:

        return self._skills[name]

    def all(self):

        return self._skills.values()