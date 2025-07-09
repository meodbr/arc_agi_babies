from arc_agi_babies.config.settings import settings

def matrix_to_text(matrix: list[list[int]]) -> str:
    return "\n".join([" ".join(map(str, row)) for row in matrix])

def example_to_text(example):
    return f"INPUT:\n{matrix_to_text(example['input'])}\nOUTPUT:\n{matrix_to_text(example['output'])}"

def task_to_text(task):
    examples = "\n\n".join([example_to_text(example) for example in task["train"]])
    return f"### EXAMPLES:\n{examples}\n\n### TEST:\nINPUT:\n{matrix_to_text(task['test'][0]['input'])}"

def wrap_success(result):
    return {
        "status": "success",
        "result": result,
    }

def wrap_error(error, process_name=""):
    if process_name == "":
        return {
            "status": "failed",
            "error": str(error),
        }
    else:
        return {
            "status": "failed",
            "error": f"An error occured during {process_name}: {str(error)}",
        }