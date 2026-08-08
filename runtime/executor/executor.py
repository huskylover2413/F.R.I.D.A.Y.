"""
==========================================================
F.R.I.D.A.Y.

Action Executor

Foundation Release 32.0
==========================================================
"""

from __future__ import annotations

from runtime.brain.action import Action
from runtime.registry.action_registry import ActionRegistry


class ActionExecutor:
    """
    Executes Actions using the Action Registry.
    """

    def __init__(
        self,
        registry: ActionRegistry,
    ) -> None:

        self._registry = registry

    def execute(
        self,
        action: Action,
    ) -> None:

        try:

            result = self._registry.execute(
                action
            )

            action.complete(
                result
            )

        except Exception as exc:

            action.fail(
                str(exc)
            )