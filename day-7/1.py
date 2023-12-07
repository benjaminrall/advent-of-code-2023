# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 6440

STRENGTHS = {n: i for i, n in enumerate('23456789TJQKA')}

def get_rank(card):
    counts = [0 for _ in range(13)]
    for c in card:
        counts[c] += 1
    if 5 in counts:
        return 7
    if 4 in counts:
        return 6
    if 3 in counts:
        return 5 if 2 in counts else 4
    if counts.count(2) == 2:
        return 3
    if 2 in counts:
        return 2
    return 1

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
        for i, line in enumerate(lines):
            lines[i][0] = [STRENGTHS[c] for c in line[0]]
            lines[i][1] = int(line[1])

    if debug: 
        print(lines)

    # --- SOLUTION CODE ---
    lines.sort(key=lambda x : (get_rank(x[0]), x[0]))
    total = 0
    for line, rank in zip(lines, range(1, len(lines) + 1)):
        total += rank * line[1]

    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
