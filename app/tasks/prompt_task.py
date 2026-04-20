from crewai import Task

def create_prompt_task(agent, user_input):
    return Task(
        description=f"Enhance this image prompt: {user_input}",
        expected_output="A detailed, high-quality image generation prompt",
        agent=agent
    )