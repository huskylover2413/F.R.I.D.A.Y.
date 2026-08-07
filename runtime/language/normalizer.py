"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/language/normalizer.py

Purpose:
    Cleans speech recognition before intent analysis.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    14.0
==========================================================
"""

from __future__ import annotations


class LanguageNormalizer:

    def normalize(
        self,
        text: str,
    ) -> str:

        value = text.lower()

        #
        # Unicode operators
        #
        value = value.replace("×", "*")
        value = value.replace("÷", "/")
        value = value.replace("−", "-")

        #
        # Common Apple Speech mistakes
        #
        corrections = {
            "squre": "square",
            "squred": "squared",
            "fctoril": "factorial",
            "factoril": "factorial",
            "factori": "factorial",
        }

        for wrong, right in corrections.items():
            value = value.replace(
                wrong,
                right,
            )

        return value