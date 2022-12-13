from common import load_file

read_lines = load_file()

parsed_list = [[list(map(len,side.split())) for side in line.strip().split(" | ")] for line in read_lines]
parsed_list_char = [[side.split() for side in line.strip().split(" | ")] for line in read_lines]

# Part 1
sum_appearances = 0
for input, output in parsed_list:
    unique_num_char = [num_char for num_char in input if input.count(num_char) == 1]
    sum_appearances += sum(char in unique_num_char for char in output)
print(f"Answer part 1: {sum_appearances}")

# Part 2
sum_output = 0
for (input, output), (input_char, output_char) in zip(parsed_list, parsed_list_char):
    unique_num_char = [num_char for num_char in input if input.count(num_char) == 1]
    
    one_chars = input_char[input.index(2)]
    four_chars = input_char[input.index(4)]
    seven_chars = input_char[input.index(3)]
    eight_chars = input_char[input.index(7)]

    for num_char, char in zip(input, input_char):
        if num_char == 5:
            if num_char == len(set(char).union(set(one_chars))):
                three_chars = char
        if num_char == 6:
            if len(set(char).union(set(one_chars))) == 7:
                six_chars = char
            elif len(set(char).union(set(four_chars)-set(one_chars))) == 7:
                zero_chars = char
            else:
                nine_chars = char

    for num_char, char in zip(input, input_char):
        if num_char == 5:
            if len(set(char).union(set(six_chars))) == 7 and char != three_chars:
                two_chars = char
            elif len(set(char).union(set(six_chars))) == 6:
                five_chars = char


    chars_to_num = [zero_chars, one_chars, two_chars, three_chars,
                    four_chars, five_chars, six_chars, 
                    seven_chars, eight_chars, nine_chars                  
    ]

    chars_to_num = [sorted(chars) for chars in chars_to_num]
    sum_output += int("".join([str(chars_to_num.index(sorted(out))) for out in output_char]))

print(f"Answer part 2: {sum_output}")