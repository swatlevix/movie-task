import os
import instructor
from app.schemas import MovieBase 

MODEL = "gemma4:31b-cloud"
client = instructor.from_provider(f"ollama/{MODEL}")

SYSTEM_PROMPT = """
You are an expert data extraction assistant specialized in movies. 
Your task is to analyze free-form user text and extract structured information about movies according to the provided schema.

Strict Rules:
1. Extract the official or most accurate title.
2. Synthesize a clean, coherent review or summary based ONLY on the user's input.
3. If information is missing, do your best to infer or leave it clean, but always respect the data types required by the schema.
"""

FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": "Tenet 2020 Nolan film. Confusing but cool",
    },
    {
        "role": "assistant",
        "content": '{"title": "Tenet", "review": "Confusing but cool Nolan film from 2020."}',
    },
    {
        "role": "user",
        "content": "Inception is hands down the best sci-fi ever! Leo was amazing in 2010.",
    },
    {
        "role": "assistant",
        "content": '{"title": "Inception", "review": "An amazing 2010 sci-fi film starring Leonardo DiCaprio."}',
    },
]


def extract_movie(text: str) -> MovieBase:
    return client.create(
        response_model=MovieBase,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *FEW_SHOT_EXAMPLES,
            {"role": "user", "content": text},
        ],
    )

