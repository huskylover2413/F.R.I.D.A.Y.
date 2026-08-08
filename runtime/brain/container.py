"""
==========================================================
F.R.I.D.A.Y.

Brain Service Container

Foundation Release 22.1
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from runtime.memory import MemorySearch
from runtime.vision.service import VisionService


@dataclass(slots=True)
class BrainServices:
    """
    Runtime services available to the Brain.
    """

    memory: MemorySearch

    vision: VisionService

    @classmethod
    def create(cls):

        return cls(
            memory=MemorySearch(),
            vision=VisionService(),
        )