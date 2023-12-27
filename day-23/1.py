# Useful imports
import math
import numpy as np
from enum import Enum

# The expected result from the test input, if using a test input
TEST_RESULT = 94

class D(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def move(pos: tuple[int, int], direction: D):
    if direction == D.UP:
        return (pos[0] - 1, pos[1])
    if direction == D.DOWN:
        return (pos[0] + 1, pos[1])
    if direction == D.LEFT:
        return (pos[0], pos[1] - 1)
    if direction == D.RIGHT:
        return (pos[0], pos[1] + 1)
    
def pos_in_grid(grid, pos):
    return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]
    
NEXT = {
    D.UP: [D.UP, D.LEFT, D.RIGHT],
    D.DOWN: [D.DOWN, D.LEFT, D.RIGHT],
    D.LEFT: [D.UP, D.DOWN, D.LEFT],
    D.RIGHT: [D.RIGHT, D.UP, D.DOWN],
}
DIRECTIONS = [D.UP, D.DOWN, D.LEFT, D.RIGHT]

def search(grid, end, pos, direction, length):
    while True:
        next_pos = []
        for d in NEXT[direction] if grid[pos] == 0 else [direction]:
            new_pos = move(pos, d)
            if not pos_in_grid(grid, new_pos) or grid[new_pos] == -1:
                continue
            elif grid[new_pos] == 0:
                next_pos.append((new_pos, d, length + 1))
            elif grid[new_pos] == 1 and (d == D.DOWN or d == D.RIGHT):
                new_pos = move(new_pos, d)
                next_pos.append((new_pos, d, length + 2))

        if len(next_pos) > 1:
            return next_pos
        
        pos, direction, length = next_pos[0]
        if pos == end:
            return [(end, d, length)]
        
# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[-1 if c == '#' else 0 if c == '.' else 1 for c in line.strip()] for line in f.readlines()])

    # --- SOLUTION CODE ---
    start_pos = (0, np.where(grid[0] == 0)[0][0])
    start_direction = D.DOWN
    end_pos = (grid.shape[0] - 1, np.where(grid[-1] == 0)[0][0])

    from collections import defaultdict
    distances = defaultdict(lambda : 0)
    queue = [(start_pos, start_direction, 0)]
    while queue:
        v = queue.pop(0)
        #print(v)
        for new_v in search(grid, end_pos, *v):
            distances[new_v[0]] = max(new_v[2], distances[new_v[0]])
            if new_v[0] != end_pos:
                queue.append(new_v)
                
    return distances[end_pos]

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
