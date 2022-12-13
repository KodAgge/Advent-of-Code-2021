from common import load_file

read_lines = load_file()

for line in read_lines:
    start = list(map(int,line.split(",")))

# Part 1
current_count = [start.count(i) for i in range(9)]
for i in range(80):
    zero_lf = current_count.pop(0)
    current_count.append(zero_lf)
    current_count[6] += zero_lf
print(f"Answer part 1: {sum(current_count)}")

# Part 2
current_count = [start.count(i) for i in range(9)]
for i in range(256):
    zero_lf = current_count.pop(0)
    current_count.append(zero_lf)
    current_count[6] += zero_lf
print(f"Answer part 2: {sum(current_count)}")