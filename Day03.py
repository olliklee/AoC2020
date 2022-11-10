def read_input_from_file(file_name):
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(line.strip())
    return lines


def solve_03a():
    riddle = read_input_from_file("Day02_input.txt")


def solve_03b():
    riddle = read_input_from_file("Day02_input.txt")



print(f"Day 03 - Part 1: {solve_03a()}")
print(f"Day 03 - Part 2: {solve_03b()}")
