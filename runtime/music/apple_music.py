"""
==========================================================
F.R.I.D.A.Y.

Apple Music Controller

Foundation Release 58.1
==========================================================
"""

from __future__ import annotations

import subprocess


class AppleMusicController:
    """
    Controlled interface to the macOS Music app.

    All Apple Music operations are explicitly defined here.
    FRIDAY never executes arbitrary AppleScript supplied by AI.
    """

    #
    # --------------------------------------------------
    # Internal AppleScript runner
    # --------------------------------------------------
    #

    @staticmethod
    def _run(
        script: str,
    ) -> str:

        result = subprocess.run(
            [
                "osascript",
                "-e",
                script,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()

    #
    # --------------------------------------------------
    # Open Music
    # --------------------------------------------------
    #

    def open(self) -> str:

        subprocess.run(
            [
                "open",
                "-a",
                "Music",
            ],
            check=True,
        )

        return "Apple Music is open."

    #
    # --------------------------------------------------
    # Playback
    # --------------------------------------------------
    #

    def play(
        self,
        target: str | None = None,
    ) -> str:

        if not target:

            self._run(
                'tell application "Music" to play'
            )

            return "Playing music."

        safe_target = self._escape(
            target
        )

        script = f'''
tell application "Music"

    set searchText to "{safe_target}"

    set matchingTracks to every track whose name is searchText

    if (count of matchingTracks) > 0 then

        play item 1 of matchingTracks

        return "SONG"

    end if

    set matchingTracks to every track whose artist is searchText

    if (count of matchingTracks) > 0 then

        play item 1 of matchingTracks

        return "ARTIST"

    end if

    set matchingTracks to every track whose album is searchText

    if (count of matchingTracks) > 0 then

        play item 1 of matchingTracks

        return "ALBUM"

    end if

    error "Music item not found."

end tell
'''

        result = self._run(script)

        if result == "SONG":

            return f"Playing {target}."

        if result == "ARTIST":

            return f"Playing music by {target}."

        if result == "ALBUM":

            return f"Playing the {target} album."

        return f"Playing {target}."

    def pause(self) -> str:

        self._run(
            'tell application "Music" to pause'
        )

        return "Music paused."

    def next(self) -> str:

        self._run(
            'tell application "Music" to next track'
        )

        return "Skipping to the next song."

    def previous(self) -> str:

        script = '''
tell application "Music"

    set player position to 0

    delay 0.1

    previous track

end tell
'''

        self._run(script)

        return "Going back to the previous song."

    #
    # --------------------------------------------------
    # Restart
    # --------------------------------------------------
    #

    def restart(self) -> str:

        script = '''
tell application "Music"

    set player position to 0

    play

end tell
'''

        self._run(script)

        return "Starting the song over."

    #
    # --------------------------------------------------
    # Repeat
    # --------------------------------------------------
    #

    def repeat_one(self) -> str:

        script = '''
tell application "Music"

    set song repeat to one

end tell
'''

        self._run(script)

        return "I'll repeat this song."

    def repeat_off(self) -> str:

        script = '''
tell application "Music"

    set song repeat to off

end tell
'''

        self._run(script)

        return "Song repeat is off."

    #
    # --------------------------------------------------
    # Now Playing
    # --------------------------------------------------
    #

    def now_playing(self) -> str:

        script = '''
tell application "Music"

    if not (exists current track) then

        return "NOTHING_PLAYING"

    end if

    set currentName to name of current track
    set currentArtist to artist of current track

    return currentName & "||| " & currentArtist

end tell
'''

        result = self._run(script)

        if result == "NOTHING_PLAYING":

            return "Nothing is currently playing."

        if "||| " in result:

            song, artist = result.split(
                "||| ",
                1,
            )

            return (
                f"Currently playing "
                f"{song} by {artist}."
            )

        return f"Currently playing {result}."

    #
    # --------------------------------------------------
    # Specific song
    # --------------------------------------------------
    #

    def play_song(
        self,
        song: str,
    ) -> str:

        safe_song = self._escape(
            song
        )

        script = f'''
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then

        error "Song not found."

    end if

    play item 1 of matchingTracks

end tell
'''

        self._run(script)

        return f"Playing {song}."

    #
    # --------------------------------------------------
    # Artist
    # --------------------------------------------------
    #

    def play_artist(
        self,
        artist: str,
    ) -> str:

        safe_artist = self._escape(
            artist
        )

        script = f'''
tell application "Music"

    set matchingTracks to every track whose artist is "{safe_artist}"

    if (count of matchingTracks) is 0 then

        error "Artist not found."

    end if

    play item 1 of matchingTracks

end tell
'''

        self._run(script)

        return f"Playing music by {artist}."

    #
    # --------------------------------------------------
    # Album
    # --------------------------------------------------
    #

    def play_album(
        self,
        album: str,
    ) -> str:

        safe_album = self._escape(
            album
        )

        script = f'''
tell application "Music"

    set matchingTracks to every track whose album is "{safe_album}"

    if (count of matchingTracks) is 0 then

        error "Album not found."

    end if

    play item 1 of matchingTracks

end tell
'''

        self._run(script)

        return f"Playing {album}."

    #
    # --------------------------------------------------
    # Playlist
    # --------------------------------------------------
    #

    def play_playlist(
        self,
        playlist: str,
    ) -> str:

        safe_playlist = self._escape(
            playlist
        )

        script = f'''
tell application "Music"

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"

    play targetPlaylist

end tell
'''

        self._run(script)

        return f"Playing the {playlist} playlist."

    #
    # --------------------------------------------------
    # Create playlist
    # --------------------------------------------------
    #

    def create_playlist(
        self,
        playlist: str,
    ) -> str:

        safe_playlist = self._escape(
            playlist
        )

        script = f'''
tell application "Music"

    if exists some user playlist whose name is "{safe_playlist}" then

        error "Playlist already exists."

    end if

    make new user playlist with properties {{name:"{safe_playlist}"}}

end tell
'''

        self._run(script)

        return f"Created the {playlist} playlist."

    #
    # --------------------------------------------------
    # Add current song to playlist
    # --------------------------------------------------
    #

    def add_current_to_playlist(
        self,
        playlist: str,
    ) -> str:

        safe_playlist = self._escape(
            playlist
        )

        script = f'''
tell application "Music"

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"

    set currentTrack to current track

    duplicate currentTrack to targetPlaylist

end tell
'''

        self._run(script)

        return (
            f"Added the current song to "
            f"the {playlist} playlist."
        )

    #
    # --------------------------------------------------
    # Add specific song to playlist
    # --------------------------------------------------
    #

    def add_song_to_playlist(
        self,
        song: str,
        playlist: str,
    ) -> str:

        safe_song = self._escape(
            song
        )

        safe_playlist = self._escape(
            playlist
        )

        script = f'''
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then

        error "Song not found."

    end if

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"

    duplicate item 1 of matchingTracks to targetPlaylist

end tell
'''

        self._run(script)

        return (
            f"Added {song} to "
            f"the {playlist} playlist."
        )

    #
    # --------------------------------------------------
    # Queue
    # --------------------------------------------------
    #

    def add_song_to_queue(
        self,
        song: str,
    ) -> str:

        safe_song = self._escape(
            song
        )

        script = f'''
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then

        error "Song not found."

    end if

    play item 1 of matchingTracks

end tell
'''

        self._run(script)

        return f"Added {song} to the queue."

    #
    # --------------------------------------------------
    # Escape AppleScript strings
    # --------------------------------------------------
    #

    @staticmethod
    def _escape(
        value: str,
    ) -> str:

        return (
            str(value)
            .replace(
                "\\",
                "\\\\",
            )
            .replace(
                '"',
                '\\"',
            )
        )