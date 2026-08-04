"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/models.py

Purpose:
    Defines models used by the Skill system.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.0
Release:
    Skills
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkillResult:
    """
    Result returned by a Skill.
    """

    message: str

    success: bool = True