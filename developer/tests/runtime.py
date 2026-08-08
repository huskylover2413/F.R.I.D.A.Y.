from runtime.core.runtime import runtime

print()

print("Runtime")

print("-------")

print(runtime.services)

print()

print(type(runtime.services.memory).__name__)

print(type(runtime.services.goals).__name__)

print(type(runtime.services.session).__name__)