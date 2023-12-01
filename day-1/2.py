numbers_strings =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
for line in lines:
    v0 = None
    v1 = None
    for i, s in enumerate(numbers_strings):
        try:
            # Get first and last occurence
            indices = [line.index(s), line.rindex(s)]
            
            # Convert written numbers to number characters
            char = s
            L = len(s)
            if L > 1:
                char = str(i + 1)

            # Assign min and max numbers
            if v0 is None or indices[0] < v0[0]:
                v0 = (indices[0], char)
            if v1 is None or indices[-1] + L > v1[0]:
                v1 = (indices[-1] + L, char)
        except:
            continue
    v = int(v0[1] + v1[1])
    total += v

print(total)