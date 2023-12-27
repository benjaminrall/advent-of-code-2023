# Useful imports
import math
import numpy as np
import sys
from collections import defaultdict
np.set_printoptions(threshold=sys.maxsize)

# The expected result from the test input, if using a test input
TEST_RESULT = None
STEPS = 500

def step_grid(grid):
    w = np.where(grid == 2)
    for y, x in zip(w[0], w[1]):
        if 0 <= y - 1 < grid.shape[0]:
            if grid[y - 1, x] == 0:
                grid[y - 1, x] = 2 
        if 0 <= x - 1 < grid.shape[1]:
            if grid[y, x - 1] == 0:
                grid[y, x - 1] = 2 
        if 0 <= y + 1 < grid.shape[0]:
            if grid[y + 1, x] == 0:
                grid[y + 1, x] = 2 
        if 0 <= x + 1 < grid.shape[1]:
            if grid[y, x + 1] == 0:
                grid[y, x + 1] = 2 
        grid[y, x] = 0

def find_limits(grid: np.ndarray):
    grid = grid.copy()
    grid[0, 0] = 2
    steps = grid.shape[0] + grid.shape[1]
    limits = (steps, {})

    # Step through
    for _ in range(steps):
        step_grid(grid)

    # Gets even and odd result
    limits[1][steps % 2 == 0] = len(np.where(grid == 2)[0]) 
    step_grid(grid)
    limits[1][steps % 2 == 1] = len(np.where(grid == 2)[0]) 

    # Return number of reachable plots
    return limits

def expand(grid: np.ndarray, start_pos, steps, limits=None):
    grid = grid.copy()
    grid[start_pos] = 2

    if limits and steps >= limits[0]:
        if (start_pos[0] + start_pos[1]) % 2 == 0:
            return limits[1][steps % 2 == 0]
        else:
            return limits[1][steps % 2 == 1]

    # Step through
    for _ in range(steps):
        step_grid(grid)
    
    # print(grid)

    # Return number of reachable plots
    return len(np.where(grid == 2)[0])

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[1 if c == '#' else 0 if c == '.' else 2 for c in line.strip()] for line in f.readlines()])

    # Gets start position
    sy, sx = np.where(grid == 2)
    sy, sx = sy[0], sx[0]
    grid[(sy, sx)] = 0

    limits = find_limits(grid)

    total = expand(grid, (sy, sx), STEPS, limits)

    sideways_steps = STEPS - sy
    sideways_grids = math.ceil(sideways_steps / grid.shape[0])
    for i in range(sideways_grids):
        steps = sideways_steps - grid.shape[0] * i - 1
        for pos in [(0, sx), (sy, 0), (grid.shape[0] - 1, sx), (sy, grid.shape[1] - 1)]:
            total += expand(grid, pos, steps, limits)

    diagonal_steps = STEPS - grid.shape[0]
    diagonal_grids = math.ceil(diagonal_steps / grid.shape[0])
    for i in range(diagonal_grids):
        steps = diagonal_steps - grid.shape[0] * i - 1
        for pos in [(0, 0), (grid.shape[0] - 1, 0), (0, grid.shape[1] - 1), (grid.shape[0] - 1, grid.shape[1] - 1)]:
            total += (i + 1) * expand(grid, pos, steps, limits)

    # --- SOLUTION CODE ---
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
STEPS = 26501365
result = solve("input.txt")
print(result)