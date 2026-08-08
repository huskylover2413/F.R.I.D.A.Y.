"""
==========================================================
F.R.I.D.A.Y.

Audio Stream

Foundation Release 50.0
==========================================================
"""

from __future__ import annotations

import queue

import numpy as np
import sounddevice as sd


class AudioStream:
    """
    Owns the physical microphone stream.

    Audio is placed into a shared queue so that
    multiple FRIDAY components can consume it.
    """

    def __init__(
        self,
        sample_rate: int = 16000,
        block_size: int = 1280,
    ) -> None:

        self._sample_rate = sample_rate
        self._block_size = block_size

        self._queue: queue.Queue[np.ndarray] = queue.Queue()

        self._stream: sd.InputStream | None = None

    @property
    def sample_rate(self) -> int:
        return self._sample_rate

    @property
    def block_size(self) -> int:
        return self._block_size

    def _callback(
        self,
        indata,
        frames,
        time,
        status,
    ) -> None:

        if status:
            print(f"Audio status: {status}")

        audio = np.asarray(
            indata[:, 0],
            dtype=np.int16,
        ).copy()

        self._queue.put(audio)

    def start(self) -> None:

        if self._stream is not None:
            return

        self._stream = sd.InputStream(
            samplerate=self._sample_rate,
            channels=1,
            dtype="int16",
            blocksize=self._block_size,
            callback=self._callback,
        )

        self._stream.start()

    def read(self) -> np.ndarray:

        return self._queue.get()

    def stop(self) -> None:

        if self._stream is None:
            return

        self._stream.stop()
        self._stream.close()

        self._stream = None

        while not self._queue.empty():

            try:
                self._queue.get_nowait()
            except queue.Empty:
                break