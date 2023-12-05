
def main(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    print(lines)

main("input.txt")
main("test.txt")
