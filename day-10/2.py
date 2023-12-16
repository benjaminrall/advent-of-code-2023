# Useful imports
import math
import numpy as np
from enum import Enum
from skimage.morphology import flood_fill

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

ENLARGED = {
    '|': [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    '-': [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    'L': [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
    'J': [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    '7': [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
    'F': [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
    '.': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
}

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
    start_where = np.where(grid == 'S')
    s_pos = (start_where[0][0], start_where[1][0])
    
    for symbol in SYMBOLS:
        loop_map = np.zeros((grid.shape[0] * 3, grid.shape[1] * 3))
        current_direction = START_DIRECTION[symbol]
        current_pos = move(s_pos, current_direction)
        if current_pos[0] < 0 or current_pos[1] < 0 or current_pos[1] >= grid.shape[1] or current_pos[0] >= grid.shape[0]:
            continue
        while current_direction != D.NONE and current_pos != s_pos:
            row, col = current_pos[0] * 3, current_pos[1] * 3
            loop_map[row:row+3, col:col+3] = ENLARGED[grid[current_pos]]
            current_direction = TRANSLATIONS[(grid[current_pos], current_direction)]
            current_pos = move(current_pos, current_direction)
            if current_pos[0] < 0 or current_pos[1] < 0 or current_pos[1] >= grid.shape[1] or current_pos[0] >= grid.shape[0]:
                break
        if current_pos == s_pos:
            print(symbol)
            row, col = current_pos[0] * 3, current_pos[1] * 3
            grid[current_pos] = symbol
            loop_map[row:row+3, col:col+3] = ENLARGED[symbol]
            loop_map = flood_fill(loop_map, (0, 0), 2)
            empty = 0
            for r in range(grid.shape[0]):
                for c in range(grid.shape[1]):
                    row, col = r * 3, c * 3
                    if (loop_map[row:row+3, col:col+3] == 0).all():
                        empty += 1
            return empty

    # Returns the result of solving the given input
    return 0





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
