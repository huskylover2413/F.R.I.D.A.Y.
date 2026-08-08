from runtime.planner import Planner

planner = Planner()

while True:

    request = input("\nYou: ")

    if request.lower() == "exit":
        break

    plan = planner.plan(request)

    print()

    print("Execution Plan")

    print("----------------")

    for task in plan.tasks:

        print("-", task.name)