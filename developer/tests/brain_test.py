from runtime.brain import BrainEngine

brain = BrainEngine()

brain.set_user("Shae")

brain.set_project("FRIDAY")

brain.set_goal("Become the world's best personal AI")

brain.begin_conversation()

brain.add_note(
    "Shae wants FRIDAY on Mac, iPhone, Apple Watch, CarPlay, and smart glasses."
)

print()

print("User:", brain.state.user_name)

print("Project:", brain.state.current_project)

print("Goal:", brain.state.active_goal)

print("Conversations:", brain.state.conversation_count)

print()

print("Notes:")

for note in brain.state.notes:
    print("-", note)