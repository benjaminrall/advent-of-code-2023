# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 288

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    return math.prod([
        t - 2 * math.ceil((t - math.sqrt(t * t - 4 * d)) / 2 + 1e-10) + 1 
        for t, d in zip(*[
            [int(t) for t in line[10:].split()] 
            for line in open(filename).readlines()
        ])
    ])

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
