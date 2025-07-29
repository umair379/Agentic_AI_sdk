from agents import Agent, Runner, function_tool #enable_verbose_stdout_logging
from gemini_config import config
import asyncio

# enable_verbose_stdout_logging()
@function_tool(
        name_override="get_weather_info",
        # description_override="get weather info according to given location",
        use_docstring_info=False
)
async def fetch_weather(location:str)->str:
    """
    fetch weather according to given location

    Args:
    location: location for getting weather
    """
    return f"weather in {location} is sunny"

@function_tool
def sum (a:int , b:int)->int:
    """
    return sum of two numbers

    Args:
    a:integer number
    b:integer number
    """
    return a+b

weather_agent = Agent(
    name = "weather Assistant",
    instructions = "you are a helpful assistant provide answer by calling fetch weather tool",
    tools = [fetch_weather,sum],
    tool_use_behavior="stop_on_first_tool" #call only 1st tool
)
# print("tools>>>>",weather_agent.tools[0])


# result = Runner.run_sync(
#     weather_agent,
#     "what is weather in karachi and please sum 2 by 2",
#     run_config=config)

async def main():

    result = await Runner.run(
        weather_agent,
        "what is weather in karachi",
        run_config=config
    )
    print("result>>>>",result.final_output)


asyncio.run(main())