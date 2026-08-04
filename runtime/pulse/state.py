"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/pulse/state.py

Purpose:
    Defines the lifecycle states for the Pulse runtime.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    Alpha 0.4 - Foundation Release 2
==========================================================
"""

from __future__ import annotations

from enum import Enum, auto


class RuntimeState(Enum):
    """
    Represents the lifecycle state of the FRIDAY runtime.

    These states describe the overall health and execution
    phase of the assistant itself, independent of the
    individual services it manages.
    """

    STOPPED = auto()
    INITIALIZING = auto()
    RUNNING = auto()
    STOPPING = auto()
    FAILED = auto()