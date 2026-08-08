from runtime.project import ProjectManager

manager = ProjectManager()

status = manager.status()

print(status.name)

print(status.version)

for task in status.tasks:

    print("-", task.title)