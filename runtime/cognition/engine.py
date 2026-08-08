"""
==========================================================
F.R.I.D.A.Y.

Cognition Engine

Foundation Release 43.0

Purpose:
Compatibility wrapper around the new Brain Engine.
==========================================================
"""

from __future__ import annotations

from runtime.brain import BrainEngine

from .models import Response


class CognitionEngine:
    """
    Legacy compatibility layer.

    Existing code throughout FRIDAY still calls
    CognitionEngine.process().

    Internally, all requests are now handled by
    the Brain.
    """

    def __init__(self) -> None:

        self._brain = BrainEngine()

    def process(
        self,
        text: str,
    ) -> Response:

        ai = self._brain.ask(
            text
        )

        return Response(

            message=ai.message,

            success=ai.success,

        )