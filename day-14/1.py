# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 136

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    if debug: print(lines)

    # --- SOLUTION CODE ---
    rows = len(lines)
    total_load = 0
    limits = [0 for _ in range(len(lines[0]))]
    for row in range(rows):
        for i, c in enumerate(lines[row]):
            if c == 'O':
                total_load += rows - limits[i]
                limits[i] += 1
            elif c == '#':
                limits[i] = row + 1
    return total_load

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
