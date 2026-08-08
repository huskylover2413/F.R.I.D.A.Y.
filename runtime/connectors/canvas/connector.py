"""
==========================================================
F.R.I.D.A.Y.

Canvas Connector

Foundation Release 20.0
==========================================================
"""

from __future__ import annotations

from runtime.connectors import Connector


class CanvasConnector(Connector):

    @property
    def name(self) -> str:

        return "Canvas"

    def available(self) -> bool:

        #
        # We'll detect login later.
        #
        return False

    def can_handle(
        self,
        request: str,
    ) -> bool:

        request = request.lower()

        return any(

            word in request

            for word in (

                "canvas",

                "assignment",

                "homework",

                "class",

                "due",

            )

        )

    def execute(
        self,
        request: str,
    ) -> str:

        return (
            "Canvas has not been "
            "configured yet."
        )