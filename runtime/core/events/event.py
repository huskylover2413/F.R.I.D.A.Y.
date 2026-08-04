"""
==========================================================
F.R.I.D.A.Y.
Fully Responsive Intelligent Digital Assistant for You

File:
    runtime/core/events/event.py

Purpose:
    Defines the base event model used throughout FRIDAY.

Author:
    Shae Simpson & OpenAI ChatGPT

Version:
    0.2.0
Release:
    Foundation Release 2
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Event:
    """
    Represents a single event flowing through FRIDAY.
    """

    name: str
    source: str
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)