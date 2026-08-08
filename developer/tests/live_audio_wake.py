from runtime.audio import AudioManager
from runtime.wake import WakeDetector
from runtime.wake import WakeResult


audio = AudioManager()

detector = WakeDetector()

print()
print("==============================================")
print("FRIDAY Live Wake Test")
print("==============================================")
print()
print("FRIDAY is listening.")
print("Say a supported wake phrase.")
print()
print("Press Control+C to stop.")
print()


audio.start()

try:

    while True:

        frame = audio.read()

        event = detector.detect(
            frame
        )

        if event.result == WakeResult.WAKE:

            print()
            print("==============================================")
            print("WAKE DETECTED")
            print(f"Model: {event.phrase}")
            print("==============================================")
            print()

except KeyboardInterrupt:

    print()
    print("Stopping FRIDAY wake listener...")

finally:

    audio.stop()

    print("Microphone stopped.")