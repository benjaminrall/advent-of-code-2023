# Useful imports
import math
import numpy as np
import sys
from collections import defaultdict
np.set_printoptions(threshold=sys.maxsize)

# The expected result from the test input, if using a test input
TEST_RESULT = 167004
STEPS = 500

directions = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]

def calculate_grid_steps(grid, positions, steps, gpos, handled_grids: set):
    new_considerations = []
    new_grid_steps = {}
    new_grids = defaultdict(lambda : defaultdict(lambda : []))

    cycles = {}

    for pos in positions[-1]:
        grid[pos] = 2
    for step in range(steps):
        w = np.where(grid == 2)
        gtup = tuple(map(tuple, grid))
        if gtup not in cycles:
            cycles[gtup] = step
        else:
            if steps % 2 == cycles[gtup] % 2:
                break
        for y, x in zip(w[0], w[1]):
            for direction in directions:
                ny, nx = np.array([y, x]) + direction
                if 0 <= ny and ny < grid.shape[0] and 0 <= nx and nx < grid.shape[1]:
                    if grid[ny, nx] == 0:
                        grid[ny, nx] = 2
                else:
                    g = (gpos[0] + ny // grid.shape[0], gpos[1] + nx // grid.shape[1])
                    if g not in handled_grids:
                        if g not in new_grid_steps:
                            new_grid_steps[g] = steps - step - 1
                        gstep = step - (steps - new_grid_steps[g])
                        new_grids[g][gstep].append((ny % grid.shape[0], nx % grid.shape[1]))
            grid[y, x] = 0
        for pos in positions[step]:
            grid[pos] = 2

    for g in new_grid_steps:
        handled_grids.add(g)
        new_considerations.append((new_grids[g], new_grid_steps[g], g))
    
    # if comp is not None:
    #     print(grid)
    #     print(comp)
    #     print(grid == comp)
    return len(np.where(grid == 2)[0]), new_considerations

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[1 if c == '#' else 0 if c == '.' else 2 for c in line.strip()] for line in f.readlines()])


    sy, sx = np.where(grid == 2)
    sy = sy[0]
    sx = sx[0]

    grid[sy, sx] = 0

    # print(grid)
    m = 5
    egrid = np.zeros((grid.shape[0] * m, grid.shape[1] * m), dtype=int)
    
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            for ym in range(m):
                for xm in range(m):
                    egrid[y + grid.shape[0] * ym, x + grid.shape[1] * xm] = grid[y, x]

    sy2 = sy + grid.shape[0] * (m // 2)
    sx2 = sx + grid.shape[1] * (m // 2)

    s2pos = defaultdict(lambda : [])
    s2pos[-1].append((sy2, sx2))
    #print(calculate_grid_steps(egrid, s2pos, STEPS, (0, 0), set(), None)[0])

    

    spos = defaultdict(lambda : [])
    spos[-1].append((sy, sx))
    total_reachable = 0
    handled_grids = set([(0, 0)])
    left_to_calculate = [[grid.copy(), spos, STEPS, (0, 0), handled_grids]]
    grid_cache = {}
    while len(left_to_calculate) > 0:
        print(f" {len(left_to_calculate)}, {left_to_calculate[0][2]}", end='\r')
        current = left_to_calculate.pop(0)
        #current.append(egrid[slice_pos[0] * grid.shape[0]:(slice_pos[0] + 1) * grid.shape[0], slice_pos[1] * grid.shape[1]:(slice_pos[1] + 1) * grid.shape[1]])
        v, expansions = calculate_grid_steps(*current)
        total_reachable += v
        for expansion in expansions:
            left_to_calculate.append([grid.copy(), expansion[0], expansion[1], expansion[2], handled_grids])

    # --- SOLUTION CODE ---
    return total_reachable

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    STEPS = 26501365
    result = solve("input.txt")
    print(result)
