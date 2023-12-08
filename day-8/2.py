# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 6

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    if debug: 
        print(lines)

    instructions = [0 if c == 'L' else 1 for c in lines[0]]
    visited = set()
    nodes = {}
    starting_nodes = []
    for node in lines[2:]:
        if node[:3].endswith('A'):
            starting_nodes.append(node[:3])
        nodes[node[:3]] = [node[7:10], node[12:15]]

    total_steps = []

    for starting_node in starting_nodes:
        instruction_position = 0
        steps = 0
        current_node = starting_node

        # --- SOLUTION CODE ---
        while not current_node.endswith('Z'):
            if current_node in visited and instruction_position == 0:
                break
            if instruction_position == 0:
                visited.add(current_node)
            current_node = nodes[current_node][instructions[instruction_position]]
            instruction_position = (instruction_position + 1) % len(instructions)
            steps += 1
        total_steps.append(steps)

    return math.lcm(*total_steps)

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
