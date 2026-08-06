from runtime.platforms.apple.speech.provider import AppleSpeechProvider
from runtime.speech.recognizer import SpeechRecognizer

provider = AppleSpeechProvider()

recognizer = SpeechRecognizer(provider)

result = recognizer.listen()

print()
print(result)