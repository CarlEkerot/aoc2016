def parse():
    with open('day12.txt') as f:
        return [l.split() for l in f]


def solve(program, regs):
    ip = 0

    def val_or_reg(v):
        return regs[v] if v in regs else int(v)

    while ip < len(program):
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
        ip += 1

    return regs['a']

p = parse()
print(solve(p, {'a': 0, 'b': 0, 'c': 0, 'd': 0}))
print(solve(p, {'a': 0, 'b': 0, 'c': 1, 'd': 0}))
