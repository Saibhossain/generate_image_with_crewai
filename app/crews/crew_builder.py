from crewai import Crew

from app.agents.prompt_agent import create_prompt_agent
from app.agents.image_agent import create_image_agent
from app.agents.critic_agent import create_critic_agent

from app.tasks.prompt_task import create_prompt_task
from app.tasks.image_task import create_image_task
from app.tasks.critic_task import create_critic_task


def build_crew(user_input):

    prompt_agent = create_prompt_agent()
    image_agent = create_image_agent()
    critic_agent = create_critic_agent()

    task1 = create_prompt_task(prompt_agent, user_input)
    task2 = create_image_task(image_agent)
    task3 = create_critic_task(critic_agent)

    crew = Crew(
        agents=[prompt_agent, image_agent, critic_agent],
        tasks=[task1, task2, task3],
        verbose=True
    )

    return crew, [task1, task2, task3]