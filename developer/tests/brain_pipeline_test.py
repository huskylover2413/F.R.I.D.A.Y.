from runtime.brain.pipeline import BrainPipeline

pipeline = BrainPipeline()

if pipeline.recall_memory:
    pipeline.step("Memory")

if pipeline.use_planner:
    pipeline.step("Planner")

if pipeline.use_reasoning:
    pipeline.step("Reasoning")

if pipeline.use_skills:
    pipeline.step("Skills")

if pipeline.use_ai:
    pipeline.step("AI")

if pipeline.learn:
    pipeline.step("Learn")

print()

print("FRIDAY Brain Pipeline")

print("---------------------")

for step in pipeline.executed:
    print(step)