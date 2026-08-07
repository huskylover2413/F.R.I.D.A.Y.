"""
Apple Speech permission management.

Responsible only for requesting and reporting the authorization
required by Apple's Speech framework.

No speech recognition occurs here.
"""

from __future__ import annotations

import threading
from enum import Enum
from typing import Final

import AVFoundation
import Speech


class PermissionState(str, Enum):
    """Unified permission state."""

    AUTHORIZED = "authorized"
    DENIED = "denied"
    RESTRICTED = "restricted"
    NOT_DETERMINED = "not_determined"


class AppleSpeechPermissions:
    """
    Handles Speech + Microphone authorization.

    This class intentionally hides Apple's asynchronous permission APIs
    behind synchronous methods so the remainder of FRIDAY can remain
    platform agnostic.
    """

    _MIC_TIMEOUT: Final[float] = 10.0
    _SPEECH_TIMEOUT: Final[float] = 10.0

    @staticmethod
    def speech_permission() -> PermissionState:
        """
        Return current Speech permission.
        """

        status = Speech.SFSpeechRecognizer.authorizationStatus()

        if status == Speech.SFSpeechRecognizerAuthorizationStatusAuthorized:
            return PermissionState.AUTHORIZED

        if status == Speech.SFSpeechRecognizerAuthorizationStatusDenied:
            return PermissionState.DENIED

        if status == Speech.SFSpeechRecognizerAuthorizationStatusRestricted:
            return PermissionState.RESTRICTED

        return PermissionState.NOT_DETERMINED

    @staticmethod
    def microphone_permission() -> PermissionState:
        """
        Return current microphone permission.
        """

        session = AVFoundation.AVAudioSession.sharedInstance()

        status = session.recordPermission()

        # Apple returns simple character constants:
        #
        # 'granted'
        # 'denied'
        # 'undetermined'
        #
        # PyObjC exposes these as strings.

        if status == "granted":
            return PermissionState.AUTHORIZED

        if status == "denied":
            return PermissionState.DENIED

        return PermissionState.NOT_DETERMINED

    @classmethod
    def request_speech_permission(cls) -> PermissionState:
        """
        Request Speech authorization.

        Blocks until Apple returns a result.
        """

        completed = threading.Event()

        result = PermissionState.NOT_DETERMINED

        def callback(status):
            nonlocal result

            if status == Speech.SFSpeechRecognizerAuthorizationStatusAuthorized:
                result = PermissionState.AUTHORIZED

            elif status == Speech.SFSpeechRecognizerAuthorizationStatusDenied:
                result = PermissionState.DENIED

            elif status == Speech.SFSpeechRecognizerAuthorizationStatusRestricted:
                result = PermissionState.RESTRICTED

            else:
                result = PermissionState.NOT_DETERMINED

            completed.set()

        Speech.SFSpeechRecognizer.requestAuthorization_(callback)

        completed.wait(cls._SPEECH_TIMEOUT)

        return result

    @classmethod
    def request_microphone_permission(cls) -> PermissionState:
        """
        Request microphone permission.

        Blocks until Apple returns.
        """

        completed = threading.Event()

        result = PermissionState.NOT_DETERMINED

        session = AVFoundation.AVAudioSession.sharedInstance()

        def callback(granted):
            nonlocal result

            result = (
                PermissionState.AUTHORIZED
                if granted
                else PermissionState.DENIED
            )

            completed.set()

        session.requestRecordPermission_(callback)

        completed.wait(cls._MIC_TIMEOUT)

        return result

    @classmethod
    def ensure_permissions(cls) -> bool:
        """
        Ensure Speech + Microphone permissions exist.

        Returns
        -------
        bool
            True if both permissions are available.
        """

        speech = cls.speech_permission()

        if speech == PermissionState.NOT_DETERMINED:
            speech = cls.request_speech_permission()

        if speech != PermissionState.AUTHORIZED:
            return False

        microphone = cls.microphone_permission()

        if microphone == PermissionState.NOT_DETERMINED:
            microphone = cls.request_microphone_permission()

        return microphone == PermissionState.AUTHORIZED