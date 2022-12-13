from common import load_file

read_lines = load_file()

crab_posositions = list(map(int,read_lines[0].split(",")))

# Part 1
total_distances = []
for pos in range(max(crab_posositions)+1):
    sum = 0
    for crab_pos in crab_posositions:
        sum += abs(crab_pos-pos)
    total_distances.append(sum)
print(f"Answer part 1: {min(total_distances)}")

# Part 2
total_distances = []
for pos in range(max(crab_posositions)+1):
    sum = 0
    for crab_pos in crab_posositions:
        n = abs(crab_pos-pos)
        sum += int(n * (n + 1) / 2)
    total_distances.append(sum)
print(f"Answer part 2: {min(total_distances)}")