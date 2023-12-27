# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 2
RANGE_LOW = 7
RANGE_HIGH = 27

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [[np.array(list(map(int, c.split(',')[:-1]))) for c in line.strip().split('@')] for line in f.readlines()]

    # 19 - 2t = 18 - s
    # 13 + t = 19 - s
    # 1 = 2t - s
    # -6 = -t - s
    # ( 2 -1)( t )   (  1 )
    # (-1 -1)( s ) = ( -6 )

    total = 0
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            p1, v1 = lines[i]
            p2, v2 = lines[j]

            A = np.vstack((-v1, v2)).T
            B = (p1 - p2)[:, None]

            try:
                X = np.linalg.inv(A) @ B
            except:
                continue

            if (X < 0).any():
                continue

            t = X[0, 0]
            intersect = p1 + t * v1
            if (intersect < RANGE_LOW).any() or (intersect > RANGE_HIGH).any():
                continue

            total += 1

    # --- SOLUTION CODE ---
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    RANGE_LOW = 200000000000000
    RANGE_HIGH = 400000000000000
    result = solve("input.txt")
    print(result)
