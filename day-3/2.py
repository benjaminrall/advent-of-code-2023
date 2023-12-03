

TESTING = 0

with open("test.txt" if TESTING else "input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ROWS = len(lines)
COLS = len(lines[0])

numbers = []

for i, line in enumerate(lines):
    current_num = None
    current_num_index = None
    for j, c in enumerate(line):
        if c.isnumeric():
            if current_num == None:
                current_num = c
                current_num_index = (i, j)
            else:
                current_num += c
        elif current_num is not None:
            numbers.append((int(current_num), current_num_index))
            current_num = None
    if current_num is not None:
        numbers.append((int(current_num), current_num_index))

from collections import defaultdict
stars = defaultdict(lambda : [])
total = 0
for num, pos in numbers:
    done = False
    for row in range(pos[0] - 1, pos[0] + 2):
        if done: 
            break
        if row < 0 or row >= ROWS:
            continue
        for col in range(pos[1] - 1, pos[1] + len(str(num)) + 1):
            if col < 0 or col >= COLS:
                continue
            if lines[row][col] == '*':
                stars[(row, col)].append(num)

for star in stars:
    nums = stars[star]
    if len(nums) == 2:
        total += nums[0] * nums[1]

print(total)