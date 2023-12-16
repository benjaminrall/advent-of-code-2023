# Useful imports
import math
import numpy as np
from enum import Enum

# The expected result from the test input, if using a test input
TEST_RESULT = 46

class D(Enum):
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8

def move(pos, direction):
    if direction == D.UP:
        return (pos[0] - 1, pos[1])
    if direction == D.DOWN:
        return (pos[0] + 1, pos[1])
    if direction == D.LEFT:
        return (pos[0], pos[1] - 1)
    if direction == D.RIGHT:
        return (pos[0], pos[1] + 1)
    
grid_mapping = {'.': 0, '/': 1, '\\': 2, '|': 3, '-': 4}
split_condition = {D.DOWN: 4, D.UP: 4, D.LEFT: 3, D.RIGHT: 3}
first_reflection = {D.UP: D.RIGHT, D.DOWN: D.LEFT, D.LEFT: D.DOWN, D.RIGHT: D.UP}
second_reflection = {D.UP: D.LEFT, D.DOWN: D.RIGHT, D.LEFT: D.UP, D.RIGHT: D.DOWN}
split = {D.UP: (D.LEFT, D.RIGHT), D.DOWN: (D.LEFT, D.RIGHT), D.LEFT: (D.UP, D.DOWN), D.RIGHT: (D.UP, D.DOWN)}

def pos_in_range(grid, pos):
    if 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]:
        return True
    return False

def follow_beam(grid, pos, direction, beams):
    while grid[pos] != split_condition[direction]:
        if grid[pos] == 1:
            direction = first_reflection[direction]
        elif grid[pos] == 2:
            direction = second_reflection[direction]

        if (beams[pos] & direction) != 0:
            return
        beams[pos] |= direction

        pos = move(pos, direction)
        if not pos_in_range(grid, pos):
            return
    
    for new_direction in split[direction]:
        if (beams[pos] & new_direction) != 0:
            return
        beams[pos] |= new_direction

        new_pos = move(pos, new_direction)
        if pos_in_range(grid, new_pos):
            follow_beam(grid, new_pos, new_direction, beams)
    

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[grid_mapping[c] for c in line.strip()] for line in f.readlines()])

    # --- SOLUTION CODE ---
    beams = np.array([[0 for _ in range(grid.shape[1])] for _ in range(grid.shape[0])])
    follow_beam(grid, (0, 0), D.RIGHT, beams)
    return len(np.where(beams != 0)[0])

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
