from runtime.platforms.apple.speech.provider import AppleSpeechProvider

provider = AppleSpeechProvider()

print("Listening...")

result = provider.recognize()

print()
print("Recognized:")
print(result.text)
print(result.confidence)