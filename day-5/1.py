
def main(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if line != '\n']

    initial_line = [int(x) for x in lines[0][lines[0].index(':') + 2:].split()]
    current = []
    for i in range(0, len(initial_line), 2):
        current.append([initial_line[i], initial_line[i] + initial_line[i + 1]])

    lines = lines[2:]

    maps = [[] for _ in range(7)]
    current_map = 0
    for line in lines:
        if not line[0].isnumeric():
            current_map += 1
            continue
        maps[current_map].append([int(x) for x in line.split()])

    import math
    minimum = math.inf
    next = []
    for map in maps:
        for map_range in map:
            for pair in current:
                pair = current.pop(0)
                print(pair)
            
                dest, src, length = map_range
                print(dest, src, length)
                if pair[0] >= src and pair[1] < src + length:
                    inc = dest - src
                    next.append([pair[0] + inc, pair[1] + inc])
                elif pair[0] >= src and pair[1] >= src + length:
                    next.append([pair[0] + dest - src, src + length - 1])
                    current.append([src + length, pair[1]])
                elif pair[0] < src and pair[1] < src + length:
                    next.append([pair[0], src - 1])
                    current.append([src, pair[1]])
                elif pair[0] >= src + length or pair[1] < src:
                    next.append(pair)
                else:
                    next.append([src, src + length - 1])
                    current.append([pair[0], src - 1])
                    current.append([src + length, pair[1]])
                print(current)
                print(next)
                input()
            print(current)
        current = next
    
    
    for pair in current:
        if pair[0] < minimum:
            minimum = pair[0]
    print(minimum)

main("test.txt")
#main("input.txt")
