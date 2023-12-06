# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 71503

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        t = int(f.readline()[10:].replace(" ", ""))
        d = int(f.readline()[10:].replace(" ", ""))

    # --- SOLUTION CODE ---
    x = math.ceil((t - math.sqrt(t * t - 4 * d)) / 2 + 1e-10)
    return t - 2 * x + 1

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
