import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("GOOGLE_API_KEY")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

external_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=external_model,
    model_provider=external_client,
    tracing_disabled=True
)

assistance = Agent(
    name='assistant',
    instructions='you are a helpful assistant',
    model=external_model,
)

output = Runner.run_sync(starting_agent=assistance, input='how are you?', run_config=config)
print(output.final_output)
