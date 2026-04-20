import os 
import PIL.Image
from openai import OpenAI
from io import BytesIO
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

import requests
import os

def generate_image(prompt: str, model: str = "openai"):
    api_key = os.getenv("AICC_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    if model == "openai":
        response = requests.post(
            "https://api.ai.cc/v1/images/generations",
            headers=headers,
            json={
                "model": "gpt-image-1",
                "prompt": prompt,
                "size": "1024x1024"
            }
        )

        response.raise_for_status()
        return response.json()["data"][0]["url"]

    elif model == "gemini":
        response = requests.post(
            "/v1beta/models/gemini-3.1-flash-image-preview:generateContent",
            headers=headers,
            json={
                "model": "gemini-3.1-flash-image-preview",
                "prompt": prompt
            }
        )

        response.raise_for_status()
        return response.json()

    else:
        raise ValueError("Model must be 'openai' or 'gemini'")

            
generate_image("A futuristic city at sunset.", "gemini")