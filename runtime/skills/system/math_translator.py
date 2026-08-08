"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/skills/system/math_translator.py

Purpose:
    Converts spoken mathematics into expressions.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    17.2
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
        # IMPORTANT:
        # Replace LONG phrases BEFORE removing words.
        #

        phrase_map = {

            "square root of": "sqrt(",
            "square root": "sqrt(",

            "factorial of": "factorial(",
            "factorial": "factorial(",

            "pi squared": "(pi^2)",
            "pi cubed": "(pi^3)",

            "to the power of": "^",
            "to the": "^",

            "multiplied by": "*",
            "divided by": "/",

            "plus": "+",
            "minus": "-",
            "times": "*",
            "over": "/",
        }

        for old, new in sorted(
            phrase_map.items(),
            key=lambda x: len(x[0]),
            reverse=True,
        ):

            expression = expression.replace(
                old,
                new,
            )

        #
        # Remove filler
        #

        for word in (

            "what is",
            "calculate",
            "compute",
            "evaluate",
            "please",
            "the",
            "a",
            "an",

        ):

            expression = expression.replace(
                word,
                "",
            )

        #
        # Remove extra whitespace
        #

        expression = re.sub(
            r"\s+",
            "",
            expression,
        )

        #
        # Automatically close
        #

        expression = re.sub(
            r"sqrt\(([^)]*)$",
            r"sqrt(\1)",
            expression,
        )

        expression = re.sub(
            r"factorial\(([^)]*)$",
            r"factorial(\1)",
            expression,
        )

        #
        # Clean punctuation
        #

        expression = expression.replace(
            "?",
            "",
        )

        return expression