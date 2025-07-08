import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, handoff, RunContextWrapper, HandoffInputData
from openai import AsyncOpenAI

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


Nextjs_Agent = Agent(
    name = 'Nextjs Assistant',
    instructions = 'you are a helpfull assistant that provides information and answers questions to the best of your ability.'
)

Python_Agent = Agent(
    name = 'Python Assistant',
    instructions = 'you are a helpfull assistant that provides information and answers questions to the best of your ability.'
)

async def on_handoff(ctx:RunContextWrapper[None]):
    print(f'Nextjs_handoff triggered with context')




# Nextjs_handoff = handoff(
#     agent=Nextjs_Agent,
#     tool_name_override='Nextjs wale baba'
# )

def handoff_input_filter(inputData:HandoffInputData):
    print("inputData>>>>",inputData)
    return HandoffInputData(
        input_history=inputData.input_history,
        pre_handoff_items=inputData.pre_handoff_items,
        new_items=inputData.new_items,
    )

handoff_obj = handoff(
    agent=Nextjs_Agent,
    on_handoff=on_handoff,
    input_filter=handoff_input_filter,
)

Triage_Agent = Agent(
    name = 'triage Assistant',
    instructions= 'you are a helpfull assistant that navigates between Nextjs and Python agents to provide the best response based on the query.',
    handoffs=[handoff_obj,Python_Agent]
)

result = Runner.run_sync(Triage_Agent,'I want to get help regarding Nextjs routing',run_config=config)
# print('final output',result.final_output)
# print('current agent',result.last_agent)