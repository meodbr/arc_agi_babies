from pydantic import BaseModel, AfterValidator
from typing import Annotated

from arc_agi_babies.config.settings import settings

STRICT_ROW_LENGTH = False

def force_length(lst, n, fill_value=None):
    return lst[:n] + [fill_value] * (n - len(lst))

def matrix_row_sizes(matrix):
    if len(matrix) < 1:
        return matrix
    width = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != width:
            if STRICT_ROW_LENGTH:
                raise ValueError(f"Every row must have the same length in a matrix:\n{matrix_to_text(matrix)}")
            else:
                matrix[i] = force_length(row, width, fill_value=0)
    
    print(f"matrix is now:\n{matrix_to_text(matrix)}")
    return matrix

class PixelMatrix(BaseModel):
    matrix: Annotated[list[list[int]], AfterValidator(matrix_row_sizes)]

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