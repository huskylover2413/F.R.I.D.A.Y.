"""
==========================================================
F.R.I.D.A.Y.

Execute Stage

Foundation Release 58.3
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
from runtime.music import (
    MusicAction,
    MusicRequest,
    MusicService,
)

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
        # Music subsystem
        #

        self._music = MusicService()

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
    # System / Music
    # --------------------------------------------------
    #

    def _system_handler(
        self,
        action,
    ):

        operation = action.operation

        arguments = action.arguments

        #
        # --------------------------------------------------
        # Open Music
        # --------------------------------------------------
        #

        if operation == "open_music":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.OPEN,
                )
            )

        #
        # --------------------------------------------------
        # Basic playback
        # --------------------------------------------------
        #

        if operation == "play_music":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY,
                )
            )

        if operation == "play":

            target = str(
                arguments.get(
                    "target",
                    "",
                )
            ).strip()

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY,
                    target=target,
                )
            )

        if operation == "pause_music":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PAUSE,
                )
            )

        if operation == "next_song":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.NEXT,
                )
            )

        if operation == "previous_song":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PREVIOUS,
                )
            )

        #
        # --------------------------------------------------
        # Current song controls
        # --------------------------------------------------
        #

        if operation == "restart_song":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.RESTART,
                )
            )

        if operation == "repeat_one":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.REPEAT_ONE,
                )
            )

        if operation == "repeat_off":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.REPEAT_OFF,
                )
            )

        #
        # --------------------------------------------------
        # Now Playing
        # --------------------------------------------------
        #

        if operation == "now_playing":

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.NOW_PLAYING,
                )
            )

        #
        # --------------------------------------------------
        # Specific song
        # --------------------------------------------------
        #

        if operation == "play_song":

            song = str(
                arguments.get(
                    "song",
                    "",
                )
            ).strip()

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY_SONG,
                    song=song,
                )
            )

        #
        # --------------------------------------------------
        # Artist
        # --------------------------------------------------
        #

        if operation == "play_artist":

            artist = str(
                arguments.get(
                    "artist",
                    "",
                )
            ).strip()

            if not artist:

                raise ValueError(
                    "No artist was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY_ARTIST,
                    artist=artist,
                )
            )

        #
        # --------------------------------------------------
        # Album
        # --------------------------------------------------
        #

        if operation == "play_album":

            album = str(
                arguments.get(
                    "album",
                    "",
                )
            ).strip()

            if not album:

                raise ValueError(
                    "No album was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY_ALBUM,
                    album=album,
                )
            )

        #
        # --------------------------------------------------
        # Playlist
        # --------------------------------------------------
        #

        if operation == "play_playlist":

            playlist = str(
                arguments.get(
                    "playlist",
                    "",
                )
            ).strip()

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.PLAY_PLAYLIST,
                    playlist=playlist,
                )
            )

        #
        # --------------------------------------------------
        # Create playlist
        # --------------------------------------------------
        #

        if operation == "create_playlist":

            playlist = str(
                arguments.get(
                    "playlist",
                    "",
                )
            ).strip()

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.CREATE_PLAYLIST,
                    playlist=playlist,
                )
            )

        #
        # --------------------------------------------------
        # Add current song to playlist
        # --------------------------------------------------
        #

        if operation == "add_current_to_playlist":

            playlist = str(
                arguments.get(
                    "playlist",
                    "",
                )
            ).strip()

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.ADD_TO_PLAYLIST,
                    playlist=playlist,
                )
            )

        #
        # --------------------------------------------------
        # Add specific song to playlist
        # --------------------------------------------------
        #

        if operation == "add_song_to_playlist":

            song = str(
                arguments.get(
                    "song",
                    "",
                )
            ).strip()

            playlist = str(
                arguments.get(
                    "playlist",
                    "",
                )
            ).strip()

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            if not playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.ADD_TO_PLAYLIST,
                    song=song,
                    playlist=playlist,
                )
            )

        #
        # --------------------------------------------------
        # Add song to queue
        # --------------------------------------------------
        #

        if operation == "add_song_to_queue":

            song = str(
                arguments.get(
                    "song",
                    "",
                )
            ).strip()

            if not song:

                raise ValueError(
                    "No song was specified."
                )

            return self._music.execute(
                MusicRequest(
                    action=MusicAction.ADD_TO_QUEUE,
                    song=song,
                )
            )

        #
        # --------------------------------------------------
        # Unknown system action
        # --------------------------------------------------
        #

        raise KeyError(
            f"Unknown FRIDAY system action: "
            f"{operation}"
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

            self._executor.execute(
                action
            )

            board.reasoning.append(
                f"{action.service.name}:"
                f"{action.operation} executed."
            )