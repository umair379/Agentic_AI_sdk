from agents import Agent, Runner, function_tool
from gemini_config import config


# @function_tool
# def get_weather(city:str)->str:
#     return "Rainy and cloudy with a chance of meatballs in San Francisco"


@function_tool(
        name_override='mosam_batao',
        description_override='fetch weather'
)
async def fetch_weather(city:str)-> str:

    """Fetch the weather for a given location.

    Args:
        city: The city to fetch the weather for.
    """
    print('running fetch_weather tool...')

    #  In real life, we'd fetch the weather from a weather from a weather API
    return f"weather sunny in {city}"

@function_tool
def get_sum(a:int,b:int)->int:
    print('running get_sum tool...')
    return a+b

agent= Agent(
    name='Nextjs Assistant',
    instructions='you are a helpful assistant that provides information',
    tools=[fetch_weather,get_sum],
)

# for tool in agent.tools:
    # if isinstance(tool, FunctionTool):
        # print(tool.name)
        # print(tool.description)
        # print(json.dumps(tool.params_json_schema, indent=2))
        # print()


# print('tools:> ',agent.tools)


result = Runner.run_sync(agent,'what is weather in karachi',run_config=config)
print(result.final_output)

