"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/platforms/apple/speech/microphone.py

Purpose:
    Persistent Apple microphone.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    1.0.0
==========================================================
"""

from __future__ import annotations

import AVFoundation
import Speech


class AppleMicrophone:
    """
    Owns the application's single AVAudioEngine.

    Lifetime:

        Session Start
            ↓
        initialize()
            ↓
        running...
            ↓
        attach(request)
            ↓
        detach()
            ↓
        attach(request)
            ↓
        ...
            ↓
        shutdown()

    The engine is NEVER recreated during a session.
    """

    def __init__(self) -> None:

        self._audio_session = (
            AVFoundation.AVAudioSession.sharedInstance()
        )

        self._engine = AVFoundation.AVAudioEngine.alloc().init()

        self._input_node = self._engine.inputNode()

        self._initialized = False

        self._attached = False

    @property
    def engine(self):
        return self._engine

    @property
    def initialized(self) -> bool:
        return self._initialized

    @property
    def attached(self) -> bool:
        return self._attached

    def initialize(self) -> None:
        """
        Configure the microphone once.
        """

        if self._initialized:
            return

        #
        # Configure audio session.
        #
        self._audio_session.setCategory_mode_options_error_(
            AVFoundation.AVAudioSessionCategoryRecord,
            AVFoundation.AVAudioSessionModeMeasurement,
            AVFoundation.AVAudioSessionCategoryOptionDuckOthers,
            None,
        )

        self._audio_session.setActive_withOptions_error_(
            True,
            AVFoundation.AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation,
            None,
        )

        #
        # Start engine once.
        #
        self._engine.prepare()

        success, error = self._engine.startAndReturnError_(None)

        if not success and error is not None:
            raise RuntimeError(str(error))

        self._initialized = True

    def attach(
        self,
        request: Speech.SFSpeechAudioBufferRecognitionRequest,
    ) -> None:
        """
        Connect microphone audio to a recognition request.
        """

        if not self._initialized:
            self.initialize()

        if self._attached:
            self.detach()

        fmt = self._input_node.outputFormatForBus_(0)

        self._input_node.installTapOnBus_bufferSize_format_block_(
            0,
            1024,
            fmt,
            lambda buffer, when:
                request.appendAudioPCMBuffer_(buffer),
        )

        self._attached = True

    def detach(self) -> None:
        """
        Disconnect the current recognition request.

        Audio engine remains running.
        """

        if not self._attached:
            return

        self._input_node.removeTapOnBus_(0)

        self._attached = False

    def shutdown(self) -> None:
        """
        Completely stop microphone.
        """

        self.detach()

        if self._initialized:

            self._engine.stop()

            self._initialized = False