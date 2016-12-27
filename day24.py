from itertools import permutations


def parse():
    with open('day24.txt') as f:
        maze = []
        nodes = {}
        for y, row in enumerate(f):
            r = []
            for x, c in enumerate(row.strip()):
                if c.isdigit():
                    nodes[(y, x)] = int(c)
                r.append(0 if c == '#' else 1)
            maze.append(r)
        return maze, nodes


def legal_moves(pos, visited, maze):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    legal = []
    for m in moves:
        new_pos = (pos[0] + m[0], pos[1] + m[1])
        if new_pos not in visited and \
           0 <= new_pos[0] < len(maze) and \
           0 <= new_pos[1] < len(maze[0]) and \
           maze[new_pos[0]][new_pos[1]]:
            legal.append((pos[0] + m[0], pos[1] + m[1]))
    return legal


def find_shortest_paths(pos, maze, nodes):
    queue = [(pos, 0)]
    visited = set([pos])
    while queue:
        p, n = queue.pop()
        if p in nodes:
            yield p, n
        for m in legal_moves(p, visited, maze):
            visited.add(m)
            queue.insert(0, (m, n + 1))


def build_adj_matrix(maze, nodes):
    m = [[0 for i in range(len(nodes))] for j in range(len(nodes))]
    for n1 in nodes:
        for n2, dist in find_shortest_paths(n1, maze, nodes):
            m[nodes[n1]][nodes[n2]] = dist
    return m


def brute_force(matrix, part=1):
    res = []
    l = len(matrix)
    for path in map(lambda t: (0,) + t, permutations(range(1, l), l - 1)):
        if part == 2:
            path += (0,)
        res.append(sum(matrix[n][m] for n, m in zip(path, path[1:])))
    print(min(res))


maze, nodes = parse()
matrix = build_adj_matrix(maze, nodes)
brute_force(matrix)
brute_force(matrix, part=2)
