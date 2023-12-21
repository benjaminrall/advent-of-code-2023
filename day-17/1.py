# Useful imports
import math
import numpy as np
from enum import Enum
from queue import PriorityQueue

# The expected result from the test input, if using a test input
TEST_RESULT = 102




class D(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

TURNS = {
    D.UP: [D.LEFT, D.RIGHT],
    D.DOWN: [D.LEFT, D.RIGHT],
    D.LEFT: [D.UP, D.DOWN],
    D.RIGHT: [D.UP, D.DOWN]
}

def move(pos, direction):
    if direction == D.UP:
        return (pos[0] - 1, pos[1])
    if direction == D.DOWN:
        return (pos[0] + 1, pos[1])
    if direction == D.LEFT:
        return (pos[0], pos[1] - 1)
    if direction == D.RIGHT:
        return (pos[0], pos[1] + 1)

def pos_in_range(grid, pos):
    if 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]:
        return True
    return False

def search(grid, pos, direction: D, path: list, visited: set, distance: int):
    #print(grid)
    #print(pos, direction, path, visited, distance)
    #input()

    if pos[0] == grid.shape[0] - 1 and pos[1] == grid.shape[1] - 1:
        return distance

    visited.add(pos)
    
    best_option = math.inf
    for d in TURNS[direction]:
        new_pos = move(pos, d)
        if pos_in_range(grid, new_pos) and new_pos not in visited:
            path.append(d)
            best_option = min(best_option, search(grid, new_pos, d, path, visited, distance + grid[new_pos]))
    
    if len(path) >= 3:
        if path[-2] == path[-1] == direction:
            visited.remove(pos)
            return best_option

    new_pos = move(pos, direction)
    if pos_in_range(grid, new_pos) and new_pos not in visited:
        path.append(direction)
        best_option = min(best_option, search(grid, new_pos, direction, path, visited, distance + grid[new_pos]))
    visited.remove(pos)
    return best_option

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[int(c) for c in line.strip()] for line in f.readlines()])

    print(grid)
    pos = (0, 0)
    for direction in [D.RIGHT, D.DOWN]:
        print(search(grid, pos, direction, [], set(), 0))
    
    # --- SOLUTION CODE ---
    return 0

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
