"""
==========================================================
F.R.I.D.A.Y.

Brain Action

Foundation Release 30.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Action:
    """
    A single executable action.
    """

    service: str

    operation: str

    priority: int = 50

    arguments: dict[str, object] = field(
        default_factory=dict
    )

    completed: bool = False

    result: object | None = None

    error: str | None = None

    def complete(
        self,
        result: object | None = None,
    ) -> None:

        self.completed = True

        self.result = result

    def fail(
        self,
        message: str,
    ) -> None:

        self.error = message