from itertools import count


def solve(t):
    eqs = [
        (t + 10 + 0) % 13,
        (t + 15 + 1) % 17,
        (t + 17 + 2) % 19,
        (t +  1 + 3) % 7,
        (t +  0 + 4) % 5,
        (t +  1 + 5) % 3
    ]
    return not any([eq != 0 for eq in eqs])


for i in count(2):
    if solve(i):
        print(i - 1)
        break

for i in count(2):
    if solve(i) and (i + 6) % 11 == 0:
        print(i - 1)
        break
