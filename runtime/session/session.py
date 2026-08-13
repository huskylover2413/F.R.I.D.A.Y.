"""
==========================================================
F.R.I.D.A.Y.

Interactive Voice Session

Foundation Release 50.3
==========================================================
"""

from __future__ import annotations

from runtime.audio import AudioListener
from runtime.audio import AudioManager
from runtime.cognition import CognitionEngine
from runtime.input import MicrophoneInput
from runtime.language import LanguageNormalizer
from runtime.profile import ProfileManager
from runtime.voice import VoiceSynthesizer
from runtime.wake import WakeDetector
from runtime.wake import WakeResult
from runtime.wake import WakePhraseParser

from .models import SessionState


class Session:
    """
    Continuous FRIDAY voice session.

    FRIDAY remains listening for her wake phrase.
    After wake detection:

        Wake
        -> Speech recognition
        -> Cognition
        -> Voice
        -> Wake listening
    """

    def __init__(self) -> None:

        self._running = False

        self._state = SessionState()

        self._profile = ProfileManager().load()

        self._cognition = CognitionEngine()

        self._normalizer = LanguageNormalizer()

        #
        # Wake-word microphone
        #
        self._audio = AudioManager()

        self._listener = AudioListener(
            self._audio
        )

        self._wake = WakeDetector()
        
        self._wake_parser = WakePhraseParser()

        #
        # Apple Speech microphone
        #
        self._input = MicrophoneInput()

        #
        # Voice output
        #
        self._voice = VoiceSynthesizer(
            self._profile
        )

    @property
    def running(self) -> bool:

        return self._running

    @property
    def state(self) -> SessionState:

        return self._state

    def initialize(self) -> None:

        self._running = True

    def run(self) -> None:

        print()
        print("====================================================")
        print("FRIDAY")
        print("====================================================")
        print()
        print("FRIDAY is listening.")
        print("Say: Hey FRIDAY")
        print()

        self._audio.start()

        try:

            while self._running:

                #
                # ========================================
                # WAIT FOR WAKE WORD
                # ========================================
                #

                frame = self._listener.read()

                event = self._wake.detect(
                    frame
                )

                if event.result != WakeResult.WAKE:

                    continue

                print()
                print("==============================================")
                print("FRIDAY: I'm listening.")
                print("==============================================")
                print()

                #
                # ========================================
                # GIVE MICROPHONE TO APPLE SPEECH
                # ========================================
                #

                self._audio.stop()

                try:

                    user_input = self._input.read()

                finally:

                    #
                    # Apple Speech is finished.
                    # Return microphone ownership
                    # to the wake detector.
                    #

                    self._audio.start()

                if not user_input:

                    print(
                        "FRIDAY: I didn't hear anything."
                    )

                    continue

                user_input = (
                    self._normalizer.normalize(
                        user_input
                    )
                )

                #
                # Update session state
                #

                self._state.last_request = (
                    user_input
                )

                self._state.conversation_turns += 1

                print()
                print(
                    f"✓ Heard: {user_input}"
                )
                print("🧠 Thinking...")
                print()

                #
                # ========================================
                # EXIT
                # ========================================
                #

                if user_input.lower() in (
                    "exit",
                    "quit",
                    "goodbye",
                    "shut down",
                ):

                    self._running = False

                    break

                #
                # ========================================
                # BRAIN
                # ========================================
                #

                response = self._cognition.process(
                    user_input
                )

                self._state.last_response = (
                    response.message
                )

                print(
                    f"🤖 {response.message}"
                )

                print()

                #
                # ========================================
                # VOICE
                # ========================================
                #

                self._voice.speak(
                    response.message
                )

                #
                # ========================================
                # BACK TO WAKE LISTENING
                # ========================================
                #

                print()
                print(
                    "FRIDAY is listening..."
                )
                print()

        except KeyboardInterrupt:

            print()
            print("Shutdown requested.")

        finally:

            self.shutdown()

    def shutdown(self) -> None:

        if not self._running:

            #
            # Still release hardware if possible.
            #

            try:
                self._audio.stop()
            except Exception:
                pass

            try:
                self._input.shutdown()
            except Exception:
                pass

            return

        self._running = False

        try:

            self._audio.stop()

        except Exception:
            pass

        try:

            self._input.shutdown()

        except Exception:
            pass

        print()
        print("FRIDAY is shutting down.")