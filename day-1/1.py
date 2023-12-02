with open("input.txt", "r") as f:
    lines = [[c for c in line[:-1] if c.isnumeric()] for line in f.readlines()]

print(sum([int(value[0] + value[-1]) for value in lines]))