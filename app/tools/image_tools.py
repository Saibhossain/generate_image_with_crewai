import os
import base64
from openai import OpenAI
from crewai.tools import BaseTool
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ImageGenerationTool(BaseTool):
    name: str = "Image Generator"
    description: str = "Generates an image from a given prompt and saves it locally."

    def _run(self, prompt: str) -> str:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = response.data[0].b64_json

        os.makedirs("images", exist_ok=True)
        image_count = len(os.listdir("images")) + 1
        file_path = f"images/generated_image_{image_count}.png"

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(image_base64))

        return file_path
 
 
 
 
  
 
 
 
 
 
    
# def generate_image(prompt: str):
#     response = client.images.generate(
#         model="gpt-image-1-mini",
#         prompt=prompt,
#         size="1024x1024"
#     )
    
#     image_base64 = response.data[0].b64_json
    
#     if not image_base64:
#         return "No image generated"
    
#     # Create folder
#     os.makedirs("images", exist_ok=True)

#     # Auto-increment filename
#     existing_files = os.listdir("images")
#     image_count = len(existing_files) + 1

#     file_path = f"images/generated_image_{image_count}.png"

#     # Download image from URL
#     with open(file_path, "wb") as f:
#         f.write(base64.b64decode(image_base64))

#     return file_path


# test image tools 
       
# print(generate_image("A futuristic city at sunset"))