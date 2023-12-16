# Useful imports
import math
import numpy as np
import re
from itertools import combinations
from functools import cache

# The expected result from the test input, if using a test input
TEST_RESULT = 525152

@cache
def count(line, groups, group_size=0):
    # Base case - counts a valid arrangement if 
    # all groups are completely used up 
    L = len(groups)
    if len(line) == 0:
        return int(
            (L == 0 and group_size == 0) or 
            (L == 1 and groups[0] == group_size)
        )
    
    c = line[0]
    group = groups[0] if L > 0 else 0

    match c:
        case '.':
            if group_size == group:
                return count(line[1:], groups[1:])
            elif group_size == 0:
                return count(line[1:], groups)
            return 0
        case '#':
            if group_size >= group:
                return 0
            return count(line[1:], groups, group_size + 1)
        case '?':
            return count('.' + line[1:], groups, group_size) \
                 + count('#' + line[1:], groups, group_size)
    return 0        

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    # --- CODE IMPLEMENTATION ---
    total = 0
    for line in lines:
        i, groups = line.split()
        i = '?'.join([i for _ in range(5)])
        groups = [int(c) for _ in range(5) for c in groups.split(',')]
        total += count(i, tuple(groups))

    # Returns the result of solving the given input
    return total





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
