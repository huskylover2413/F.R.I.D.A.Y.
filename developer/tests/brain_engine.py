from runtime.brain import BrainEngine

brain = BrainEngine()

response = brain.ask(
    "Explain recursion in one paragraph."
)

print()

print(response)

print()

print(response.message)