from google.adk.agents import Agent

from arc_agi_babies.prompt import MAIN_SYSTEM_INSTRUCTIONS
from arc_agi_babies.config.settings import settings

root_agent = Agent(
    name="main_agent",
    model=settings.GEMINI_MODEL,
    description=(
        "Agent résolvant des puzzles visuels prenant en entrée et en sortie une grille de pixel"
    ),
    instruction=MAIN_SYSTEM_INSTRUCTIONS,
)