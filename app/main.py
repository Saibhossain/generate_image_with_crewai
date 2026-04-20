import os
from dotenv import load_dotenv
load_dotenv()

from langtrace_python_sdk import langtrace
langtrace.init(api_key=os.getenv("LANGTRACE_API_KEY"))

from app.crews.crew_builder import build_crew



def run_pipeline():
    user_input = input("Enter your image idea: ")

    crew, tasks = build_crew(user_input)

    result = crew.kickoff()

    print("\n=== FINAL OUTPUT ===\n")
    print(result)

    print("\n=== TASK OUTPUTS ===\n")
    for i, task in enumerate(tasks, 1):
        print(f"\nTask {i}:")
        print(task.output)

if __name__ == "__main__":
    run_pipeline()
