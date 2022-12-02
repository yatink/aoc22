small_test = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

big_test = """
"""

def parse_input(inpt):
    calories_per_elf = inpt.split("\n\n")
    cpe = {}
    for (i,c) in enumerate(calories_per_elf):
        cpe[i] = map(int, c.split("\n"))
    return cpe

def part1(inpt):
    cpe = parse_input(inpt)
    return max(map(sum, cpe.values()))

def part2(inpt):
    cpe = parse_input(inpt)
    total_foods = sorted(map(sum, cpe.values()), reverse=True)
    return sum(total_foods[:3])
