from openai import OpenAI
import os

client = OpenAI()


def query(query: str) -> str:
    response = client.responses.create(model="gpt-4.1", input=query)
    return response.output_text
