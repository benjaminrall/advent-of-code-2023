# Useful imports
import math
import numpy as np
import copy

# The expected result from the test input, if using a test input
TEST_RESULT = 167409079868000


def split_interval_gt(interval, split):
    if interval[0] > split:
        return interval, None
    if interval[1] <= split:
        return None, interval
    moved_interval = (split + 1, interval[1])
    kept_interval = (interval[0], split)
    return moved_interval, kept_interval

def split_interval_lt(interval, split):
    if interval[1] < split:
        return interval, None
    if interval[0] >= split:
        return None, interval
    moved_interval = (interval[0], split - 1)
    kept_interval = (split, interval[1])
    return moved_interval, kept_interval

def parse_rule(intervals, rule: tuple[str, str]):
    if rule[0] is None:
        return rule[1], intervals, None
    if rule[0].find('>') > 0:
        i, v = rule[0].split('>')
        interval = intervals[i]
        moved_interval, kept_interval = split_interval_gt(interval, int(v))
        kept_intervals = copy.copy(intervals)
        intervals[i] = moved_interval
        kept_intervals[i] = kept_interval
        return rule[1], intervals, kept_intervals
    if rule[0].find('<') > 0:
        i, v = rule[0].split('<')
        interval = intervals[i]
        moved_interval, kept_interval = split_interval_lt(interval, int(v))
        kept_intervals = copy.copy(intervals)
        intervals[i] = moved_interval
        kept_intervals[i] = kept_interval
        return rule[1], intervals, kept_intervals
    
    return None, None, intervals
    

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
    
    start_intervals = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

    accepted = []
    queue = [('in', start_intervals)]
    while len(queue) > 0:
        workflow, intervals = queue.pop(0)
        for rule in workflows[workflow]:
            output, moved, intervals = parse_rule(intervals, rule)
            if moved is not None:
                if output == 'A':
                    accepted.append(moved)
                elif output == 'R':
                    pass
                else:
                    queue.append((output, moved))
            if intervals is None:
                break

    total = 0
    for ranges in accepted:
        possibilities = 1
        for key in ranges:
            interval = ranges[key]
            possibilities *= interval[1] - interval[0] + 1
        total += possibilities

    return total

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
