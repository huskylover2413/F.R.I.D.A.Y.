"""
==========================================================
F.R.I.D.A.Y.
Intent Engine

Foundation Release 17.1
==========================================================
"""

from __future__ import annotations

import re

from .models import IntentResult, IntentType


class IntentEngine:

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
                "today's date",
                "what day",
                "what date",
                "today",
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
            "square root",
            "sqrt",
            "factorial",
            "power",
            "squared",
            "cubed",
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

        #
        # Whole-word matching
        #

        words = set(
            re.findall(
                r"[a-z]+",
                value,
            )
        )

        if (
            any(
                keyword in value
                if " " in keyword
                else keyword in words
                for keyword in math_keywords
            )
            or re.search(
                r"\d+\s*[-+*/%^×÷]\s*\d+",
                value,
            )
        ):

            return IntentResult(
                IntentType.MATH_REQUEST,
                1.0,
            )

        #
        # Constants
        #

        if " pi " in f" {value} ":

            return IntentResult(
                IntentType.MATH_REQUEST,
                1.0,
            )

        if value == "pi":

            return IntentResult(
                IntentType.MATH_REQUEST,
                1.0,
            )

        return IntentResult(
            IntentType.UNKNOWN,
            0.0,
        )