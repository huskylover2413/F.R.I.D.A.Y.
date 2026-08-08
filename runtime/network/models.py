"""
==========================================================
F.R.I.D.A.Y.
Network Models

Foundation Release 20.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class NetworkMessage:
    """
    Message exchanged between FRIDAY devices.
    """

    sender: str

    recipient: str

    request: str

    created: datetime

    conversation_id: str | None = None