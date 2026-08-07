"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/intent/engine.py

Purpose:
    Determines user intent from recognized speech.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.7
==========================================================
"""

from __future__ import annotations

import re

from .models import IntentResult, IntentType


class IntentEngine:
    """
    Rule-based intent engine.
    """

    def analyze(
        self,
        text: str,
    ) -> IntentResult:

        value = text.lower().strip()

        #
        # Identity
        #
        if any(
            phrase in value
            for phrase in (
                "who are you",
                "what are you",
                "identify yourself",
                "tell me about yourself",
            )
        ):
            return IntentResult(
                IntentType.IDENTITY_REQUEST,
                1.0,
            )

        #
        # Help
        #
        if any(
            phrase in value
            for phrase in (
                "help",
                "what can you do",
                "capabilities",
                "commands",
            )
        ):
            return IntentResult(
                IntentType.HELP_REQUEST,
                1.0,
            )

        #
        # Greetings
        #
        if any(
            phrase in value
            for phrase in (
                "hello",
                "hi",
                "hey",
                "good morning",
                "good afternoon",
                "good evening",
            )
        ):
            return IntentResult(
                IntentType.GREETING,
                1.0,
            )

        #
        # Time
        #
        if any(
            phrase in value
            for phrase in (
                "time",
                "what time",
                "current time",
                "tell me the time",
            )
        ):
            return IntentResult(
                IntentType.TIME_REQUEST,
                1.0,
            )

        #
        # Date
        #
        if any(
            phrase in value
            for phrase in (
                "date",
                "today",
                "what day",
                "day is it",
                "month",
                "year",
            )
        ):
            return IntentResult(
                IntentType.DATE_REQUEST,
                1.0,
            )

        #
        # Math
        #
        math_keywords = (
            "calculate",
            "compute",
            "evaluate",
            "plus",
            "minus",
            "times",
            "multiplied",
            "divided",
            "over",
            "square root",
            "sqrt",
            "factorial",
            "power",
            "squared",
            "cubed",
            "pi",
            "sin",
            "cos",
            "tan",
            "log",
            "mean",
            "median",
            "gcd",
            "lcm",
            "comb",
            "perm",
            "hypot",
        )

        has_operator = bool(
            re.search(r"[+\-*/%^()×÷]", value)
        )

        has_number = bool(
            re.search(r"\d", value)
        )

        if (
            any(keyword in value for keyword in math_keywords)
            or (has_operator and has_number)
        ):
            return IntentResult(
                IntentType.MATH_REQUEST,
                1.0,
            )

        return IntentResult(
            IntentType.UNKNOWN,
            0.0,
        )