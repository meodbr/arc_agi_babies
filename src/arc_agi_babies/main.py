import sys
import json
import asyncio
import random
import os
import pathlib

from arc_agi_babies.runner import solve_task
from arc_agi_babies.agents.raw.agent import root_agent
from arc_agi_babies.utils import utils
from arc_agi_babies.utils.plot import plot_ARC_task

async def process_task_file(agent, task_file):
    with open(task_file, "r") as file:
        task = json.load(file)
    result = await solve_task(agent, task)
    return {
        "name": task_file.name,
        "task": task,
        "prediction": result.matrix,
    }

async def run_folder(agent, folder_path, max_tasks=10):
    task_files = [f for f in folder_path.glob("*.json") if f.is_file()]
    
    if not task_files:
        raise RuntimeError("No task files found in folder")
    
    if len(task_files) > max_tasks:
        task_files = random.sample(task_files, max_tasks)

    # Create coroutines for each file and run them in parallel
    tasks = [asyncio.create_task(process_task_file(agent, f)) for f in task_files]
    return await asyncio.gather(*tasks)

def main(args) -> int:
    tasks_folder = pathlib.Path(args[1])

    if not tasks_folder.is_dir() and not tasks_folder.is_file():
        print(f"Error: {tasks_folder} is not a folder.")
        return 1

    results = []
    if tasks_folder.is_dir():
        results = asyncio.run(run_folder(root_agent, tasks_folder, max_tasks=5))
    else:
        results = [asyncio.run(process_task_file(root_agent, tasks_folder))]

    sum = 0
    for res_dict in results:
        task = res_dict["task"]
        prediction = res_dict["prediction"]
        is_solved = utils.is_solved(task, prediction)
        solved_string = "Solved" if is_solved else "Failed"
        print(f"Task {res_dict['name']}: {solved_string}")
        if is_solved:
            sum += 1
    mean = sum / len(results)
    print(f"Tasks solved: {sum}/{len(results)} {mean*100:.1f}%")
    
    input("appuyez sur entrée")
    for res_dict in results:
        result_name = f"{res_dict['name']}_{root_agent.name}"
        plot_ARC_task(res_dict['task'], res_dict['prediction'], result_name, save=False)



if __name__ == "__main__":
    sys.exit(main(args=sys.argv))