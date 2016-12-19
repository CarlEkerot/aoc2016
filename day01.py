import re


def parse():
    with open("day01.txt") as f:
        matches = re.findall("(([LR])(\d+)),?\s*", f.read())
        dir = 1j
        movs = []
        for (_, d, s) in matches:
            dir *= {'R': -1j, 'L': 1j}[d]
            movs += [dir]*int(s)
        return movs


def get_dist(dirs):
    return abs(sum(dirs).real) + abs(sum(dirs).imag)


def get_dist_visited_twice(dirs):
    sums = [sum(dirs[:i+1]) for i in range(len(dirs))]
    pos = [d for i, d in enumerate(sums) if d in sums[:i]][0]
    return abs(pos.real) + abs(pos.imag)


print(get_dist(parse()))
print(get_dist_visited_twice(parse()))
