microchips = {}
generators = {}


class Floor:
    def __init__(self, components):
        self.components = components
    def __repr__(self):
        return str(self.components)


class Microchip:
    def __init__(self, isotope):
        self.isotope = isotope
        microchips[isotope] = self
    def __repr__(self):
        return self.isotope + 'M'
    def other(self):
        return generators[self.isotope]


class Generator:
    def __init__(self, isotope):
        self.isotope = isotope
        generators[isotope] = self
    def __repr__(self):
        return self.isotope + 'G'
    def other(self):
        return microchips[self.isotope]


class Building:
    def __init__(self, level, floors):
        self.floors = floors
        self.level = level

    def __str__(self):
        print(self.floors)
        components = [repr(m) for m in microchips] + [repr(g) + 'G' for g in generators]

        print(components)
        s = ''
        for i, f in enumerate(self.floors):
            s += 'F%d: %2s %2s %2s %2s %2s' ()
        return s


building = Building(
    0, [
        Floor([Microchip('H'), Microchip('L')]),
        Floor([Generator('H')]),
        Floor([Generator('L')]),
        Floor([]),
    ])

print(building)