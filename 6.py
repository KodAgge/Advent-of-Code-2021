with open("6.in") as file:
    for line in file:
        start = list(map(int,line.split(",")))

current_count = [start.count(i) for i in range(9)]
for i in range(80):
    zero_lf = current_count.pop(0)
    current_count.append(zero_lf)
    current_count[6] += zero_lf
print(f"Answer part 1: {sum(current_count)}")

current_count = [start.count(i) for i in range(9)]
for i in range(256):
    zero_lf = current_count.pop(0)
    current_count.append(zero_lf)
    current_count[6] += zero_lf
print(f"Answer part 2: {sum(current_count)}")