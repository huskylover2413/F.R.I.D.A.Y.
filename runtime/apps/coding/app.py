"""
==========================================================
F.R.I.D.A.Y.

Coding Application

Foundation Release 3.1
==========================================================
"""

from __future__ import annotations

from runtime.apps import Application


class CodingApplication(Application):

    @property
    def name(self) -> str:

        return "Coding"

    def handles(
        self,
        request: str,
    ) -> bool:

        request = request.lower()

        return any(

            phrase in request

            for phrase in (

                "python",

                "code",

                "coding",

                "program",

                "programming",

                "bug",

                "error",

                "debug",

                "class",

                "function",

                "script",

            )

        )

    def execute(
        self,
        request: str,
    ) -> str:

        return (
            "The Coding Application is installed. "
            "AI integration is coming next."
        )