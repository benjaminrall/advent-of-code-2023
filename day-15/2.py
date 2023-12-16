# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 145

def hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value = (value * 17) % 256
    return value

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()][0]

    if debug: print(lines)

    total = 0

    boxes = [{} for _ in range(256)]

    for instruction in lines.split(','):
        if '=' in instruction:
            label, focal = instruction.split('=')
            value = hash(label)
            boxes[value][label] = int(focal)
        else:
            label = instruction[:-1]
            value = hash(label)
            if label in boxes[value]:
                boxes[value].pop(label)

    total = 0
    for box in range(256):
        for i, key in enumerate(boxes[box].keys()):
            total += (box + 1) * (i + 1) * boxes[box][key]


    # --- SOLUTION CODE ---
    return total    

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
