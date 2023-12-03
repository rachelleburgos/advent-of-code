def find_digits(s, reversed=False):
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

    nums = (1,2,3,4,5,6,7,8,9)

    items = [None, None]
    positions = [1e8, -1] # Keep track of the positions of the replacements


    # Find the leftmost number
    for num in nums:
        # Find the position of the number
        pos = s.find(str(num))

        # If the number is in the string
        if pos != -1:
            # If the position is smaller than the previous smallest
            if pos < positions[0]:
                # Update the smallest position
                positions[0] = pos
                # Update the number
                items[0] = str(num)
    for num in spelled_out:
        # Find the position of the number
        pos = s.find(num)

        # If the number is in the string
        if pos != -1:
            # If the position is smaller than the previous smallest
            if pos < positions[0]:
                # Update the smallest position
                positions[0] = pos
                # Update the number
                items[0] = spelled_out[num]

    # Find the rightmost number
    for num in nums:
        # Find the position of the number
        pos = s.rfind(str(num))

        # If the number is in the string
        if pos != -1:
            # If the position is larger than the previous largest
            if pos > positions[1]:
                # Update the largest position
                positions[1] = pos
                # Update the number
                items[1] = str(num)
    for num in spelled_out:
        # Find the position of the number
        pos = s.rfind(num)

        # If the number is in the string
        if pos != -1:
            # If the position is larger than the previous largest
            if pos > positions[1]:
                # Update the largest position
                positions[1] = pos
                # Update the number
                items[1] = spelled_out[num]

    return items


# Open the input file using a context manager
with open("input.txt", "r") as f_in:
    total = 0
    for line in f_in:
        # Turn into lowecase & remove whitespaces
        line = line.lower().strip()

        positions = find_digits(line)

        if positions[0] and positions[1]:
            total += int(positions[0] + positions[1])

    print(total)

