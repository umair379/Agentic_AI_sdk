import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

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


assistance = Agent(
    name='assistant',
    instructions='you are a helpful assistant',
    model=external_model,
)

output = Runner.run_sync(starting_agent=assistance, input='what is your name?')
print(output.final_output)
