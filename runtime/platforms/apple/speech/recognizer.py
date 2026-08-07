"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/recognizer.py

Purpose:
<<<<<<< HEAD
    Apple speech recognizer.
=======
    Continuous Apple Speech recognizer.
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
<<<<<<< HEAD
    11.2
=======
    1.0.0
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
==========================================================
"""

from __future__ import annotations

<<<<<<< HEAD
from datetime import datetime, timedelta

import AppKit
import AVFoundation
import Speech


class AppleRecognizer:
    """
    Apple Speech recognizer.

    Keeps AVAudioEngine alive between recognition
    requests and returns after a short period of
    silence instead of waiting for Apple's final
    result.
    """

    def __init__(self) -> None:

        self._engine = AVFoundation.AVAudioEngine.alloc().init()

        self._input_node = self._engine.inputNode()

        self._recognizer = Speech.SFSpeechRecognizer.alloc().init()

        self._started = False

    def _ensure_engine(self) -> None:

        if self._started:
            return

        session = AVFoundation.AVAudioSession.sharedInstance()

        session.setCategory_mode_options_error_(
            AVFoundation.AVAudioSessionCategoryRecord,
            AVFoundation.AVAudioSessionModeMeasurement,
            AVFoundation.AVAudioSessionCategoryOptionDuckOthers,
            None,
        )

        session.setActive_withOptions_error_(
            True,
            AVFoundation.AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation,
            None,
        )

        self._engine.prepare()

        self._engine.startAndReturnError_(None)

        self._started = True

    def recognize(
        self,
        timeout: float = 10.0,
    ) -> str:

        self._ensure_engine()

        spoken = ""

        last_update = datetime.now()

        request = (
            Speech.SFSpeechAudioBufferRecognitionRequest.alloc().init()
        )

        request.setShouldReportPartialResults_(True)

        recording_format = (
            self._input_node.outputFormatForBus_(0)
        )

        self._input_node.installTapOnBus_bufferSize_format_block_(
            0,
            1024,
            recording_format,
            lambda buffer, when:
                request.appendAudioPCMBuffer_(buffer),
        )

        def callback(result, error):

            nonlocal spoken
            nonlocal last_update

            if error is not None:
=======
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
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
                return

            if result is None:
                return

<<<<<<< HEAD
            spoken = (
=======
            text = (
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
                result.bestTranscription()
                .formattedString()
                .strip()
            )

<<<<<<< HEAD
            last_update = datetime.now()

        task = self._recognizer.recognitionTaskWithRequest_resultHandler_(
            request,
            callback,
        )

        deadline = (
            datetime.now()
            + timedelta(seconds=timeout)
        )

        silence = timedelta(milliseconds=700)

        while datetime.now() < deadline:

            AppKit.NSRunLoop.currentRunLoop().runUntilDate_(
                datetime.now()
                + timedelta(milliseconds=100)
            )

            #
            # Return after 700 ms of no speech updates.
            #
            if (
                spoken
                and datetime.now() - last_update > silence
            ):
                break

        request.endAudio()

        task.cancel()

        self._input_node.removeTapOnBus_(0)

        return spoken

    def shutdown(self) -> None:

        if not self._started:
            return

        self._engine.stop()

        self._started = False
=======
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
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1
