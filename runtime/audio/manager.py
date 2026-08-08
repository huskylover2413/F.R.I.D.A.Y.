"""
==========================================================
F.R.I.D.A.Y.

Audio Manager

Foundation Release 50.0
==========================================================
"""

from __future__ import annotations

from .stream import AudioStream


class AudioManager:
    """
    High-level owner of FRIDAY's microphone.

    Only this manager should open or close
    the physical microphone stream.
    """

    def __init__(self) -> None:

        self._stream = AudioStream()

        self._running = False

    @property
    def running(self) -> bool:

        return self._running

    @property
    def sample_rate(self) -> int:

        return self._stream.sample_rate

    @property
    def block_size(self) -> int:

        return self._stream.block_size

    def start(self) -> None:

        if self._running:
            return

        self._stream.start()

        self._running = True

    def read(self):

        if not self._running:

            raise RuntimeError(
                "AudioManager is not running."
            )

        return self._stream.read()

    def stop(self) -> None:

        if not self._running:
            return

        self._stream.stop()

        self._running = False