"""
==========================================================
F.R.I.D.A.Y.
Voice Demonstration

Purpose:
    Demonstrates the Voice subsystem using the
    macOS speech synthesizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    9
==========================================================
"""

from __future__ import annotations

from runtime.voice import (
    MacOSVoiceProvider,
    VoiceSynthesizer,
)


def main() -> None:
    """
    Demonstrate FRIDAY's voice.
    """

    synthesizer = VoiceSynthesizer(
        MacOSVoiceProvider()
    )

    message = "Good afternoon, Shae."

    print()
    print("==========================================")
    print("FRIDAY Voice Demonstration")
    print("==========================================")
    print()
    print(f'Speaking: "{message}"')
    print()

    synthesizer.speak(message)

    print("Voice demonstration complete.")
    print()


if __name__ == "__main__":
    main()