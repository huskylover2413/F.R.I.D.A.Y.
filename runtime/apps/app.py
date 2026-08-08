"""
==========================================================
F.R.I.D.A.Y.

Application Base Class

Foundation Release 3.0
==========================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class Application(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def handles(
        self,
        request: str,
    ) -> bool:
        ...

    @abstractmethod
    def execute(
        self,
        request: str,
    ) -> str:
        ...