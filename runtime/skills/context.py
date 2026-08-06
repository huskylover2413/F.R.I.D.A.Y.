"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/context.py

Purpose:
    Defines the context provided to every skill.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    8.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from runtime.profile import UserProfile


@dataclass(slots=True, frozen=True)
class SkillContext:
    """
    Shared information available to every skill.
    """

    profile: UserProfile