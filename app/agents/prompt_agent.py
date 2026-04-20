from crewai import Agent
from app.llm.config import get_llm


def create_prompt_agent():
    return Agent(
        role ="Prompt Engineer",
        goal="You have to enhance user prompts for high-quality image generation",
        backstory="You are a creative image generation expert also expert in creative AI prompt engineering and visual storytelling",
        llm=get_llm("openai"),
        verbose=True
    )