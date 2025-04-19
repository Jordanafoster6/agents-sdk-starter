from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List, Literal

from agents.run_context import RunContextWrapper
from agents import Agent, function_tool, Runner
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# --- Define memory tools for storing/retrieving context ---
@function_tool
def store_color(ctx: RunContextWrapper[dict], color: str) -> str:
    ctx.context["color"] = color
    return f"Got it. I’ll remember that your favorite color is {color}."

@function_tool
def get_color(ctx: RunContextWrapper[dict]) -> str:
    return ctx.context.get("color", "You haven’t told me your favorite color.")

# --- Configure the agent with tool access ---
agent = Agent(
    name="MemoryAgent",
    instructions="Use tools to store and recall the user's favorite color.",
    tools=[store_color, get_color],
    model="gpt-4"
)

# --- Input model expected from Node backend ---
class AgentInput(BaseModel):
    input: str
    context: Dict[str, Any]

# --- Output message shape expected by frontend ---
class AgentMessage(BaseModel):
    type: Literal["chat"]
    role: Literal["user", "assistant"]
    content: str

@app.post("/agent")
async def run_agent(data: AgentInput):
    context = data.context or {}

    result = await Runner.run(agent, data.input, context=context)

    return {
        "messages": [
            AgentMessage(type="chat", role="assistant", content=result.final_output)
        ],
        "context": context,
    }
