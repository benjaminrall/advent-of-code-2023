# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = None




# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    # Prints lines to ensure input is being read correctly
    if debug: print(lines)

    # --- CODE IMPLEMENTATION ---



    # Returns the result of solving the given input
    return 0





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
