# Useful imports
import math
import numpy as np
from enum import Enum

# The expected result from the test input, if using a test input
TEST_RESULT = 10

class D(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

SYMBOLS = ['|', '-', 'L', 'J', '7', 'F']
TRANSLATIONS = {
    # (Tile, Current Direction): Direction after leaving
    ('|', D.UP): D.UP, ('|', D.DOWN): D.DOWN, ('|', D.LEFT): D.NONE, ('|', D.RIGHT): D.NONE,
    ('-', D.UP): D.NONE, ('-', D.DOWN): D.NONE, ('-', D.LEFT): D.LEFT, ('-', D.RIGHT): D.RIGHT,
    ('L', D.UP): D.NONE, ('L', D.DOWN): D.RIGHT, ('L', D.LEFT): D.UP, ('L', D.RIGHT): D.NONE,
    ('J', D.UP): D.NONE, ('J', D.DOWN): D.LEFT, ('J', D.LEFT): D.NONE, ('J', D.RIGHT): D.UP,
    ('7', D.UP): D.LEFT, ('7', D.DOWN): D.NONE, ('7', D.LEFT): D.NONE, ('7', D.RIGHT): D.DOWN,
    ('F', D.UP): D.RIGHT, ('F', D.DOWN): D.NONE, ('F', D.LEFT): D.DOWN, ('F', D.RIGHT): D.NONE,
    ('.', D.UP): D.NONE, ('.', D.DOWN): D.NONE, ('.', D.LEFT): D.NONE, ('.', D.RIGHT): D.NONE
}
START_DIRECTION = {'|': D.UP, '-': D.LEFT, 'L': D.UP, 'J': D.LEFT, '7': D.LEFT, 'F': D.DOWN}

def move(pos, direction):
    match direction:
        case D.NONE:
            return pos
        case D.UP:
            return (pos[0] - 1, pos[1])
        case D.DOWN:
            return (pos[0] + 1, pos[1])
        case D.LEFT:
            return (pos[0], pos[1] - 1)
        case D.RIGHT:
            return (pos[0], pos[1] + 1)
        
def project(pos, direction, loop_map, max_dist):
    pos = move(pos, direction)
    prev_val = loop_map[pos]
    while pos[0] >= 0 and pos[1] >= 0 and pos[0] < loop_map.shape[0] and pos[1] < loop_map.shape[1]:
        pos = move(pos, direction)
        new_val = loop_map[pos]
        if new_val == 0:
            return pos
        dist = abs(new_val - prev_val)
        if dist != max_dist and dist > 1:
            return None
        prev_val = new_val
    return None

def project_up(pos, l, r, loop_map, max_dist):
    pos1 = (pos[0], l)
    pos2 = (pos[0], r)
    proj1 = project(pos1, D.UP, loop_map, max_dist)
    if proj1:
        return proj1
    else:
        return project(pos2, D.UP, loop_map, max_dist)
    
def project_down(pos, l, r, loop_map, max_dist):
    pos1 = (pos[0], l)
    pos2 = (pos[0], r)
    proj1 = project(pos1, D.DOWN, loop_map, max_dist)
    if proj1:
        return proj1
    else:
        return project(pos2, D.DOWN, loop_map, max_dist)
    
def project_left(pos, u, d, loop_map, max_dist):
    pos1 = (u, pos[1])
    pos2 = (d, pos[1])
    proj1 = project(pos1, D.LEFT, loop_map, max_dist)
    if proj1:
        return proj1
    else:
        return project(pos2, D.LEFT, loop_map, max_dist)

def project_right(pos, u, d, loop_map, max_dist):
    pos1 = (u, pos[1])
    pos2 = (d, pos[1])
    proj1 = project(pos1, D.RIGHT, loop_map, max_dist)
    if proj1:
        return proj1
    else:
        return project(pos2, D.RIGHT, loop_map, max_dist)


# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # Opens the file and reads the lines into a list
    with open(filename) as f:
        lines = [[c for c in line.strip()] for line in f.readlines()]    

    # --- CODE IMPLEMENTATION ---
    grid = np.array(lines)
    if debug: print(grid)
    s_type = None
    start_where = np.where(grid == 'S')
    s_pos = (start_where[0][0], start_where[1][0])
    
    for symbol in SYMBOLS:
        distance = 1
        loop_map = np.zeros(grid.shape, dtype=int)
        loop_map[s_pos] = distance
        current_direction = START_DIRECTION[symbol]
        current_pos = move(s_pos, current_direction)
        while current_direction != D.NONE and current_pos != s_pos:
            distance += 1
            loop_map[current_pos] = distance
            current_direction = TRANSLATIONS[(grid[current_pos], current_direction)]
            current_pos = move(current_pos, current_direction)
        if current_pos == s_pos:
            max_dist = distance - 1
            grid[current_pos] = symbol
            grid = np.pad(grid, ((1, 1), (1, 1)))
            loop_map = np.pad(loop_map, ((1, 1), (1, 1)))
            print(loop_map)
            loop_map[0, 0] = -1
            frontier = [(0, 0)]
            while len(frontier) > 0:
                v = frontier.pop(0)
                # Regular adjacency cases
                for d in [D.UP, D.DOWN, D.LEFT, D.RIGHT]:
                    vn = move(v, d)
                    if vn[0] < 0 or vn[1] < 0 or vn[0] >= grid.shape[0] or vn[1] >= grid.shape[1]:
                        continue
                    if loop_map[vn] == 0:
                        loop_map[vn] = -1
                        frontier.append(vn)
                        
                
                # Special squeeze cases
                u = v[0] > 0
                d = v[0] < grid.shape[0] - 1
                l = v[1] > 0
                r = v[1] < grid.shape[1] - 1
                if u and d and r:
                    # Check right three
                    mid = move(v, D.RIGHT)
                    mid_n = loop_map[mid]
                    up_n = loop_map[move(mid, D.UP)]
                    down_n = loop_map[move(mid, D.DOWN)]
                    if up_n > 0 and mid_n > 0 and down_n > 0:
                        um_dist = abs(up_n - mid_n)
                        md_dist = abs(mid_n - down_n)
                        if um_dist != max_dist and um_dist > 1:
                            vn = project_right(v, v[0] - 1, v[0], loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                        if md_dist != max_dist and md_dist > 1:
                            vn = project_right(v, v[0], v[0] + 1, loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                if u and d and l:
                    # Check left three
                    mid = move(v, D.LEFT)
                    mid_n = loop_map[mid]
                    up_n = loop_map[move(mid, D.UP)]
                    down_n = loop_map[move(mid, D.DOWN)]
                    if up_n > 0 and mid_n > 0 and down_n > 0:
                        um_dist = abs(up_n - mid_n)
                        md_dist = abs(mid_n - down_n)
                        if um_dist != max_dist and um_dist > 1:
                            vn = project_left(v, v[0] - 1, v[0], loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                        if md_dist != max_dist and md_dist > 1:
                            vn = project_left(v, v[0], v[0] + 1, loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                if l and r and u:
                    # Check upper three
                    mid = move(v, D.UP)
                    mid_n = loop_map[mid]
                    left_n = loop_map[move(mid, D.LEFT)]
                    right_n = loop_map[move(mid, D.RIGHT)]
                    if left_n > 0 and mid_n > 0 and right_n > 0:
                        lm_dist = abs(left_n - mid_n)
                        mr_dist = abs(mid_n - right_n)
                        if lm_dist != max_dist and lm_dist > 1:
                            vn = project_up(v, v[1] - 1, v[1], loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                        if mr_dist != max_dist and mr_dist > 1:
                            vn = project_up(v, v[1], v[1] + 1, loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                if l and r and d:
                    # Check lower three
                    mid = move(v, D.DOWN)
                    mid_n = loop_map[mid]
                    left_n = loop_map[move(mid, D.LEFT)]
                    right_n = loop_map[move(mid, D.RIGHT)]
                    if left_n > 0 and mid_n > 0 and right_n > 0:
                        lm_dist = abs(left_n - mid_n)
                        mr_dist = abs(mid_n - right_n)
                        if lm_dist != max_dist and lm_dist > 1:
                            vn = project_down(v, v[1] - 1, v[1], loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
                        if mr_dist != max_dist and mr_dist > 1:
                            vn = project_down(v, v[1], v[1] + 1, loop_map, max_dist)
                            if vn is not None:
                                frontier.append(vn)
            print(loop_map)
            return len(np.where(loop_map == 0)[0])

    # Returns the result of solving the given input
    return 0





# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
