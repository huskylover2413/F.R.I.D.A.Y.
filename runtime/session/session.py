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
    11.0
==========================================================
"""

from __future__ import annotations

from runtime.cognition import CognitionEngine
from runtime.platforms.apple.speech.provider import AppleSpeechProvider
from runtime.profile import ProfileManager
from runtime.speech.recognizer import SpeechRecognizer
from runtime.voice import VoiceSynthesizer


class Session:
    """
    Represents one interactive FRIDAY session.
    """

    def __init__(self) -> None:

        self._running = False

        #
        # Core systems
        #
        self._cognition = CognitionEngine()

        #
        # User profile
        #
        self._profile = ProfileManager().load()

        #
        # Speech recognition
        #
        self._speech = SpeechRecognizer(
            AppleSpeechProvider()
        )

        #
        # Voice output
        #
        self._voice = VoiceSynthesizer(
            self._profile
        )

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

                print()
                print("Listening...")

                speech = self._speech.listen()

                user_input = speech.text.strip()

                if user_input:
                    print(f"You: {user_input}")

            except (EOFError, KeyboardInterrupt):

                print()
                break

            if not user_input:
                continue

            if user_input.lower() in {
                "exit",
                "quit",
            }:
                break

            response = self._cognition.process(
                user_input
            )

            print()
            print(response.message)
            print()

            self._voice.speak(
                response.message
            )

        self.shutdown()

    def shutdown(self) -> None:
        """
        Shutdown the session.
        """

        self._running = False

        #
        # Shutdown speech subsystem if supported.
        #
        provider = getattr(self._speech, "_provider", None)

        if provider is not None and hasattr(provider, "shutdown"):
            provider.shutdown()

        print()
        print("Goodbye.")

        self._voice.speak(
            "Goodbye."
        )