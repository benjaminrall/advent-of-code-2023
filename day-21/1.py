# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 16
STEPS = 6

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[1 if c == '#' else 0 if c == '.' else 2 for c in line.strip()] for line in f.readlines()])


    print(grid)
    print(np.where(grid == 2))


    for step in range(STEPS):
        w = np.where(grid == 2)
        for y, x in zip(w[0], w[1]):
            if 0 <= y - 1 < grid.shape[0]:
                if grid[y - 1, x] == 0:
                    grid[y - 1, x] = 2 
            if 0 <= x - 1 < grid.shape[1]:
                if grid[y, x - 1] == 0:
                    grid[y, x - 1] = 2 
            if 0 <= y + 1 < grid.shape[0]:
                if grid[y + 1, x] == 0:
                    grid[y + 1, x] = 2 
            if 0 <= x + 1 < grid.shape[1]:
                if grid[y, x + 1] == 0:
                    grid[y, x + 1] = 2 
            grid[y, x] = 0
        print(grid)

    # --- SOLUTION CODE ---
    return len(np.where(grid == 2)[0])

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    STEPS = 64
    result = solve("input.txt")
    print(result)
