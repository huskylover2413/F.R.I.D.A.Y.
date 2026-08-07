"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/math_translator.py

Purpose:
    Converts natural language into mathematical expressions.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    13.10
==========================================================
"""

from __future__ import annotations

import re


_NUMBER_WORDS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
}


class MathTranslator:

    def translate(
        self,
        text: str,
    ) -> str:

        expression = text.lower()

        #
        # Unicode operators
        #
        expression = (
            expression
            .replace("×", "*")
            .replace("÷", "/")
            .replace("−", "-")
        )

        #
        # Spoken numbers
        #
        for word, number in _NUMBER_WORDS.items():
            expression = re.sub(
                rf"\b{word}\b",
                number,
                expression,
            )

        #
        # Remove filler words
        #
        for word in (
            "what is",
            "calculate",
            "compute",
            "evaluate",
            "the",
            "a",
            "an",
        ):
            expression = expression.replace(word, "")

        #
        # Functions
        #
        expression = expression.replace(
            "square root of",
            "sqrt("
        )

        expression = expression.replace(
            "factorial of",
            "factorial("
        )

        #
        # Operators
        #
        replacements = {
            "multiplied by": "*",
            "divided by": "/",
            "times": "*",
            "plus": "+",
            "minus": "-",
            "over": "/",
            "pi squared": "pi^2",
            "pi cubed": "pi^3",
        }

        for old, new in sorted(
            replacements.items(),
            key=lambda item: len(item[0]),
            reverse=True,
        ):
            expression = expression.replace(old, new)

        #
        # Remove whitespace
        #
        expression = re.sub(
            r"\s+",
            "",
            expression,
        )

        #
        # Close one-argument function calls
        #
        expression = re.sub(
            r"sqrt\(([^)]+)$",
            r"sqrt(\1)",
            expression,
        )

        expression = re.sub(
            r"factorial\(([^)]+)$",
            r"factorial(\1)",
            expression,
        )

        #
        # Remove question marks
        #
        expression = expression.replace("?", "")

        return expression