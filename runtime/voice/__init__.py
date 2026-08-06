"""
FRIDAY Voice subsystem.
"""

from .macos_provider import MacOSVoiceProvider
from .provider import VoiceProvider
from .service import VoiceService
from .synthesizer import VoiceSynthesizer

__all__ = [
    "VoiceProvider",
    "VoiceSynthesizer",
    "MacOSVoiceProvider",
    "VoiceService",
]