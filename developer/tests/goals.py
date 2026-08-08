from runtime.goals import GoalManager

goals = GoalManager()

goals.add(
    "Build FRIDAY"
)

goals.add(
    "Finish Calculus"
)

goals.add(
    "Get Bakery Job"
)

print()

print("Goals")

print("-----")

for goal in goals.active():

    print(goal)