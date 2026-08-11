"""
==========================================================
F.R.I.D.A.Y.

Music Service

Foundation Release 58.2
==========================================================
"""

from __future__ import annotations

from .apple_music import AppleMusicController
from .models import MusicAction, MusicRequest


class MusicService:
    """
    High-level Apple Music service.

    Receives structured MusicRequest objects and delegates
    approved operations to AppleMusicController.

    This service does not parse natural language.
    """

    def __init__(self) -> None:

        self._controller = AppleMusicController()

    def execute(
        self,
        request: MusicRequest,
    ) -> str:

        action = request.action

        #
        # --------------------------------------------------
        # Open Music
        # --------------------------------------------------
        #

        if action == MusicAction.OPEN:

            return self._controller.open()

        #
        # --------------------------------------------------
        # Basic playback
        # --------------------------------------------------
        #

        if action == MusicAction.PLAY:

            if request.target:

                return self._controller.play(
                    request.target
                )

            return self._controller.play()

        if action == MusicAction.PAUSE:

            return self._controller.pause()

        if action == MusicAction.NEXT:

            return self._controller.next()

        if action == MusicAction.PREVIOUS:

            return self._controller.previous()

        if action == MusicAction.RESTART:

            return self._controller.restart()

        #
        # --------------------------------------------------
        # Repeat
        # --------------------------------------------------
        #

        if action == MusicAction.REPEAT_ONE:

            return self._controller.repeat_one()

        if action == MusicAction.REPEAT_OFF:

            return self._controller.repeat_off()

        #
        # --------------------------------------------------
        # Now Playing
        # --------------------------------------------------
        #

        if action == MusicAction.NOW_PLAYING:

            return self._controller.now_playing()

        #
        # --------------------------------------------------
        # Specific song
        # --------------------------------------------------
        #

        if action == MusicAction.PLAY_SONG:

            if not request.song:

                raise ValueError(
                    "No song was specified."
                )

            return self._controller.play_song(
                request.song
            )

        #
        # --------------------------------------------------
        # Artist
        # --------------------------------------------------
        #

        if action == MusicAction.PLAY_ARTIST:

            if not request.artist:

                raise ValueError(
                    "No artist was specified."
                )

            return self._controller.play_artist(
                request.artist
            )

        #
        # --------------------------------------------------
        # Album
        # --------------------------------------------------
        #

        if action == MusicAction.PLAY_ALBUM:

            if not request.album:

                raise ValueError(
                    "No album was specified."
                )

            return self._controller.play_album(
                request.album
            )

        #
        # --------------------------------------------------
        # Playlist
        # --------------------------------------------------
        #

        if action == MusicAction.PLAY_PLAYLIST:

            if not request.playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._controller.play_playlist(
                request.playlist
            )

        #
        # --------------------------------------------------
        # Create playlist
        # --------------------------------------------------
        #

        if action == MusicAction.CREATE_PLAYLIST:

            if not request.playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            return self._controller.create_playlist(
                request.playlist
            )

        #
        # --------------------------------------------------
        # Add to playlist
        # --------------------------------------------------
        #

        if action == MusicAction.ADD_TO_PLAYLIST:

            if not request.playlist:

                raise ValueError(
                    "No playlist was specified."
                )

            if request.song:

                return (
                    self._controller
                    .add_song_to_playlist(
                        request.song,
                        request.playlist,
                    )
                )

            return (
                self._controller
                .add_current_to_playlist(
                    request.playlist
                )
            )

        #
        # --------------------------------------------------
        # Add to queue
        # --------------------------------------------------
        #

        if action == MusicAction.ADD_TO_QUEUE:

            if not request.song:

                raise ValueError(
                    "No song was specified."
                )

            return (
                self._controller
                .add_song_to_queue(
                    request.song
                )
            )

        #
        # --------------------------------------------------
        # Unknown action
        # --------------------------------------------------
        #

        raise ValueError(
            f"Unsupported music action: {action}"
        )