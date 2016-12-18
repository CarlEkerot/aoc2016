def is_wall(x, y, num):
    s = x * x + 3 * x + 2 * x * y + y + y * y + num
    count = 0
    while s:
        if s & 1:
            count += 1
        s >>= 1
    return count & 1 == 1


def legal_moves(pos, visited, num):
    legal = []
    for m in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        res = (pos[0] + m[0], pos[1] + m[1])
        if res[0] >= 0 and res[1] >= 0 and \
                not is_wall(res[1], res[0], num) and \
                res not in visited:
            legal.append(res)
    return legal


def solve(dst, num, part='1'):
    queue = [((1, 1), 0)]
    visited = [(1, 1)]
    while True:
        pos, d = queue.pop()
        if part == '1' and pos == dst:
            break
        elif part == '2' and any([e[1] == 50 for e in queue]):
            break
        for move in legal_moves(pos, visited, num):
            queue.insert(0, (move, d + 1))
            visited.append(move)
    return d if part == '1' else len(visited)

print(solve((39, 31), 1364, part='1'))
print(solve((39, 31), 1364, part='2'))
