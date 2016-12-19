from itertools import combinations
from copy import deepcopy

components = {}


class Component:
    subfix = ''
    other_subfix = ''

    def __init__(self, isotope):
        self.isotope = isotope
        components[str(self)] = self

    def other(self):
        return components[self.isotope + self.other_subfix]

    def __str__(self):
        return self.isotope + self.subfix

    def __eq__(self, other):
        return self.isotope == other.isotope and self.subfix == other.subfix


class Microchip(Component):
    subfix = 'M'
    other_subfix = 'G'


class Generator(Component):
    subfix = 'G'
    other_subfix = 'M'


class Building:
    def __init__(self, floors):
        self.floors = floors
        self.level = 0

    def __eq__(self, other):
        return [list(sorted(f, key=lambda x: str(x))) for f in self.floors] == \
               [list(sorted(f, key=lambda x: str(x))) for f in other.floors]

    def _valid_combo(self, c):
        return len(c) == 1 or c[0].subfix == c[1].subfix or c[0] == c[1].other()

    def _valid_floor(self, floor):
        no_pairs = [c for c in floor if c.other() not in floor]
        combo = list(combinations(no_pairs, 2))
        return all(map(self._valid_combo, combo))

    def _can_add(self, floor, components):
        return self._valid_floor(components + floor)

    def _can_remove(self, floor, components):
        return self._valid_floor([c for c in floor if c not in components])

    def move(self, dir, cs):
        diff = 1 if dir == 'up' else -1

        if not self._can_add(self.floors[self.level + diff], cs):
            return False

        if not self._can_remove(self.floors[self.level], cs):
            return False

        for c in cs:
            self.floors[self.level].remove(c)
            self.floors[self.level + diff].append(c)
        self.level += diff

        return True


def solve(b, prev, depth=0):
    if len(b.floors[-1]) == len(components):
        return depth

    moves = []
    single = [[p] for p in b.floors[b.level]]
    double = list(map(list, combinations(b.floors[b.level], 2)))
    if b.level < len(b.floors) - 1:
        moves += [('up', m) for m in double + single]
    if b.level > 0:
        moves += [('down', m) for m in single + double]

    for dir, m in moves:
        bcopy = deepcopy(b)
        if not bcopy.move(dir, m) or bcopy == prev:
            continue

        return solve(bcopy, b, depth + 1)


building1 = Building([
    [Generator('T'), Microchip('T'), Generator('P'), Generator('S')],
    [Microchip('P'), Microchip('S')],
    [Generator('O'), Microchip('O'), Generator('R'), Microchip('R')],
    [],
])

print(solve(building1, building1))

building2 = Building([
    [Generator('T'), Microchip('T'), Generator('P'), Generator('S'),
     Generator('E'), Microchip('E'), Generator('D'), Microchip('D')],
    [Microchip('P'), Microchip('S')],
    [Generator('O'), Microchip('O'), Generator('R'), Microchip('R')],
    [],
])

print(solve(building2, building2))
