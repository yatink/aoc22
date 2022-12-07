import re

small_test = """"""

class Directory(object):
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.directories = {}

    def build_tree(self, line_iterator):
        while True: # Parse ls output
            line = next(line_iterator, None)
            if line is None:
                return
            mat_ls_file = ls_file_pat.match(line)
            mat_ls_dir = ls_dir_pat.match(line)
            if mat_ls_file or mat_ls_dir:
                if mat_ls_file:
                    size, f_name = mat_ls_file.groups()
                    self.files[f_name] = int(size)
                elif mat_ls_dir:
                    _, dir_name = mat_ls_dir.groups()
                    self.directories[dir_name] = Directory(dir_name)
            else:
                break
        if line == go_back:
            return
        while True:
            mat_cd = cd_pat.match(line)
            if mat_cd:
                _, dir_name = mat_cd.groups()
                assert next(line_iterator) == ls
                self.directories[dir_name].build_tree(line_iterator)
                line = next(line_iterator, None)
                if line is None:
                    return
            else:
                break
        

go_back = '$ cd ..'
ls = '$ ls'
cd_pat = re.compile(r'^\$ (cd) ([a-zA-Z]+)$')
ls_dir_pat = re.compile(r'^(dir) ([a-zA-Z]+)$')
ls_file_pat = re.compile(r'^([0-9]+) ([a-zA-Z.]+)$')

             
def parse_input(inpt):
    line_iter = iter(inpt.split("\n"))
    curr = Directory('/')
    next(line_iter) # cd /
    next(line_iter) # dir
    curr.build_tree(line_iter)
    return curr

def calculate_total_sizes(curr, total_sizes):
    files_size = sum(curr.files.values())
    directories_size = sum(
        calculate_total_sizes(d, total_sizes) for d in curr.directories.values())
    total_size = files_size + directories_size
    total_sizes.append((curr.name, total_size))
    return total_size
    

def part1(inpt):
    dir_tree = parse_input(inpt)
    total_sizes = []
    calculate_total_sizes(dir_tree, total_sizes)
    return sum(x[1] for x in total_sizes if x[1] <= 100000)


def part2(inpt):
    dir_tree = parse_input(inpt)
    total_sizes = []
    calculate_total_sizes(dir_tree, total_sizes)
    root_size = max(total_sizes, key=lambda x: x[1])
    free_size = 30000000 - 70000000 + root_size[1]
    return min((x for x in total_sizes if x[1] > free_size), key=lambda x: x[1]) 
    
