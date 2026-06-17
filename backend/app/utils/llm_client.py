import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class LLMClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    def generate_fix(
        self,
        error_description,
        file_content
    ):

        prompt = f"""
You are an expert Python developer.

Fix the error described below.

Error:
{error_description}

File Content:
{file_content}

Return ONLY the corrected file content.
No markdown.
No explanation.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content