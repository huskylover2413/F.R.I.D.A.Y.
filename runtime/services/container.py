"""
==========================================================
F.R.I.D.A.Y.

Runtime Service Container

Foundation Release 28.0
==========================================================
"""

from __future__ import annotations

from runtime.ai import AIManager
from runtime.goals import GoalManager
from runtime.memory import MemoryManager
from runtime.planner import Planner
from runtime.session import SessionManager
from runtime.vision.service import VisionService


class ServiceContainer:
    """
    Owns the application's shared runtime services.
    """

    def __init__(self) -> None:

        self.memory = MemoryManager()

        self.goals = GoalManager()

        self.session = SessionManager()

        self.vision = VisionService()

        self.ai = AIManager()

        self.planner = Planner()