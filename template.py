

TESTING = 1

with open("test.txt" if TESTING else "input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)