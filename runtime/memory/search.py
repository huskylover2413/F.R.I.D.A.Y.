"""
==========================================================
F.R.I.D.A.Y.

Memory Search

Foundation Release 21.2
==========================================================
"""

from __future__ import annotations

from runtime.memory import MemoryManager


class MemorySearch:
    """
    Finds memories relevant to a request.

    This is currently keyword-based.

    Later it will become semantic AI search.
    """

    def __init__(self):

        self._memory = MemoryManager()

    def search(
        self,
        request: str,
    ) -> list:

        request = request.lower()

        results = []

        for memory in self._memory.all():

            text = (
                f"{memory.key} "
                f"{memory.value}"
            ).lower()

            if any(

                word in text

                for word in request.split()

            ):

                results.append(
                    memory
                )

        return results