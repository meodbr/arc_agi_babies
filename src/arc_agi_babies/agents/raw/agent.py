from google.adk.agents import Agent
from pydantic import BaseModel, Field

from arc_agi_babies.config.settings import settings
from arc_agi_babies.agents.raw.prompt import SYSTEM_INSTRUCTIONS

class OutputPixelGrid(BaseModel):
    output: list[list[int]]


root_agent = Agent(
    name="raw_agent",
    model=settings.GEMINI_MODEL,
    description=(
        "Agent solving 2D pixel puzzles"
    ),
    instruction=SYSTEM_INSTRUCTIONS,
    output_schema=OutputPixelGrid,
)