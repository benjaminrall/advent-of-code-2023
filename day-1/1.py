numbers_strings =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open("input.txt", "r") as f:
    lines = [[c for c in line[:-1] if c in '123456789' or c in numbers_strings] for line in f.readlines()]

total = 0
for value in lines:
    v0 = value[0]
    if value[0] not in '123456789':
        v0 = str(numbers_strings.index(value[0]) + 1)
    v1 = value[-1]
    if value[-1] not in '123456789':
        v1 = str(numbers_strings.index(value[-1]) + 1)
    total += int(v0 + v1)

print(total)