from runtime.brain.action import Action
from runtime.registry.action_registry import ActionRegistry

registry = ActionRegistry()


def memory_handler(
    action: Action,
):

    print(
        "Memory executed."
    )

    return "ok"


registry.register(
    "memory",
    memory_handler,
)

action = Action(
    service="memory",
    operation="search",
)

result = registry.execute(
    action
)

print()

print(result)