from google.adk.agents import Agent
from pydantic import BaseModel, Field

from arc_agi_babies.config.settings import settings
from arc_agi_babies.agents.raw.prompt import SYSTEM_INSTRUCTIONS
from arc_agi_babies.utils import utils


root_agent = Agent(
    name="raw_agent",
    model=settings.GEMINI_MODEL,
    description=(
        "Agent solving 2D pixel puzzles"
    ),
    instruction=SYSTEM_INSTRUCTIONS,
    output_schema=utils.PixelMatrix,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)