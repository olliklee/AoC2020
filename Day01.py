def read_input_from_file(file_name):
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(int(line.strip()))
    return lines


def solve_01a():
    riddle = read_input_from_file("Day01_input.txt")
    goal = 2020

    for number in riddle:
        if (goal - number) in riddle:
            break

    return (goal - number) * number

def solve_01b():
    riddle = read_input_from_file("Day01_input.txt")
    goal = 2020

    for number in riddle:
        for i in range(1,len(riddle)):
            if (goal - number - riddle[i]) in riddle:
                result = (number, riddle[i], goal - number - riddle[i])
                break
    return result[0] * result[1] * result[2]


print(f"Day 01 - Part 1: {solve_01a()}")
print(f"Day 01 - Part 2: {solve_01b()}")
