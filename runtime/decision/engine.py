"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/decision/engine.py

Purpose:
    Converts Intent into executable decisions.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.6.1
Release:
    Skills Integration
==========================================================
"""

from __future__ import annotations

from runtime.intent import IntentResult, IntentType

from .models import DecisionResult, DecisionType


class DecisionEngine:
    """
    Determines what FRIDAY should do next.
    """

    def decide(
        self,
        intent: IntentResult,
    ) -> DecisionResult:

        match intent.intent:

            case IntentType.GREETING:
                skill = "Greeting"

            case IntentType.TIME_REQUEST:
                skill = "Time"

            case IntentType.DATE_REQUEST:
                skill = "Date"

            case _:
                return DecisionResult(
                    decision=DecisionType.UNKNOWN,
                    skill_name=None,
                    confidence=0.0,
                )

        return DecisionResult(
            decision=DecisionType.EXECUTE_SKILL,
            skill_name=skill,
            confidence=1.0,
        )