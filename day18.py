start = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'


def check(x):
    return '.' if x == x[::-1] else '^'


def next_row(prev):
    p = '.' + prev + '.'
    return ''.join([check(p[i:i+3]) for i in range(len(p) - 2)])


def count_safe(rows, prev):
    num_safe = 0
    for i in range(rows):
        num_safe += prev.count('.')
        prev = next_row(prev)
    return num_safe


print(count_safe(40, start))
print(count_safe(400000, start))
