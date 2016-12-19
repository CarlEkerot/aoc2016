from functools import lru_cache
from hashlib import md5


def in_a_row(s, n):
    for i, c in enumerate(s):
        if len(s) - i > n and all([x == c for x in s[i:i + n]]):
            return c


@lru_cache(maxsize=None)
def calc_hash(salt, i, itrs=1):
    h = salt + str(i)
    for i in range(itrs):
        h = md5(h.encode('utf-8')).hexdigest()
    return h


def solve(salt, itrs):
    i = 0
    keys = 0
    while keys < 64:
        c1 = in_a_row(calc_hash(salt, i, itrs), 3)
        i += 1
        if not c1:
            continue
        for j in range(i, i + 1000):
            c2 = in_a_row(calc_hash(salt, j, itrs), 5)
            if not c2:
                continue
            if c1 == c2:
                keys += 1
                break
    return i - 1

print(solve('cuanljph', 1))
print(solve('cuanljph', 2017))
