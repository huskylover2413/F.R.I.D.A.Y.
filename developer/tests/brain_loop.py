from runtime.brain import BrainContext
from runtime.brain import BrainLoop

context = BrainContext(
    request="Remember that my favorite language is Python."
)

brain = BrainLoop()

context = brain.run(context)

print()

print("Reasoning")
print("---------")

for line in context.blackboard.reasoning:
    print(line)

print()

print("Actions")
print("-------")

for action in context.blackboard.actions:
    print(action)