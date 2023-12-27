# Useful imports
import math
import numpy as np
from enum import Enum
from queue import PriorityQueue

# The expected result from the test input, if using a test input
TEST_RESULT = 94

class D(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

TURNS = {
    0: [2, 3],
    1: [2, 3],
    2: [0, 1],
    3: [0, 1],
}

def pos_in_grid(pos, grid):
    return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]

def move_pos(pos, direction):
    match direction:
        case 0:
            return (pos[0] - 1, pos[1])
        case 1:
            return (pos[0] + 1, pos[1])
        case 2:
            return (pos[0], pos[1] - 1)
        case 3:
            return (pos[0], pos[1] + 1)
    return None

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[int(c) for c in line.strip()] for line in f.readlines()])

    print(grid)

    start = (0, 0)
    end = (grid.shape[0] - 1, grid.shape[1] - 1)

    print(start, end)

    indices = [(row, col) for row in range(grid.shape[0]) for col in range(grid.shape[1])]
    from collections import defaultdict
    distances = defaultdict(lambda : math.inf)
    open_nodes = PriorityQueue()
    closed_nodes = set()
    start_node = ((0, 0), 1, 0)
    start_node_2 = ((0, 0), 3, 0)
    distances[start_node] = 0
    distances[start_node_2] = 0
    open_nodes.put((distances[start_node], start_node))
    open_nodes.put((distances[start_node_2], start_node_2))

    while open_nodes.qsize() > 0:
        dist, node = open_nodes.get()
        pos, direction, consecutive = node

        if node in closed_nodes:
            continue

        closed_nodes.add(node)

        if pos == end and consecutive >= 4:
            return dist

        neighbours = []
        if consecutive < 10:
            neighbours.append((direction, consecutive + 1))
        if consecutive >= 4 and consecutive <= 10:
            neighbours.extend([(d, 1) for d in TURNS[direction]])

        for d, c in neighbours:
            new_pos = move_pos(pos, d)

            if not pos_in_grid(new_pos, grid):
                continue

            new_node = (new_pos, d, c)

            if new_node in closed_nodes:
                continue
            
            alt = dist + grid[new_pos]


            if alt < distances[new_node]:
                distances[new_node] = alt
                open_nodes.put((distances[new_node], new_node))

    # --- SOLUTION CODE ---
    return 0

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
