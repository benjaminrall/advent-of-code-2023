

TESTING = 0

with open("test.txt" if TESTING else "input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def handle_card(line):
    winning, held = line[line.index(":") + 1:].split("|")
    winning = set([int(n) for n in winning.split(" ") if n != ' ' and n != ''])
    held = set([int(n) for n in held.split(" ") if n != ' ' and n != ''])
    n =  len(winning.intersection(held))
    return 1 << (n - 1) if n > 0 else 0
    

total = 0
for line in lines:
    total += handle_card(line)
print(total)