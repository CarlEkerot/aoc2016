from itertools import count


def parse():
    with open('day25.txt') as f:
        return [l.split() for l in f]


def get_out(program, regs, n):
    ip = 0

    def val_or_reg(v):
        return regs[v] if v in regs else int(v)

    output = []
    while len(output) < n:
        op = program[ip]
        if op[0] == 'cpy':
            regs[op[2]] = val_or_reg(op[1])
        elif op[0] == 'inc':
            regs[op[1]] += 1
        elif op[0] == 'dec':
            regs[op[1]] -= 1
        elif op[0] == 'jnz':
            ip += val_or_reg(op[2]) if val_or_reg(op[1]) != 0 else 1
            continue
        elif op[0] == 'out':
            output.append(val_or_reg(op[1]))
        ip += 1

    return output


def find_pattern(p):
    for i in count():
        if get_out(p, {'a': i, 'b': 0, 'c': 0, 'd': 0}, 12) == [0, 1] * 6:
            return i

p = parse()
print(find_pattern(p))
