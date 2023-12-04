

TESTING = 0

with open("test.txt" if TESTING else "input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def handle_card(line):
    winning, held = line[line.index(":") + 1:].split("|")
    winning = set([int(n) for n in winning.split(" ") if n != ' ' and n != ''])
    held = set([int(n) for n in held.split(" ") if n != ' ' and n != ''])
    n =  len(winning.intersection(held))
    return n
    

total = 0
held = [1 for i in range(len(lines))]
for i, line in enumerate(lines):
    n = handle_card(line)
    for j in range(i + 1, min(i + n + 1, len(lines))):
        held[j] += held[i]
    
print(sum(held))
    