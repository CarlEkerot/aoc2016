from collections import defaultdict

def parse():
    with open('day23.txt') as f:
        return [l.split() for l in f]


def solve(program, regs):
    ip = 0

    def val_or_reg(v):
        return regs[v] if v in regs else int(v)

    def toggle(op):
        l = len(op)
        if l == 2:
            op[0] = 'dec' if op[0] == 'inc' else 'inc'
        else:
            op[0] = 'cpy' if op[0] == 'jnz' else 'jnz'

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
        elif op[0] == 'tgl':
            v = val_or_reg(op[1])
            p = ip + v
            if 0 <= p < len(program):
                toggle(program[p])
        ip += 1

    return regs['a']

p = parse()
print(solve(p, defaultdict(lambda: 0, {'a': 7, 'b': 0, 'c': 0, 'd': 0})))
print(solve(p, defaultdict(lambda: 0, {'a': 12, 'b': 0, 'c': 0, 'd': 0})))
