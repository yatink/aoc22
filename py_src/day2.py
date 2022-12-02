small_test = """A Y
B X
C Z"""

big_test = """
"""

def parse_input(inpt):
    return [i.split(" ") for i in inpt.split("\n")]

def part1(inpt):
    inpt = parse_input(inpt)
    running_sum = 0
    for (first, second) in inpt:
        if ord(second) - ord(first) == 23:
            running_sum += 3 + ord(second) - ord("W")
        elif ord(second) - ord(first) == 24 or ord(second) - ord(first) == 21:
            running_sum += 6 + ord(second) - ord("W")
        else:
            running_sum += ord(second) - ord("W")
        print(running_sum)
    return running_sum

def part2(inpt):
    inpt = parse_input(inpt)
    running_sum = 0
    for (first, second) in inpt:
        if second == "X":
            choice = (ord(first) - 65 - 1) %3 + 1
            running_sum += choice + 0
        elif second == "Y":
            choice = (ord(first) - 65) % 3 + 1
            running_sum += choice + 3
        elif second == "Z":
            choice = (ord(first) - 65 + 1) %3 + 1
            running_sum += choice + 6
        print(choice)
        print(running_sum) 
    return running_sum
