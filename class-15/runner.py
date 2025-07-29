from agents import Agent, Runner
from gemini_config import config


assistance = Agent(
    name='assistant',
    instructions='you are a helpful assistant',
)

output = Runner.run_sync(starting_agent=assistance, input='how are you?', run_config=config)
print(output.final_output)
