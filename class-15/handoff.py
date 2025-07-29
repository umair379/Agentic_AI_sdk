from agents import Agent, Runner, handoff, RunContextWrapper, HandoffInputData
from gemini_config import config

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