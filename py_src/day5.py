import re
from collections import defaultdict
small_test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

big_test = """[Q]         [N]             [N]    
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
 1   2   3   4   5   6   7   8   9 

move 3 from 6 to 2
move 2 from 8 to 7
move 3 from 3 to 8
move 2 from 5 to 3
move 5 from 9 to 7
move 5 from 3 to 5
move 1 from 4 to 2
move 3 from 2 to 1
move 2 from 9 to 6
move 4 from 1 to 4
move 6 from 5 to 8
move 1 from 6 to 3
move 8 from 8 to 9
move 5 from 9 to 2
move 1 from 3 to 4
move 11 from 7 to 2
move 1 from 4 to 1
move 1 from 5 to 9
move 1 from 3 to 9
move 1 from 9 to 5
move 21 from 2 to 6
move 2 from 8 to 4
move 5 from 8 to 6
move 4 from 9 to 7
move 2 from 5 to 6
move 5 from 4 to 2
move 4 from 7 to 2
move 20 from 6 to 9
move 7 from 2 to 7
move 1 from 2 to 6
move 7 from 9 to 6
move 3 from 7 to 9
move 7 from 1 to 9
move 3 from 7 to 4
move 1 from 2 to 5
move 1 from 5 to 2
move 1 from 1 to 9
move 23 from 9 to 1
move 1 from 2 to 4
move 1 from 9 to 6
move 1 from 1 to 5
move 20 from 1 to 7
move 1 from 5 to 9
move 12 from 4 to 2
move 2 from 1 to 3
move 1 from 3 to 5
move 4 from 2 to 9
move 2 from 6 to 4
move 9 from 7 to 4
move 11 from 6 to 7
move 7 from 2 to 8
move 1 from 5 to 7
move 2 from 9 to 7
move 1 from 6 to 4
move 6 from 8 to 2
move 3 from 7 to 1
move 6 from 2 to 4
move 1 from 3 to 2
move 7 from 4 to 3
move 1 from 8 to 5
move 3 from 6 to 7
move 1 from 2 to 9
move 1 from 6 to 7
move 4 from 4 to 1
move 1 from 3 to 1
move 22 from 7 to 6
move 3 from 7 to 6
move 4 from 7 to 6
move 5 from 4 to 5
move 26 from 6 to 2
move 8 from 1 to 9
move 2 from 6 to 5
move 9 from 9 to 5
move 2 from 9 to 4
move 1 from 5 to 3
move 1 from 9 to 5
move 1 from 5 to 6
move 1 from 4 to 3
move 3 from 5 to 8
move 1 from 6 to 2
move 1 from 6 to 1
move 1 from 1 to 8
move 4 from 5 to 2
move 7 from 2 to 4
move 8 from 5 to 3
move 1 from 5 to 7
move 12 from 2 to 8
move 6 from 3 to 8
move 1 from 7 to 6
move 10 from 3 to 4
move 11 from 8 to 7
move 6 from 8 to 3
move 11 from 7 to 4
move 1 from 6 to 3
move 6 from 3 to 1
move 6 from 1 to 5
move 15 from 4 to 7
move 1 from 3 to 5
move 7 from 2 to 3
move 5 from 5 to 9
move 2 from 3 to 8
move 1 from 9 to 4
move 1 from 9 to 7
move 1 from 4 to 5
move 5 from 7 to 8
move 13 from 4 to 1
move 8 from 8 to 2
move 2 from 2 to 7
move 7 from 7 to 4
move 1 from 5 to 1
move 1 from 5 to 9
move 3 from 8 to 9
move 7 from 9 to 8
move 1 from 5 to 2
move 6 from 8 to 2
move 6 from 7 to 6
move 2 from 2 to 7
move 2 from 8 to 3
move 3 from 4 to 5
move 1 from 7 to 1
move 3 from 3 to 5
move 4 from 4 to 6
move 3 from 6 to 3
move 11 from 2 to 9
move 5 from 3 to 4
move 1 from 1 to 4
move 7 from 9 to 4
move 1 from 6 to 4
move 5 from 5 to 4
move 9 from 1 to 3
move 4 from 6 to 3
move 2 from 1 to 7
move 3 from 9 to 8
move 1 from 9 to 5
move 5 from 3 to 4
move 3 from 4 to 6
move 3 from 7 to 5
move 4 from 2 to 4
move 10 from 3 to 1
move 2 from 8 to 9
move 1 from 8 to 4
move 2 from 2 to 9
move 5 from 5 to 8
move 2 from 6 to 3
move 4 from 9 to 4
move 2 from 3 to 7
move 2 from 6 to 3
move 1 from 6 to 1
move 1 from 8 to 5
move 1 from 5 to 8
move 1 from 4 to 8
move 17 from 4 to 2
move 11 from 4 to 2
move 1 from 8 to 6
move 28 from 2 to 3
move 10 from 3 to 1
move 3 from 8 to 1
move 1 from 7 to 8
move 1 from 7 to 1
move 1 from 6 to 5
move 10 from 1 to 5
move 20 from 3 to 5
move 3 from 1 to 6
move 3 from 8 to 1
move 18 from 5 to 1
move 4 from 4 to 6
move 4 from 5 to 1
move 1 from 6 to 8
move 7 from 5 to 8
move 2 from 5 to 3
move 34 from 1 to 8
move 4 from 1 to 7
move 36 from 8 to 6
move 6 from 8 to 4
move 3 from 6 to 4
move 1 from 1 to 2
move 1 from 3 to 2
move 1 from 3 to 5
move 1 from 1 to 8
move 1 from 7 to 2
move 3 from 2 to 8
move 3 from 8 to 1
move 2 from 7 to 5
move 5 from 6 to 4
move 31 from 6 to 4
move 1 from 7 to 3
move 13 from 4 to 7
move 2 from 5 to 9
move 1 from 1 to 9
move 1 from 3 to 1
move 11 from 4 to 9
move 12 from 4 to 3
move 4 from 9 to 1
move 1 from 9 to 8
move 1 from 5 to 9
move 3 from 6 to 5
move 3 from 5 to 1
move 11 from 7 to 8
move 6 from 4 to 8
move 3 from 3 to 8
move 5 from 1 to 6
move 1 from 7 to 3
move 5 from 8 to 3
move 2 from 4 to 7
move 8 from 8 to 4
move 5 from 8 to 2
move 2 from 2 to 1
move 7 from 9 to 2
move 5 from 6 to 7
move 6 from 2 to 4
move 3 from 9 to 1
move 3 from 1 to 4
move 2 from 2 to 1
move 5 from 1 to 2
move 6 from 2 to 9
move 4 from 7 to 6
move 2 from 9 to 6
move 1 from 2 to 5
move 1 from 6 to 5
move 5 from 3 to 1
move 1 from 5 to 3
move 2 from 6 to 1
move 1 from 9 to 7
move 3 from 7 to 3
move 4 from 8 to 4
move 1 from 5 to 6
move 9 from 1 to 4
move 4 from 6 to 8
move 2 from 7 to 4
move 2 from 1 to 9
move 10 from 3 to 1
move 7 from 1 to 3
move 1 from 1 to 2
move 1 from 2 to 4
move 2 from 3 to 8
move 6 from 8 to 9
move 2 from 1 to 2
move 30 from 4 to 3
move 29 from 3 to 7
move 2 from 2 to 4
move 7 from 9 to 5
move 6 from 4 to 8
move 5 from 8 to 9
move 5 from 5 to 7
move 1 from 5 to 4
move 17 from 7 to 9
move 6 from 3 to 9
move 4 from 3 to 7
move 1 from 8 to 6
move 17 from 9 to 8
move 8 from 9 to 3
move 1 from 5 to 6
move 9 from 8 to 7
move 3 from 9 to 5
move 1 from 4 to 5
move 2 from 6 to 1
move 3 from 3 to 8
move 2 from 3 to 5
move 1 from 3 to 8
move 10 from 8 to 4
move 2 from 1 to 9
move 1 from 8 to 1
move 1 from 1 to 5
move 1 from 8 to 6
move 4 from 4 to 5
move 1 from 3 to 9
move 3 from 9 to 6
move 1 from 9 to 8
move 2 from 9 to 1
move 2 from 1 to 7
move 1 from 9 to 1
move 3 from 4 to 6
move 2 from 4 to 9
move 1 from 1 to 8
move 2 from 8 to 1
move 5 from 6 to 2
move 2 from 1 to 4
move 2 from 9 to 1
move 2 from 6 to 3
move 2 from 3 to 1
move 2 from 4 to 7
move 4 from 1 to 5
move 15 from 5 to 4
move 4 from 2 to 5
move 7 from 4 to 2
move 4 from 4 to 5
move 1 from 3 to 9
move 3 from 5 to 2
move 9 from 2 to 1
move 3 from 5 to 4
move 1 from 5 to 3
move 1 from 9 to 7
move 1 from 5 to 8
move 4 from 1 to 6
move 1 from 3 to 2
move 2 from 1 to 2
move 3 from 2 to 8
move 14 from 7 to 2
move 2 from 6 to 4
move 19 from 7 to 8
move 1 from 7 to 1
move 23 from 8 to 2
move 33 from 2 to 1
move 1 from 7 to 1
move 7 from 4 to 3
move 1 from 6 to 2
move 15 from 1 to 7
move 6 from 2 to 8
move 1 from 8 to 2
move 1 from 2 to 8
move 2 from 3 to 8
move 3 from 8 to 5
move 1 from 6 to 1
move 2 from 4 to 7
move 1 from 5 to 9
move 3 from 8 to 3
move 1 from 2 to 6
move 18 from 1 to 4
move 1 from 6 to 3
move 2 from 5 to 1
move 2 from 8 to 2
move 5 from 1 to 9
move 15 from 4 to 9
move 5 from 9 to 5
move 1 from 1 to 5
move 1 from 1 to 3
move 1 from 1 to 2
move 3 from 2 to 8
move 9 from 9 to 8
move 11 from 8 to 4
move 1 from 8 to 3
move 4 from 7 to 8
move 3 from 3 to 1
move 3 from 3 to 7
move 3 from 5 to 8
move 3 from 5 to 3
move 5 from 9 to 7
move 9 from 4 to 3
move 1 from 8 to 9
move 9 from 3 to 7
move 2 from 3 to 2
move 1 from 4 to 1
move 1 from 8 to 6
move 10 from 7 to 1
move 2 from 2 to 6
move 2 from 6 to 8
move 2 from 9 to 4
move 14 from 1 to 9
move 3 from 4 to 7
move 1 from 6 to 3
move 2 from 8 to 4
move 8 from 7 to 5
move 6 from 7 to 5
move 12 from 9 to 3
move 3 from 9 to 8
move 8 from 8 to 2
move 7 from 2 to 1
move 1 from 7 to 2
move 6 from 7 to 2
move 7 from 3 to 6
move 1 from 6 to 3
move 7 from 2 to 1
move 5 from 4 to 8
move 2 from 7 to 9
move 1 from 2 to 7
move 4 from 6 to 1
move 2 from 8 to 1
move 1 from 7 to 6
move 2 from 6 to 1
move 3 from 3 to 7
move 1 from 4 to 6
move 7 from 3 to 8
move 6 from 8 to 1
move 1 from 9 to 7
move 22 from 1 to 9
move 2 from 7 to 2
move 3 from 3 to 2
move 5 from 1 to 3
move 2 from 2 to 7
move 2 from 6 to 9
move 3 from 9 to 4
move 2 from 4 to 5
move 1 from 4 to 7
move 1 from 1 to 9
move 13 from 9 to 7
move 3 from 9 to 5
move 14 from 5 to 3
move 5 from 9 to 5
move 2 from 9 to 7
move 9 from 5 to 3
move 15 from 3 to 2
move 12 from 7 to 3
move 3 from 2 to 7
move 8 from 7 to 5
move 4 from 8 to 9
move 1 from 9 to 6
move 1 from 7 to 5
move 14 from 2 to 7
move 2 from 9 to 4
move 1 from 6 to 5
move 18 from 3 to 2
move 5 from 3 to 9
move 2 from 3 to 6
move 2 from 4 to 8
move 15 from 7 to 6
move 1 from 9 to 1
move 2 from 8 to 3
move 1 from 7 to 9
move 6 from 9 to 6
move 2 from 3 to 7
move 3 from 5 to 8
move 8 from 5 to 3
move 2 from 7 to 9
move 22 from 6 to 9
move 12 from 2 to 3
move 1 from 1 to 9
move 1 from 2 to 6
move 1 from 6 to 5
move 6 from 2 to 6
move 7 from 6 to 3
move 20 from 9 to 4
move 5 from 9 to 3
move 7 from 3 to 5
move 14 from 4 to 6
move 2 from 4 to 1
move 2 from 8 to 3
move 2 from 1 to 5
move 9 from 6 to 1
move 20 from 3 to 4
move 5 from 6 to 8
move 1 from 5 to 9
move 1 from 9 to 6
move 9 from 5 to 7
move 1 from 6 to 5
move 2 from 3 to 4
move 4 from 8 to 2
move 2 from 8 to 4
move 3 from 3 to 7
move 5 from 1 to 7
move 4 from 2 to 7
move 1 from 1 to 3
move 3 from 3 to 6
move 4 from 7 to 3
move 1 from 1 to 4
move 3 from 3 to 5
move 1 from 1 to 7
move 28 from 4 to 3
move 20 from 3 to 5
move 16 from 5 to 6
move 3 from 3 to 2
move 2 from 3 to 6
move 6 from 7 to 5
move 1 from 3 to 6
move 1 from 2 to 1
move 10 from 6 to 8
move 2 from 1 to 5
move 1 from 4 to 8
move 1 from 6 to 9
move 2 from 2 to 5
move 10 from 7 to 4
move 2 from 3 to 4
move 1 from 3 to 8
move 1 from 9 to 4
move 6 from 4 to 1
move 10 from 8 to 6
move 1 from 1 to 4
move 8 from 4 to 9
move 3 from 1 to 5
move 14 from 5 to 8
move 2 from 7 to 5
move 3 from 9 to 7
move 5 from 9 to 5
move 2 from 7 to 3
move 16 from 6 to 9
move 3 from 6 to 3
move 1 from 1 to 5
move 1 from 1 to 4
move 1 from 7 to 3
move 2 from 6 to 1
move 2 from 5 to 7
move 2 from 7 to 1
move 3 from 3 to 8
move 12 from 5 to 4
move 1 from 5 to 8
move 1 from 1 to 4
move 9 from 4 to 1
move 11 from 1 to 7
move 10 from 7 to 4
move 3 from 3 to 7
move 1 from 1 to 7
move 5 from 4 to 5
move 8 from 4 to 1
move 1 from 4 to 1
move 5 from 5 to 4
move 2 from 7 to 5
move 2 from 7 to 3
move 9 from 1 to 7
move 16 from 8 to 5
move 3 from 8 to 7
move 6 from 4 to 3
move 17 from 5 to 1
move 14 from 1 to 2
move 7 from 2 to 4
move 5 from 2 to 6"""


move_pattern = re.compile(r'^move ([0-9]+) from ([0-9]+) to ([0-9]+)$')
def parse_input(inpt):
    init, move_lines = inpt.split("\n\n")
    stack_lines = init.split("\n")
    stack_lines_reversed = list(reversed(stack_lines[:-1]))
    def _fn(x):
        return int(x.strip())
    last_stack_id = list(map(_fn, stack_lines[-1].split("   ")))[-1]
    stack = defaultdict(list)
    for i in range(last_stack_id):
        for line in stack_lines_reversed:
            pos = 1 + 4*i
            if pos >= len(line):
                continue
            else:
                if line[pos] != ' ':
                    stack[i+1].append(line[pos])
    moves = []
    for move in move_lines.split("\n"):
        moves.append(list(map(int, move_pattern.match(move).groups())))
    return stack, moves

def part1(inpt):
    stack, moves = parse_input(inpt)
    for move in moves:
        num, _from, _to = move
        stack[_from], stack[_to] = stack[_from][:-num], stack[_to] + list(reversed(stack[_from][-num:]))
    final = []
    for i in sorted(stack.keys()):
        if stack[i]:
            final.append(stack[i][-1])
    return ''.join(final)

def part2(inpt):
    stack, moves = parse_input(inpt)
    for move in moves:
        num, _from, _to = move
        stack[_from], stack[_to] = stack[_from][:-num], stack[_to] + stack[_from][-num:]
    final = []
    for i in sorted(stack.keys()):
        if stack[i]:
            final.append(stack[i][-1])
    return ''.join(final)
