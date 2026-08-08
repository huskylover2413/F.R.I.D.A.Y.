"""
==========================================================
F.R.I.D.A.Y.

Brain Pipeline

Foundation Release 19.0
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BrainPipeline:

    recall_memory: bool = True

    use_vision: bool = False

    use_planner: bool = True

    use_reasoning: bool = True

    use_skills: bool = True

    use_ai: bool = True

    learn: bool = True

    executed: list[str] = field(default_factory=list)

    def step(
        self,
        name: str,
    ) -> None:

        self.executed.append(name)