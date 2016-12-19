import re


def parse():
    with open('day07.txt') as f:
        return [(re.split(r'\[\w+\]', l), re.findall(r'\[(\w+)\]', l)) for l in map(str.strip, f.readlines())]


def get_abbas(s, n):
    substrs = (s[i:i+n] for i in range(len(s) - (n - 1)))
    return filter(lambda p: p == p[::-1] and p[0] != p[1], substrs)


def has_abba(s, n):
    return list(get_abbas(s, n)) != []


def tls(ips, hns):
    return any(has_abba(i, 4) for i in ips) and not any(has_abba(h, 4) for h in hns)


def ssl(ips, hns):
    i_abas = [a for i in ips for a in get_abbas(i, 3)]
    h_abas = [a for h in hns for a in get_abbas(h, 3)]
    return any(i[1] + i[0] + i[1] in h_abas for i in i_abas)


def count_abbas(data, fun):
    return list(map(lambda d: fun(d[0], d[1]), data)).count(True)


data = parse()
print(count_abbas(data, tls))
print(count_abbas(data, ssl))
