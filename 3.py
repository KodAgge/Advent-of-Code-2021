from common import load_file

read_lines = load_file()

# Part 1
lines = [line.strip() for line in read_lines]
n_bits = len(lines)
common_bits = []
for i in range(len(lines[0])):
    count = 0
    for line in lines:
        count += int(line[i])
    common_bits.append(1 * (count > n_bits // 2))
uncommon_bits = [1 - bit for bit in common_bits]
gamma = int("".join(map(str,common_bits)), 2)
epsilon = int("".join(map(str,uncommon_bits)), 2)
print(f"Answer part 1: {gamma*epsilon}")

# Part 2
lines = [line.strip() for line in read_lines]
n_bits = len(lines)
prev_list = lines
for i in range(len(lines[0])):
    count = 0
    for bit in prev_list:
        count += int(bit[i])
    most_common = 1 * (count >= len(prev_list) / 2)
    current_list = []
    for bit in prev_list:
        if bit[i] == str(most_common):
            current_list.append(bit)
    if len(current_list) == 1:
        break
    else:
        prev_list = current_list
oxygen = int(current_list[0], 2)

prev_list = lines
for i in range(len(lines[0])):
    count = 0
    for bit in prev_list:
        count += int(bit[i])
    most_uncommon = 1 * (count < len(prev_list) / 2)
    current_list = []
    for bit in prev_list:
        if bit[i] == str(most_uncommon):
            current_list.append(bit)
    if len(current_list) == 1:
        break
    else:
        prev_list = current_list
co2 = int(current_list[0], 2)
print(f"Answer part 2: {oxygen*co2}")