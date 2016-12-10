import re
from functools import partial
import numpy as np


def rect(w, h, d):
    d[:h, :w] = np.ones((h, w))


def rot_row(x, n, d):
    d[x] = np.roll(d[x], n)


def rot_col(y, n, d):
    d[:, y] = np.roll(d[:, y], n)

ops = [
    (r'rect (\d+)x(\d+)', rect),
    (r'rotate column x=(\d+) by (\d+)', rot_col),
    (r'rotate row y=(\d+) by (\d+)', rot_row),
]


def parse():
    with open('8.txt') as f:
        for l in f:
            for p, o in ops:
                m = re.match(p, l)
                if m:
                    yield partial(o, *map(int, m.groups()))


d = np.zeros((6, 50))

for o in parse():
    o(d)

print(np.sum(d))
for r in d:
    print(''.join(['.' if c == 0 else '#' for c in r]))
