from runtime.platforms.apple.speech.recognizer import AppleRecognizer

recognizer = AppleRecognizer()

print()
print("Speak...")
print()

text = recognizer.recognize()

print()
print("Recognized:")
print(text)