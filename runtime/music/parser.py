"""
==========================================================
F.R.I.D.A.Y.

Apple Music Parser

Foundation Release 58.3
==========================================================
"""

from __future__ import annotations

from .models import MusicAction, MusicRequest


class MusicParser:
    """
    Converts natural-language music commands into
    structured MusicRequest objects.

    The parser never executes Apple Music commands.
    It only determines what the user wants FRIDAY to do.
    """

    def parse(
        self,
        request: str,
    ) -> MusicRequest | None:

        text = (
            str(request)
            .strip()
            .lower()
        )

        if not text:
            return None

        #
        # --------------------------------------------------
        # Now Playing
        # --------------------------------------------------
        #

        if text in {
            "what's playing",
            "what is playing",
            "what's playing?",
            "what is playing?",
            "what song is playing",
            "what song is playing?",
            "what song is this",
            "what song is this?",
            "who is playing",
            "who's playing",
            "who is singing",
            "who's singing",
        }:

            return MusicRequest(
                action=MusicAction.NOW_PLAYING
            )

        #
        # --------------------------------------------------
        # Basic playback
        # --------------------------------------------------
        #

        if text in {
            "play",
            "play music",
            "play my music",
            "play the music",
            "resume",
            "resume music",
            "start playing",
        }:

            return MusicRequest(
                action=MusicAction.PLAY
            )

        if text in {
            "pause",
            "pause music",
            "pause the music",
            "stop music",
            "stop the music",
        }:

            return MusicRequest(
                action=MusicAction.PAUSE
            )

        #
        # --------------------------------------------------
        # Next
        # --------------------------------------------------
        #

        if text in {
            "next",
            "next song",
            "next track",
            "skip",
            "skip song",
            "skip this song",
            "skip track",
            "skip this track",
        }:

            return MusicRequest(
                action=MusicAction.NEXT
            )

        #
        # --------------------------------------------------
        # Previous
        # --------------------------------------------------
        #

        if text in {
            "previous",
            "previous song",
            "previous track",
            "last song",
            "go back",
            "go back to the previous song",
            "go back to the previous track",
            "go to the previous song",
            "go to the previous track",
        }:

            return MusicRequest(
                action=MusicAction.PREVIOUS
            )

        #
        # --------------------------------------------------
        # Restart
        # --------------------------------------------------
        #

        if text in {
            "restart",
            "restart song",
            "restart the song",
            "restart this song",
            "restart the current song",
            "restart track",
            "restart this track",
            "restart the current track",
            "start the song over",
            "start this song over",
            "start the current song over",
            "start this track over",
        }:

            return MusicRequest(
                action=MusicAction.RESTART
            )

        #
        # --------------------------------------------------
        # Repeat current song
        # --------------------------------------------------
        #

        if text in {
            "play this again",
            "play the song again",
            "play this song again",
            "repeat",
            "repeat this",
            "repeat this song",
            "repeat the song",
            "loop",
            "loop this",
            "loop this song",
            "loop the song",
        }:

            return MusicRequest(
                action=MusicAction.REPEAT_ONE
            )

        #
        # --------------------------------------------------
        # Stop repeat
        # --------------------------------------------------
        #

        if text in {
            "stop looping",
            "stop the loop",
            "turn repeat off",
            "turn off repeat",
            "repeat off",
            "stop repeating",
            "stop repeat",
        }:

            return MusicRequest(
                action=MusicAction.REPEAT_OFF
            )

        #
        # --------------------------------------------------
        # Explicit song
        # --------------------------------------------------
        #

        prefixes = (
            "play the song called ",
            "play the song ",
            "play song ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                song = text[
                    len(prefix):
                ].strip()

                if song:

                    return MusicRequest(
                        action=MusicAction.PLAY_SONG,
                        song=song,
                    )

        #
        # --------------------------------------------------
        # Explicit artist
        # --------------------------------------------------
        #

        prefixes = (
            "play artist ",
            "play music by ",
            "play songs by ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                artist = text[
                    len(prefix):
                ].strip()

                if artist:

                    return MusicRequest(
                        action=MusicAction.PLAY_ARTIST,
                        artist=artist,
                    )

        #
        # --------------------------------------------------
        # Explicit album
        # --------------------------------------------------
        #

        prefixes = (
            "play the album ",
            "play album ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                album = text[
                    len(prefix):
                ].strip()

                if album:

                    return MusicRequest(
                        action=MusicAction.PLAY_ALBUM,
                        album=album,
                    )

        #
        # --------------------------------------------------
        # Explicit playlist
        # --------------------------------------------------
        #

        prefixes = (
            "play my playlist ",
            "play the playlist ",
            "play playlist ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                playlist = text[
                    len(prefix):
                ].strip()

                if playlist:

                    return MusicRequest(
                        action=MusicAction.PLAY_PLAYLIST,
                        playlist=playlist,
                    )

        #
        # --------------------------------------------------
        # Create playlist
        # --------------------------------------------------
        #

        prefixes = (
            "create a playlist called ",
            "create a playlist named ",
            "make a playlist called ",
            "make a playlist named ",
            "create playlist ",
            "make playlist ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                playlist = text[
                    len(prefix):
                ].strip()

                if playlist:

                    return MusicRequest(
                        action=MusicAction.CREATE_PLAYLIST,
                        playlist=playlist,
                    )

        #
        # --------------------------------------------------
        # Add current song to playlist
        # --------------------------------------------------
        #

        prefixes = (
            "add this song to my ",
            "add this song to the ",
            "add this to my ",
            "add this to the ",
            "add current song to my ",
            "add current song to the ",
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                playlist = text[
                    len(prefix):
                ].strip()

                if playlist.endswith(
                    " playlist"
                ):

                    playlist = playlist[
                        :-len(" playlist")
                    ].strip()

                if playlist:

                    return MusicRequest(
                        action=MusicAction.ADD_TO_PLAYLIST,
                        playlist=playlist,
                    )

        #
        # --------------------------------------------------
        # Add specific song to playlist
        # --------------------------------------------------
        #

        marker = " to my "

        if (
            text.startswith("add ")
            and marker in text
        ):

            song, playlist = text[
                len("add "):
            ].split(
                marker,
                1,
            )

            song = song.strip()
            playlist = playlist.strip()

            if playlist.endswith(
                " playlist"
            ):

                playlist = playlist[
                    :-len(" playlist")
                ].strip()

            if song and playlist:

                return MusicRequest(
                    action=MusicAction.ADD_TO_PLAYLIST,
                    song=song,
                    playlist=playlist,
                )

        marker = " to the "

        if (
            text.startswith("add ")
            and marker in text
        ):

            song, playlist = text[
                len("add "):
            ].split(
                marker,
                1,
            )

            song = song.strip()
            playlist = playlist.strip()

            if playlist.endswith(
                " playlist"
            ):

                playlist = playlist[
                    :-len(" playlist")
                ].strip()

            if song and playlist:

                return MusicRequest(
                    action=MusicAction.ADD_TO_PLAYLIST,
                    song=song,
                    playlist=playlist,
                )

        #
        # --------------------------------------------------
        # Add song to queue
        # --------------------------------------------------
        #

        queue_prefixes = (
            "add ",
            "queue ",
            "put ",
        )

        queue_suffixes = (
            " to my queue",
            " to the queue",
            " to queue",
            " in my queue",
            " in the queue",
        )

        for prefix in queue_prefixes:

            if not text.startswith(prefix):
                continue

            for suffix in queue_suffixes:

                if text.endswith(suffix):

                    song = text[
                        len(prefix):
                        -len(suffix)
                    ].strip()

                    if song:

                        return MusicRequest(
                            action=MusicAction.ADD_TO_QUEUE,
                            song=song,
                        )

        #
        # --------------------------------------------------
        # Natural "play ___"
        # --------------------------------------------------
        #

        if text.startswith("play "):

            target = text[
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

            if target:

                return MusicRequest(
                    action=MusicAction.PLAY,
                    target=target,
                )

        #
        # --------------------------------------------------
        # Not a music command
        # --------------------------------------------------
        #

        return None