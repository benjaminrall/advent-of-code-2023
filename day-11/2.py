# Useful imports
import math
import numpy as np
from bisect import bisect

# The expected result from the test input, if using a test input
TEST_RESULT = None
EXPANSION = 1000000

def distance(pos1, pos2, er, ec):
    pos1_e = (bisect(er, pos1[0]), bisect(ec, pos1[1]))
    pos2_e = (bisect(er, pos2[0]), bisect(ec, pos2[1]))
    diff_e = abs(pos1_e[0] - pos2_e[0]) + abs(pos1_e[1] - pos2_e[1])
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + diff_e * (EXPANSION - 1)

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [[1 if c == '#' else 0 for c in line.strip()] for line in f.readlines()]

    # --- CODE IMPLEMENTATION ---
    # Expansion of galaxy
    galaxies = np.array(lines)
    galaxy_pos = np.argwhere(galaxies == 1)

    expansion_rows = np.where(np.all(galaxies == 0, axis=1))[0]
    expansion_cols = np.where(np.all(galaxies == 0, axis=0))[0]

    total = 0
    for i in range(len(galaxy_pos) - 1):
        for j in range(i + 1, len(galaxy_pos)):
            total += distance(galaxy_pos[i], galaxy_pos[j], expansion_rows, expansion_cols)

    # Returns the result of solving the given input
    return total


# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
