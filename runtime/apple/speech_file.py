"""
==========================================================
F.R.I.D.A.Y.

Apple Speech File Recognizer

Purpose:
    Recognizes speech from an audio file using the
    native Apple Speech framework.

Author:
    Shae Simpson & OpenAI ChatGPT

Foundation Release:
    10.3
==========================================================
"""

from __future__ import annotations

import pathlib
import threading

from Foundation import NSLocale, NSURL
from Speech import (
    SFSpeechRecognizer,
    SFSpeechURLRecognitionRequest,
)


class AppleSpeechFileRecognizer:
    """
    Recognize speech from an audio file.
    """

    def __init__(
        self,
        locale: str = "en-US",
    ) -> None:

        self._recognizer = (
            SFSpeechRecognizer.alloc().initWithLocale_(
                NSLocale.alloc().initWithLocaleIdentifier_(
                    locale
                )
            )
        )

    @property
    def available(self) -> bool:
        return bool(
            self._recognizer.isAvailable()
        )

    def recognize(
        self,
        filename: str,
    ) -> str:
        """
        Recognize speech contained in an audio file.
        """

        path = pathlib.Path(filename)

        if not path.exists():

            raise FileNotFoundError(filename)

        finished = threading.Event()

        transcript = ""
        error = None

        request = (
            SFSpeechURLRecognitionRequest.alloc().initWithURL_(
                NSURL.fileURLWithPath_(
                    str(path.resolve())
                )
            )
        )

        def handler(result, err):

            nonlocal transcript
            nonlocal error

            if err is not None:

                error = err

                finished.set()

                return

            if result is not None:

                transcript = (
                    result.bestTranscription().formattedString()
                )

                if bool(result.isFinal()):

                    finished.set()

        self._recognizer.recognitionTaskWithRequest_resultHandler_(
            request,
            handler,
        )

        finished.wait()

        if error is not None:

            raise RuntimeError(str(error))

        return transcript