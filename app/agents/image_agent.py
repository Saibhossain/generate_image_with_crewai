from crewai import Agent
from app.llm.config import get_llm
from app.tools.image_tools import ImageGenerationTool

def create_image_agent():
    return Agent(
        role="Image Generator",
        goal="Generate images from optimized prompts",
        backstory="AI artist specialized in generating high-quality visuals",
        tools=[ImageGenerationTool()],
        llm=get_llm("openai"),
        verbose=True
    )
    
    
    
    

# test llm

# result = get_llm("openai").call("what is the best time to learn about agent ? ")
# print(result)