# Open the input file
f_in = open("input.txt", "r")

total = 0

for line in f_in:
    line = ''.join(ch for ch in line if ch.isdigit())
    if len(line) < 1: continue
    total += int(line[0] + line[-1])

print(total)
