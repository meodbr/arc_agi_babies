import os
from . import agent

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"

def main() -> None:
    print("Hello from arc-agi-babies!")
