from crewai import Agent
from app.llm.config import get_llm
from app.tools.image_tools import generate_image

# test llm
# result = get_llm("gemini").call("what is the best time to learn about agent ? ")
# print(result)

def generate_image(prompt):
    return Agent(
        role="Image Generator",
        goal="Generate images from optimized prompts",
        backstory="AI artist specialized in generating high-quality visuals",
        tools=[generate_image],
        llm=get_llm(),
        verbose=True
    )