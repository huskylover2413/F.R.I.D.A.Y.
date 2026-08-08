from runtime.memory.classifier import MemoryClassifier

classifier = MemoryClassifier()

tests = [
    "I love dark chocolate.",
    "My major is Computer Science.",
    "I'm building FRIDAY.",
    "I'm eating pizza.",
    "Remember that I cheer at Oregon State.",
]

for text in tests:

    result = classifier.classify(text)

    print(f"Input: {text}")
    print(f"Store: {result.should_store}")
    print(f"Category: {result.category}")
    print(f"Confidence: {result.confidence}")
    print("-" * 40)