"""
==========================================================
F.R.I.D.A.Y.

Execution Models

Foundation Release 25.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ExecutionResult:

    success: bool

    message: str