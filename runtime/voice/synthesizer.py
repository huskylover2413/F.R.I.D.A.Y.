"""
==========================================================
F.R.I.D.A.Y.

Voice Synthesizer

Coordinates speech synthesis.
==========================================================
"""

from __future__ import annotations

from runtime.profile import UserProfile

from .macos_provider import MacOSVoiceProvider


class VoiceSynthesizer:
    """
    High-level speech synthesizer.
    """

    def __init__(
        self,
        profile: UserProfile,
    ) -> None:

        self._provider = MacOSVoiceProvider(
            voice=profile.voice,
        )

    def speak(
        self,
        message: str,
    ) -> None:
        """
        Speak a message.
        """

        self._provider.speak(message)