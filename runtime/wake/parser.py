"""
==========================================================
F.R.I.D.A.Y.

Wake Phrase Parser

Foundation Release 50.1
==========================================================
"""

from __future__ import annotations

import re


class WakePhraseParser:
    """
    Determines whether spoken text is addressing FRIDAY.

    The acoustic wake-word detector and this parser have
    separate responsibilities:

        Acoustic model -> detects the spoken name
        Parser        -> understands how FRIDAY was addressed
    """

    WAKE_NAMES = {
        "friday",
        "fri",
    }

    GREETINGS = {
        "hey",
        "hi",
        "hello",
        "good morning",
        "good afternoon",
        "good evening",
        "morning",
        "afternoon",
        "evening",
        "excuse me",
        "please",
    }

    def normalize(
        self,
        text: str,
    ) -> str:

        normalized = text.lower()

        normalized = re.sub(
            r"[^\w\s]",
            "",
            normalized,
        )

        normalized = re.sub(
            r"\s+",
            " ",
            normalized,
        )

        return normalized.strip()

    def is_address(
        self,
        text: str,
    ) -> bool:

        normalized = self.normalize(
            text
        )

        if not normalized:
            return False

        #
        # Direct name:
        #
        # Friday
        # Fri
        #

        if normalized in self.WAKE_NAMES:
            return True

        #
        # Greeting + name:
        #
        # Hey Friday
        # Good morning Friday
        # Excuse me Fri
        #

        for greeting in sorted(
            self.GREETINGS,
            key=len,
            reverse=True,
        ):

            prefix = greeting + " "

            if normalized.startswith(prefix):

                remainder = normalized[
                    len(prefix):
                ].strip()

                if remainder in self.WAKE_NAMES:
                    return True

        return False

    def extract_name(
        self,
        text: str,
    ) -> str | None:

        normalized = self.normalize(
            text
        )

        words = normalized.split()

        for name in self.WAKE_NAMES:

            if name in words:

                return name

        return None