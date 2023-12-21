# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 952408144115
from skimage.morphology import flood_fill


def move(pos, direction, amount):
    match direction:
        case 'U':
            return (pos[0] - amount, pos[1])
        case 'D':
            return (pos[0] + amount, pos[1])
        case 'L':
            return (pos[0], pos[1] - amount)
        case 'R':
            return (pos[0], pos[1] + amount)
        
def convert_hex_instruction(i):
    direction = 0
    if i[7] == '0':
        direction = 'R'
    elif i[7] == '1':
        direction = 'D'
    elif i[7] == '2':
        direction = 'L'
    elif i[7] == '3':
        direction = 'U'

    magnitude = int(i[2:7], 16)
    
    return (direction, magnitude)

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        instructions = [convert_hex_instruction(line.strip().split()[-1]) for line in f.readlines()]

    instructions = [[i[0], int(i[1])] for i in instructions]
    pos = [0, 0]

    ps = []
    for i in instructions:
        pos = move(pos, i[0], int(i[1]))
        ps.append(pos)

    A = 0
    for i, _ in enumerate(ps):
        A += ps[i - 1][0] * ps[i][1] - ps[i][0] * ps[i - 1][1]
        A += -(abs(ps[i - 1][0] - ps[i][0]) + abs(ps[i - 1][1] - ps[i][1]))
    
    
    # --- SOLUTION CODE ---
    return int(abs(A / 2)) + 1

import sys
np.set_printoptions(threshold=sys.maxsize)

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
