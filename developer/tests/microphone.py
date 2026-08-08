from runtime.audio.microphone import Microphone

mic = Microphone()

print()

print("Starting microphone...")

mic.start()

for i in range(10):

    frame = mic.read()

    print(

        "Frame",

        i + 1,

        frame.shape,

    )

mic.stop()

print()

print("Done.")