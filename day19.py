from collections import deque


def solve1(elves):
    cnt = 0
    l = [1] * elves
    while l.count(1) > 1:
        for i in range(elves):
            if l[i] == 1:
                cnt += 1
                l[i] = cnt % 2
    return l.index(1) + 1


def solve2(elves):
    left = deque(range(1, (elves + 1) // 2))
    right = deque(range((elves + 1) // 2), elves + 1)

    while True:
        if len(right) >= len(left):
            right.popleft()
        else:
            left.pop()
        if len(left) + len(right) == 1:
            return left.pop()
        left.append(right.popleft())
        right.append(left.popleft())

print(solve1(3014603))
print(solve2(3014603))
