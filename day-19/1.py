# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 19114

def parse_rule(part, rule: tuple[str, str]):
    if rule[0] is None:
        return rule[1]
    if rule[0].find('>') > 0:
        i, v = rule[0].split('>')
        if part[i] > int(v):
            return rule[1]
    if rule[0].find('<') > 0:
        i, v = rule[0].split('<')
        if part[i] < int(v):
            return rule[1]
    return None

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        ws, ps = [[c for c in line.strip().split('\n')] for line in f.read().split('\n\n')]

    workflows = {}
    for workflow in ws:
        identifier = workflow[:workflow.index('{')]
        rules = workflow[workflow.index('{') + 1:-1].split(',')
        for i in range(len(rules)):
            spl = rules[i].split(':')
            if len(spl) == 2:
                rules[i] = spl
            else:
                rules[i] = [None, rules[i]]
        workflows[identifier] = rules
    
    parts = []
    for part in ps:
        parts.append({i: int(v) for i, v in [c.split('=') for c in part[1:-1].split(',')]})
    
    total = 0
    for part in parts:
        current_workflow = 'in'
        while True:
            for rule in workflows[current_workflow]:
                output = parse_rule(part, rule)
                if output is not None:
                    current_workflow = output
                    break
            if current_workflow == 'R':
                break
            elif current_workflow == 'A':
                for k in part:
                    total += part[k]
                break

    # --- SOLUTION CODE ---
    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
