def read_input_from_file(file_name):
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(line.strip())
    return lines


def solve_02a():
    riddle = read_input_from_file("Day02_input.txt")
    counter = 0
    for line in riddle:
        line = line.split(" ")
        rule = [int(num) for num in line[0].split("-")]
        char = line[1].strip(":")
        password = line[2]
        is_valid = password.count(char) in range(rule[0], rule[1] + 1)

        if is_valid :
            counter += 1

    return counter


def solve_02b():
    riddle = read_input_from_file("Day02_input.txt")
    counter = 0
    for line in riddle:
        line = line.split(" ")
        rule = [int(num) for num in line[0].split("-")]
        char = line[1].strip(":")
        password = line[2]
        is_valid = (password[rule[0] - 1] == char and not password[rule[1] - 1] == char) or \
                   (password[rule[1] - 1] == char and not password[rule[0] - 1] == char)

        if is_valid:
            counter += 1

    return counter


print(f"Day 02 - Part 1: {solve_02a()}")
print(f"Day 02 - Part 2: {solve_02b()}")
