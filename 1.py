from common import load_file

read_lines = load_file()

# Part 1
depths = [int(d.strip()) for d in read_lines]
increases = 0
for p,c in zip(depths[:-1],depths[1:]):
    increases += c > p
print(f"Answer part 1: {increases}")

# Part 2
depths = [int(d.strip()) for d in read_lines]
increases = 0
for i in range(3, len(depths)):
    increases += sum(depths[i-2:i+1]) > sum(depths[i-3:i])
print(f"Answer part 2: {increases}")