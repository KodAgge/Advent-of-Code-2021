from common import load_file

read_lines = load_file()

parsed_lines = [list(map(int,line.strip().replace(" -> ", ",").split(","))) for line in read_lines]

import numpy as np

# Part 1
count = np.zeros((np.max(parsed_lines)+1, np.max(parsed_lines)+1))
for x1, y1, x2, y2 in parsed_lines:
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            count[y1,x] += 1
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            count[y,x1] += 1

print(f"Answer part 1: {np.sum(count > 1)}")

# Part 2
count = np.zeros((np.max(parsed_lines)+1, np.max(parsed_lines)+1))
for x1, y1, x2, y2 in parsed_lines:
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            count[y1,x] += 1
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            count[y,x1] += 1
    else:
        if x1 < x2:
            x_range = [x for x in range(x1, x2+1)]
        elif x1 > x2:
            x_range = [x for x in range(x1, x2-1, -1)]
        if y1 < y2:
            y_range = [y for y in range(y1, y2+1)]
        elif y1 > y2:
            y_range = [y for y in range(y1, y2-1, -1)]
        for x,y in zip(x_range, y_range):
            count[y,x] += 1

print(f"Answer part 2: {np.sum(count > 1)}")
