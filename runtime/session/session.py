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
    7
==========================================================
"""

from __future__ import annotations

from runtime.cognition import CognitionEngine


class Session:
    """
    Represents one interactive user session.

    A Session owns the conversation between the
    user and FRIDAY.

    It does NOT manage runtime services.
    It does NOT manage application startup.

    Its only responsibility is interaction.
    """

    def __init__(self) -> None:
        self._running = False
        self._cognition = CognitionEngine()

    @property
    def running(self) -> bool:
        return self._running

    def initialize(self) -> None:
        """
        Prepare the session.
        """
        self._running = True

    def run(self) -> None:
        """
        Run the interactive session.
        """

        print()
        print("====================================================")
        print("FRIDAY Interactive Session")
        print("Type 'exit' to quit.")
        print("====================================================")
        print()

        while self._running:

            try:

                user_input = input("> ").strip()

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

            response = self._cognition.process(user_input)

            print()
            print(response.message)
            print()

        self.shutdown()

    def shutdown(self) -> None:
        """
        Shutdown the session.
        """

        self._running = False

        print()
        print("Goodbye.")