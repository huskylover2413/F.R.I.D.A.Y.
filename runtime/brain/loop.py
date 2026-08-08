"""
==========================================================
F.R.I.D.A.Y.

Brain Loop

Foundation Release 38.0
==========================================================
"""

from __future__ import annotations

from .context import BrainContext
from .pipeline import DecisionStage
from .pipeline import ExecuteStage
from .pipeline import GoalStage
from .pipeline import LearnStage
from .pipeline import PlanStage
from .pipeline import ReasonStage
from .pipeline import RecallStage


class BrainLoop:
    """
    Coordinates FRIDAY's cognitive pipeline.
    """

    def __init__(self) -> None:

        self._recall = RecallStage()

        self._goals = GoalStage()

        self._decision = DecisionStage()

        self._plan = PlanStage()

        self._reason = ReasonStage()

        self._execute = ExecuteStage()

        self._learn = LearnStage()

    def run(
        self,
        context: BrainContext,
    ) -> BrainContext:

        #
        # Initial reasoning pipeline
        #

        self._recall.run(context)

        self._goals.run(context)

        self._decision.run(context)

        self._plan.run(context)

        self._reason.run(context)

        #
        # Execute planned actions
        #

        self._execute.run(context)

        #
        # Learn from the interaction
        #

        self._learn.run(context)

        #
        # Execute any NEW actions produced
        # by learning.
        #

        self._execute.run(
            context,
            learning_only=True,
        )

        return context