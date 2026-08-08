from runtime.wake.detector import WakeDetector

detector = WakeDetector()

tests = [

    "Friday",

    "Hey Friday",

    "Hello Friday",

    "Good morning Friday",

    "Hey Fri",

    "Fri",

    "What's the weather?",

    "Hello there",

]

for phrase in tests:

    event = detector.detect(

        phrase

    )

    print(

        phrase,

        "->",

        event.result,

    )