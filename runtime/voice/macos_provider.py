"""
==========================================================
F.R.I.D.A.Y.

macOS Voice Provider

Uses the built-in macOS speech synthesizer.
==========================================================
"""

from __future__ import annotations

import subprocess

from .provider import VoiceProvider


class MacOSVoiceProvider(VoiceProvider):
    """
    macOS speech provider.
    """

    def __init__(
        self,
        voice: str = "Samantha",
    ) -> None:

        self._voice = voice

    def speak(
        self,
        message: str,
    ) -> None:
        """
        Speak the supplied message.
        """

        subprocess.run(
            [
                "say",
                "-v",
                self._voice,
                message,
            ],
            check=False,
        )