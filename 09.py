from common import load_file

read_lines = load_file()

import numpy as np

heights = np.array([list(map(int,[*line.strip()])) for line in read_lines])
n_rows, n_columns = heights.shape
low_points = np.zeros(heights.shape)

for row in range(n_rows):
    for column in range(n_columns):
        indices_to_maybe_check = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
        indices_to_check = [(r,c) for r,c in indices_to_maybe_check if r>=0 and r<n_rows and c>=0 and c<n_columns]

        low_point = True
        for r,c in indices_to_check:
            low_point = low_point and (heights[row, column] < heights[r, c])
        if low_point:
            low_points[row, column] = 1

# Part 1
risks = np.multiply(heights+1, low_points)
print(f"Answer part 1: {int(np.sum(risks))}")

# Part 2
low_point_indices = np.where(low_points == 1)

basin_sizes = []
for row_low_point, column_low_point in zip(low_point_indices[0], low_point_indices[1]):
    points = [(row_low_point, column_low_point)]
    visited = [(row_low_point, column_low_point)]
    while points:
        row, column = points.pop(0)
        indices_to_maybe_check = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
        indices_to_check = [(r,c) for r,c in indices_to_maybe_check if r>=0 and r<n_rows and c>=0 and c<n_columns]
        for point in indices_to_check:
            if point not in visited and heights[point] < 9:
                points.append(point)
                visited.append(point)
    basin_sizes.append(len(visited))

basin_product = 1
for basin_size in sorted(basin_sizes)[-3:]:
    basin_product *= basin_size
print(f"Answer part 2: {basin_product}")