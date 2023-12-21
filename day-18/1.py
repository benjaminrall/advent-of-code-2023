# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 62
from skimage.morphology import flood_fill


def move(pos, direction):
    match direction:
        case 'U':
            return (pos[0] - 1, pos[1])
        case 'D':
            return (pos[0] + 1, pos[1])
        case 'L':
            return (pos[0], pos[1] - 1)
        case 'R':
            return (pos[0], pos[1] + 1)
        
# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        instructions = [[c for c in line.strip().split()[:2]] for line in f.readlines()]

    if debug: print(instructions)

    max_width, min_width, max_height, min_height = 0, 0, 0, 0

    current_width, current_height = 0, 0

    for i in instructions:
        if i[0] == 'R':
            current_width += int(i[1])
        if i[0] == 'L':
            current_width -= int(i[1])
        if i[0] == 'U':
            current_height -= int(i[1])
        if i[0] == 'D':
            current_height += int(i[1])
        max_width = max(max_width, current_width)
        min_width = min(min_width, current_width)
        max_height = max(max_height, current_height)
        min_height = min(min_height, current_height)

    width = max_width - min_width + 1
    height = max_height - min_height + 1
    current_pos = (-min_height, -min_width)

    grid = np.zeros((height, width), dtype=int)
    grid[current_pos] = 1
    for i in instructions:
        for _ in range(int(i[1])):
            current_pos = move(current_pos, i[0])
            grid[current_pos] = 1

    grid = np.pad(grid, ((1, 1), (1, 1)))
    grid = flood_fill(grid, (0, 0), 2)
    # --- SOLUTION CODE ---
    return len(np.where(np.logical_or(grid == 1, grid == 0))[0])

import sys
np.set_printoptions(threshold=sys.maxsize)

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
