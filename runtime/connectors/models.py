"""
==========================================================
F.R.I.D.A.Y.

Connector Models

Foundation Release 20.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ConnectorResult:

    success: bool

    message: str

    data: dict | None = None