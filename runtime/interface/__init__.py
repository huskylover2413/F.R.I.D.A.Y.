"""
==========================================================
F.R.I.D.A.Y.

Interface Package

Provides user interfaces for FRIDAY.
==========================================================
"""

from .service import InterfaceService
from .terminal import TerminalInterface

__all__ = [
    "InterfaceService",
    "TerminalInterface",
]