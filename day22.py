import re
from collections import namedtuple
from itertools import permutations

Node = namedtuple('Node', ['x', 'y', 'used', 'avail'])


def parse():
    p = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%')
    with open('day22.txt') as f:
        nodes = [Node(*tuple(map(int, p.match(l).groups()))) for l in f if p.match(l)]
        node_max = max(nodes)
        matrix = [[None for i in range(node_max.x + 1)] for j in range(node_max.y + 1)]
        for n in nodes:
            matrix[n.y][n.x] = n
        return matrix


def viable_nodes(nodes):
    flat = [n for row in nodes for n in row]
    return [a for a, b in permutations(flat, 2) if a.used > 0 and a.used <= b.avail]


def print_nodes(nodes):
    viable = viable_nodes(nodes)
    for row in nodes:
        r = []
        for n in row:
            if n.used == 0:
                r.append('_')
            elif n in viable:
                r.append('.')
            else:
                r.append('#')
        print(''.join(r))


nodes = parse()

print(len(viable_nodes(nodes)))

# Solved by hand:
# We can move the empty space to any viable node.
# All we need to do is to move the empty space beyond
# the wall of huge nodes, go to upper right corner and
# transfer the payload incrementally towards (0, 0).
print_nodes(nodes)
