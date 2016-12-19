from functools import reduce

pad_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

pad_b = [
    [0x0, 0x0, 0x1, 0x0, 0x0],
    [0x0, 0x2, 0x3, 0x4, 0x0],
    [0x5, 0x6, 0x7, 0x8, 0x9],
    [0x0, 0xa, 0xb, 0xc, 0x0],
    [0x0, 0x0, 0xd, 0x0, 0x0],
]

m = {
    'U': [-1, 0],
    'R': [0, 1],
    'D': [1, 0],
    'L': [0, -1],
}


def parse():
    with open('day02.txt') as f:
        return list(map(str.strip, f.readlines()))


def add(pos, delta, pad):
    y, x = list(map(lambda x, y: max(min(x + y, len(pad) - 1), 0), pos, delta))
    return [y, x] if pad[y][x] != 0x0 else pos


def solve(ins, pad, start):
    for i in ins:
        y, x = reduce(lambda a, b: add(a, b, pad), [m[d] for d in i], start)
        yield '%X' % pad[y][x]

ins = parse()
print(''.join(solve(ins, pad_a, [1, 1])))
print(''.join(solve(ins, pad_b, [2, 0])))
