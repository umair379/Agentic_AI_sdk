import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

gemini_client = AsyncOpenAI(
    api_key = api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta"
)

external_model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = gemini_client
)

config = RunConfig(
    model = external_model,
    model_provider = gemini_client,
    tracing_disabled = True
)
