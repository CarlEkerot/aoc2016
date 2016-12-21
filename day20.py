from functools import reduce


def parse():
    with open('day20.txt') as f:
        return [tuple(map(int, l.split('-'))) for l in f]


def find_gaps(itvs):
    max_end = 0
    for start, end in sorted(list(itvs)):
        if start > max_end + 1:
            yield (max_end + 1, start - 1)
        max_end = max(max_end, end)


gaps = list(find_gaps(parse()))
print(gaps[0][0])
print(reduce(lambda a, x: a + (x[1] - x[0] + 1), gaps, 0))
