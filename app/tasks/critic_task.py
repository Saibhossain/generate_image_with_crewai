from crewai import Task

def create_critic_task(agent):
    return Task(
        description="Evaluate the generated image and suggest improvements",
        expected_output="Detailed critique and improved prompt suggestion",
        agent=agent
    )
