"""
==========================================================
F.R.I.D.A.Y.

Execute Stage

Foundation Release 39.0
==========================================================
"""

from __future__ import annotations

from runtime.core.runtime import runtime
from runtime.executor import ActionExecutor
from runtime.registry.action_registry import ActionRegistry

from ..context import BrainContext
from ..services import BrainService


class ExecuteStage:
    """
    Executes Brain Actions using shared runtime services.
    """

    def __init__(self) -> None:

        #
        # Shared Runtime
        #

        self._runtime = runtime

        #
        # Registry
        #

        registry = ActionRegistry()

        registry.register(
            BrainService.MEMORY,
            self._memory_handler,
        )

        registry.register(
            BrainService.AI,
            self._ai_handler,
        )

        registry.register(
            BrainService.VISION,
            lambda action: "Vision pending",
        )

        self._executor = ActionExecutor(
            registry
        )

    #
    # --------------------------------------------------
    # Memory
    # --------------------------------------------------
    #

    def _memory_handler(
        self,
        action,
    ):

        if action.operation == "search":

            query = action.arguments.get(
                "query",
                "",
            )

            return self._runtime.memory.search(
                query
            )

        if action.operation == "remember":

            self._runtime.memory.remember(

                action.arguments["category"],

                "conversation",

                action.arguments["text"],

            )

            return "stored"

        return None

    #
    # --------------------------------------------------
    # AI
    # --------------------------------------------------
    #

    def _ai_handler(
        self,
        action,
    ):

        prompt = action.arguments.get(
            "prompt",
            "",
        )

        return self._runtime.ai.generate(
            prompt
        )

    #
    # --------------------------------------------------
    # Execute
    # --------------------------------------------------
    #

    def run(
        self,
        context: BrainContext,
        learning_only: bool = False,
    ) -> None:

        board = context.blackboard

        for action in board.actions:

            #
            # Skip work already completed.
            #

            if action.completed:

                continue

            #
            # Skip learning actions during
            # the first execution pass.
            #

            if (

                not learning_only

                and action.operation == "remember"

            ):

                continue

            #
            # Only execute learning actions
            # during the second pass.
            #

            if (

                learning_only

                and action.operation != "remember"

            ):

                continue

            #
            # Populate runtime arguments.
            #

            if action.service == BrainService.MEMORY:

                if action.operation == "search":

                    action.arguments["query"] = (
                        context.request
                    )

            elif action.service == BrainService.AI:

                action.arguments["prompt"] = (
                    context.request
                )

            #
            # Execute
            #

            self._executor.execute(
                action
            )

            board.reasoning.append(

                f"{action.service.name}:{action.operation} executed."

            )