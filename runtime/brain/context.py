"""
==========================================================
F.R.I.D.A.Y.

Brain Context

Foundation Release 46.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .blackboard import Blackboard


@dataclass(slots=True)
class BrainContext:
    """
    Context passed through the Brain Loop.

    Contains the current request plus the immediate
    conversational history needed for follow-up requests.
    """

    request: str

    last_request: str = ""

    last_response: str = ""

    conversation_turns: int = 0

    current_topic: str = ""

    current_project: str = ""

    current_task: str = ""

    metadata: dict = field(
        default_factory=dict
    )

    blackboard: Blackboard = field(
        default_factory=Blackboard
    )

    remember_after_response: bool = False