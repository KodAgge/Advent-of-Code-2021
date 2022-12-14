from common import load_file
import numpy as np

read_lines = load_file()

dumbo_array = np.array([list(map(int, list(line.strip()))) for line in read_lines])
MAX_ROW, MAX_COLUMN = dumbo_array.shape
N_DUMBOS = dumbo_array.size

n_flashed_dumbos = 0
for i in range(1000):
    n_flashed_dumbos_this_step = 0
    dumbo_array += 1
    flashed_dumbos = set()
    while np.sum(dumbo_array > 9):
        flash_indices = np.where(dumbo_array > 9)
        for row, column in zip(flash_indices[0], flash_indices[1]):
            n_flashed_dumbos += 1
            n_flashed_dumbos_this_step += 1
            dumbo_array[row, column] = 0
            flashed_dumbos.add((row, column))
            dumbo_indices_to_maybe_check = [
                (row+1, column+1), (row+1, column), (row+1, column-1),
                (row, column+1), (row, column-1),
                (row-1, column+1), (row-1, column), (row-1, column-1)
            ]
            dumbo_indices_to_check = [(r, c) for (r, c) in dumbo_indices_to_maybe_check if r >= 0 and r < MAX_ROW and c >= 0 and c < MAX_COLUMN]
            for (r,c) in dumbo_indices_to_check:
                if (r, c) not in flashed_dumbos:
                    dumbo_array[r, c] += 1

    if i == 99:
        print(f"Answer part 1: {n_flashed_dumbos}")
    if n_flashed_dumbos_this_step == N_DUMBOS:
        print(f"Answer part 2: {i+1}")
        break