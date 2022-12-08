from itertools import product, takewhile

small_test = """30373
25512
65332
33549
35390"""

big_test = """"""


def parse_input(inpt):
    return [list(map(int, line)) for line in inpt.split("\n")]

def is_visible(x, y, trees):
    top = all(trees[y][x] > trees[j][x] for j in range(0, y))
    bottom = all(trees[y][x] > trees[j][x] for j in range(y+1, len(trees)))
    left = all(trees[y][x] > trees[y][i] for i in range(0, x))
    right = all(trees[y][x] > trees[y][i] for i in range(x+1, len(trees[0])))
    print ((x,y), trees[y][x], (top, left, bottom, right))
    return top or bottom or left or right

def scenic_score(x, y, trees):
    visible_top = all(trees[y][x] > trees[j][x] for j in range(0, y))
    visible_bottom = all(trees[y][x] > trees[j][x] for j in range(y+1, len(trees)))
    visible_left = all(trees[y][x] > trees[y][i] for i in range(0, x))
    visible_right = all(trees[y][x] > trees[y][i] for i in range(x+1, len(trees[0])))

    def shorter_than(coords):
        i,j = coords
        return trees[y][x] > trees[j][i]
    
    top = (0 if visible_top else 1)  + sum(1 for j in takewhile(shorter_than, ((x,j) for j in reversed(range(0, y)))))
    bottom = (0 if visible_bottom else 1) + sum(1 for j in takewhile(shorter_than, ((x,j) for j in range(y+1, len(trees)))))
    left = (0 if visible_left else 1) + sum(1 for i in takewhile(shorter_than, ((i, y) for i in reversed(range(0,x)))))
    right = (0 if visible_right else 1) + sum(1 for i in takewhile(shorter_than, ((i,y) for i in range(x+1, len(trees[0])))))
    print ((x,y), trees[y][x], ((visible_top, top), (visible_left, left),(visible_bottom, bottom), (visible_right,right)))
    return top * bottom * left * right

def part1(inpt):
    trees = parse_input(inpt)
    num = 0
    for (x,y) in product(range(1, len(trees[0]) - 1), range(1, len(trees) - 1)):
        if is_visible(x, y, trees):
            print (x,y)
            num += 1
    return num + 2 * len(trees) + 2*len(trees[0]) - 4    

def part2(inpt):
    trees = parse_input(inpt)
    max_score = 0
    for (x,y) in product(range(1, len(trees[0]) - 1), range(1, len(trees) - 1)):
        s = scenic_score(x, y, trees)
        if s > max_score:
            print (x,y)
            max_score = s
    return max_score
