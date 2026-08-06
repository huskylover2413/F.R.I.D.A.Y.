from runtime.platforms.apple.speech.provider import AppleSpeechProvider

provider = AppleSpeechProvider()

print()
print("Speak...")
print()

result = provider.recognize()

print()
print(result)