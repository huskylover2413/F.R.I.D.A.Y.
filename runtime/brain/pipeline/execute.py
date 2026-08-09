"""
==========================================================
F.R.I.D.A.Y.

Execute Stage

Foundation Release 44.2
==========================================================
"""

from __future__ import annotations

from runtime.ai.manager import AIManager
from runtime.memory import MemoryManager
from runtime.profile import ProfileManager
from runtime.registry.action_registry import ActionRegistry
from runtime.skills.context import SkillContext
from runtime.skills.system import (
    DateSkill,
    GreetingSkill,
    HelpSkill,
    IdentitySkill,
    MathSkill,
    TimeSkill,
)

from runtime.executor import ActionExecutor

from ..context import BrainContext
from ..services import BrainService


class ExecuteStage:
    """
    Executes Brain Actions.

    This stage owns the handlers needed by the
    Brain pipeline and does not import the global
    Runtime object, preventing circular imports.
    """

    def __init__(self) -> None:

        #
        # Runtime services
        #

        self._memory = MemoryManager()

        self._ai = AIManager()

        self._profile = ProfileManager().load()

        #
        # System skills
        #

        self._skills = {
            "time": TimeSkill(),
            "date": DateSkill(),
            "greeting": GreetingSkill(),
            "help": HelpSkill(),
            "identity": IdentitySkill(),
            "math": MathSkill(),
        }

        #
        # Action registry
        #

        registry = ActionRegistry()

        registry.register(
            BrainService.MEMORY,
            self._memory_handler,
        )

        registry.register(
            BrainService.AI,
            self._ai_handler,
        )

        registry.register(
            BrainService.SKILLS,
            self._skill_handler,
        )

        registry.register(
            BrainService.VISION,
            self._vision_handler,
        )

        self._executor = ActionExecutor(
            registry
        )

    #
    # --------------------------------------------------
    # Memory
    # --------------------------------------------------
    #

    def _memory_handler(
        self,
        action,
    ):

        if action.operation == "search":

            query = action.arguments.get(
                "query",
                "",
            )

            return self._memory.search(
                query
            )

        if action.operation == "remember":

            self._memory.remember(
                action.arguments["category"],
                "conversation",
                action.arguments["text"],
            )

            return "stored"

        return None

    #
    # --------------------------------------------------
    # AI
    # --------------------------------------------------
    #

    def _ai_handler(
        self,
        action,
    ):

        prompt = action.arguments.get(
            "prompt",
            "",
        )

        return self._ai.generate(
            prompt
        )

    #
    # --------------------------------------------------
    # Skills
    # --------------------------------------------------
    #

    def _skill_handler(
        self,
        action,
    ):

        skill_name = action.operation.lower()

        skill = self._skills.get(
            skill_name
        )

        if skill is None:

            raise KeyError(
                f"Unknown FRIDAY skill: "
                f"{action.operation}"
            )

        context = SkillContext(
            profile=self._profile,
            request=action.arguments.get(
                "request",
                "",
            ),
        )

        return skill.execute(
            context
        )

    #
    # --------------------------------------------------
    # Vision
    # --------------------------------------------------
    #

    def _vision_handler(
        self,
        action,
    ):

        return "Vision pending"

    #
    # --------------------------------------------------
    # Execute
    # --------------------------------------------------
    #

    def run(
        self,
        context: BrainContext,
        learning_only: bool = False,
    ) -> None:

        board = context.blackboard

        for action in board.actions:

            if action.completed:
                continue

            #
            # Learning actions are executed only
            # during the learning pass.
            #

            if (
                not learning_only
                and action.operation == "remember"
            ):

                continue

            if (
                learning_only
                and action.operation != "remember"
            ):

                continue

            #
            # Populate action arguments.
            #

            if action.service == BrainService.MEMORY:

                if action.operation == "search":

                    action.arguments["query"] = (
                        context.request
                    )

            elif action.service == BrainService.AI:

                action.arguments["prompt"] = (
                    context.request
                )

            elif action.service == BrainService.SKILLS:

                action.arguments["request"] = (
                    context.request
                )

            #
            # Execute
            #

            self._executor.execute(
                action
            )

            board.reasoning.append(
                f"{action.service.name}:"
                f"{action.operation} executed."
            )