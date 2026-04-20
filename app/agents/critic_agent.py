from crewai import Agent
from app.llm.config import get_llm

def create_critic_agent():
    return Agent(
        role="Critic",
        goal="Evaluate and improve prompt and image quality",
        backstory="Expert in visual critique and AI-generated content evaluation",
        llm=get_llm(),
        verbose=True
    )