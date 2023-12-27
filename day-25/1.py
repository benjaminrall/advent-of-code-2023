# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 54

def get_cut(graph: dict, subset: set):
    cut_size = 0
    for node in subset:
        for neighbour in graph[node]:
            if neighbour not in subset:
                cut_size += 1
    return cut_size

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [[c.strip() for c in line.strip().split(':')] for line in f.readlines()]

    from collections import defaultdict
    graph = defaultdict(lambda : set())
    for line in lines:
        for connected in line[1].split(' '):
            graph[line[0]].add(connected)
            graph[connected].add(line[0])
    
    nodes = [k for k in graph]

    subset = set(nodes[:1])

    while get_cut(graph, subset) != 3:
        best_cut = math.inf
        best_neighbour = None
        for node in subset:
            for neighbour in graph[node]:
                if neighbour not in subset:
                    subset.add(neighbour)
                    cut = get_cut(graph, subset)
                    subset.remove(neighbour)

                    if cut < best_cut:
                        best_cut = cut
                        best_neighbour = neighbour
        subset.add(best_neighbour)

    

    # --- SOLUTION CODE ---
    return len(subset) * (len(nodes) - len(subset))

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
