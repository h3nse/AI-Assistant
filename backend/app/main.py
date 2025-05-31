from openai import OpenAI
import os

client = OpenAI()
# api_key: str = os.getenv("OPENAI_API_KEY")


def query(query: str) -> str:
    response = client.responses.create(model="gpt-4.1", input=query)
    return response.output_text
