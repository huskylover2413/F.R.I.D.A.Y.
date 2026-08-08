"""
==========================================================
F.R.I.D.A.Y.

Planner

Version 2.0
==========================================================
"""

from __future__ import annotations

from .models import Plan
from .providers.ai import AIPlannerProvider


class Planner:
    """
    AI-powered planner.
    """

    def __init__(self) -> None:

        self._provider = AIPlannerProvider()

    def plan(
        self,
        request: str,
    ) -> Plan:

        plan = Plan()

        tasks = self._provider.plan(
            request
        )

        for task in tasks:

            plan.add(
                task
            )

        return plan