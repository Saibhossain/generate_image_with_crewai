import os
from crewai import LLM

from dotenv import load_dotenv
load_dotenv()

def get_llm(provider="openai"):
    if provider == "gemini":
        return LLM(
            model = "gemini/gemini-2.5-flash-lite",
            temperature=0.1,
            api_key=os.getenv("GEMINI_API_KEY")
        )
    elif provider == "openai":
        return LLM(
            model="gpt-4o-mini",
            temperature=0.1,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    else :
        print("No model selected")
        
        
        
