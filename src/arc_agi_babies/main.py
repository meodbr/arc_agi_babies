import sys
import json
import asyncio

from arc_agi_babies.runner import run_task
from arc_agi_babies.agents.raw.agent import root_agent

def main(args) -> int:
    task_file = args[1]
    with open(task_file, "r") as file:
        task = json.load(file)
    print(task)
    asyncio.run(run_task(root_agent, task))

if __name__ == "__main__":
    sys.exit(main(args=sys.argv))