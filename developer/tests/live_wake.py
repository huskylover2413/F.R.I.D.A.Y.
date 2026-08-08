from runtime.audio.microphone import Microphone
from runtime.wake import WakeDetector
from runtime.wake import WakeResult

print()
print("Listening...")
print("Say: Hey FRIDAY")
print()

mic = Microphone()

detector = WakeDetector()

mic.start()

try:

    while True:

        frame = mic.read()

        event = detector.detect(frame)

        if event.result == WakeResult.WAKE:

            print()
            print("WAKE DETECTED")
            print(event.phrase)
            print()

except KeyboardInterrupt:

    pass

finally:

    mic.stop()