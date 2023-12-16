# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 1320

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()][0]

    if debug: print(lines)

    total = 0
    for string in lines.split(','):
        value = 0
        for c in string:
            value += ord(c)
            value *= 17
            value = value % 256
        total += value


    # --- SOLUTION CODE ---
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
