# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 374


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [[1 if c == '#' else 0 for c in line.strip()] for line in f.readlines()]

    # Prints lines to ensure input is being read correctly
    if debug: print(lines)

    # --- CODE IMPLEMENTATION ---
    # Expansion of galaxy
    galaxies = np.array(lines)
    expansion_rows = []
    expansion_cols = []
    for i, row in enumerate(lines):
        if sum(row) == 0:
            expansion_rows.append(i)
    for i, col in enumerate(zip(*lines)):
        if sum(col) == 0:
            expansion_cols.append(i)
    galaxies = np.insert(galaxies, expansion_rows, 0, 0)
    galaxies = np.insert(galaxies, expansion_cols, 0, 1)

    galaxy_pos = []
    for i, row in enumerate(galaxies):
        for j, elem in enumerate(row):
            if elem == 1:
                galaxy_pos.append((i, j))
    
    total = 0
    for i in range(len(galaxy_pos) - 1):
        for j in range(i + 1, len(galaxy_pos)):
            total += distance(galaxy_pos[i], galaxy_pos[j])

    # Returns the result of solving the given input
    return total





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
