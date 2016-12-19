from string import ascii_letters
import re


def rot(s, n):
    return ''.join([chr((ord(c) + n - ord('a')) % 26 + ord('a')) if c in ascii_letters else ' ' for c in s])


def parse():
    with open('day04.txt') as f:
        return [re.match("([a-z-]+)(\d+)\[(\w+)\]", l).groups() for l in f]


def checksum(name):
    return ''.join([cnt[1] for cnt in sorted([(-name.count(c), c) for c in set(name)])][:5])


def solve1(rooms):
    return sum([int(id) for name, id, sum in rooms if sum == checksum(name.replace('-', ''))])


def solve2(rooms, s):
    plain = [(rot(name, int(id)).strip(), id) for name, id, _ in rooms]
    return next((id for name, id in plain if name == s))


rooms = parse()
print(solve1(rooms))
print(solve2(rooms, 'northpole object storage'))
