"""
==========================================================
F.R.I.D.A.Y.

Planner Models

Foundation Release 24.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Task:
    """
    One executable task.
    """

    name: str

    confidence: float = 1.0


@dataclass(slots=True)
class Plan:
    """
    A complete execution plan.
    """

    tasks: list[Task] = field(default_factory=list)

    def add(
        self,
        name: str,
        confidence: float = 1.0,
    ) -> None:

        self.tasks.append(
            Task(
                name=name,
                confidence=confidence,
            )
        )

    @property
    def empty(self) -> bool:

        return len(self.tasks) == 0