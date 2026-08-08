"""
==========================================================
F.R.I.D.A.Y.

Session Models

Foundation Release 27.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SessionState:
    """
    Current conversational state.
    """

    current_topic: str = ""

    current_project: str = ""

    current_task: str = ""

    last_request: str = ""

    last_response: str = ""

    conversation_turns: int = 0

    metadata: dict = field(
        default_factory=dict
    )