with open("2.in") as file:
    x, y = 0, 0
    for line in file:
        direction, units = line.strip().split()
        if direction == "forward":
            x += int(units)
        elif direction == "down":
            y += int(units)
        elif direction == "up":
            y -= int(units)
    print(f"Answer part 1: {x*y}")

with open("2.in") as file:
    x, y, aim = 0, 0, 0
    for line in file:
        direction, units = line.strip().split()
        if direction == "forward":
            x += int(units)
            y += int(units) * aim
        elif direction == "down":
            aim += int(units)
        elif direction == "up":
            aim -= int(units)
    print(f"Answer part 1: {x*y}")