from agents import Agent, Runner, function_tool
from gemini_config import config
from pydantic import BaseModel

class WeatherAnswer(BaseModel):
  location: str
  temperature_c: float
  summary: str
# weather_obj = WeatherRequest(city="karachi", weather="sunny", temperature="25°C")

@function_tool
def fetch_weather(location: str) ->str:
    """
    Fetches the weather for a given location.
    """
    return f"The weather in {location} is sunny with a temperature of 25°C."


simple_agent = Agent(
    name = "Simple Agent",
    instructions = "This is a simple agent that can handle basic tasks",
    tools=[fetch_weather],
    output_type=WeatherAnswer
)

result = Runner.run_sync(simple_agent,"what is the weather in karachi",run_config = config)
print("type>>>>",type(result.final_output))
print(result.final_output)