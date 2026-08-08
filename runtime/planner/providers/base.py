"""
==========================================================
F.R.I.D.A.Y.

Planner Provider

Foundation Release 24.0
==========================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class PlannerProvider(ABC):

    @abstractmethod
    def plan(
        self,
        request: str,
    ) -> list[str]:
        ...