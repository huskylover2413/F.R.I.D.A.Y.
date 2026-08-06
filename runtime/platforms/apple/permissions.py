"""
==========================================================
F.R.I.D.A.Y.

Apple Permissions

Author:
    Shae Simpson & OpenAI ChatGPT
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