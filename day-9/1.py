# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 2


def find_next_layer(current_layer):
    return [current_layer[i + 1] - current_layer[i] for i in range(len(current_layer) - 1)]


# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]

    # Prints lines to ensure input is being read correctly
    if debug: print(lines)

    # --- CODE IMPLEMENTATION ---
    ns = []
    for sequence in lines:
        layers = [sequence]
        while not all([n == 0 for n in layers[-1]]):
            layers.append(find_next_layer(layers[-1]))

        n = 0
        for layer in reversed(layers[:-1]):
            n = layer[0] - n
        ns.append(n)

    # Returns the result of solving the given input
    return sum(ns)





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
