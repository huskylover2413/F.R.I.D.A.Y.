"""
==========================================================
F.R.I.D.A.Y.

Input Source

Defines the interface for all FRIDAY input sources.
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class InputSource(ABC):
    """
    Base class for every FRIDAY input source.
    """

    @abstractmethod
    def read(self) -> str:
        """
        Read one user request.
        """
        raise NotImplementedError