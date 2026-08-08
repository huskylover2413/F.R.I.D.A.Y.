"""
==========================================================
F.R.I.D.A.Y.

Action Registry

Foundation Release 31.0
==========================================================
"""

from __future__ import annotations

from collections.abc import Callable

from runtime.brain.action import Action


class ActionRegistry:
    """
    Maps Action services to handler functions.
    """

    def __init__(self) -> None:

        self._handlers: dict[
            str,
            Callable[[Action], object],
        ] = {}

    def register(
        self,
        service: str,
        handler: Callable[[Action], object],
    ) -> None:

        self._handlers[service] = handler

    def execute(
        self,
        action: Action,
    ) -> object | None:

        handler = self._handlers.get(
            action.service
        )

        if handler is None:

            raise KeyError(
                f"No handler registered for '{action.service}'."
            )

        return handler(action)