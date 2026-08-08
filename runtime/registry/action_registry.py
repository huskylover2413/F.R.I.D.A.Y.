"""
==========================================================
F.R.I.D.A.Y.

Action Registry

Foundation Release 33.0
==========================================================
"""

from __future__ import annotations

from collections.abc import Callable

from runtime.brain.action import Action
from runtime.brain.services import BrainService


class ActionRegistry:
    """
    Maps Brain services to handler functions.
    """

    def __init__(self) -> None:

        self._handlers: dict[
            BrainService,
            Callable[[Action], object],
        ] = {}

    def register(
        self,
        service: BrainService,
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
                f"No handler registered for {action.service.name}"
            )

        return handler(action)