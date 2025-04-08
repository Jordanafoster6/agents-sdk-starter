from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from agents.run_context import RunContextWrapper
from agents import Agent, function_tool, Runner
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Example memory tool
@function_tool
def store_color(ctx: RunContextWrapper[dict], color: str) -> str:
    ctx.context["color"] = color
    return f"Got it. I’ll remember that your favorite color is {color}."

@function_tool
def get_color(ctx: RunContextWrapper[dict]) -> str:
    return ctx.context.get("color", "You haven’t told me your favorite color.")

# @function_tool
# def test_memory(key: str, value: str, context: dict) -> str:
#     context[key] = value
#     return f"Saved {key} = {value}"

agent = Agent(
    name="MemoryAgent",
    instructions="Use tools to store and recall the user's favorite color.",
    tools=[store_color, get_color],
    model="gpt-4"
)

class AgentInput(BaseModel):
    input: str
    context: Dict[str, Any]

@app.post("/agent")
async def run_agent(data: AgentInput):
    context = data.context or {}  # just a dict, no import needed
    result = await Runner.run(agent, data.input, context=context)
    # print(result.__dict__) # inspect all available fields
    return {
      "output": result.final_output,
      "updatedContext": context,  # this will be a dict
    }

