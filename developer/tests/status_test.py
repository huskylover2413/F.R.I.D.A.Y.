from runtime.status import StatusManager

manager = StatusManager()

for system in manager.check():

    icon = "✓" if system.healthy else "✗"

    print(
        icon,
        system.name,
        "-",
        system.message,
    )