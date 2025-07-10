import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from typing import Any

PALETTE = [
    "#000000",
    "#0000ff",
    "#ff0000",
    "#00ff00",
    "#ffff00",
    "#b0b0b0",
    "#ff00b0",
    "#ffb000",
    "#00ffff",
    "#b00000",
    "#ffffff",
]
CMAP = ListedColormap(PALETTE)

def plot_ARC_image(pixel_grid: list[list[int]]):
    plot_ARC_image_np_array(np.array(pixel_grid))

def plot_pixel_matrix(pixel_matrix):
    plot_ARC_image(pixel_matrix.matrix)

def plot_ARC_image_np_array(image):
    plt.imshow(image, cmap=CMAP, vmin=0, vmax=len(PALETTE)-1)
    plt.show()

def plot_formatted_image(formatted):
    image = np.argmax(formatted, axis=0)
    plot_ARC_image(image)

def plot_ARC_task(task: dict[str, Any], prediction=None):
    
    prediction_col = []
    if prediction and "test" in task.keys():
        prediction_col.append({
            "input": task["test"][0]["input"],
            "output": prediction
        })

    # Estimate size
    rows = 2
    cols = len(task['train']) + len(task['test']) + len(prediction_col)

    images = [[example["input"], example["output"]] for example in task["train"] + task["test"] + prediction_col]

    fig, axes = plt.subplots(rows, cols, figsize=(cols*2, rows*2))
    for i in range(rows):
        for j in range(cols):
            ax = axes[i][j]
            ax.imshow(images[j][i], cmap=CMAP, vmin=0, vmax=len(PALETTE)-1)
            ax.axis("off")
    
    plt.tight_layout()
    plt.show()

