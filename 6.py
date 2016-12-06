from collections import Counter


def parse():
    with open('6.txt') as f:
        return map(str.strip, f.readlines())


def solve(ls, least_common=False):
    return ''.join(Counter(c).most_common()[-1 if least_common else 0][0] for c in zip(*ls))


print(solve(parse()))
print(solve(parse(), least_common=True))
