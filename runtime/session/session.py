"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/session/session.py

Purpose:
    Owns an interactive user session with FRIDAY.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    7
==========================================================
"""

from __future__ import annotations


class Session:
    """
    Represents one interactive FRIDAY session.

    The Session owns user interaction.

    It does NOT manage services.

    It does NOT manage runtime lifecycle.

    It simply hosts a conversation between
    the user and FRIDAY.
    """

    def __init__(self) -> None:
        self.running = False

    def initialize(self) -> None:
        """Prepare the session."""
        self.running = True

    def run(self) -> None:
        """
        Execute the session.

        (Interactive terminal arrives in the next step.)
        """
        print()
        print("FRIDAY Session initialized.")
        print("Interactive console coming next...")
        print()

    def shutdown(self) -> None:
        """Shutdown the session."""
        self.running = False