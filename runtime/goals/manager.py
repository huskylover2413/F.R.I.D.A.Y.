"""
==========================================================
F.R.I.D.A.Y.

Goal Manager

Foundation Release 26.0
==========================================================
"""

from __future__ import annotations

from .models import Goal


class GoalManager:

    def __init__(self):

        self._goals: list[Goal] = []

    def add(
        self,
        title: str,
        description: str = "",
    ) -> Goal:

        goal = Goal(
            title=title,
            description=description,
        )

        self._goals.append(
            goal
        )

        return goal

    def all(self):

        return list(self._goals)

    def active(self):

        return [

            goal

            for goal in self._goals

            if goal.active

        ]