# Useful imports
import math
import numpy as np
from enum import Enum
from functools import cache

# The expected result from the test input, if using a test input
TEST_RESULT = 154

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

def get_links(grid, start_pos, end):
    connections = []
    for direction in DIRECTIONS:
        pos = move(start_pos, direction)
        if not pos_in_grid(grid, pos) or grid[pos] == -1:
            continue

        length = 1
        found_connection = True

        while True:
            next_positions = []
            for d in NEXT[direction]:
                new_pos = move(pos, d)
                if not pos_in_grid(grid, new_pos) or grid[new_pos] == -1:
                    continue
                next_positions.append((new_pos, d, length + 1))
  
            if len(next_positions) == 0:
                found_connection = False
                break
            if len(next_positions) > 1:
                break

            pos, direction, length = next_positions[0]
            if pos == end:
                break

        if found_connection:
            connections.append((pos, length))

    return connections

@cache
def search(grid, end, pos, direction, length: int = 0, visited: set = set(), depth: int = 0):
    while True:
        next_positions = []
        for d in NEXT[direction]:
            new_pos = move(pos, d)
            if not pos_in_grid(grid, new_pos) or grid[new_pos] == -1 or new_pos in visited:
                continue
            next_positions.append((new_pos, d, length + 1))
    
        if len(next_positions) == 0:
            return 0
        if len(next_positions) > 1:
            break

        pos, direction, length = next_positions[0]
        if pos == end:
            return length
    
    visited.add(pos)
    for next_pos in next_positions:
        length = max(length, search(grid, end, *next_pos, visited, depth + 1))
    visited.remove(pos)

    return length
        
def search_neighbours(neighbours, end, pos, length = 0, visited: set = set()):
    if pos == end:
        return length

    visited.add(pos)
    lengths = []
    for npos, nlength in neighbours[pos]:
        if npos not in visited:
            lengths.append(search_neighbours(
                neighbours, end, npos, length + nlength, visited
            ))
    visited.remove(pos)

    return max(lengths) if len(lengths) > 0 else 0
# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        grid = np.array([[-1 if c == '#' else 0 for c in line.strip()] for line in f.readlines()])

    # --- SOLUTION CODE ---
    start_pos = (0, np.where(grid[0] == 0)[0][0])
    end_pos = (grid.shape[0] - 1, np.where(grid[-1] == 0)[0][0])

    queue = [start_pos]
    from collections import defaultdict
    visited = set([start_pos])
    neighbours = defaultdict(lambda : [])
    while queue:
        v = queue.pop(0)
        for neighbour in get_links(grid, v, end_pos):
            neighbours[v].append(neighbour)
            if neighbour[0] not in visited:
                visited.add(neighbour[0])
                queue.append(neighbour[0])

    return search_neighbours(neighbours, end_pos, start_pos)

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
