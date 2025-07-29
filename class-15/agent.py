from agents import Agent, Runner
from gemini_config import config, external_model

assistance = Agent(
    name='assistant',
    instructions='you are a helpful assistant',
    model=external_model,
)

output = Runner.run_sync(starting_agent=assistance, input='what is your name?')
print(output.final_output)
