"""
==========================================================
F.R.I.D.A.Y.

Status Models

Version 1.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SystemStatus:

    name: str

    healthy: bool

    message: str