# Useful imports
import math
from copy import deepcopy
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 7

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    if debug: print(lines)

    maxes = [0, 0, 0]
    cubes = []
    for line in lines:
        start, end = line.split('~')
        start = [int(v) for v in start.split(',')]
        end = [int(v) for v in end.split(',')]
        for i in range(3):
            maxes[i] = max(maxes[i], start[i], end[i])
        cubes.append((start, end))
    maxes = np.array(maxes) + 1
    grid = np.zeros(maxes, dtype=int)
    
    cubes.sort(key=lambda x:x[0][2])
    grid[0:maxes[0], 0:maxes[1], 0] = 1
    for i, cube in enumerate(cubes):
        start, end = cube
        grid[start[0]:end[0] + 1, start[1]:end[1] + 1, start[2]:end[2] + 1] = i + 2

    print(grid)

    for cube in range(2, len(cubes) + 2):
        xs, ys, zs = np.where(grid == cube)
        can_move = True
        while True:
            for pos in zip(xs, ys, zs - 1):
                if grid[pos] != 0 and grid[pos] != cube:
                    can_move = False
                    break
            if not can_move:
                break
            for pos, new_pos in zip(zip(xs, ys, zs), zip(xs, ys, zs - 1)):
                grid[pos] = 0
                grid[new_pos] = cube
            zs -= 1
    
    from collections import defaultdict
    supported_by = defaultdict(lambda : set())
    supports = defaultdict(lambda : set())
    for cube in range(len(cubes) + 1, 1, -1):
        xs, ys, zs = np.where(grid == cube)
        for pos in zip(xs, ys, zs - 1):
            if grid[pos] != 0 and grid[pos] != cube:
                supported_by[cube].add(grid[pos])
                supports[grid[pos]].add(cube)

    free = set()
    for cube in range(2, len(cubes) + 2):
        s = supports[cube]
        other_supports = True
        for ncube in s:
            if len(supported_by[ncube]) == 1:
                other_supports = False
                break
        if other_supports:
            free.add(cube)
    
    total = 0
    for cube in range(2, len(cubes) + 2):
        if cube not in free:
            disintegrated = set()
            queue = [cube]
            sby = deepcopy(supported_by)
            while queue:
                v = queue.pop(0)
                for c in supports[v]:
                    sby[c].remove(v)
                    if len(sby[c]) == 0 and c not in disintegrated:
                        disintegrated.add(c)
                        queue.append(c)
            total += len(disintegrated)
    
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
