"""
==========================================================
F.R.I.D.A.Y.

Task Executor

Foundation Release 25.1
==========================================================
"""

from __future__ import annotations

from runtime.profile import UserProfile
from runtime.skills import (
    SkillContext,
    SkillRegistry,
)

from .models import ExecutionResult


class TaskExecutor:

    def __init__(
        self,
        registry: SkillRegistry,
    ) -> None:

        self._registry = registry

    def execute(
        self,
        plan,
        profile: UserProfile,
        request: str,
    ) -> ExecutionResult:

        final_message = ""

        for task in plan.tasks:

            skill = self._registry.get(
                task.name
            )

            if skill is None:
                continue

            context = SkillContext(
                profile=profile,
                request=request,
            )

            result = skill.execute(
                context
            )

            if not result.success:

                return ExecutionResult(
                    success=False,
                    message=result.message,
                )

            final_message = result.message

        return ExecutionResult(
            success=True,
            message=final_message,
        )