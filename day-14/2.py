# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 64

def get_load(grid: np.ndarray):
    load = 0
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == 1:
                load += grid.shape[0] - row
    return load

def tilt_north(grid: np.ndarray):
    limits = [0 for _ in range(grid.shape[1])]
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == 1:
                grid[row, col] = 0
                grid[limits[col], col] = 1
                limits[col] += 1
            elif grid[row, col] == 2:
                limits[col] = row + 1
    return grid

def tilt_south(grid: np.ndarray):
    limits = [grid.shape[0] - 1 for _ in range(grid.shape[1])]
    for row in reversed(range(grid.shape[0])):
        for col in range(grid.shape[1]):
            if grid[row, col] == 1:
                grid[row, col] = 0
                grid[limits[col], col] = 1
                limits[col] -= 1
            elif grid[row, col] == 2:
                limits[col] = row - 1
    return grid

def tilt_west(grid: np.ndarray):
    limits = [0 for _ in range(grid.shape[0])]
    for col in range(grid.shape[1]):
        for row in range(grid.shape[0]):
            if grid[row, col] == 1:
                grid[row, col] = 0
                grid[row, limits[row]] = 1
                limits[row] += 1
            elif grid[row, col] == 2:
                limits[row] = col + 1
    return grid

def tilt_east(grid: np.ndarray):
    limits = [grid.shape[1] - 1 for _ in range(grid.shape[0])]
    for col in reversed(range(grid.shape[1])):
        for row in range(grid.shape[0]):
            if grid[row, col] == 1:
                grid[row, col] = 0
                grid[row, limits[row]] = 1
                limits[row] -= 1
            elif grid[row, col] == 2:
                limits[row] = col - 1
    return grid

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [[1 if c == 'O' else 2 if c == '#' else 0 for c in line.strip()] for line in f.readlines()]

    if debug: print(lines)

    # --- SOLUTION CODE ---
    grid = np.array(lines)
    states = {}
    TARGET = 1000000000
    for cycle in range(TARGET):
        grid = tilt_east(tilt_south(tilt_west(tilt_north(grid))))
        hashable = tuple(map(tuple, grid))
        if not hashable in states:
            states[hashable] = cycle
        else:
            loop_length = cycle - states[hashable]
            i = (TARGET - cycle) % loop_length
            print("LOOP", cycle, states[hashable], i)
            if i == 1:
                break
    print(grid)

    return get_load(grid)

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)

