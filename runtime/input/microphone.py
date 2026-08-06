"""
==========================================================
F.R.I.D.A.Y.

Microphone Input

Placeholder for Foundation Release 10.2
==========================================================
"""

from __future__ import annotations

from .source import InputSource


class MicrophoneInput(InputSource):
    """
    Future microphone implementation.
    """

    def read(self) -> str:

        raise NotImplementedError(
            "Microphone input has not been implemented yet."
        )