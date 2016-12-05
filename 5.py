from itertools import count, islice
from hashlib import md5


def hashes(room):
    return (md5((room + str(i)).encode('utf-8')).hexdigest() for i in count())


def candidates(room):
    return filter(lambda h: h[:5] == '00000', hashes(room))


def solve1(room):
    return ''.join(islice((h[5] for h in candidates(room)), 8))


def solve2(room):
    r = [None]*8
    c = candidates(room)
    while not all(r):
        h = next(c)
        i = int(h[5], 16)
        if i < len(r) and r[i] is None:
            r[i] = h[6]
    return ''.join(r)


r = 'abbhdwsy'
print(solve1(r))
print(solve2(r))
