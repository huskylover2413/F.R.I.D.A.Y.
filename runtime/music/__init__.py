"""
F.R.I.D.A.Y.

Music subsystem.
"""

from .apple_music import AppleMusicController
from .models import MusicAction, MusicRequest
from .parser import MusicParser
from .service import MusicService

__all__ = [
    "AppleMusicController",
    "MusicAction",
    "MusicRequest",
    "MusicParser",
    "MusicService",
]