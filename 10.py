from common import load_file

read_lines = load_file()

start_delimiter = ["(", "[", "{", "<"] 
end_delimiter = [")", "]", "}", ">"]

# Part 1
delimiter_values = [3, 57, 1197, 25137]
syntax_error_score = 0
incomplete_lines = []
for line in read_lines:
    incomplete_line = True
    delimiter_stack = []
    for delimiter in line.strip():
        if delimiter in start_delimiter:
            delimiter_stack.append(delimiter)
        elif delimiter in end_delimiter:
            chunk_start_delimiter = delimiter_stack.pop()
            if end_delimiter[start_delimiter.index(chunk_start_delimiter)] != delimiter:
                syntax_error_score += delimiter_values[end_delimiter.index(delimiter)]
                incomplete_line = False
                break
    if incomplete_line:
        incomplete_lines.append(line.strip())

print(f"Answer part 1: {syntax_error_score}")

# Part 2
total_scores = []
for line in incomplete_lines:
    total_score = 0
    delimiter_stack = []
    for delimiter in line:
        if delimiter in start_delimiter:
            delimiter_stack.append(delimiter)
        elif delimiter in end_delimiter:
            chunk_start_delimiter = delimiter_stack.pop()
    for delimiter in delimiter_stack[::-1]:
        total_score *= 5 
        total_score += start_delimiter.index(delimiter) + 1
    total_scores.append(total_score)

print(f"Answer part 2: {sorted(total_scores)[len(total_scores)//2]}")