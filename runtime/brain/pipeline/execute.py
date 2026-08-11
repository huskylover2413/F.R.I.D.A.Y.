"""
==========================================================
F.R.I.D.A.Y.

Execute Stage

Foundation Release 56.3
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
from runtime.music.apple_music import AppleMusicController

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
        # Apple Music
        #

        self._music = AppleMusicController()

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
            BrainService.SYSTEM,
            self._system_handler,
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
    # System / Apple Music
    # --------------------------------------------------
    #

    def _system_handler(
        self,
        action,
    ):

        #
        # Open Music
        #

        if action.operation == "open_music":

            return self._music.open()

        #
        # Basic playback
        #
        # "play_music" means resume/play the current
        # Music app playback.
        #
        # "play" means intelligently resolve the
        # requested target.
        #

        if action.operation == "play_music":

            return self._music.play()

        if action.operation == "play":

            target = str(
                action.arguments.get(
                    "target",
                    "",
                )
            ).strip()

            if not target:

                return self._music.play()

            return self._music.play(
                target
            )

        if action.operation == "pause_music":

            return self._music.pause()

        if action.operation == "next_song":

            return self._music.next()

        if action.operation == "previous_song":

            return self._music.previous()

        #
        # Current song controls
        #

        if action.operation == "restart_song":

            return self._music.restart()

        if action.operation == "repeat_one":

            return self._music.repeat_one()

        if action.operation == "repeat_off":

            return self._music.repeat_off()

        #
        # Specific song
        #

        if action.operation == "play_song":

            song = str(
                action.arguments.get(
                    "song",
                    "",
                )
            )

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            return self._music.play_song(
                song
            )

        #
        # Artist
        #

        if action.operation == "play_artist":

            artist = str(
                action.arguments.get(
                    "artist",
                    "",
                )
            )

            if not artist:

                raise ValueError(
                    "No artist was specified."
                )

            return self._music.play_artist(
                artist
            )

        #
        # Album
        #

        if action.operation == "play_album":

            album = str(
                action.arguments.get(
                    "album",
                    "",
                )
            )

            if not album:

                raise ValueError(
                    "No album was specified."
                )

            return self._music.play_album(
                album
            )

        #
        # Playlist
        #

        if action.operation == "play_playlist":

            playlist = str(
                action.arguments.get(
                    "playlist",
                    "",
                )
            )

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.play_playlist(
                playlist
            )

        #
        # Create playlist
        #

        if action.operation == "create_playlist":

            playlist = str(
                action.arguments.get(
                    "playlist",
                    "",
                )
            )

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.create_playlist(
                playlist
            )

        #
        # Add current song to playlist
        #

        if action.operation == "add_current_to_playlist":

            playlist = str(
                action.arguments.get(
                    "playlist",
                    "",
                )
            )

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.add_current_to_playlist(
                playlist
            )

        #
        # Add specific song to playlist
        #

        if action.operation == "add_song_to_playlist":

            song = str(
                action.arguments.get(
                    "song",
                    "",
                )
            )

            playlist = str(
                action.arguments.get(
                    "playlist",
                    "",
                )
            )

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.add_song_to_playlist(
                song,
                playlist,
            )

        #
        # Add song to queue
        #

        if action.operation == "add_song_to_queue":

            song = str(
                action.arguments.get(
                    "song",
                    "",
                )
            )

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            return self._music.add_song_to_queue(
                song
            )

        #
        # Unknown system action
        #

        raise KeyError(
            f"Unknown FRIDAY system action: "
            f"{action.operation}"
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
            # System actions already contain their
            # structured arguments from PlanStage.
            #

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