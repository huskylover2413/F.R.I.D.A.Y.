"""
==========================================================
F.R.I.D.A.Y.

Execute Stage

Foundation Release 32.0
==========================================================
"""

from __future__ import annotations

from runtime.executor import ActionExecutor
from runtime.registry.action_registry import ActionRegistry

from ..action import Action
from ..context import BrainContext


class ExecuteStage:
    """
    Dispatches Actions to the runtime executor.
    """

    def __init__(self) -> None:

        registry = ActionRegistry()

        #
        # Temporary handlers
        #

        registry.register(
            "memory",
            lambda action: "memory complete",
        )

        registry.register(
            "ai",
            lambda action: "ai complete",
        )

        registry.register(
            "vision",
            lambda action: "vision complete",
        )

        self._executor = ActionExecutor(
            registry
        )

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        for action in board.actions:

            self._executor.execute(
                action
            )

            board.reasoning.append(

                f"{action.service} executed."

            )