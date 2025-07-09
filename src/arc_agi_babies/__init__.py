import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"

def main() -> None:
    print("Hello from arc-agi-babies!")
