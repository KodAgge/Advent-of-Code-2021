from common import load_file
from itertools import product

read_lines = load_file()

polymer = read_lines[0].strip()

insertion_processes = dict()
for insertion_process in read_lines[2:]:
    pair, child = insertion_process.strip().split(" -> ")
    insertion_processes[pair] = child

starting_combinations = [polymer[i:i+2] for i in range(len(polymer)-1)]

unique_characters = list(set("".join(list(polymer) + list(insertion_processes.values()) + list(insertion_processes.keys()))))
unique_combinations = ["".join(list(tuple)) for tuple in list(product(unique_characters,repeat=2))]

character_count = dict()
for char in unique_characters:
    character_count[char] = 0
for char in polymer:
    character_count[char] += 1

combination_count = dict()
for combination in unique_combinations:
    combination_count[combination] = 0
for combination in starting_combinations:
    combination_count[combination] += 1

for step in range(40):
    combination_count_step = combination_count.copy()
    for combination in combination_count:
        if combination_count[combination] > 0:
            new_pair_1, new_pair_2 = combination[0] + insertion_processes[combination], insertion_processes[combination] + combination[1]
            character_count[insertion_processes[combination]] += combination_count[combination]
            combination_count_step[new_pair_1] += combination_count[combination]
            combination_count_step[new_pair_2] += combination_count[combination]
            combination_count_step[combination] = combination_count_step[combination] - combination_count[combination]
    combination_count = combination_count_step.copy()
    if step == 9:
        appearance_count_sorted = sorted(character_count.values())
        print(f"Answer part 1: {appearance_count_sorted[-1]-appearance_count_sorted[0]}")

appearance_count_sorted = sorted(character_count.values())
print(f"Answer part 2: {appearance_count_sorted[-1]-appearance_count_sorted[0]}")