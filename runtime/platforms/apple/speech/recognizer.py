"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/recognizer.py

Purpose:
    Continuous Apple Speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    1.0.0
==========================================================
"""

from __future__ import annotations

import queue
from datetime import datetime, timedelta

import AppKit
import Speech

from .microphone import AppleMicrophone


class AppleRecognizer:
    """
    Continuous Apple Speech recognizer.

    This object owns:

        • SFSpeechRecognizer
        • RecognitionRequest
        • RecognitionTask

    It does NOT own the microphone.

    Completed phrases are placed into an internal queue.
    """

    def __init__(
        self,
        microphone: AppleMicrophone,
    ) -> None:

        self._microphone = microphone

        self._recognizer = Speech.SFSpeechRecognizer.alloc().init()

        self._request = None
        self._task = None

        self._queue: queue.Queue[str] = queue.Queue()

        self._current_text = ""

        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    def start(self) -> None:
        """
        Starts continuous recognition.

        Safe to call multiple times.
        """

        if self._running:
            return

        Speech.SFSpeechRecognizer.requestAuthorization_(None)

        self._request = (
            Speech.SFSpeechAudioBufferRecognitionRequest.alloc().init()
        )

        self._request.setShouldReportPartialResults_(True)

        self._microphone.attach(self._request)

        def callback(result, error):

            if error is not None:
                print(error)
                return

            if result is None:
                return

            text = (
                result.bestTranscription()
                .formattedString()
                .strip()
            )

            self._current_text = text

            #
            # Queue completed utterances.
            #
            if result.isFinal():

                if text:

                    self._queue.put(text)

                #
                # Prepare next recognition request.
                #
                self.restart()

        self._task = (
            self._recognizer
            .recognitionTaskWithRequest_resultHandler_(
                self._request,
                callback,
            )
        )

        self._running = True

    def restart(self) -> None:
        """
        Starts the next recognition request
        without restarting the microphone.
        """

        if self._task is not None:
            self._task.cancel()

        if self._request is not None:
            self._request.endAudio()

        self._microphone.detach()

        self._running = False

        self.start()

    def next_phrase(
        self,
        timeout: float | None = None,
    ) -> str:
        """
        Wait for the next completed phrase.
        """

        if not self._running:
            self.start()

        end = None

        if timeout is not None:
            end = datetime.now() + timedelta(seconds=timeout)

        while True:

            try:

                return self._queue.get_nowait()

            except queue.Empty:

                if (
                    end is not None
                    and datetime.now() >= end
                ):
                    return ""

                AppKit.NSRunLoop.currentRunLoop().runUntilDate_(
                    datetime.now()
                    + timedelta(milliseconds=100)
                )

    def shutdown(self) -> None:
        """
        Shutdown recognition.
        """

        if self._task is not None:
            self._task.cancel()

        if self._request is not None:
            self._request.endAudio()

        self._microphone.shutdown()

        self._running = False