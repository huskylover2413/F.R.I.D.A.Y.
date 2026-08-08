"""
==========================================================
F.R.I.D.A.Y.
Vision Provider

Foundation Release 22.2
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class VisionProvider(ABC):

    @abstractmethod
    def describe(
        self,
        image: Path,
        prompt: str,
    ) -> str:
        ...