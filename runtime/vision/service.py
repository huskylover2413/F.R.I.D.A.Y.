"""
==========================================================
F.R.I.D.A.Y.
Vision Service

Foundation Release 22.3
==========================================================
"""

from __future__ import annotations

from .capture import ScreenCaptureProvider
from .providers import GemmaVisionProvider


class VisionService:
    """
    High-level vision service.
    """

    def __init__(self) -> None:

        self._capture = ScreenCaptureProvider()

        self._provider = GemmaVisionProvider()

    def describe(
        self,
        prompt: str = (
            "Describe what is visible on this screen. "
            "Summarize it clearly for the user."
        ),
    ) -> str:

        capture = self._capture.capture()

        return self._provider.describe(
            capture.path,
            prompt,
        )