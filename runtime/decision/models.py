"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/decision/models.py

Purpose:
    Defines models used by the Decision Engine.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.1
Release:
    Skills Integration
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class DecisionType(Enum):
    """
    Supported FRIDAY decisions.
    """

    UNKNOWN = auto()
    EXECUTE_SKILL = auto()


@dataclass(slots=True, frozen=True)
class DecisionResult:
    """
    Result produced by the Decision Engine.
    """

    decision: DecisionType

    skill_name: str | None

    confidence: float