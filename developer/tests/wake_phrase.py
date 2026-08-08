from runtime.wake import WakePhraseParser


parser = WakePhraseParser()


tests = [

    "Friday",

    "Fri",

    "Hey Friday",

    "Hey Fri",

    "Hi Friday",

    "Hi Fri",

    "Hello Friday",

    "Hello Fri",

    "Good morning Friday",

    "Good afternoon Friday",

    "Good evening Friday",

    "Morning Friday",

    "Excuse me Friday",

    "Please Friday",

    "What's the weather?",

    "Hello there",

    "Hey Michael",

]


for phrase in tests:

    result = parser.is_address(
        phrase
    )

    print(
        f"{phrase:<30} -> {result}"
    )