

TESTING = 0

def parse_set(s):
    cubes = [0, 0, 0]
    for info in s.split(','):
        digit = ''
        for c in info:
            if c.isnumeric():
                digit += c
            else:
                cubes['rgb'.index(c)] = int(digit)
                break
    return cubes

def parse_input(line):
    cubes = [0, 0, 0] # R, G, B

    line = line[line.index(':') + 1:]

    sets = [parse_set(s) for s in line.split(';')]
    for s in sets:
        cubes[0] = max(cubes[0], s[0])
        cubes[1] = max(cubes[1], s[1])
        cubes[2] = max(cubes[2], s[2])
    return cubes


with open("test.txt" if TESTING else "input.txt", "r") as f:
    lines = [parse_input(line.strip().replace(" ", "")) for line in f.readlines()]

total = 0
for i, line in enumerate(lines):
    power = line[0] * line[1] * line[2]
    total += power

print(total)