"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/recognizer.py

Purpose:
    Apple speech recognizer.

Author:
    Shae Simpson & OpenAI ChatGPT
==========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

import AppKit
import AVFoundation
import Speech


class AppleRecognizer:
    """
    Performs one speech recognition request.
    """

    def recognize(self, timeout: float = 10.0) -> str:

        spoken_text = ""

        #
        # Authorization
        #
        Speech.SFSpeechRecognizer.requestAuthorization_(None)

        #
        # Audio Session
        #
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

        #
        # Speech Recognizer
        #
        recognizer = Speech.SFSpeechRecognizer.alloc().init()

        request = (
            Speech.SFSpeechAudioBufferRecognitionRequest.alloc().init()
        )

        request.setShouldReportPartialResults_(True)

        #
        # Audio Engine
        #
        engine = AVFoundation.AVAudioEngine.alloc().init()

        input_node = engine.inputNode()

        recording_format = input_node.outputFormatForBus_(0)

        input_node.installTapOnBus_bufferSize_format_block_(
            0,
            1024,
            recording_format,
            lambda buffer, when:
                request.appendAudioPCMBuffer_(buffer),
        )

        engine.prepare()
        engine.startAndReturnError_(None)

        finished = False

        def callback(result, error):

            nonlocal spoken_text
            nonlocal finished

            if error is not None:
                finished = True
                return

            if result is None:
                return

            spoken_text = (
                result.bestTranscription()
                .formattedString()
            )

            if result.isFinal():
                finished = True

        task = recognizer.recognitionTaskWithRequest_resultHandler_(
            request,
            callback,
        )

        end = datetime.now() + timedelta(seconds=timeout)

        while not finished and datetime.now() < end:

            AppKit.NSRunLoop.currentRunLoop().runUntilDate_(
                datetime.now() + timedelta(milliseconds=100)
            )

        request.endAudio()

        task.cancel()

        input_node.removeTapOnBus_(0)

        engine.stop()

        return spoken_text.strip()