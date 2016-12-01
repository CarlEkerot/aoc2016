import re


def parse():
    with open("1.txt") as f:
        matches = re.findall("(([LR])(\d+)),?\s*", f.read())
        return map(lambda (a, b, c): (b, int(c)), matches)


def get_dist(directions):
    curr_dir = 1  # Start facing north
    curr_pos = 0

    for (rot, steps) in directions:
        curr_dir *= {'R': -1j, 'L': 1j}[rot]
        curr_pos += steps * curr_dir
    return abs(curr_pos.imag) + abs(curr_pos.real)


def get_dist_visited_twice(directions):
    curr_dir = 1  # Start facing north
    curr_pos = 0
    visited = {curr_pos: 1}

    for (rot, steps) in directions:
        curr_dir *= {'R': -1j, 'L': 1j}[rot]
        for i in range(1, steps+1):
            curr_pos += curr_dir
            if curr_pos in visited:
                return abs(curr_pos.imag) + abs(curr_pos.real)
            else:
                visited[curr_pos] = 1
    raise Exception("No location visited twice")


print(get_dist(parse()))
print(get_dist_visited_twice(parse()))
