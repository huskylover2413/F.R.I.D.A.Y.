"""
==========================================================
F.R.I.D.A.Y.

Apple Permission Utilities

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    10.2
==========================================================
"""

from __future__ import annotations

import threading

from Speech import (
    SFSpeechRecognizer,
    SFSpeechRecognizerAuthorizationStatusAuthorized,
)


class ApplePermissions:
    """
    Handles Apple permission requests.
    """

    @staticmethod
    def request_speech_authorization() -> bool:
        """
        Request speech recognition permission.
        """

        event = threading.Event()

        authorized = False

        def handler(status):

            nonlocal authorized

            authorized = (
                status ==
                SFSpeechRecognizerAuthorizationStatusAuthorized
            )

            event.set()

        SFSpeechRecognizer.requestAuthorization_(handler)

        event.wait()

        return authorized