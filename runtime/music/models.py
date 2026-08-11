"""
==========================================================
F.R.I.D.A.Y.

Apple Music Models

Foundation Release 57.5
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class MusicAction(str, Enum):
    """
    Approved Apple Music operations.
    """

    OPEN = "open"

    PLAY = "play"

    PAUSE = "pause"

    NEXT = "next"

    PREVIOUS = "previous"

    RESTART = "restart"

    REPEAT_ONE = "repeat_one"

    REPEAT_OFF = "repeat_off"

    PLAY_SONG = "play_song"

    PLAY_ARTIST = "play_artist"

    PLAY_ALBUM = "play_album"

    PLAY_PLAYLIST = "play_playlist"

    CREATE_PLAYLIST = "create_playlist"

    ADD_TO_PLAYLIST = "add_to_playlist"

    ADD_TO_QUEUE = "add_to_queue"


@dataclass(slots=True)
class MusicRequest:
    """
    Structured request for Apple Music.
    """

    action: MusicAction

    target: str = ""

    song: str = ""

    artist: str = ""

    album: str = ""

    playlist: str = ""