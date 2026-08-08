from runtime.brain import BrainContext
from runtime.brain import BrainLoop

context = BrainContext(
    request="Help me remember my Bronco."
)

brain = BrainLoop()

context = brain.run(
    context
)

print()

print("Actions")

print("-------")

for action in context.blackboard.actions:

    print(action)

print()

print("Reasoning")

print("---------")

for line in context.blackboard.reasoning:

    print(line)