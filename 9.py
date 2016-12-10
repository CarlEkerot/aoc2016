def eat(s, n):
    return ''.join(s.pop(0) for _ in range(n))


def eat_until(s, c):
    return eat(s, s.index(c))


def parse_marker(s):
    assert(eat(s, 1) == '(')
    l = int(eat_until(s, 'x'))
    assert(eat(s, 1) == 'x')
    n = int(eat_until(s, ')'))
    assert(eat(s, 1) == ')')
    return l, n


def decompress1(s):
    res = 0
    while s:
        if s[0] == '(':
            l, n = parse_marker(s)
            eat(s, l)
            res += l * n
        else:
            eat(s, 1)
            res += 1
    return res


def decompress2(s):
    res = 0
    while s:
        if s[0] == '(':
            l, n = parse_marker(s)
            res += n * decompress2(s[:l])
            eat(s, l)
        else:
            eat(s, 1)
            res += 1
    return res


def parse():
    with open('9.txt') as f:
        return list(f.read().strip())

p = parse()
print(decompress1(p[:]))
print(decompress2(p[:]))
