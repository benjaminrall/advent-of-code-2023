# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 400

# Checks whether a given vertical mirror line exists
def check_vertical(puzzle, vi):
    # Values to index puzzle with
    vpos = vi + 1
    limit = min(vpos, puzzle.shape[1] - vpos)

    # Gets both sides of the mirror line
    left = np.fliplr(puzzle[:, vpos - limit:vpos])
    right = puzzle[:, vpos:vpos + limit]

    # Checks if the sides are mirrored
    return np.sum(left != right) == 1

# Checks whether a given horizontal mirror line exists
def check_horizontal(puzzle, hi):
    # Values to index puzzle with
    hpos = hi + 1
    limit = min(hpos, puzzle.shape[0] - hpos)

    # Gets both sides of the mirror line
    up = np.flipud(puzzle[hpos - limit:hpos])
    down = puzzle[hpos:hpos + limit]

    # Checks if the sides are mirrored
    return np.sum(up != down) == 1

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        puzzles = [
            np.array([
                [1 if c == '#' else 0 for c in line] 
                for line in puzzle.split('\n')
            ])
            for puzzle in f.read().strip().split('\n\n')
        ]

    # --- SOLUTION CODE ---
    total = 0
    for puzzle in puzzles:
        # Finds vertical mirrors
        for vi in range(puzzle.shape[1] - 1):
            if check_vertical(puzzle, vi):
                total += vi + 1

        # Finds horizontal mirrors
        for hi in range(puzzle.shape[0] - 1):
            if check_horizontal(puzzle, hi):
                total += (hi + 1) * 100

    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
