from runtime.wake import WakeManager

manager = WakeManager()

tests = [

    "hello",

    "Friday",

    "what's up?",

    "Hey Friday",

]

for phrase in tests:

    awakened = manager.process(
        phrase
    )

    print()

    print("Input :", phrase)

    print("Wake  :", awakened)

    print("State :", manager.state)

    if awakened:

        manager.sleep()