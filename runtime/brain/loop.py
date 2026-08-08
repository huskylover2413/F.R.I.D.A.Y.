"""
==========================================================
F.R.I.D.A.Y.

Brain Loop

Foundation Release 26.1
==========================================================
"""

from __future__ import annotations

from .context import BrainContext
from .pipeline import ExecuteStage
from .pipeline import GoalStage
from .pipeline import PlanStage
from .pipeline import ReasonStage
from .pipeline import RecallStage


class BrainLoop:
    """
    Coordinates FRIDAY's thinking pipeline.
    """

    def __init__(self) -> None:

        self._recall = RecallStage()
        self._goals = GoalStage()
        self._plan = PlanStage()
        self._reason = ReasonStage()
        self._execute = ExecuteStage()

    def run(
        self,
        context: BrainContext,
    ) -> BrainContext:

        self._recall.run(context)

        self._goals.run(context)

        self._plan.run(context)

        self._reason.run(context)

        self._execute.run(context)

        context.blackboard.reasoning.append(
            "LEARN pending"
        )

        return context