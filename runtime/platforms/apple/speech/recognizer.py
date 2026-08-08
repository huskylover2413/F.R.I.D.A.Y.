"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/recognizer.py

Purpose:
    Apple Speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    16.1
==========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

import AppKit
import AVFoundation
import Speech


class AppleRecognizer:
    """
    Apple Speech recognizer.

    Keeps the audio engine alive between
    recognition requests for fast response.
    """

    def __init__(self) -> None:

        self._engine = AVFoundation.AVAudioEngine.alloc().init()

        self._input_node = self._engine.inputNode()

        self._recognizer = (
            Speech.SFSpeechRecognizer.alloc().init()
        )

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
            Speech.SFSpeechAudioBufferRecognitionRequest
            .alloc()
            .init()
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
                return

            if result is None:
                return

            spoken = (
                result.bestTranscription()
                .formattedString()
                .strip()
            )

            last_update = datetime.now()

        task = (
            self._recognizer
            .recognitionTaskWithRequest_resultHandler_(
                request,
                callback,
            )
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