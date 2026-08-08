"""
==========================================================
F.R.I.D.A.Y.

Connector Base

Foundation Release 20.1
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import ConnectorResult


class Connector(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def available(self) -> bool:
        ...

    @abstractmethod
    def execute(
        self,
        request: str,
    ) -> ConnectorResult:
        ...