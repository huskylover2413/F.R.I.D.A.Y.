from runtime.memory import MemoryManager

memory = MemoryManager()

memory.remember(
    "person",
    "favorite_color",
    "Blue",
)

print(memory.recall("favorite_color"))

print()

print(memory.search("blue"))

print()

print(memory.all())