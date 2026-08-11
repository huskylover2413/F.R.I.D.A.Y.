"""
==========================================================
F.R.I.D.A.Y.

Plan Stage

Foundation Release 56.4
==========================================================
"""

from __future__ import annotations

from ..action import Action
from ..context import BrainContext
from ..services import BrainService


class PlanStage:
    """
    Produces executable actions for the Brain.

    Local skills and approved system commands take
    priority over AI.
    """

    def run(
        self,
        context: BrainContext,
    ) -> None:

        board = context.blackboard

        board.actions.clear()

        request = board.metadata.get(
            "resolved_request",
            context.request.lower().strip(),
        )

        local_action = False

        #
        # --------------------------------------------------
        # Apple Music / Mac controls
        # --------------------------------------------------
        #

        if self._is_open_music_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="open_music",
                    priority=120,
                )
            )

            local_action = True

        #
        # Natural:
        #
        # "play Hollywood Sign"
        # "play Ed Sheeran"
        #
        # The Apple Music controller determines whether
        # the target is a song, artist, or album.
        #

        elif self._is_play_request(request):

            target = self._extract_play_target(
                request
            )

            if target:

                board.actions.append(
                    Action(
                        service=BrainService.SYSTEM,
                        operation="play",
                        priority=120,
                        arguments={
                            "target": target,
                        },
                    )
                )

                local_action = True

        #
        # Explicit song command
        #
        # "play song Hollywood Sign"
        #

        elif self._is_play_song_request(request):

            song = self._extract_song(
                request
            )

            if song:

                board.actions.append(
                    Action(
                        service=BrainService.SYSTEM,
                        operation="play_song",
                        priority=120,
                        arguments={
                            "song": song,
                        },
                    )
                )

                local_action = True

        #
        # Explicit artist command
        #
        # "play artist Ed Sheeran"
        #

        elif self._is_play_artist_request(request):

            artist = self._extract_artist(
                request
            )

            if artist:

                board.actions.append(
                    Action(
                        service=BrainService.SYSTEM,
                        operation="play_artist",
                        priority=120,
                        arguments={
                            "artist": artist,
                        },
                    )
                )

                local_action = True

        #
        # Explicit album command
        #
        # "play album Divide"
        #

        elif self._is_play_album_request(request):

            album = self._extract_album(
                request
            )

            if album:

                board.actions.append(
                    Action(
                        service=BrainService.SYSTEM,
                        operation="play_album",
                        priority=120,
                        arguments={
                            "album": album,
                        },
                    )
                )

                local_action = True

        #
        # Explicit playlist command
        #
        # "play my playlist Road Trip"
        #

        elif self._is_play_playlist_request(request):

            playlist = self._extract_playlist(
                request
            )

            if playlist:

                board.actions.append(
                    Action(
                        service=BrainService.SYSTEM,
                        operation="play_playlist",
                        priority=120,
                        arguments={
                            "playlist": playlist,
                        },
                    )
                )

                local_action = True

        #
        # Basic music playback
        #

        elif self._is_play_music_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="play_music",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_pause_music_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="pause_music",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_next_song_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="next_song",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_previous_song_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="previous_song",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_restart_song_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="restart_song",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_repeat_one_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="repeat_one",
                    priority=110,
                )
            )

            local_action = True

        elif self._is_repeat_off_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SYSTEM,
                    operation="repeat_off",
                    priority=110,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Time
        # --------------------------------------------------
        #

        elif self._is_time_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="time",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Date / Calendar
        # --------------------------------------------------
        #

        elif self._is_date_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="date",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Greeting
        # --------------------------------------------------
        #

        elif self._is_greeting(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="greeting",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Identity
        # --------------------------------------------------
        #

        elif self._is_identity_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="identity",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Help
        # --------------------------------------------------
        #

        elif self._is_help_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="help",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Math
        # --------------------------------------------------
        #

        elif self._is_math_request(request):

            board.actions.append(
                Action(
                    service=BrainService.SKILLS,
                    operation="math",
                    priority=100,
                )
            )

            local_action = True

        #
        # --------------------------------------------------
        # Memory
        # --------------------------------------------------
        #

        if any(
            word in request
            for word in (
                "remember",
                "memory",
            )
        ):

            board.actions.append(
                Action(
                    service=BrainService.MEMORY,
                    operation="search",
                    priority=90,
                )
            )

        #
        # --------------------------------------------------
        # Vision
        # --------------------------------------------------
        #

        if any(
            word in request
            for word in (
                "look",
                "screen",
                "image",
                "photo",
                "picture",
                "see",
            )
        ):

            board.actions.append(
                Action(
                    service=BrainService.VISION,
                    operation="describe",
                    priority=80,
                )
            )

        #
        # --------------------------------------------------
        # AI fallback
        # --------------------------------------------------
        #

        if not local_action:

            board.actions.append(
                Action(
                    service=BrainService.AI,
                    operation="respond",
                    priority=50,
                )
            )

        #
        # --------------------------------------------------
        # Highest priority first
        # --------------------------------------------------
        #

        board.actions.sort(
            key=lambda action: action.priority,
            reverse=True,
        )

        board.reasoning.append(
            f"Created {len(board.actions)} action(s)."
        )

    #
    # ======================================================
    # APPLE MUSIC — OPEN
    # ======================================================
    #

    @staticmethod
    def _is_open_music_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "open apple music",
                "open music",
                "launch apple music",
                "launch music",
            )
        )

    #
    # ======================================================
    # APPLE MUSIC — NATURAL PLAY
    # ======================================================
    #

    @staticmethod
    def _is_play_request(
        request: str,
    ) -> bool:

        if not request.startswith("play "):
            return False

        blocked = (
            "play music",
            "play my music",
            "play the music",
            "play song ",
            "play the song ",
            "play artist ",
            "play music by ",
            "play songs by ",
            "play album ",
            "play the album ",
            "play playlist ",
            "play the playlist ",
            "play my playlist ",
        )

        return not request.startswith(
            blocked
        )

    @staticmethod
    def _extract_play_target(
        request: str,
    ) -> str:

        target = request[
            len("play "):
        ].strip()

        endings = (
            " from apple music",
            " on apple music",
            " in apple music",
        )

        for ending in endings:

            if target.endswith(ending):

                target = target[
                    : -len(ending)
                ].strip()

        return target

    #
    # ======================================================
    # APPLE MUSIC — SPECIFIC SONG
    # ======================================================
    #

    @staticmethod
    def _is_play_song_request(
        request: str,
    ) -> bool:

        return (
            request.startswith("play song ")
            or request.startswith("play the song ")
            or "play the song called " in request
            or "play the song " in request
        )

    @staticmethod
    def _extract_song(
        request: str,
    ) -> str:

        prefixes = (
            "play the song called ",
            "play the song ",
            "play song ",
        )

        for prefix in prefixes:

            if request.startswith(prefix):

                return request[
                    len(prefix):
                ].strip()

        return ""

    #
    # ======================================================
    # APPLE MUSIC — ARTIST
    # ======================================================
    #

    @staticmethod
    def _is_play_artist_request(
        request: str,
    ) -> bool:

        return (
            request.startswith("play artist ")
            or request.startswith("play music by ")
            or request.startswith("play songs by ")
        )

    @staticmethod
    def _extract_artist(
        request: str,
    ) -> str:

        prefixes = (
            "play artist ",
            "play music by ",
            "play songs by ",
        )

        for prefix in prefixes:

            if request.startswith(prefix):

                return request[
                    len(prefix):
                ].strip()

        return ""

    #
    # ======================================================
    # APPLE MUSIC — ALBUM
    # ======================================================
    #

    @staticmethod
    def _is_play_album_request(
        request: str,
    ) -> bool:

        return (
            request.startswith("play album ")
            or request.startswith("play the album ")
        )

    @staticmethod
    def _extract_album(
        request: str,
    ) -> str:

        prefixes = (
            "play the album ",
            "play album ",
        )

        for prefix in prefixes:

            if request.startswith(prefix):

                return request[
                    len(prefix):
                ].strip()

        return ""

    #
    # ======================================================
    # APPLE MUSIC — PLAYLIST
    # ======================================================
    #

    @staticmethod
    def _is_play_playlist_request(
        request: str,
    ) -> bool:

        return (
            request.startswith("play playlist ")
            or request.startswith("play the playlist ")
            or request.startswith("play my playlist ")
        )

    @staticmethod
    def _extract_playlist(
        request: str,
    ) -> str:

        prefixes = (
            "play my playlist ",
            "play the playlist ",
            "play playlist ",
        )

        for prefix in prefixes:

            if request.startswith(prefix):

                return request[
                    len(prefix):
                ].strip()

        return ""

    #
    # ======================================================
    # APPLE MUSIC — BASIC PLAYBACK
    # ======================================================
    #

    @staticmethod
    def _is_play_music_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "play music",
                "play my music",
                "resume music",
                "resume",
                "start playing",
            )
        )

    @staticmethod
    def _is_pause_music_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "pause music",
                "pause",
                "stop the music",
                "stop music",
            )
        )

    @staticmethod
    def _is_next_song_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "next song",
                "next track",
                "skip song",
                "skip this song",
                "skip track",
                "skip this track",
            )
        )

    @staticmethod
    def _is_previous_song_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "previous song",
                "previous track",
                "last song",
                "go back",
                "go to the previous song",
                "go to the previous track",
            )
        )

    @staticmethod
    def _is_restart_song_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "start this song over",
                "start the song over",
                "restart this song",
                "restart the song",
                "restart song",
                "start this track over",
                "restart this track",
                "restart the current song",
                "restart the current track",
            )
        )

    @staticmethod
    def _is_repeat_one_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "play this again",
                "play the song again",
                "play this song again",
                "repeat this song",
                "repeat the song",
                "loop this song",
                "loop the song",
                "repeat this",
                "loop this",
            )
        )

    @staticmethod
    def _is_repeat_off_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "stop looping",
                "stop the loop",
                "turn repeat off",
                "turn off repeat",
                "repeat off",
                "stop repeating",
                "stop repeat",
            )
        )

    #
    # ======================================================
    # TIME
    # ======================================================
    #

    @staticmethod
    def _is_time_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "what time is it",
                "what's the time",
                "what is the time",
                "current time",
                "tell me the time",
            )
        )

    #
    # ======================================================
    # DATE / CALENDAR
    # ======================================================
    #

    @staticmethod
    def _is_date_request(
        request: str,
    ) -> bool:

        date_phrases = (
            "what date is it",
            "what's the date",
            "what is the date",
            "today's date",
            "todays date",
            "current date",
            "what day is it",
            "what day is today",
            "what day of the week is it",
            "what day of the week is today",
            "what is today",
            "what's today",
            "what is tomorrow",
            "what's tomorrow",
            "what day is tomorrow",
            "what day will tomorrow be",
            "what was yesterday",
            "what day was yesterday",
            "what day was it yesterday",
            "what day of the week was yesterday",
        )

        if any(
            phrase in request
            for phrase in date_phrases
        ):
            return True

        if (
            "tomorrow" in request
            or "yesterday" in request
        ):
            return True

        weekdays = (
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        )

        if request in weekdays:
            return True

        for day in weekdays:

            if (
                f"what is {day}" in request
                or f"what's {day}" in request
                or f"what day is {day}" in request
            ):
                return True

        if (
            "what month" in request
            or "current month" in request
            or "what year" in request
            or "current year" in request
        ):
            return True

        return False

    #
    # ======================================================
    # GREETING
    # ======================================================
    #

    @staticmethod
    def _is_greeting(
        request: str,
    ) -> bool:

        return request in {
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        }

    #
    # ======================================================
    # IDENTITY
    # ======================================================
    #

    @staticmethod
    def _is_identity_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "who are you",
                "what are you",
                "who is friday",
                "what is your name",
                "what's your name",
                "your name",
            )
        )

    #
    # ======================================================
    # HELP
    # ======================================================
    #

    @staticmethod
    def _is_help_request(
        request: str,
    ) -> bool:

        return any(
            phrase in request
            for phrase in (
                "help",
                "what can you do",
                "what do you do",
            )
        )

    #
    # ======================================================
    # MATH
    # ======================================================
    #

    @staticmethod
    def _is_math_request(
        request: str,
    ) -> bool:

        math_phrases = (
            "calculate",
            "plus",
            "minus",
            "times",
            "multiplied by",
            "divided by",
            "square root",
            "power of",
        )

        if any(
            phrase in request
            for phrase in math_phrases
        ):
            return True

        if any(
            operator in request
            for operator in (
                "*",
                "/",
                "%",
                "^",
            )
        ):
            return True

        if "+" in request:
            return True

        if (
            "-"
            in request
            and any(
                character.isdigit()
                for character in request
            )
        ):
            return True

        return False