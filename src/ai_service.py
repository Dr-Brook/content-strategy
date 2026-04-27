"""Ollama AI service for content generation."""

import os
from openai import OpenAI

BASE_URL = os.environ.get("OPENAI_API_BASE", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "ollama/glm-5.1:cloud")
API_MODEL = MODEL_NAME.replace("ollama/", "") if MODEL_NAME.startswith("ollama/") else MODEL_NAME
API_KEY = os.environ.get("OPENAI_API_KEY", "ollama")

_client = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    return _client


def check_ollama_available() -> bool:
    try:
        client = _get_client()
        client.models.list()
        return True
    except Exception:
        return False


def generate_content(prompt: str) -> str:
    client = _get_client()
    response = client.chat.completions.create(
        model=API_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=1500,
    )
    return response.choices[0].message.content.strip()


def regenerate_content(prompt: str, tweak: str = "") -> str:
    if tweak:
        prompt = f"{prompt}\n\nADDITIONAL INSTRUCTIONS: {tweak}"
    return generate_content(prompt)