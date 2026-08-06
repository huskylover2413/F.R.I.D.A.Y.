"""
==========================================================
F.R.I.D.A.Y.

Keyboard Input
==========================================================
"""

from __future__ import annotations

from .source import InputSource


class KeyboardInput(InputSource):
    """
    Reads user input from the keyboard.
    """

    def read(self) -> str:

        return input("> ").strip()