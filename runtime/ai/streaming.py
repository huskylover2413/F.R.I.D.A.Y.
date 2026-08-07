"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/ai/streaming.py

Purpose:
    Coordinates streamed AI responses.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.0
==========================================================
"""

from __future__ import annotations

from collections.abc import Callable


class StreamingCoordinator:
    """
    Receives streamed text from an AI provider and forwards
    completed sentences to the consumer.
    """

    def __init__(
        self,
        callback: Callable[[str], None],
    ) -> None:

        self._callback = callback
        self._buffer = ""

    def push(
        self,
        chunk: str,
    ) -> None:

        self._buffer += chunk

        while True:

            index = -1

            for punctuation in (". ", "! ", "? "):

                position = self._buffer.find(
                    punctuation
                )

                if position != -1:

                    index = (
                        position
                        + len(punctuation)
                    )

                    break

            if index == -1:
                return

            sentence = (
                self._buffer[:index]
                .strip()
            )

            self._buffer = (
                self._buffer[index:]
            )

            if sentence:

                self._callback(
                    sentence
                )

    def finish(self) -> None:

        remaining = (
            self._buffer.strip()
        )

        if remaining:

            self._callback(
                remaining
            )

        self._buffer = ""