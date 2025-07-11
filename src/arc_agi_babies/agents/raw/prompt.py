from arc_agi_babies.config.settings import settings

SYSTEM_INSTRUCTIONS = """Based on the examples INPUT and OUTPUT pixel grids given, infer the TEST OUTPUT pixel grid.
The rule to get from input to output is:
each 1 is a blue pixel
each 2 is a red pixel
There are uncompleted blue (1) squares in the input, they are each missing one blue (1) pixel to be complete, let's call it the EXIT.

In the output:
* Each blue (1) square must be filled by red (2) pixels.
* The EXIT is pointing in a direction, a red (2) line must be drawn from this exit to the opposite side of the grid.
"""