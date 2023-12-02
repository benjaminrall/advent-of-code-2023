NUMBERS =  ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
for line in lines:
    first, last = None, None

    # Tests for each possible number (both spelled out words and single characters)
    for i, s in enumerate(NUMBERS):
        try:
            # Gets first and last occurence of the number
            indices = [line.index(s), line.rindex(s)]
            
            # Convert written out numbers to single number characters
            char = str(i + 1) if len(s) > 1 else s

            # Reassign first and last numbers to the current number 
            # if it's at a smaller/larger position than them
            if first is None or indices[0] < first[0]:
                first = (indices[0], char)
            if last is None or indices[-1] > last[0]:
                last = (indices[-1], char)

        # Empty except to just ignore cases where a number doesn't exist
        except:
            continue

    total += int(first[1] + last[1])

print(total)