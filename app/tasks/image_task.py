from crewai import Task

def create_image_task(agent):
    return Task(
        description="Generate an image from the enhanced prompt",
        expected_output="Image URL generated from the prompt",
        agent=agent
    )
