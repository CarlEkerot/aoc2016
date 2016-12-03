import re

DIRS = [
    [0, 1],   # North
    [1, 0],   # East
    [0, -1],  # South
    [-1, 0],  # West
]


def parse():
    with open("1.txt") as f:
        matches = re.findall("(([LR])(\d+)),?\s*", f.read())
        return map(lambda m: (m[1], int(m[2])), matches)


def get_dist(directions):
    curr_dir = 0  # Start facing north
    curr_pos = [0, 0]

    for (rot, steps) in directions:
        curr_dir = (curr_dir + {'R': 1, 'L': -1}[rot]) % 4
        curr_pos[0] += steps * DIRS[curr_dir][0]
        curr_pos[1] += steps * DIRS[curr_dir][1]
    return sum(curr_pos)


def get_dist_visited_twice(directions):
    curr_dir = 0  # Start facing north
    curr_pos = [0, 0]
    visited = {tuple(curr_pos): 1}

    for (rot, steps) in directions:
        curr_dir = (curr_dir + {'R': 1, 'L': -1}[rot]) % 4
        for i in range(1, steps+1):
            curr_pos[0] += DIRS[curr_dir][0]
            curr_pos[1] += DIRS[curr_dir][1]
            if tuple(curr_pos) in visited:
                return sum(curr_pos)
            else:
                visited[tuple(curr_pos)] = 1
    raise Exception("No location visited twice")


print(get_dist(parse()))
print(get_dist_visited_twice(parse()))
