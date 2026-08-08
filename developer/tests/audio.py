from runtime.audio import AudioListener
from runtime.audio import AudioManager

audio = AudioManager()

listener = AudioListener(
    audio
)

print()
print("Starting FRIDAY audio...")
print("Listening for 10 frames.")
print()

audio.start()

try:

    for number in range(10):

        frame = listener.read()

        print(
            f"Frame {number + 1}: "
            f"shape={frame.shape} "
            f"dtype={frame.dtype}"
        )

finally:

    audio.stop()

print()
print("Audio test complete.")

