small_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

big_input = """"""

def parse_input(inpt):
    lines = inpt.split("\n")
    lines_with_sizes = [(len(line), line) for line in lines]
    return lines_with_sizes

def conv_to_priority(ch):
    if 65 <= ord(ch) <= 90:
        return ord(ch) - 64 + 26
    elif ord(ch) >= 97:
        return ord(ch) - 96

def part1(inpt):
    lines = parse_input(inpt)
    running_sum = 0
    for sz, line in lines:
        s1 = slice(sz//2)
        s2 = slice(sz//2, sz)
        char = set(line[s1]) & set(line[s2])
        print(char)
        running_sum += conv_to_priority(char.pop())
        print(running_sum)
    return running_sum

def part2(inpt):
    lines = iter(line[1] for line in parse_input(inpt))
    running_sum = 0
    for s1, s2, s3 in zip(lines, lines, lines):
        print(s1)
        print(s2)
        print(s3)
        running_sum += conv_to_priority((set(s1) & set(s2) & set(s3)).pop())
    return running_sum
