
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
    for map in maps:
        next = []
        for map_range in map:
            next_current = []
            for pair in current:  
                dest, src, length = map_range

                if pair[0] >= src + length or pair[1] < src:
                    next_current.append(pair)
                elif pair[0] >= src and pair[1] < src + length:
                    inc = dest - src
                    next.append([pair[0] + inc, pair[1] + inc])
                elif pair[0] >= src and pair[1] >= src + length:
                    inc = dest - src
                    next.append([pair[0] + inc, src + length - 1 + inc])
                    next_current.append([src + length, pair[1]])
                elif pair[0] < src and pair[1] < src + length:
                    inc = dest - src
                    next_current.append([pair[0], src - 1])
                    next.append([src + inc, pair[1] + inc])
                else:
                    inc = dest - src
                    next.append([src + inc, src + length - 1 + inc])
                    next_current.append([pair[0], src - 1])
                    next_current.append([src + length, pair[1]])
                
            current = next_current

        for pair in current:
            next.append(pair)
        current = next
    
    
    for pair in current:
        if pair[0] < minimum:
            minimum = pair[0]
    print(minimum)

main("test.txt")
main("input.txt")
