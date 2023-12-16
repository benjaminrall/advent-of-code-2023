# Useful imports
import math
import numpy as np
from enum import Enum

# The expected result from the test input, if using a test input
TEST_RESULT = 8

class D(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

SYMBOLS = ['|', '-', 'L', 'J', '7', 'F']
TRANSLATIONS = {
    # (Tile, Current Direction): Direction after leaving
    ('|', D.UP): D.UP, ('|', D.DOWN): D.DOWN, ('|', D.LEFT): D.NONE, ('|', D.RIGHT): D.NONE,
    ('-', D.UP): D.NONE, ('-', D.DOWN): D.NONE, ('-', D.LEFT): D.LEFT, ('-', D.RIGHT): D.RIGHT,
    ('L', D.UP): D.NONE, ('L', D.DOWN): D.RIGHT, ('L', D.LEFT): D.UP, ('L', D.RIGHT): D.NONE,
    ('J', D.UP): D.NONE, ('J', D.DOWN): D.LEFT, ('J', D.LEFT): D.NONE, ('J', D.RIGHT): D.UP,
    ('7', D.UP): D.LEFT, ('7', D.DOWN): D.NONE, ('7', D.LEFT): D.NONE, ('7', D.RIGHT): D.DOWN,
    ('F', D.UP): D.RIGHT, ('F', D.DOWN): D.NONE, ('F', D.LEFT): D.DOWN, ('F', D.RIGHT): D.NONE,
    ('.', D.UP): D.NONE, ('.', D.DOWN): D.NONE, ('.', D.LEFT): D.NONE, ('.', D.RIGHT): D.NONE
}
START_DIRECTION = {'|': D.UP, '-': D.LEFT, 'L': D.UP, 'J': D.LEFT, '7': D.LEFT, 'F': D.DOWN}

def move(pos, direction):
    match direction:
        case D.NONE:
            return pos
        case D.UP:
            return (pos[0] - 1, pos[1])
        case D.DOWN:
            return (pos[0] + 1, pos[1])
        case D.LEFT:
            return (pos[0], pos[1] - 1)
        case D.RIGHT:
            return (pos[0], pos[1] + 1)


# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [[c for c in line.strip()] for line in f.readlines()]    

    # --- CODE IMPLEMENTATION ---
    grid = np.array(lines)
    if debug: print(grid)
    s_type = None
    start_where = np.where(grid == 'S')
    s_pos = (start_where[0][0], start_where[1][0])
    
    for symbol in SYMBOLS:
        distance = 1
        current_direction = START_DIRECTION[symbol]
        current_pos = move(s_pos, current_direction)
        while current_direction != D.NONE and current_pos != s_pos:
            distance += 1
            current_direction = TRANSLATIONS[(grid[current_pos], current_direction)]
            current_pos = move(current_pos, current_direction)
        if current_pos == s_pos:
            s_type = symbol
            return distance // 2

    

    # Returns the result of solving the given input
    return 0





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
