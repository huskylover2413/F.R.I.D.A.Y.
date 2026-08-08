from runtime.brain import BrainContext

context = BrainContext(
    request="Help me with calculus."
)

context.recalled_memories.append(
    "Professor prefers step-by-step work."
)

context.observations.append(
    "Vision not required."
)

context.planned_services.extend(
    [
        "Memory",
        "AI",
    ]
)

context.reasoning.append(
    "Need educational explanation."
)

context.response = (
    "Let's solve it one step at a time."
)

context.remember_after_response = False

print()

print(context)