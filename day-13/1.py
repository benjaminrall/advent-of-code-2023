# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 405

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    if debug: print(lines)

    # --- SOLUTION CODE ---
    puzzles = []
    puzzle = []
    for line in lines:
        if line == '':
            puzzles.append(np.array(puzzle))
            puzzle = []
        else:
            puzzle.append([1 if c == '#' else 0 for c in line])
    puzzles.append(np.array(puzzle))

    total = 0
    for puzzle in puzzles:
        found = False
        for vertical in range(puzzle.shape[1] - 1):
            stack = []
            for v1 in range(vertical + 1):
                stack.append(puzzle[:, v1])
            valid = True
            for v2 in range(vertical + 1, puzzle.shape[1]):
                if len(stack) == 0:
                    break
                p = stack.pop()
                if not (p == puzzle[:, v2]).all():
                    valid = False
                    break
            if valid:
                found = True
                total += vertical + 1
                break
        if found:
            continue
        for horizontal in range(puzzle.shape[0] - 1):
            stack = []
            for v1 in range(horizontal + 1):
                stack.append(puzzle[v1])
            valid = True
            for v2 in range(horizontal + 1, puzzle.shape[0]):
                if len(stack) == 0:
                    break
                p = stack.pop()
                if not (p == puzzle[v2]).all():
                    valid = False
                    break
            if valid:
                total += 100 * (horizontal + 1)
                break
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
