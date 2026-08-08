"""
==========================================================
F.R.I.D.A.Y.

Audio Listener

Foundation Release 50.0
==========================================================
"""

from __future__ import annotations

from .manager import AudioManager


class AudioListener:
    """
    Consumes microphone frames from AudioManager.

    This class does not own the microphone.
    """

    def __init__(
        self,
        audio: AudioManager,
    ) -> None:

        self._audio = audio

    def read(self):

        return self._audio.read()