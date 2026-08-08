"""
==========================================================
F.R.I.D.A.Y.

Recall Stage

Foundation Release 22.2
==========================================================
"""

from __future__ import annotations

from runtime.memory import MemorySearch

from ..context import BrainContext


class RecallStage:
    """
    Loads relevant memories into the Brain Blackboard.
    """

    def __init__(self) -> None:

        self._memory = MemorySearch()

    def run(
        self,
        context: BrainContext,
    ) -> None:

        context.blackboard.reasoning.append(
            "Searching relevant memories..."
        )

        memories = self._memory.search(
            context.request
        )

        for memory in memories:

            context.blackboard.memories.append(
                f"{memory.key}: {memory.value}"
            )

        context.blackboard.reasoning.append(
            f"Found {len(memories)} relevant memories."
        )