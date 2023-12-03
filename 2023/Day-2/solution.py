# Advent of Code 2023 - Day 2 Solution
# https://adventofcode.com/2023/day/2

from functools import reduce
import operator as oper

# def set_default():
#     return {
#         "red" : 12,
#         "green" : 13,
#         "blue" : 14
#     }

def parse_line(line):
    line = line.split()

    # colours = set_default()
    mins = [0, 0, 0] # R, G, B

    for i in range(2, len(line), 2):
        num, colour = int(line[i]), line[i+1] \
                      if line[i+1][-1].isalpha() \
                      else line[i+1][:-1]

        # colours[colour] -= num
        # if colours[colour] < 0: return 0

        if colour == "red": mins[0] = max(mins[0], num)
        elif colour == "green": mins[1] = max(mins[1], num)
        elif colour == "blue": mins[2] = max(mins[2], num)

        # if line[i+1][-1] == ';':
        #     colours = set_default()
        if line[i+1][-1] != ',' and line[i+1][-1] != ";":
            mins = list(filter(lambda x: x > 1, mins))
            return reduce(oper.mul, mins)

with open("input.txt", "r") as f_in:
    sum = 0
    for line in f_in:
        line = line.lower().strip()
        sum += parse_line(line)
    print(sum)