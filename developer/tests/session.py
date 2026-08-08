from runtime.services import ServiceContainer

services = ServiceContainer()

print()

print("Runtime Services")

print("----------------")

print(type(services.memory).__name__)

print(type(services.goals).__name__)

print(type(services.session).__name__)

print(type(services.vision).__name__)

print(type(services.ai).__name__)

print(type(services.planner).__name__)