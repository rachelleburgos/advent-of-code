# Advent of Code 2023 - Day 1 Solution
# https://adventofcode.com/2023/day/1

def find_digits(s):
    spelled_out = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    spelled_out_lengths = {word: len(word) for word in spelled_out}
    nums = set(range(1, 10))

    items = [None, None]
    positions = [float('inf'), -1]  # Keep track of the positions

    for i in range(len(s)):
        if s[i].isdigit():
            num = s[i]
            if int(num) in nums:
                if i < positions[0]:
                    positions[0] = i
                    items[0] = num
                if i > positions[1]:
                    positions[1] = i
                    items[1] = num
        else:
            for word, num in spelled_out.items():
                if s[i:i + spelled_out_lengths[word]] == word:
                    if i < positions[0]:
                        positions[0] = i
                        items[0] = num
                    if i > positions[1]:
                        positions[1] = i
                        items[1] = num

    return items

# File processing
with open("input.txt", "r") as f_in:
    total = 0
    for line in f_in:
        line = line.lower().strip()
        positions = find_digits(line)

        if positions[0] is not None and positions[1] is not None:
            total += int(positions[0] + positions[1])

    print(total)
