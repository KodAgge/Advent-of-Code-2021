from common import load_file
import numpy as np

read_lines = load_file()

dot_indices = []
fold_axis = []
read_indices = True
for line in read_lines:
    if read_indices:
        if line == "\n":
            read_indices = False
            dot_indices = np.array(dot_indices)
            continue
        else:
            dot_indices.append(list(map(int,line.strip().split(","))))
    else:
        fold_axis.append(line.strip().split()[2][0])

MAX_ROW = max(dot_indices[:,1])
MAX_COLUMN = max(dot_indices[:,0])

paper = np.zeros((MAX_ROW+1+(MAX_ROW%2), MAX_COLUMN+1+(MAX_COLUMN%2)))

for (column, row) in dot_indices:
    paper[row, column] = 1

def print_dots(indices):
    string = ""
    for row in indices.tolist():
        for value in row:
            string += "██" if value > 0 else "  "
        string += "\n"
    print(string)

axis = fold_axis[0]

for i, axis in enumerate(fold_axis):
    max_row, max_column = paper.shape
    if axis == "x":
        paper = paper[:,:max_column//2] + np.flip(paper[:,max_column//2+1:], axis=1)
    else:
        paper = paper[:max_row//2,:] + np.flip(paper[max_row//2+1:,:], axis=0)
    if i == 0:
        print(f"Answer part 1: {np.sum(paper > 0)}")

print("Answer part 2:")
print_dots(paper)