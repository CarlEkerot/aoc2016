def parse():
    with open('3.txt') as f:
        return list(map(lambda l: list(map(int, l.split())), f.readlines()))


def transpose(sides):
    return [s for t in [zip(*sides[i:i+3]) for i in range(0, len(sides), 3)] for s in t]


def solve(sides):
    return len(list(filter(lambda s: abs(s[0] - s[1]) < s[2] < s[0] + s[1], map(list, sides))))


s = parse()
print(solve(s))
print(solve(transpose(s)))
