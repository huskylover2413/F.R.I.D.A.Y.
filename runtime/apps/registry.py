"""
==========================================================
F.R.I.D.A.Y.

Application Registry

Foundation Release 3.0
==========================================================
"""

from __future__ import annotations

from .app import Application


class ApplicationRegistry:

    def __init__(self):

        self._apps = []

    def register(
        self,
        app: Application,
    ) -> None:

        self._apps.append(app)

    def find(
        self,
        request: str,
    ) -> Application | None:

        for app in self._apps:

            if app.handles(request):

                return app

        return None