# Useful imports
import math
import numpy as np

# The expected result from the test input, if using a test input
TEST_RESULT = 32000000

# MODULE : identifier -> (type, outputs)

# Method to solve the input stored in a given file name
def solve(filename: str, debug: bool = False) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    print(lines)

    config = {}
    complements = {}
    states = {}
    for line in lines:
        i, d = line.split(' -> ')
        if i == 'broadcaster':
            config[i] = (0, d.split(', '))
        elif i.startswith('%'):
            config[i[1:]] = (1, d.split(', '))
            states[i[1:]] = 0
        elif i.startswith('&'):
            config[i[1:]] = (2, d.split(', '))
            complements[i[1:]] = {}

    for key in config:
        module = config[key]
        for output in module[1]:
            if output in complements:
                complements[output][key] = 0
    
    low_pulses = 0
    high_pulses = 0
    for press in range(1000):
        low_pulses += 1
        pulse_queue = [('broadcaster', 0)]
        while len(pulse_queue) > 0:
            src, power = pulse_queue.pop(0)
            source_module = config[src]
            for key in source_module[1]:
                if power == 0:
                    low_pulses += 1
                else:
                    high_pulses += 1
                if key not in config:
                    continue
                module = config[key]
                if module[0] == 1 and power == 0:
                    states[key] = int(not states[key])
                    pulse_queue.append((key, states[key]))
                elif module[0] == 2:
                    complements[key][src] = power
                    if all([1 == complements[key][k] for k in complements[key]]):
                        pulse_queue.append((key, 0))
                    else:
                        pulse_queue.append((key, 1))

    # --- SOLUTION CODE ---
    return high_pulses * low_pulses

# DO NOT TOUCH - AUTO TEST AND SUBMISSION CODE
test_result = solve("test.txt", True)
print(test_result)
if TEST_RESULT is None or test_result == TEST_RESULT:
    # Prints the result of solving the main input file
    result = solve("input.txt")
    print(result)
