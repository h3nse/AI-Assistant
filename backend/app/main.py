from openai import OpenAI
import os
from app import config

client = OpenAI()


def query(query: str) -> str:
    response = client.responses.create(
        model="gpt-4.1",
        instructions=config.aiInstructions,
        store=False,
        stream=True,
        input=query,
    )
    for event in response:
        if event.type == "response.output_text.delta":
            yield event.delta
