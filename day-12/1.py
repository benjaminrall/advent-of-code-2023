# Useful imports
import math
import numpy as np
import re
from itertools import combinations

# The expected result from the test input, if using a test input
TEST_RESULT = 21




# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    inputs = []
    patterns = []
    for line in lines:
        i, counts = line.split()
        inputs.append((['1' if c == '#' else '0' for c in i], sum([int(n) for n in counts.split(',')]) - i.count('#'), [n for n in range(len(i)) if i[n] == '?']))
        patterns.append(re.compile(r'0*' + r'0+'.join([rf'1{{{n}}}' for n in counts.split(',')]) + r'0*'))
    
    # --- CODE IMPLEMENTATION ---
    total = 0
    for i, pattern in zip(inputs, patterns):
        k, c, missing = i
        for combo in combinations(missing, c):
            for choice in combo:
                k[choice] = '1'
            if pattern.fullmatch(''.join(k)):
                total += 1
            for choice in combo:
                k[choice] = '0'


    # Returns the result of solving the given input
    return total





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
