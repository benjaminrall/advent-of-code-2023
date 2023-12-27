# Useful imports
import math
import numpy as np
from decimal import Decimal

# The expected result from the test input, if using a test input
TEST_RESULT = 47
MIN_X_RANGE = -10
MAX_X_RANGE = 10
MIN_Y_RANGE = -10
MAX_Y_RANGE = 10
MIN_Z_RANGE = -10
MAX_Z_RANGE = 10

def get(P, V, t):
    return P + t * V

def point_intersect(line, point):
    p, v = line
    pd = point - p
    t = pd[v != 0] / v[v != 0]
    return (len(t) == 0 or np.isclose(t, t[0]).all()) and (np.isclose(pd[v == 0], v[v == 0], 1, 1e-1)).all()

def intersect(line1, line2):
    p1, v1 = line1
    p2, v2 = line2

    A = np.vstack((-v1, v2)).T
    B = (p1 - p2)[:, None]

    try:
        X = np.linalg.inv(A) @ B
    except:
        return None, 0

    if (X < 0).any():
        return None, 0

    t = X[0, 0]
    intersect = get(p1, v1, t)
    
    return intersect, t

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [[np.array(list(map(int, c.split(',')))) for c in line.strip().split('@')] for line in f.readlines()]

    print(lines)

    possible_rock_xys = []
    for x in range(MIN_X_RANGE, MAX_X_RANGE + 1):
        for y in range(MIN_Y_RANGE, MAX_Y_RANGE + 1):
            print(f"Checked: {x} {y}  ", end='\r')
            vr = np.array([x, y])
            p1, v1 = lines[0]
            p2, v2 = lines[1]

            i, t = intersect([p1[:-1], v1[:-1] - vr], [p2[:-1], v2[:-1] - vr])
            valid = False
            if i is not None:
                valid = True
                for line in range(2, len(lines)):
                    pi, vi = lines[line]
                    if not point_intersect([pi[:-1], vi[:-1] - vr], i):
                        valid = False
                        break
            if valid:
                possible_rock_xys.append((np.array([x, y]), round(t)))
                print(f"V: {x}, {y}, {i}, {t}        ")
            
    for possibility, t in possible_rock_xys:
        for z in range(MIN_Z_RANGE, MAX_Z_RANGE + 1):
            vr = np.array([possibility[0], possibility[1], z])

            p, v = lines[0]
            i = get(p, v - vr, t)
            
            valid = False
            if i is not None:
                valid = True
                for line in range(2, len(lines)):
                    pi, vi = lines[line]
                    if not point_intersect([pi, vi - vr], i):
                        valid = False
                        break
            if valid:
                return np.sum(i)


    # --- SOLUTION CODE ---
    return 0

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    MIN_X_RANGE = -300
    MAX_X_RANGE = 300
    MIN_Y_RANGE = -300
    MAX_Y_RANGE = 300
    MIN_Z_RANGE = -300
    MAX_Z_RANGE = 300
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
