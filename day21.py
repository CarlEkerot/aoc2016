import re
from functools import reduce

patterns = [
    re.compile(r'(swap position) (\d+) with position (\d+)'),
    re.compile(r'(swap letter) (\w) with letter (\w)'),
    re.compile(r'(rotate) (right|left) (\d+) step[s]?'),
    re.compile(r'(rotate based on position) of letter (\w)'),
    re.compile(r'(reverse positions) (\d+) through (\d+)'),
    re.compile(r'(move) position (\d+) to position (\d+)'),
]


def rot(s, dir, n):
    return s[len(s) - n:] + s[:len(s) - n] if dir == 'right' else s[n:] + s[:n]


def rot_pos(s, x, dir):
    idx = s.index(x)
    return rot(s, dir, idx + 1 + (1 if idx >= 4 else 0))


def rev_rot_pos(s, x, dir):
    lookup = [1, 1, 6, 2, 7, 3, 8, 4]
    return rot(s, dir, lookup[s.index(x)])


def rev(s, start, end):
    return s[:start] + s[start:end + 1][::-1] + s[end + 1:]


def swap_pos(s, a, b):
    ls = list(s)
    ls[a], ls[b] = s[b], s[a]
    return ''.join(ls)


def swap_char(s, a, b):
    return swap_pos(s, s.index(a), s.index(b))


def move(s, x, y):
    ls = list(s)
    ls.insert(y, ls.pop(x))
    return ''.join(ls)


def parse():
    with open('day21.txt') as f:
        for l in f:
            i = next((p.match(l).groups() for p in patterns if p.match(l)))
            if i[0] == 'swap position':
                yield (swap_pos, int(i[1]), int(i[2]))
            elif i[0] == 'swap letter':
                yield (swap_char, i[1], i[2])
            elif i[0] == 'rotate':
                yield (rot, i[1], int(i[2]))
            elif i[0] == 'rotate based on position':
                yield (rot_pos, i[1], 'right')
            elif i[0] == 'reverse positions':
                yield (rev, int(i[1]), int(i[2]))
            elif i[0] == 'move':
                yield (move, int(i[1]), int(i[2]))


def reverse_instruction(i):
    if i[0] == rot:
        return (rot, 'left' if i[1] == 'right' else 'right', int(i[2]))
    elif i[0] == rot_pos:
        return (rev_rot_pos, i[1], 'left')
    elif i[0] == move:
        return (move, i[2], i[1])
    else:
        return i

ins = list(parse())
rev_ins = map(reverse_instruction, reversed(ins))

print(reduce(lambda s, i: i[0](s, *i[1:]), ins, 'abcdefgh'))
print(reduce(lambda s, i: i[0](s, *i[1:]), rev_ins, 'fbgdceah'))
