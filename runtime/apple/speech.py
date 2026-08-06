"""
==========================================================
F.R.I.D.A.Y.

Apple Speech Utilities

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    10.2
==========================================================
"""

from __future__ import annotations

from Speech import SFSpeechRecognizer

from .permissions import ApplePermissions


class AppleSpeech:
    """
    Basic Apple Speech wrapper.
    """

    def __init__(self) -> None:

        if not ApplePermissions.request_speech_authorization():

            raise PermissionError(
                "Speech recognition permission denied."
            )

        recognizer = SFSpeechRecognizer.alloc().init()

        if recognizer is None:

            raise RuntimeError(
                "Unable to create SFSpeechRecognizer."
            )

        self._recognizer = recognizer

    @property
    def available(self) -> bool:

        return bool(
            self._recognizer.isAvailable()
        )

    @property
    def supports_on_device(self) -> bool:

        return bool(
            self._recognizer.supportsOnDeviceRecognition()
        )