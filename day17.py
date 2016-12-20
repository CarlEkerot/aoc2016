from hashlib import md5

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
char_map = {m: c for m, c in zip(moves, 'UDLR')}
shape = (4, 4)


def hash_moves(seq):
    h = md5(seq.encode('utf-8')).hexdigest()
    return [p for p, c in zip(moves, h[:4]) if c in 'bcdef']


def legal_moves(pos, seq):
    for m in hash_moves(seq):
        if 0 <= pos[0] + m[0] < shape[0] and 0 <= pos[1] + m[1] < shape[1]:
            yield m


def solve(seq, calc_longest=False):
    target = (shape[0] - 1, shape[1] - 1)
    queue = [((0, 0), seq)]
    longest = 0
    while len(queue) > 0:
        p, s = queue.pop()
        for m in legal_moves(p, s):
            new_p = (p[0] + m[0], p[1] + m[1])
            new_s = s + char_map[m]
            if new_p == target:
                if not calc_longest:
                    return new_s[len(seq):]
                else:
                    longest = len(new_s) - len(seq)
            else:
                queue.insert(0, (new_p, new_s))
    return longest

print(solve('edjrjqaa'))
print(solve('edjrjqaa', calc_longest=True))
