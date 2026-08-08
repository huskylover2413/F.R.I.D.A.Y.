"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/session/session.py

Purpose:
    Owns one interactive FRIDAY session.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.1
==========================================================
"""

from __future__ import annotations

from runtime.cognition import CognitionEngine
from runtime.input import MicrophoneInput
from runtime.language import LanguageNormalizer
from runtime.profile import ProfileManager
from runtime.voice import VoiceSynthesizer


class Session:
    """
    Represents one interactive FRIDAY session.
    """

    def __init__(self) -> None:

        self._running = False

        self._cognition = CognitionEngine()

        self._profile = ProfileManager().load()

        self._input = MicrophoneInput()

        self._voice = VoiceSynthesizer(
            self._profile
        )

        self._normalizer = LanguageNormalizer()

    @property
    def running(self) -> bool:
        return self._running

    def initialize(self) -> None:

        self._running = True

    def run(self) -> None:

        print()
        print("====================================================")
        print("FRIDAY Voice Session")
        print("Say 'exit' to quit.")
        print("====================================================")
        print()

        welcome = (
            f"{self._profile.greeting}, "
            f"{self._profile.display_name}."
        )

        print(welcome)
        print()

        self._voice.speak(welcome)

        while self._running:

            try:

                print("🎤 Listening...")

                user_input = self._input.read()

            except (EOFError, KeyboardInterrupt):

                print()
                break

            if not user_input:
                continue

            user_input = self._normalizer.normalize(
                user_input
            )

            print()
            print(f"✓ Heard: {user_input}")
            print("🧠 Thinking...")
            print()

            if user_input.lower() in (
                "exit",
                "quit",
            ):
                break

            response = self._cognition.process(
                user_input
            )

            print(f"🤖 {response.message}")
            print()

            self._voice.speak(
                response.message
            )

        self.shutdown()

    def shutdown(self) -> None:

        self._running = False

        try:
            self._input.shutdown()
        except Exception:
            pass

        print()
        print("Goodbye.")

        self._voice.speak(
            "Goodbye."
        )