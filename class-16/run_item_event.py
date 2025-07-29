import asyncio
from agents import Agent, Runner,function_tool, ItemHelpers
from gemini_config import config
import random

@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 20)


async def main():
    agent = Agent(
        name="Joker",
        instructions="First call the 'how_many_jokes' tool, then tell that many jokes.",
        tools=[how_many_jokes],
    )

    result = Runner.run_streamed(agent, input="please call the tool and tell me jokes",run_config=config)
    async for event in result.stream_events():
        if event.type == "run_item_stream_event":
            print("event.item",event.item.type)
            if event.item.type == "tool_call_item":
                print("-- Tool was called")
            elif event.item.type == "tool_call_output_item":
                print(f"-- Tool output: {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
            # else:
            #     pass  # Ignore other event types

if __name__ == "__main__":
    asyncio.run(main())

