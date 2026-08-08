from runtime.memory.classifier import MemoryClassifier

classifier = MemoryClassifier()

tests = [
    "Remember that my favorite language is Python.",
    "I attend Oregon State University.",
    "I'm building FRIDAY.",
    "I'm eating lunch.",
]

for text in tests:

    result = classifier.classify(text)

    print(text)

    print(result)

    print()