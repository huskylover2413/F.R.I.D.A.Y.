"""
==========================================================
F.R.I.D.A.Y.

Apple Music Controller

Foundation Release 58.6
==========================================================
"""

from __future__ import annotations

import subprocess


class AppleMusicController:

    @staticmethod
    def _run(script: str) -> str:

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

    @staticmethod
    def _escape(value: str) -> str:

        return (
            str(value)
            .replace("\\", "\\\\")
            .replace('"', '\\"')
        )

    @staticmethod
    def _shuffle_commands(
        shuffle: bool,
    ) -> str:

        if shuffle:

            return """
    set shuffle enabled to true
    set shuffle mode to songs
"""

        return """
    set shuffle enabled to false
"""

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
    # Basic playback
    # --------------------------------------------------
    #

    def play(
        self,
        target: str | None = None,
        shuffle: bool = False,
    ) -> str:

        if not target:

            script = f"""
tell application "Music"
{self._shuffle_commands(shuffle)}
    play
end tell
"""

            self._run(script)

            if shuffle:
                return "Playing music shuffled."

            return "Playing music."

        safe_target = self._escape(target)

        script = f"""
tell application "Music"

    set searchText to "{safe_target}"

    set matchingTracks to every track whose name is searchText

    if (count of matchingTracks) > 0 then
{self._shuffle_commands(shuffle)}
        play item 1 of matchingTracks
        return "SONG"
    end if

    set matchingTracks to every track whose artist is searchText

    if (count of matchingTracks) > 0 then
{self._shuffle_commands(shuffle)}
        play item 1 of matchingTracks
        return "ARTIST"
    end if

    set matchingTracks to every track whose album is searchText

    if (count of matchingTracks) > 0 then
{self._shuffle_commands(shuffle)}
        play item 1 of matchingTracks
        return "ALBUM"
    end if

    error "Music item not found."

end tell
"""

        result = self._run(script)

        if result == "SONG":
            return (
                f"Playing {target} shuffled."
                if shuffle
                else f"Playing {target}."
            )

        if result == "ARTIST":
            return (
                f"Playing music by {target} shuffled."
                if shuffle
                else f"Playing music by {target}."
            )

        if result == "ALBUM":
            return (
                f"Playing the {target} album shuffled."
                if shuffle
                else f"Playing the {target} album."
            )

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

        self._run(
            'tell application "Music" to previous track'
        )

        return "Going back to the previous song."

    def restart(self) -> str:

        self._run(
            'tell application "Music" to set player position to 0'
        )

        self._run(
            'tell application "Music" to play'
        )

        return "Starting the song over."

    #
    # --------------------------------------------------
    # Repeat
    # --------------------------------------------------
    #

    def repeat_one(self) -> str:

        self._run(
            'tell application "Music" to set song repeat to one'
        )

        return "I'll repeat this song."

    def repeat_off(self) -> str:

        self._run(
            'tell application "Music" to set song repeat to off'
        )

        return "Song repeat is off."

    #
    # --------------------------------------------------
    # Now Playing
    # --------------------------------------------------
    #

    def now_playing(self) -> str:

        script = """
tell application "Music"

    if not (exists current track) then
        return "Nothing is currently playing."
    end if

    set currentName to name of current track
    set currentArtist to artist of current track

    if currentArtist is not "" then
        return currentName & " by " & currentArtist
    end if

    return currentName

end tell
"""

        result = self._run(script)

        return result or "Nothing is currently playing."

    #
    # --------------------------------------------------
    # Specific song
    # --------------------------------------------------
    #

    def play_song(
        self,
        song: str,
        shuffle: bool = False,
    ) -> str:

        safe_song = self._escape(song)

        script = f"""
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then
        error "Song not found."
    end if

{self._shuffle_commands(shuffle)}
    play item 1 of matchingTracks

end tell
"""

        self._run(script)

        return (
            f"Playing {song} shuffled."
            if shuffle
            else f"Playing {song}."
        )

    #
    # --------------------------------------------------
    # Artist
    # --------------------------------------------------
    #

    def play_artist(
        self,
        artist: str,
        shuffle: bool = False,
    ) -> str:

        safe_artist = self._escape(artist)

        #
        # Normal artist playback keeps the existing
        # behavior: find one track and play it.
        #

        if not shuffle:

            script = f"""
tell application "Music"

    set matchingTracks to every track whose artist is "{safe_artist}"

    if (count of matchingTracks) is 0 then
        error "Artist not found."
    end if

    set shuffle enabled to false

    play item 1 of matchingTracks

end tell
"""

            self._run(script)

            return f"Playing music by {artist}."

        #
        # Artist shuffle needs a real collection. Apple Music
        # cannot reliably turn one selected track into an
        # artist-only shuffled queue, so build a dedicated
        # FRIDAY playlist from the artist's library tracks.
        #

        safe_playlist_name = self._escape(
            f"FRIDAY Shuffle - {artist}"
        )

        script = f"""
tell application "Music"

    set matchingTracks to every track whose artist is "{safe_artist}"

    if (count of matchingTracks) is 0 then
        error "Artist not found."
    end if

    set playlistName to "{safe_playlist_name}"

    if exists some user playlist whose name is playlistName then

        set targetPlaylist to some user playlist whose name is playlistName

        try
            delete every track of targetPlaylist
        end try

    else

        set targetPlaylist to make new user playlist with properties {{name:playlistName}}

    end if

    repeat with sourceTrack in matchingTracks
        duplicate sourceTrack to targetPlaylist
    end repeat

    set shuffle enabled to true
    set shuffle mode to songs

    play targetPlaylist

end tell
"""

        self._run(script)

        return (
            f"Playing music by "
            f"{artist} shuffled."
        )

    #
    # --------------------------------------------------
    # Album
    # --------------------------------------------------
    #

    def play_album(
        self,
        album: str,
        shuffle: bool = False,
    ) -> str:

        safe_album = self._escape(album)

        script = f"""
tell application "Music"

    set matchingTracks to every track whose album is "{safe_album}"

    if (count of matchingTracks) is 0 then
        error "Album not found."
    end if

{self._shuffle_commands(shuffle)}
    play item 1 of matchingTracks

end tell
"""

        self._run(script)

        return (
            f"Playing the {album} album shuffled."
            if shuffle
            else f"Playing {album}."
        )

    #
    # --------------------------------------------------
    # Playlist
    # --------------------------------------------------
    #

    def play_playlist(
        self,
        playlist: str,
        shuffle: bool = False,
    ) -> str:

        safe_playlist = self._escape(playlist)

        script = f"""
tell application "Music"

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"

{self._shuffle_commands(shuffle)}
    play targetPlaylist

end tell
"""

        self._run(script)

        return (
            f"Playing the {playlist} playlist shuffled."
            if shuffle
            else f"Playing the {playlist} playlist."
        )

    #
    # --------------------------------------------------
    # Create playlist
    # --------------------------------------------------
    #

    def create_playlist(
        self,
        playlist: str,
    ) -> str:

        safe_playlist = self._escape(playlist)

        script = f"""
tell application "Music"

    if exists some user playlist whose name is "{safe_playlist}" then
        error "Playlist already exists."
    end if

    make new user playlist with properties {{name:"{safe_playlist}"}}

end tell
"""

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

        safe_playlist = self._escape(playlist)

        script = f"""
tell application "Music"

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"
    set currentTrack to current track
    duplicate currentTrack to targetPlaylist

end tell
"""

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

        safe_song = self._escape(song)
        safe_playlist = self._escape(playlist)

        script = f"""
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then
        error "Song not found."
    end if

    set targetPlaylist to some user playlist whose name is "{safe_playlist}"

    duplicate item 1 of matchingTracks to targetPlaylist

end tell
"""

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

        safe_song = self._escape(song)

        script = f"""
tell application "Music"

    set matchingTracks to every track whose name is "{safe_song}"

    if (count of matchingTracks) is 0 then
        error "Song not found."
    end if

    play item 1 of matchingTracks

end tell
"""

        self._run(script)

        return f"Added {song} to the queue."