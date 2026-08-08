from runtime.platforms.apple.speech.provider import AppleSpeechProvider
<<<<<<< HEAD

provider = AppleSpeechProvider()

print()
print("Speak...")
print()

result = provider.recognize()
=======
from runtime.speech.recognizer import SpeechRecognizer

provider = AppleSpeechProvider()

recognizer = SpeechRecognizer(provider)

result = recognizer.listen()
>>>>>>> e76d99d509e97f70b16c6efbe46da2be6ee2a1b1

print()
print(result)