from common import load_file

read_lines = load_file()

# Part 1
x, y = 0, 0
for line in read_lines:
    direction, units = line.strip().split()
    if direction == "forward":
        x += int(units)
    elif direction == "down":
        y += int(units)
    elif direction == "up":
        y -= int(units)
print(f"Answer part 1: {x*y}")

# Part 2
x, y, aim = 0, 0, 0
for line in read_lines:
    direction, units = line.strip().split()
    if direction == "forward":
        x += int(units)
        y += int(units) * aim
    elif direction == "down":
        aim += int(units)
    elif direction == "up":
        aim -= int(units)
print(f"Answer part 1: {x*y}")