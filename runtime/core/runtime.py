"""
==========================================================
F.R.I.D.A.Y.

Runtime

Foundation Release 29.0
==========================================================
"""

from __future__ import annotations

from runtime.services import ServiceContainer


class Runtime:

    def __init__(self) -> None:

        self.services = ServiceContainer()


runtime = Runtime()