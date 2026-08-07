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
<<<<<<< HEAD
    14.1
=======
    11.0
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
==========================================================
"""

from __future__ import annotations

from runtime.cognition import CognitionEngine
<<<<<<< HEAD
from runtime.input import MicrophoneInput
from runtime.language import LanguageNormalizer
=======
from runtime.platforms.apple.speech.provider import AppleSpeechProvider
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
from runtime.profile import ProfileManager
from runtime.speech.recognizer import SpeechRecognizer
from runtime.voice import VoiceSynthesizer


class Session:
    """
<<<<<<< HEAD
    Represents one interactive user session.
=======
    Represents one interactive FRIDAY session.
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
    """

    def __init__(self) -> None:

        self._running = False

        self._cognition = CognitionEngine()

<<<<<<< HEAD
        self._profile = ProfileManager().load()

        #
        # Active input source
        #
        self._input = MicrophoneInput()
=======
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
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

        #
        # Voice output
        #
        self._voice = VoiceSynthesizer(
            self._profile
        )

        #
        # Language normalization
        #
        self._normalizer = LanguageNormalizer()

    @property
    def running(self) -> bool:
        return self._running

    def initialize(self) -> None:
<<<<<<< HEAD

=======
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
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

<<<<<<< HEAD
                print("🎤 Listening...")

                user_input = self._input.read()
=======
                print()
                print("Listening...")

                speech = self._speech.listen()

                user_input = speech.text.strip()

                if user_input:
                    print(f"You: {user_input}")
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

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

            if user_input.lower() in {
                "exit",
                "quit",
            }:
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

<<<<<<< HEAD
        try:
            self._input.shutdown()
        except Exception:
            pass
=======
        #
        # Shutdown speech subsystem if supported.
        #
        provider = getattr(self._speech, "_provider", None)

        if provider is not None and hasattr(provider, "shutdown"):
            provider.shutdown()
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

        print()
        print("Goodbye.")

        self._voice.speak(
            "Goodbye."
        )