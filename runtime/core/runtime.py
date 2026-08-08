"""
==========================================================
F.R.I.D.A.Y.

Runtime

Foundation Release 39.0
==========================================================
"""

from __future__ import annotations

from runtime.ai.manager import AIManager
from runtime.memory import MemoryManager
from runtime.goals import GoalManager
from runtime.session import SessionManager


class Runtime:
    """
    Shared runtime services.

    One instance exists for the lifetime
    of FRIDAY.
    """

    def __init__(self) -> None:

        self.memory = MemoryManager()

        self.ai = AIManager()

        self.goals = GoalManager()

        self.session = SessionManager()


runtime = Runtime()